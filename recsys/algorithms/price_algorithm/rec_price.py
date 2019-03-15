import recsys.algorithms.utils as utils


def calc_recommendation(df_expl):
    """Calculate recommendations based on price of items.

    The final data frame will have an impression list sorted according to the price per item in a reference data frame.

    :param df_expl: Data frame with exploded impression and price list
    :return: Data frame with sorted impression list according to price
    """

    sorted_idx = df_expl.groupby(utils.GR_COLS)['prices'].transform(lambda grp: grp.sort_values().index)
    df_sorted = df_expl.reindex(sorted_idx.rename(None))

    df_sorted['impressions'] = df_sorted['impressions'].apply(str)

    df_out = utils.group_concat(df_sorted, utils.GR_COLS, "impressions")
    df_out.rename(columns={'impressions': 'item_recommendations'}, inplace=True)

    return df_out
