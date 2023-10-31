from fastapi import FastAPI

import models
from database import engine
from routers import auth, todos, admin, users

app = FastAPI()

# CREATE DATABASE
# dynamically create a database  w/o having to write sql queries
# creates everything from database.py and models.py files
# to be able to create a new db with a table of todos w
# of the columns we laid out w our models.py file
# this only runs if the db does not exist
models.Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(users.router)







