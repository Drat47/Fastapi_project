from fastapi import FastAPI
from data import product
from database import getData,add_data,update_data,delete_data
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

app.add_middleware(CORSMiddleware,
                   allow_origins=["http://localhost:3000"],
                   allow_methods = ['*']
)

products = [
    product(id =1,name = "laptop",description = "Dell laptoop",price = 145,quantity = 10),
    product(id =2,name = "laptop",description = "hp laptoop",price = 15,quantity = 610),
    product(id =3,name = "laptop",description = "ell laptoop",price = 53,quantity = 60),
    product(id =4,name = "laptop",description = "h laptoop",price = 5,quantity = 90)
    ]


@app.get('/products')
def get_products():
    return getData()

#add producat :: post 

@app.post('/products')
def add_product(product : product):
    return add_data(product) 
#update the products

@app.put('/products/{id}')
def update_product(id:int,product:product):
    
    return update_data(id,product)
#delete 

@app.delete('/prducts/{id}')
def delete_product(id:int):
    return delete_data(id)
        
    
