# Snowflake CI/CD Demo

This repository demonstrates a CI/CD pipeline to deploy `.sql`, `.py`, and notebook files to Snowflake stages using Jenkins.

## Directory Structure
- **sql/**: Contains SQL files for database operations.
- **scripts/**: Python scripts for data processing.
- **notebooks/**: Jupyter notebooks for analysis.
- **tests/**: Unit and integration tests.

## Usage
1. Clone the repository.
2. Configure SnowSQL connections in your environment.
3. Run the Jenkins pipeline to test, update, and execute files.

## Pipeline Features
- Validates SQL, Python scripts, and notebooks.
- Deploys files to Snowflake's `PROD_NOTEBOOK_STAGE`.
- Sends email notifications upon success or failure.
