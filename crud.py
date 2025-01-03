from sqlalchemy.orm import Session
from models import Blog
from database import get_db
# from main import app
from schemas import Blog_Pyd,Blog_up
from fastapi import Depends,status,Response, HTTPException, APIRouter,FastAPI

crud_router = APIRouter()

#  for the APIROuter we have tags, prefix etc

app = FastAPI()

@app.post('/createblog')
# @crud_router.post('/createblog/test/')
def create_blog(request:Blog_Pyd):
    if request.name and request.price:
        return f"blog title: {request.title},price:{request.price},description:{request.description}"
    return f"blog title: {request.title},price:{request.price}"


@app.post("/blogs/", response_model=Blog_Pyd)
# @crud_router.post("/blogs/", response_model=Blog_Pyd)
def post_blog(blog: Blog_Pyd, db: Session = Depends(get_db)):
    db_blog = Blog(id = blog.id,name=blog.name, price=blog.price, author= blog.author)
    db.add(db_blog)
    db.commit()
    db.refresh(db_blog)  # Refresh to get the auto-generated id
    return db_blog


# @app.post("/create_blog/",status_code=status.HTTP_201_CREATED)
@crud_router.post("/create_blog/",status_code=status.HTTP_201_CREATED)
def create_blog(request:Blog_Pyd,db:Session=Depends(get_db)):
    new_blog = Blog(id = request.id,name=request.name, price=request.price, author= request.author)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

# @app.get("/get_blog/{id}/",status_code=200)
@crud_router.get("/get_blog/{id}/",status_code=200)
def get_blog(id,response = Response, db:Session=Depends(get_db)):
    # blog = db.query(models.Blog).all()  // for all
    blog = db.query(Blog).filter(Blog.id == id).first()
    if not blog:
    #     response.status_code = status.HTTP_404_NOT_FOUND
    #     return {"comment":f"blog with id {id} is not found"}
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"comment":"blog with id {id}- is not found"})

    return blog

# @app.get("/get_blogs/")
@crud_router.get("/get_blogs/")
def get_blog(db:Session=Depends(get_db)):
    blog = db.query(Blog).all()   # for all
    # blog = db.query(Blog).filter(Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"comment":"blog with id {id}- is not found"})
        # Response.status_code = status.HTTP_404_NOT_FOUND
        # return {"comment":"blog with id {id} is not found"}
    return blog

# @app.put("/update_blog/{id}/")
@crud_router.put("/update_blog/{id}/")
def update_blog(request:Blog_up,db: Session= Depends(get_db)):
    blog = db.query(Blog).filter(Blog.id == request.id)
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"comment":"blog with id {id}- is not found"})
    update_blog = request.dict(exclude_unset=True)
    blog.update(update_blog)
    db.commit()
    return "updated"

    