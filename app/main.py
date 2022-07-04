from fastapi import FastAPI
from fastapi import Depends, Form, Request
from fastapi.staticfiles import StaticFiles

from sqlalchemy.orm import Session
from .database import get_db
from .routers import crud
from .model import Product
from fastapi.templating import Jinja2Templates
from fastapi.encoders import jsonable_encoder
from fastapi.responses import HTMLResponse
from . import model, database

try:
    model.Base.metadata.create_all(bind=database.engine)
    print("database conncetion succefull")
except Exception as exc:
    print("could'nt connect to database")
    print(exc)



app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory='templates')


@app.get("/product")
def product_list(request:Request, db:Session=Depends(get_db)):
    products = crud.product_list(db=db)
    return templates.TemplateResponse("list.html", {"request":request,
                                                    "product":jsonable_encoder(products)})


@app.get("/product/form")
def form_post(request:Request):
    return templates.TemplateResponse('form.html', context={'request':request})

@app.post('/product/form')
def form_post(request:Request, name:str=Form(...),
            description:str=Form(...),
            url:str = Form(...),
            price:float=Form(...),
            db:Session=Depends(get_db)):
    result = Product(name=name, description=description,url=url,price=price)
    db.add(result)
    db.commit()
    db.refresh(result)
    return templates.TemplateResponse('form.html', context={'request':request, 'result':result})