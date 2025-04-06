import pendulum
from airflow import DAG
from airflow.decorators import dag, task

@dag(
    schedule="0 21 * * *",
    start_date=pendulum.datetime(2025, 1, 1, tz="Asia/Seoul"),
    catchup=False,
)
def example_bash_dag():
    @task.bash
    def bash_example():
        return "echo 'Hello, World!'"
    
    bash_example()

example_bash_dag()