import recsys.algorithms.utils as utils


def calc_recommendation(df_test, df_target):
    """Calculate recommendations based on most frequently viewed hotel.

    The final data frame will have an impression list sorted according the order the impressions have been shown.
    If the most frequently viewed hotel is in the list, it is sorted to the front.

    :param df_test: Data frame with all test data
    :param df_target: Data frame with target rows
    :return: Data frame with sorted impression list according to impression order and most frequently viewed hotel
    """

    def most_frequent(l):

        if len(l) != 0:
            counter = 0
            num = l[0]

            for i in l:
                curr_frequency = l.count(i)
                if (curr_frequency > counter):
                    counter = curr_frequency
                    num = i
            return num
        else:
            return -1

    df_grouped = df_test.groupby(['user_id', 'session_id'], as_index=False)['reference'].apply(list)
    df_references = df_grouped.reset_index(name='references')

    df_references['most_ref_hotel'] = df_references['references'].apply(
        lambda x: most_frequent([e for e in x if str(e).isdigit()]))

    df_most_ref_hotel = df_references[df_references['most_ref_hotel'] != -1][['user_id', 'session_id', 'most_ref_hotel']]

    df_target['impressions'] = df_target['impressions'].apply(utils.string_to_array)

    df_joined = df_target.merge(df_most_ref_hotel, on=['user_id', 'session_id'], how='left')

    def reorder(x):
        impressions = x['impressions'].copy()
        most_ref_hotel = str(x['most_ref_hotel'])
        if most_ref_hotel in impressions:
            impressions.remove(most_ref_hotel)
            impressions = [most_ref_hotel] + impressions
        return impressions

    df_joined['impressions_reordered'] = df_joined.apply(reorder, axis=1)

    df_out = df_joined[utils.GR_COLS + ['impressions_reordered']]
    df_out['impressions_reordered'] = df_out['impressions_reordered'].apply(lambda x: ' '.join(x))
    df_out.rename(columns={'impressions_reordered': 'item_recommendations'}, inplace=True)

    return df_out
