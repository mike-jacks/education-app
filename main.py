from sqlalchemy import create_engine, text, insert, Table
from sqlalchemy.orm import Session

sqlite_name = "sqlite+pysqlite:///education.db"

engine = create_engine(sqlite_name, echo=True)

create_students_table = """
CREATE TABLE students (
    student_id Integer primary key,
    first_name text, 
    last_name text,
    email text,
    enrollment_year Integer
    )
"""

insert_student = """
INSERT INTO students (first_name, last_name, email, enrollment_year)
VALUES ("Mike", "Jacks", "mikejacks@email.com", 2024);
"""


with engine.connect() as conn:
    # t = text(create_students_table)
    # result = conn.execute(t)
    # conn.commit()
    conn.execute(text(insert_student))
    conn.commit()
    results = conn.execute(text("select * from students").execution_options(autoflush=True))
    print(results.all())


