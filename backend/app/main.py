from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import services, models
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Readen API")

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/books/")
def read_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    books = services.get_books(db, skip=skip, limit=limit)
    return books

@app.get("/books/{book_id}")
def read_book(book_id: int, db: Session = Depends(get_db)):
    db_book = services.get_book(db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book
