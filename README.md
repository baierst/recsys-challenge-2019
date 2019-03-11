# Get the data

Download the data from Slack and store under `data`

## Installation and usage

Create a virtual environment:

    python3 -m venv recsys_env
    source trvrecsys2019/bin/activate

Install the package:

    pip install -e .
    
### Getting started notebook

Checkout the `notebooks/getting_started.ipynb` to get familiar with the data and the task.

### Baseline algorithm
To execute the code for the baseline algorithm, run::

    rec-popular --data-path=<path-to-csv-files-directory>

### Verify submission
To execute the code to verify the submission format, run::

    verify-submission --data-path=<path-to-csv-files-directory> --submission-file <name-of-submission-file> --test-file <name-of-provided-test-file>


### Score submission
To execute the code to score the submission, run::

    score-submission --data-path=<path-to-csv-files-directory> --submission-file <name-of-submission-file> --ground-truth-file <name-of-ground-truth-file>

Note that there will be no ground truth file provided. The script rather illustrates the usage and calculation of the error metric and can be used for testing purposes on holdout data created by the participants.
