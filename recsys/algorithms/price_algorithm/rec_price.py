



def calc_recommendation(df_expl_impressions, df_expl_prices):
    """Calculate recommendations based on price of items.

    The final data frame will have an impression list sorted according to the price per item in a reference data frame.

    :param df_expl_impressions: Data frame with exploded impression list
    :param df_expl_price: Data frame with exploded price list
    :return: Data frame with sorted impression list according to price
    """

    df_expl_clicks = (
        df_expl[GR_COLS + ["impressions"]]
        .merge(df_pop,
               left_on="impressions",
               right_on="reference",
               how="left")
    )

    df_out = (
        df_expl_clicks
        .assign(impressions=lambda x: x["impressions"].apply(str))
        .sort_values(GR_COLS + ["n_clicks"],
                     ascending=[True, True, True, True, False])
    )

    df_out = group_concat(df_out, GR_COLS, "impressions")
    df_out.rename(columns={'impressions': 'item_recommendations'}, inplace=True)

    return df_out
