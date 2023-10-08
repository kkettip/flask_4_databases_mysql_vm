from flask import Flask, render_template
from pandas import read_sql
import pandas as pd
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, inspect
import sqlalchemy

app = Flask(__name__)


load_dotenv()  # Load environment variables from .env file

# Database connection settings from environment variables
DB_HOST = os.getenv("DB_HOST")
DB_DATABASE = os.getenv("DB_DATABASE")
DB_USERNAME = os.getenv("DB_USERNAME")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_PORT = int(os.getenv("DB_PORT", 3306))
DB_CHARSET = os.getenv("DB_CHARSET", "utf8mb4")

# Connection string
conn_string = (
    f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"
    f"?charset={DB_CHARSET}"
)

# Create a database engine
db_engine = create_engine(conn_string, echo=False)



@app.route('/')
def index():
    query_patients = "SELECT * FROM patients limit 10"
    df_patients = read_sql(query_patients, db_engine)
    patients = df_patients.to_dict(orient='records')
   

    query_conditions = "SELECT * FROM conditions limit 10"
    df_conditions = read_sql(query_conditions, db_engine)
    conditions = df_conditions.to_dict(orient='records')

    query_patient_conditions = "SELECT * FROM patient_conditions limit 10"
    df_patient_conditions= read_sql(query_patient_conditions, db_engine)
    patient_conditions = df_patient_conditions.to_dict(orient='records')
    

    return render_template('index.html', patients=patients, conditions=conditions, patient_conditions=patient_conditions)

if __name__ == '__main__':
    app.run(
        debug=True,
        port=3306
        )