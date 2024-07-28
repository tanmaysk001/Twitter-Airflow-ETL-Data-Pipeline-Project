FROM apache/airflow:2.5.0

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY dags /opt/airflow/dags
COPY scripts /opt/airflow/scripts
COPY config /opt/airflow/config

ENV AIRFLOW__CORE__LOAD_EXAMPLES=False
