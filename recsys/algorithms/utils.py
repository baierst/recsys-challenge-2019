import math
import pandas as pd
import numpy as np
from typing import *

GR_COLS = ["user_id", "session_id", "timestamp", "step"]


def get_submission_target(df):
    """Identify target rows with missing click outs."""

    mask = df["reference"].isnull() & (df["action_type"] == "clickout item")
    df_out = df[mask]

    return df_out


def string_to_array(s):
    """Convert pipe separated string to array."""

    if isinstance(s, str):
        out = s.split("|")
    elif math.isnan(s):
        out = []
    else:
        raise ValueError("Value must be either string of nan")
    return out


def explode(df_in: pd.DataFrame, cols_expl: List[str])->pd.DataFrame:
    """Explode column col_expl of array type into multiple rows."""

    if type(cols_expl) != list:
        cols_expl = [cols_expl]

    df = df_in.copy()

    for col_expl in cols_expl:
        df.loc[:, col_expl] = df[col_expl].apply(string_to_array)

    df_out = pd.DataFrame(
        {col: np.repeat(df[col].values,
                        df[col_expl].str.len())
         for col in df.columns.drop(cols_expl)}
    )

    for col_expl in cols_expl:
        df_out.loc[:, col_expl] = np.concatenate(df[col_expl].values)
        df_out.loc[:, col_expl] = df_out[col_expl].apply(int)

    return df_out


def group_concat(df, gr_cols, col_concat):
    """Concatenate multiple rows into one."""

    df_out = (
        df
        .groupby(gr_cols)[col_concat]
        .apply(lambda x: ' '.join(x))
        .to_frame()
        .reset_index()
    )

    return df_out
