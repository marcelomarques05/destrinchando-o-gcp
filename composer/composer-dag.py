from datetime import datetime, timedelta
from textwrap import dedent
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'Composer Example',
    'depends_on_past': False,
    'email': ['email@composer.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

with DAG(
        'destrinchando-composer',
        default_args=default_args,
        description='Hello DAG',
        schedule_interval=datetime(2021, 1, 1),
        catchup=False,
        tags=['destrinchando-o-gcp']
        ) as dag:

    # Print the dag_run id from the Airflow logs
    t1 = BashOperator(
        task_id='print_t1',
        bash_command='date',
        )

    t2 = BashOperator(
        task_id='sleep',
        depends_on_past=False,
        bash_command='sleep 5',
        retries=3,
        )
    t1.doc_md = dedent(
      """\
    #### Task Documentation
    You can document your task using the attributes doc_m* (markdown),
    'doc' (plain text), 'doc_rst', 'doc_json', 'doc_yaml' which gets rendered in the UI's Task Instance Details page.
    ! [img] (http: //montcs.bloomu.edu/~bobmon/Semesters/2012-01/491/import%20soul.png)
    """
    )

    dag.doc_md = __doc__
    dag.doc_md = """
    This is a documentation placed anywhere
    """
    templated_command = dedent(
      """
    {% for i in range (5) %}
        echo "{{ ds }}"
        echo "{{ macros.ds_add(ds, 7)}}"
        echo "{{ params.my_param }}"
    {% endfor %}
    """
    )

    t3 = BashOperator (
      task_id='templated',
      depends_on_past=False,
      bash_command=templated_command,
      params={'my_param': 'Parameter I passed in'},
)

t1 >> [t2, t3]
