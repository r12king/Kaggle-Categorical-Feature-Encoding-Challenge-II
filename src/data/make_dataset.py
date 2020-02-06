# -*- coding: utf-8 -*-
import logging
import pandas as pd


def main(input_filepath, output_filepath):
    """ Runs data processing scripts to turn raw data from (../raw) into
        cleaned data ready to be analyzed (saved in ../processed).
    """
    logger = logging.getLogger(__name__)
    logger.info('making final data set from raw data')

    # read in training data
    logger.info('reading in data from: {}'.format(input_filepath))
    df_training = pd.read_csv("{}/train.csv".format(input_filepath))
    df_test = pd.read_csv("{}/test.csv".format(input_filepath))

    # save to output directory
    logger.info('saving data to: {}'.format(output_filepath))
    df_training.to_csv(path_or_buf="{}/train.csv".format(output_filepath), index=False, header=True)
    df_test.to_csv(path_or_buf="{}/test.csv".format(output_filepath), index=False, header=True)

    logger.info('make_datasets.py is complete!')

    return None


if __name__ == '__main__':
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    print(log_fmt)
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    main(input_filepath="data/raw", output_filepath="data/processed")
