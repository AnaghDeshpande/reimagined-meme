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
    
def add_application_to_db(job_id, data):
    with engine.connect() as conn:
        query = text(
            "INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url)" \
            "VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)"
        )

        conn.execute(query, {
            "job_id": job_id,
            "full_name": data["full_name"],
            "email": data["email"],
            "linkedin_url": data["linkedin_url"],
            "education": data["education"],
            "work_experience": data["work_experience"],
            "resume_url": data["resume_url"]
        })

        conn.commit()