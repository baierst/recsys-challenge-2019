import recsys.algorithms.utils as utils
import pickle
from recsys.config import Config


def calc_recommendation(df_test, df_target):
    """Calculate recommendations based on last viewed hotel.

    The final data frame will have an impression list sorted according the order the impressions have been shown.
    If a hotel has been viewed before, it is sorted to the front.

    :param df_test: Data frame with all test data
    :param df_target: Data frame with target rows
    :return: Data frame with sorted impression list according to impression order and last viewd hotel
    """

    config = Config()
    last_booked_lookup = pickle.load(open(config.data_path / "last_booked_lookup.pkl", "rb"))

    def last_element(l):
        if len(l) != 0:
            return l
        else:
            return -1

    df_grouped = df_test.groupby(['user_id', 'session_id'], as_index=False)['reference'].apply(list)
    df_references = df_grouped.reset_index(name='references')

    df_references['last_ref_hotel'] = df_references['references'].apply(
        lambda x: last_element([e for e in x if str(e).isdigit()]))

    df_last_ref = df_references[df_references['last_ref_hotel'] != -1][['user_id', 'session_id', 'last_ref_hotel']]

    df_target['impressions'] = df_target['impressions'].apply(utils.string_to_array)

    df_joined = df_target.merge(df_last_ref, on=['user_id', 'session_id'], how='left')

    def reorder(x):

        user_id = x['user_id']

        last_booked = None

        if user_id in last_booked_lookup.keys():
            last_booked = last_booked_lookup[user_id]

        impressions = x['impressions'].copy()

        if type(x['last_ref_hotel']) == list:
            for last_ref_hotel in x['last_ref_hotel']:
                if str(last_ref_hotel) in impressions:
                    impressions.remove(str(last_ref_hotel))
                    impressions = [str(last_ref_hotel)] + impressions

        if last_booked is not None:
            for item in last_booked:
                if item in impressions:
                    impressions.remove(item)
                    impressions = [item] + impressions


        return impressions

    df_joined['impressions_reordered'] = df_joined.apply(reorder, axis=1)

    df_out = df_joined[utils.GR_COLS + ['impressions_reordered']]
    df_out['impressions_reordered'] = df_out['impressions_reordered'].apply(lambda x: ' '.join(x))
    df_out.rename(columns={'impressions_reordered': 'item_recommendations'}, inplace=True)

    return df_out
