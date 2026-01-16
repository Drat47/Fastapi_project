import mysql.connector as sql
from data import product 

conn = sql.connect(host='localhost',user="root",password="1234")

conn.autocommit = True
cur = conn.cursor()
cur.execute('use data')


def getData():
    products_list = []
    cur.execute("select * from fastData")
    data = cur.fetchall()
    for i in data:
        products_list.append(
            product(id=i[0],name=i[1],description=i[2],price=i[3],quantity=i[4]))
    return products_list


def add_data(product: product):
    query = f"insert into fastdata values \
    ({product.id},'{product.name}','{product.description}',{product.price},{product.quantity});"
    cur.execute(query)
    return "record added successfully"


def update_data(id: int, product: product):
    query = f"update fastdata set name = '{product.name}', \
    description = '{product.description}', price = {product.price}, \
    quantity = {product.quantity} where id = {id};"
    cur.execute(query)
    return "data updated successfully"


def delete_data(id: int):
    query = f"delete from fastdata where id = {id};"
    cur.execute(query)
    return "data deleted successfully"
