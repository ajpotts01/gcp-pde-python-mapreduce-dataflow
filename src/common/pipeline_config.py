import argparse
import os


def setup_pipeline_config(cloud: bool=False) -> tuple[argparse.Namespace, list[str]]:
    ENV_KEY_PROJECT = "GCP_PROJECT"
    ENV_GCS_BUCKET = "GCS_BUCKET"

    config: argparse.ArgumentParser = argparse.ArgumentParser(
        description="Find most-used Java packages in sample code"
    )

    input_path: str = "..\search_files\*.java"
    output_path: str = "../results/result"

    if (cloud):
        project: str = os.getenv(ENV_KEY_PROJECT) # Assumes environment variables already loaded
        bucket: str = os.getenv(ENV_GCS_BUCKET)
        job_name: str = "gcp-pde-python-mapreduce-dataflow" 
        region: str = "australia-southeast1"
        runner: str = "DataFlowRunner"
        setup_file: str = "./setup.py"
        staging_path: str = f"gs://{bucket}/staging"

        input_path = f"gs://{bucket}/search_files/*.java"
        output_path = f"gs://{bucket}/results/results"

        config.add_argument(
            "--project", default=project,
            help="GCP project to run in"
        )

        config.add_argument(
            "--job_name", default=job_name,
            help="Dataflow job name in GCP"
        )

        # config.add_argument(
        #     "--save_main_session", default="True"
        # )

        config.add_argument(
            "--staging_location", default=staging_path,            
        )

        config.add_argument(
            "--temp_location", default=staging_path,            
        )        

        config.add_argument(
            "--region", default=region,            
        )

        config.add_argument(
            "--runner", default=runner,            
        )        

        config.add_argument(
            "--setup_file", default=setup_file,            
        )        

    config.add_argument(
        "--output-prefix",
        default=output_path,
        help="Output destination - both path and prefix",
    )

    # Since this pipeline searches for *.java at execution time,
    # a backslash is required for the path here. Appears to be a Beam bug.
    # https://stackoverflow.com/questions/56584908/apache-beam-readfromtext-pattern-match-returns-no-results
    config.add_argument(
        "--input",
        default=input_path,
        help="Input directory - containing sample Java files",
    )

    return config.parse_known_args()
