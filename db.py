from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()  

db_connections = os.getenv("DB_CONNECTION_STR")
engine = create_engine(db_connections)


def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * from jobs"))
        jobs = []
        for row in result.all():
            print()
            jobs.append(row._asdict())
        return jobs

def load_job_from_db(id):
    with engine.connect() as conn:
        result = conn.execute(text("Select * from jobs where id = :val"), {"val": id})
        rows = result.all()
        if len(rows) == 0:
            return None
        else:
            return rows[0]._asdict()