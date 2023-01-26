import argparse


def setup_pipeline_config() -> tuple[argparse.Namespace, list[str]]:
    config: argparse.ArgumentParser = argparse.ArgumentParser(
        description="Find most-used Java packages in sample code"
    )

    config.add_argument(
        "--output-prefix",
        default="../results/result",
        help="Output destination - both path and prefix",
    )

    # Since this pipeline searches for *.java at execution time,
    # a backslash is required for the path here. Appears to be a Beam bug.
    # https://stackoverflow.com/questions/56584908/apache-beam-readfromtext-pattern-match-returns-no-results
    config.add_argument(
        "--input",
        default="..\search_files",
        help="Input directory - containing sample Java files",
    )

    return config.parse_known_args()
