import recsys.algorithms.utils as utils


def calc_recommendation(df_expl):
    """Calculate recommendations based on order of impressions.

    The final data frame will have an impression list sorted according the order the impressions have been shown.

    :param df_expl: Data frame with exploded impressions and impression_orders
    :return: Data frame with sorted impression list according to impression order
    """

    sorted_idx = df_expl.groupby(utils.GR_COLS)['orders_impressions'].transform(lambda grp: grp.sort_values().index)
    df_sorted = df_expl.reindex(sorted_idx.rename(None))

    df_sorted['impressions'] = df_sorted['impressions'].apply(str)

    df_out = utils.group_concat(df_sorted, utils.GR_COLS, "impressions")
    df_out.rename(columns={'impressions': 'item_recommendations'}, inplace=True)

    return df_out
