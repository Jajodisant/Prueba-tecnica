# INVENTORY MANAGEMENT -->  Gestión del inventario

# Funtion to register products --> Función para registrar productos
def register_products(list_inventory: list, product: dict):
    # I add a product to the book list --> Agrego un producto a la lista
    list_inventory.append(product)
    return list_inventory

# Funtion to check products --> Función para consultar productos
def check_product(list_inventory: list, book_title: str):

    # I go through the list of books and check if the book is available. --> recorro la lista de libros y reviso que el que busco esté disponible
    for product in list_inventory:
        if book_title != product["title"]:
            # If it's not available I'm continue sherching --> Si no esta disponible sigo buscando
            continue 
        else:
            # I return product updated --> Retorno el producto actualizado
            return product      

# Funtion to update products --> Función para actualizar productos
def update_product(list_inventory: list, book_title: str, new_price: float= None, new_quantity_stock: int=None):

    # I go through the list of books and check if the book is available. --> recorro la lista de libros y reviso que el que busco esté disponible
    for product in list_inventory:
        if book_title != product["title"]:
            # If it's not available I'm continue sherching --> Si no esta disponible sigo buscando
            continue 
        else:
            # The price and quantity are updated --> El precio y la cantidad son actualizados
            product["price"] = new_price
            product["quantity"] =   new_quantity_stock
            # I return product updated --> Retorno el producto actualizado
            return product  

# Funtion to remove product --> Función para eliminar un producto
def remove_product(list_inventory: list, book_title: str):

    # I go through the list of books and check if the book is available. --> recorro la lista de libros y reviso que el que busco esté disponible
    for product in list_inventory:
        if book_title != product["title"]:
            # If it's not available I'm continue sherching --> Si no esta disponible sigo buscando
            continue
        else:
            # I remove product --> Producto eliminado
            list_inventory.remove(product)
            # I return list_inventory updated --> Retorno inventario actualizado
            return list_inventory 


