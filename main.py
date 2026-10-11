# from fastapi import FastAPI,Request,Form
# from fastapi.templating import Jinja2Templates
# from fastapi.responses import HTMLResponse
# from database import get_connection

# app=FastAPI()
# templates=Jinja2Templates(directory="templates")
# @app.get("/",response_class=HTMLResponse)
# def home():
#     sai_hi="Hello,Welcome to my cafe"

#     return f"""<!DOCTYPE html>
# <html lang="en">
#     <head>
#         <meta charset="UTF-8"/>
#         <meta name="viewport" content="width-device-width"/>
#         <title>Document</title>
#     </head>
#     <body>
#         <h1>Welcome</h1>
#         <p>{sai_hi}</p>
#     </body>
# </html>"""

# @app.get('/products',response_class=HTMLResponse)
# def products(req:Request):
#     html_content=""
#     # for p in products:
#     #     html_content+=f"""<div>
#     # <h3>{p[0]}</h3>
#     # <h1>{p[1]}</h1>
#     # <h2>{p[2]}</h2>
#     # </div>"""
#     # print(html_content)
#     return templates.TemplateResponse(
#         request=req,
#         name="products.html",
#         context={"products":products}
#     )
# @app.post("/login")
# def login(req:Request,username:str = Form(),password:str =Form()):
#     print(username,password)
#     connection=get_connection()
#     query=""
#     cursor=connection.cursor()
#     connection.commit(query)
#     cursor.close()
#     connection.close()
    
#     products=[(1,"Laptop",70000),(2,"Phone",87000),(3,"smartwatch",5000),(4,"Headphones",20000),(5,"toys",150)]
#     return templates.TemplateResponse(
#         request=req,
#         name="products.html",
#         context={"products":products}
#     )

from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from database import get_connection

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
def home(req: Request):
    return templates.TemplateResponse(
        request=req,
        name="home.html",
        context={}
    )


@app.get("/products", response_class=HTMLResponse)
def products(req: Request, search: str = ""):
    connection = get_connection()
    cursor = connection.cursor()

    if search:
        query = """
            SELECT id, name, price, category
            FROM products
            WHERE name LIKE %s
        """
        cursor.execute(query, ("%" + search + "%",))
    else:
        query = """
            SELECT id, name, price, category
            FROM products
        """
        cursor.execute(query)

    product_list = cursor.fetchall()

    cursor.close()
    connection.close()

    return templates.TemplateResponse(
        request=req,
        name="products.html",
        context={
            "products": product_list,
            "search": search
        }
    )
