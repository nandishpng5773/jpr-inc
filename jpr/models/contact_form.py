import sqlalchemy
from datetime import datetime

metadata = sqlalchemy.MetaData()
contact_form = sqlalchemy.Table(
    "contact_form",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True,autoincrement=True),
    sqlalchemy.Column("name", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("mobile", sqlalchemy.String(length=10), nullable=False),
    sqlalchemy.Column("email", sqlalchemy.String(length=100), nullable=False),
    sqlalchemy.Column("message", sqlalchemy.String(length=1000), nullable=False),
    #sqlalchemy.Column("ip_address", sqlalchemy.String(length=100), nullable=False),
    sqlalchemy.Column("browser_type", sqlalchemy.String(length=255), nullable=False),
    sqlalchemy.Column("created_date", sqlalchemy.DateTime, nullable=False)

)

course_category= sqlalchemy.Table(
    "course_category",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column("name", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("description", sqlalchemy.String(length=1000), nullable=False),
    sqlalchemy.Column("created_date", sqlalchemy.DateTime, nullable=False),
    #sqlalchemy.Column("updated_date", sqlalchemy.DateTime, nullable=False)


)

mentor_info = sqlalchemy.Table(
    "mentor_info",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True,autoincrement=True),
    sqlalchemy.Column("mentor_id",sqlalchemy.String(length=50),nullable=True),
    sqlalchemy.Column("first_name", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("last_name", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("education", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("year_of_experience", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("comm_address", sqlalchemy.String(length=255), nullable=True),
    sqlalchemy.Column("permanent_address", sqlalchemy.String(length=250), nullable=True),
    sqlalchemy.Column("gender", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("comm_city", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("comm_state", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("comm_landmark", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("comm_mobile", sqlalchemy.String(length=10), nullable=True),
    sqlalchemy.Column("permanent_city", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("permanent_state", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("permanent_country", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("alternate_mobile", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("email", sqlalchemy.String(length=100), nullable=True),
    sqlalchemy.Column("permanent_landmark", sqlalchemy.String(length=100), nullable=True),
    sqlalchemy.Column("created_date", sqlalchemy.DateTime, nullable=True),
    sqlalchemy.Column("updated_date", sqlalchemy.DateTime, nullable=True)

)
course_info = sqlalchemy.Table(
    "course_info",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True),
    sqlalchemy.Column("title", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("course_description", sqlalchemy.String(length=250), nullable=True),
    sqlalchemy.Column("course_duration", sqlalchemy.Integer, nullable=True),
    sqlalchemy.Column("language", sqlalchemy.String(length=100), nullable=True),
    sqlalchemy.Column("course_classroom", sqlalchemy.String(length=100), nullable=True),
    sqlalchemy.Column("created_date", sqlalchemy.DateTime, nullable=True),
    sqlalchemy.Column("updated_date", sqlalchemy.DateTime, nullable=True)


)
mentee_info = sqlalchemy.Table(
    "mentee_info",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True,autoincrement=True),
    sqlalchemy.Column("mentee_id",sqlalchemy.String(length=50),nullable=True),
    sqlalchemy.Column("first_name", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("last_name", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("education", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("year_of_experience", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("comm_address", sqlalchemy.String(length=255), nullable=True),
    sqlalchemy.Column("permanent_address", sqlalchemy.String(length=250), nullable=True),
    sqlalchemy.Column("gender", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("comm_city", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("comm_state", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("comm_landmark", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("comm_mobile", sqlalchemy.String(length=10), nullable=True),
    sqlalchemy.Column("permanent_city", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("permanent_state", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("permanent_country", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("alternate_mobile", sqlalchemy.String(length=50), nullable=True),
    sqlalchemy.Column("email", sqlalchemy.String(length=100), nullable=True),
    sqlalchemy.Column("permanent_landmark", sqlalchemy.String(length=100), nullable=True),
    sqlalchemy.Column("created_date", sqlalchemy.DateTime, nullable=True),
    sqlalchemy.Column("updated_date", sqlalchemy.DateTime, nullable=True)

)
