import argparse
import os

from common.execute_pipeline import execute_pipeline
from common.pipeline_config import setup_pipeline_config

from dotenv import load_dotenv

def clear_folder(path: str):
    pass # TODO: Clear out GCS Bucket?


def run():
    ENV_PATH = 'pipeline.env'
    RESULTS_PATH = '../results'

    options: argparse.Namespace = None
    pipeline_args: list[str] = None

    clear_folder(RESULTS_PATH)
    load_dotenv(ENV_PATH)

    options, pipeline_args = setup_pipeline_config(cloud=True)
    opts_list = [f"--{x}={y}" for x, y in vars(options).items() if (x != "input" and x != "output_prefix")]
    #print(opts_list)
    execute_pipeline(
        arguments=opts_list,
        input_path=options.input,
        output_path=options.output_prefix,
    )


if __name__ == "__main__":
    run()
