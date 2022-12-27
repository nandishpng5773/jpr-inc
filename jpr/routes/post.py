from pydantic import BaseModel,EmailStr
from fastapi import status,APIRouter,HTTPException
from datetime import datetime
from database import get_database
from models.contact_form import contact_form,course_category, mentor_info, course_info,mentee_info


router = APIRouter()


class UserBase(BaseModel):
    id: int
    name: str
    mobile: str
    email: EmailStr
    message: str
    created_date: datetime


class UserType(UserBase):
    browser_type: str


class CourseCategory(BaseModel):
    id: int
    name: str
    description: str
    created_date: datetime
    #updated_date:datetime


class MentorInfo(BaseModel):
    id:int
    mentor_id:str
    first_name:str
    last_name:str
    education:str
    year_of_experience:str
    comm_address:str
    permanent_address:str
    gender: str
    comm_city:str
    comm_state:str
    comm_landmark:str
    comm_mobile: str
    permanent_city:str
    permanent_state:str
    permanent_country:str
    alternate_mobile:str
    email: EmailStr
    permanent_landmark:str
    created_date:datetime
    updated_date:datetime


class CourseInfo(BaseModel):
    id: int
    title: str
    course_description: str
    course_duration: int
    language: str
    course_classroom: str
    created_date: datetime
    updated_date: datetime


class MenteeInfo(BaseModel):
    id:int
    mentee_id:str
    first_name:str
    last_name:str
    education:str
    year_of_experience:str
    comm_address:str
    permanent_address:str
    gender: str
    comm_city:str
    comm_state:str
    comm_landmark:str
    comm_mobile: str
    permanent_city:str
    permanent_state:str
    permanent_country:str
    alternate_mobile:str
    email: EmailStr
    permanent_landmark:str
    created_date:datetime
    updated_date:datetime



@router.post("/contact_form", status_code=status.HTTP_201_CREATED)
async def register(user: UserType):
    try:
        db = get_database()
        insert_query = contact_form.insert().values(id=user.id,
                                                    name=user.name,
                                                    mobile=user.mobile,
                                                    email=user.email,
                                                    message=user.message,
                                                    created_date=user.created_date,
                                                    browser_type=user.browser_type
                                                    )

        await db.execute(insert_query)
        #print(insert_query)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='enter valid details')



@router.get("/person-data")
async def retrieve_info():
    select_stmt = contact_form.select()
    result = await get_database().fetch_all(select_stmt)
    return result


@router.get("/individual_data")
async def retrieve_mentee_info(mobile: str):
    db = get_database()
    select_query = contact_form.select().where(contact_form.c.mobile == mobile)
    result = await db.fetch_one(select_query)
    #print(result)
    return result


@router.post("/course_category", status_code=status.HTTP_201_CREATED)
async def register(user: CourseCategory):
    try:
        db = get_database()
        insert_query = course_category.insert().values(
                                                    id=user.id,
                                                    name=user.name,
                                                    description=user.description,
                                                    created_date=user.created_date,
                                                    #updated_date=user.updated_date
                                                     )

        await db.execute(insert_query)
        #print(insert_query)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='enter valid details')


@router.get("/course_data")
async def retrieve_info():
    select_stmt = course_category.select()
    result = await get_database().fetch_all(select_stmt)
    return result


@router.get("/")
async def retrieve_course_info(name:str):
    db = get_database()
    select_query = course_category.select().where(course_category.c.name==name)
    result = await db.fetch_one(select_query)
    print(result)
    return result


@router.post("/mentor_info", status_code=status.HTTP_201_CREATED)
async def mentor(user: MentorInfo):
    try:
        db = get_database()
        insert_query = mentor_info.insert().values(
                                                   id=user.id,
                                                   mentor_id=user.mentor_id,
                                                   first_name=user.first_name,
                                                   last_name=user.last_name,
                                                   education=user.education,
                                                   year_of_experience=user.year_of_experience,
                                                   comm_address=user.comm_address,
                                                   permanent_address=user.permanent_address,
                                                   gender=user.gender,
                                                   comm_city=user.comm_city,
                                                   comm_state=user.comm_state,
                                                   comm_mobile=user.comm_mobile,
                                                   comm_landmark=user.comm_landmark,
                                                   permanent_city=user.permanent_city,
                                                   permanent_state=user.permanent_state,
                                                   permanent_country=user.permanent_country,
                                                   alternate_mobile=user.alternate_mobile,
                                                   email=user.email,
                                                   permanent_landmark=user.permanent_landmark,
                                                   created_date=user.created_date,
                                                   updated_date=user.updated_date
                                                   )

        await db.execute(insert_query)
        #print(insert_query)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='enter valid details')


@router.get("/mentor_data")
async def mentor_information():
    select_stmt = mentor_info.select()
    result = await get_database().fetch_all(select_stmt)
    return result


@router.get("/trainer_info")
async def trainer_info(mentor_id: str):
    db = get_database()
    select_query = mentor_info.select().where(mentor_info.c.mentor_id == mentor_id)
    result = await db.fetch_one(select_query)
    print(result)
    return result


@router.post("/courses_info", status_code=status.HTTP_201_CREATED)
async def course(user: CourseInfo):
    try:
        db = get_database()
        insert_query = course_info.insert().values(
                                                        id=user.id,
                                                        title=user.title,
                                                        course_description=user.course_description,
                                                        course_duration=user.course_duration,
                                                        language=user.language,
                                                        course_classroom=user.course_classroom,
                                                        created_date=user.created_date,
                                                        updated_date=user.updated_date
                                                    )

        await db.execute(insert_query)
        print(insert_query)

    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='enter valid details')


@router.get("/course_info")
async def courses_data():
    select_stmt=course_info.select()
    result = await get_database().fetch_all(select_stmt)
    return result

@router.get("/data")
async def course_data(title:str):
    db=get_database()
    select_stmt=course_info.select().where(course_info.c.title == title)
    result=await db.fetch_one(select_stmt)
    print(result)
    return result


@router.post("/mentee_info", status_code=status.HTTP_201_CREATED)
async def mentor(user: MenteeInfo):
    try:
        db = get_database()
        insert_query = mentee_info.insert().values(
                                                   id=user.id,
                                                   mentee_id=user.mentee_id,
                                                   first_name=user.first_name,
                                                   last_name=user.last_name,
                                                   education=user.education,
                                                   year_of_experience=user.year_of_experience,
                                                   comm_address=user.comm_address,
                                                   permanent_address=user.permanent_address,
                                                   gender=user.gender,
                                                   comm_city=user.comm_city,
                                                   comm_state=user.comm_state,
                                                   comm_mobile=user.comm_mobile,
                                                   comm_landmark=user.comm_landmark,
                                                   permanent_city=user.permanent_city,
                                                   permanent_state=user.permanent_state,
                                                   permanent_country=user.permanent_country,
                                                   alternate_mobile=user.alternate_mobile,
                                                   email=user.email,
                                                   permanent_landmark=user.permanent_landmark,
                                                   created_date=user.created_date,
                                                   updated_date=user.updated_date
                                                   )

        await db.execute(insert_query)
        #print(insert_query)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='enter valid details')


@router.get("/mentee")
async def mentee_data():
    select_stmt=mentor_info.select()
    result=await get_database().fetch_all(select_stmt)
    return result


@router.get("/mentee-data")
async def student_data(mentee_id: str):
    db = get_database()
    select_stmt = mentee_info.select().where(mentee_info.c.mentee_id == mentee_id)
    result=await db.fetch_one(select_stmt)
    print(result)
    return result
