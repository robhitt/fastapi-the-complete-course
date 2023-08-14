from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Path
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from starlette import status

from database import SessionLocal
from models import Todos

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        # The field means only the code prior to and incl
        # the yield statement is executed before sending a response
        yield db
    finally:
        # after the response has been delivered
        db.close()


# Annotated is from the typing package
# 'Depends' is dependency injection, do something before we execute
# I.e., this session relies on get_db to do some work behind the scenes
# before we can then utilize it
db_dependency = Annotated[Session, Depends(get_db)]


# Pydantic Request Schema
# We don't pass in the id to allow the
# database to autoincrement the id
class TodoRequest(BaseModel):
    title: str = Field(min_length=3)
    description: str = Field(min_length=3, max_length=100)
    priority: int = Field(gt=0, lt=6)
    complete: bool

    class Config:
        schema_extra = {
            "example":  {
                "title": "Learn FastAPI",
                "description": "Fast Api Tutorial",
                "priority": "5",
                "complete": False
            }
        }


@router.get("/", status_code=status.HTTP_200_OK)
async def read_all(db: db_dependency):
    return db.query(Todos).all()


@router.get("/todo/{todo_id}", status_code=status.HTTP_200_OK)
async def read_todo(db: db_dependency, todo_id: int = Path(gt=0)):

    todo_model = db.query(Todos).filter((Todos.id == todo_id)).one()

    if todo_model is not None:
        return todo_model

    raise HTTPException(status_code=404, detail='Todo not found.')


@router.post("/todo", status_code=status.HTTP_201_CREATED)
async def create_todo(db: db_dependency, todo_request: TodoRequest):
    todo_model = Todos(**todo_request.dict())
    db.add(todo_model)
    db.commit()


@router.put("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_todo(db: db_dependency,
                      todo_request: TodoRequest,
                      todo_id: int = Path(gt=0)):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()
    if todo_model is None:
        raise HTTPException(status_code=404, detail='Todo not found.')

    # by assigning the request to the currently existing
    # todo_model, and then adding the todo_model, sqlalchemy knows
    # not to create a new item but rather simply update the existing
    todo_model.title = todo_request.title
    todo_model.description = todo_request.description
    todo_model.priority = todo_request.priority
    todo_model.complete = todo_request.complete

    db.add(todo_model)
    db.commit()


@router.delete("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(db: db_dependency, todo_id: int = Path(gt=0)):
    todo_model = db.query(Todos).filter(Todos.id == todo_id).first()

    if todo_model is None:
        raise HTTPException(status_code=404, detail="todo not found")

    db.query(Todos).filter(Todos.id == todo_id).delete()

    db.commit()