# Twitter ETL Project with Apache Airflow

This project aims to build an ETL (Extract, Transform, Load) pipeline using Apache Airflow. The pipeline extracts data from the Twitter API, transforms it by cleaning the tweets, and then loads the processed data into an Amazon S3 bucket.

## Table of Contents

- [Project Structure](#project-structure)
- [Setup](#setup)
- [Configuration](#configuration)
- [Running the Project](#running-the-project)
- [Airflow DAG](#airflow-dag)
- [Contributing](#contributing)
- [License](#license)

## Project Structure

```
twitter_etl_project/
├── dags/
│   ├── twitter_etl_dag.py
├── scripts/
│   ├── twitter_extraction.py
│   ├── data_transformation.py
│   ├── data_loading.py
├── logs/
├── config/
│   ├── config.py
│   ├── .env
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
```

- **dags/**: Contains the Airflow DAG.
- **scripts/**: Contains the scripts for data extraction, transformation, and loading.
- **logs/**: Directory for Airflow logs.
- **config/**: Contains configuration files and environment variables.
- **requirements.txt**: List of Python dependencies.
- **Dockerfile**: Dockerfile to set up the Airflow environment.
- **docker-compose.yml**: Docker Compose file to run the project.

## Setup

### Prerequisites

- Docker
- Docker Compose

### Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/twitter_etl_project.git
    cd twitter_etl_project
    ```

2. Install the required Python packages:

    ```sh
    pip install -r requirements.txt
    ```

3. Set up the `.env` file:

    ```sh
    cp config/.env.example config/.env
    ```

   Then, fill in the `.env` file with your Twitter API and AWS credentials.

### Configuration

In the `config` directory, the `config.py` file loads environment variables from the `.env` file.

**config/config.py**:

```python
import os
from dotenv import load_dotenv

# Load the .env file from the config directory
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

TWITTER_API_KEY = os.getenv('TWITTER_API_KEY')
TWITTER_API_SECRET_KEY = os.getenv('TWITTER_API_SECRET_KEY')
TWITTER_ACCESS_TOKEN = os.getenv('TWITTER_ACCESS_TOKEN')
TWITTER_ACCESS_SECRET = os.getenv('TWITTER_ACCESS_SECRET')
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_S3_BUCKET_NAME = os.getenv('AWS_S3_BUCKET_NAME')
```

## Running the Project

1. Build and start the Docker containers:

    ```sh
    docker-compose up --build
    ```

2. Access the Airflow web interface at `http://localhost:8080`.

3. Trigger the DAG `twitter_etl_dag` manually or wait for the scheduled run.

## Airflow DAG

The Airflow DAG (`twitter_etl_dag.py`) orchestrates the ETL pipeline. It contains tasks for extracting, transforming, and loading the data.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have any improvements or new features to add.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
