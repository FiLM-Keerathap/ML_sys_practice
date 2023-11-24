## Directory Structure

```
.
├── CHANGELOG.md
├── docker
│   ├── Dockerfile.base
│   └── Dockerfile.test
├── Makefile
├── mypy.ini
├── poetry.lock
├── pyproject.toml
├── pytest.ini
├── README.md
├── src
│   ├── components
│   │   ├── calculate_training_decision.py
│   │   ├── load_dataset.py
│   │   ├── model_evaluation.py
│   │   ├── model_prediction.py
│   │   ├── model_training.py
│   │   ├── postprocessing.py
│   │   ├── preprocessing.py
│   │   ├── prerequisite.py
│   │   ├── validate_data.py
│   │   └── write_append_to_bq.py
│   ├── config.py
│   ├── configs
│   │   ├── data_validation.yaml
│   │   ├── hyperparameter_tuning.yaml
│   │   └── settings.yaml
│   ├── jobs
│   │   ├── hyperparameter_tuning.py
│   │   ├── model_evaluation.py
│   │   ├── model_prediction.py
│   │   ├── model_training.py
│   │   ├── postprocessing.py
│   │   └── preprocessing.py
│   ├── main.ipynb
│   ├── main.py
│   ├── pipeline.py
│   ├── pipeline_templates
│   │   ├── demand_forecast_pipeline_dev.json
│   │   └── demand_forecast_pipeline_local.json
│   ├── queries
│   │   ├── dense.sql
│   │   ├── sparse.sql
│   │   ├── unitconv.sql
│   │   ├── very_dense.sql
│   │   └── very_sparse.sql
│   ├── trigger_function
│   │   ├── main.py
│   │   └── requirements.txt
│   └── utils
│       ├── calculation.py
│       ├── hyperparameter_tuning.py
│       ├── __init__.py
│       ├── pipeline_parameter.py
│       ├── preprocess.py
│       └── storage.py
└── tests
    ├── assets
    │   └── mock_unprocessed_dataset.csv
    └── unit_tests
        ├── jobs
        │   ├── test_model_evaluation.py
        │   ├── test_model_prediction.py
        │   ├── test_model_training.py
        │   ├── test_postprocessing.py
        │   └── test_preprocessing.py
        └── utils
            ├── test_calculation.py
            ├── test_hyperparameter_tuning.py
            ├── test_pipeline_parameter.py
            ├── test_preprocess.py
            ├── test_storage.py
            └── test_utils.py
```