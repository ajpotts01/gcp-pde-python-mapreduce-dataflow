import argparse
import os

from common.execute_pipeline import execute_pipeline
from common.pipeline_config import setup_pipeline_config


def clear_folder(path: str):
    """
    Deletes all files in the selected path.

    :param str target: path to clear out.
    """
    for next_file in os.listdir(path):
        # Just supplying the filename to the os methods is not sufficient
        full_path: str = f"{path}/{next_file}"
        print(f"Deleting {next_file}")
        if os.path.isfile(full_path):
            os.remove(full_path)


def run():
    options: argparse.Namespace = None
    pipeline_args: list[str] = None

    options, pipeline_args = setup_pipeline_config()

    clear_folder("../results")

    execute_pipeline(
        arguments=pipeline_args,
        input_path=options.input,
        output_path=options.output_prefix,
    )


if __name__ == "__main__":
    run()
