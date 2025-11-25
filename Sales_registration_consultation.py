 # SALES REGISTRATION AND CONSULTATION --> Registro y consulta de ventas

 # Funtion to register sales --> Función para registar venta
def register_sales(sales_inventory: list, product_sales: dict):
     # The sale record is added to the list. --> Se agrega el registro de la venta a la lista
     sales_inventory.append(product_sales)
     return product_sales

# Funtion to function to check sales --> Función para consultar ventas
def check_sales(sales_inventory: list,  book_title: str):
     #  I go through the list and check that the option I am looking for is available. -->  recorro la lista y reviso que la opción por la que estoy buscando la venta esté disponible
     for product_sales in sales_inventory:
       
         if book_title != product_sales["product_sold"]:
             continue        
         else:
             return product_sales




# # sin implementar
# def update_inventory(lista, lista2):

#     for i in lista:
#         for j in lista2:
#             i["quantity_stock"] =  i["quantity_stock"] - j["quantity"]

#     return lista

