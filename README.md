# airflow-demo
A demo of an airflow based project

## How to run
1. In the airflow-demo directory, run the following command. This will create a Airflow UID
`echo -e "AIRFLOW_UID=$(id -u)" > .env`
2. Initiate the airflow database if you haven't already done so in the terminal:
`docker compose up airflow-init`
3. Run `docker compose up`
4. Once airflow is started up after a few minutes, in your browser log into `http://localhost:8080` and use the default username:password `airflow:airflow`