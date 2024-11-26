from sqlalchemy.orm import Session
from models import Blog
from database import get_db
from main import app,Blog_Pyd
from fastapi import Depends


@app.post('/createblog')
def create_blog(request:Blog_Pyd):
    if request.name and request.price:
        return f"blog title: {request.title},price:{request.price},description:{request.description}"
    return f"blog title: {request.title},price:{request.price}"


@app.post("/blogs/", response_model=Blog_Pyd)
def post_blog(blog: Blog_Pyd, db: Session = Depends(get_db)):
    db_blog = Blog(id = blog.id,name=blog.name, price=blog.price, author= blog.author)
    db.add(db_blog)
    db.commit()
    db.refresh(db_blog)  # Refresh to get the auto-generated id
    return db_blog