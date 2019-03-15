from pathlib import Path

import click
import pandas as pd
from recsys.config import Config

from . import rec_price as rec
from .. import utils


@click.command()
@click.option('--data-path', default=None, help='Directory for the CSV files')
def main(data_path):

    config = Config()

    # calculate path to files
    default_data_directory = config.data_path
    data_directory = Path(data_path) if data_path else default_data_directory
    test_csv = data_directory.joinpath('test.csv')
    subm_csv = data_directory.joinpath('submission_price.csv')

    print(f"Reading {test_csv} ...")
    df_test = pd.read_csv(test_csv)

    print("Identify target rows...")
    df_target = utils.get_submission_target(df_test)

    print("Get recommendations...")
    df_expl = utils.explode(df_target, ["prices", "impressions"])
    df_out = rec.calc_recommendation(df_expl)

    print(f"Writing {subm_csv}...")
    df_out.to_csv(subm_csv, index=False)

    print("Finished calculating recommendations.")


if __name__ == '__main__':
    main()
