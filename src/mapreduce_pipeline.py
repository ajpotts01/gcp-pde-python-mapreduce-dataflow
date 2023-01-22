import argparse

from common.execute_pipeline import execute_pipeline
from common.pipeline_config import setup_pipeline_config


def run():
    options: argparse.Namespace = None
    pipeline_args: list[str] = None

    options, pipeline_args = setup_pipeline_config()

    execute_pipeline(
        arguments=pipeline_args,
        input_path=options.input,
        output_path=options.output_prefix,
    )


if __name__ == "__main__":
    run()
