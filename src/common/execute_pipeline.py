# Standard lib imports
import os

# Project lib imports
from common.pipeline_methods import simple_grep, count_package_use

# Third-party lib imports
import apache_beam as beam
from apache_beam.transforms.combiners import Top


def execute_pipeline(arguments: list[str], input_path: str, output_path: str):
    """
    Main pipeline. Uses a beam.FlatMap call + a simple grep generator method to demonstrate pulling search terms out of lines of text.

    :param list[str] arguments: Pipeline arguments per the Apache Beam/GCP Dataflow standard.
    """
    print("Started pipeline")
    print(arguments)
    search_term = "import"

    #java_input = f"{input_path}\*.java"

    # Important note:
    # If running a beam pipeline with a context manager, calling run() or wait_until_finish() is not necessary.
    # This runs as part of the context manager cleanup.
    with beam.Pipeline(argv=arguments) as pipeline:
        (
            pipeline
            | "read_java_files" >> beam.io.ReadFromText(file_pattern=input_path)
            | "find_imports"
            >> beam.FlatMap(
                lambda next_line: simple_grep(
                    text_line=next_line, search_term=search_term
                )
            )
            | "count_package_use"
            >> beam.FlatMap(
                lambda next_line: count_package_use(
                    text_line=next_line, search_term=search_term
                )
            )
            | "total_package_use" >> beam.CombinePerKey(fn=sum)
            | "get_top_5" >> Top.Of(n=5, key=lambda kv: kv[1])
            | "write_to_file" >> beam.io.WriteToText(file_path_prefix=output_path)
        )
