from inventory_manament import register_products, check_product, update_product, remove_product
from Sales_registration_consultation import register_sales, check_sales


sales_inventory = []



list_inventory = []


while True:
    #Comprehensive Inventory and Sales Management System with Dynamic Reports --> Sistema Integral de Gestión de Inventario y Ventas con Reportes Dinámicos
    print("Comprehensive Inventory and Sales Management System for a National Bookstore".upper()) # Sistema integral de gestión de inventario y ventas para una librería nacional
    # MAIN MENU --> MENÚ PRINCIPAL
    print("\n1. INVENTORY MANAGEMENT\n2. SALES REGISTRATION AND CONSULTATION") # Gestión del inventario y/o Registro y consulta de ventas
    # Main menu options --> Opciones del menú principal
    main_option = input("\nChoose an option: ") 

    # I verify that the option is not text. --> Verifico que la entrada no sea un texto
    if not main_option.isdigit():
        print(">>>Error! Text is NOT allowed.!\n") 
        continue  

    # I convert the option to an integer so that I can use it in if statements. --> Convierto la opción a número entero para poder usarla en los if
    main_option = int(main_option)

    # I verify that the option is within the allowed range (1 or 2). --> Verifico que la opción esté dentro del rango permitido (1 ó 2)
    if main_option < 1 or main_option > 2:
        print(">>>Error! Please enter a valid option!\n")
        continue  

    # INVENTORY MANAGEMENT
    if main_option == 1:

        while True:

            # Inventory menu --> Menú del inventario 
            print("1. Register products\n" \
            "2. Check products\n" \
            "3. Update products\n" \
            "4. Delete products\n" \
            "5. Exit")
            # Inventory menu options
            inventory_option = input("\nChoose an option: ")
            
            # I verify that the option is not text. --> Verifico que la entrada no sea un texto
            if not inventory_option.isdigit():
                print(">>>Error! Text is NOT allowed.!\n") 
                continue 

             # I convert the option to an integer so that I can use it in if statements. --> Convierto la opción a número entero para poder usarla en los if
            inventory_option = int(inventory_option)

            # I verify that the option is within the allowed range (1 or 2). --> Verifico que la opción esté dentro del rango permitido (1-5)
            if inventory_option < 1 or inventory_option > 5:
                print(">>>Error! Please enter a valid option!\n")
                continue

            # Register products 
            if inventory_option == 1:

                while True:     

                    # I request the product details. -->  Pido los datos del producto 
                    title = input("Enter the title of the book: ")
                    author = input("Enter the author: ")
                    category = input("Enter the category: ")
                    price = float(input("Enter the price: "))
                    quantity_stock = int(input("Enter the available amount: "))

                    # Create a dictionary with the entered data -->  Creo un diccionario con los datos ingresados
                    product = {"title": title, "author": author, "category": category, "price": price, "quantity_stock": quantity_stock}

                    # I call the function that adds the product to my inventory list. --> Llamo a la función que agrega el producto a mi lista de inventario
                    register_products(list_inventory, product)

                  
                    while True:

                        # Validation if you want to continue adding products --> Validación si desea continuar añadiendo productos
                        continue_option = input("Do you want to continue adding products? (s/n): ").lower()

                        # If it says “s” we keep adding. --> Si dice "s", seguimos agregando
                        if continue_option == "s":
                            continuar = True  
                            break

                        # If it says “n” I exit the loop. --> Si dice "n", salgo del ciclo
                        elif continue_option == "n":
                            continuar = False  
                            break
                        
                         # I do not allow numbers in this question. -->  No permito números en esta pregunta
                        elif continue_option.isdigit():                           
                            print(">>>Opción incorrecta, no se admiten números")

                        else:
                            # I reject any input other than “y” or “n.” --> Cualquier otro ingreso que no sea "s" o "n" lo rechazo
                            print(">>>Opción incorrecta, ingresa 's' o 'n'")

                        # If I don't want to continue, I exit the product addition cycle.--> Si no quiero continuar, salgo del ciclo de agregar productos
                    if not continuar:
                        break

            # Check product
            elif inventory_option == 2:
                book_title = input("Enter the title of the book you want to search for: ")
                print(check_product(list_inventory, book_title))

            # Update products
            elif inventory_option == 3:

                book_title = input("Enter the title of the book you want to update: ")
                new_price = float(input("Enter the new price: "))
                new_quantity_stock = int(input("Enter the new price: "))
                print(update_product(list_inventory, book_title, new_price))

            # Delete products
            elif inventory_option == 4:
                book_title = input("Enter the title of the book you want to remove: ")
                print(remove_product(list_inventory, book_title))

            # Exit
            elif inventory_option == 5:           
                print(">>> Leaving the product registry <<<")
                break




    # SALES REGISTRATION AND CONSULTATION
    elif main_option == 2:

        while True:

            # Sales menu --> Menú de ventas
            print("1. Register sales\n" \
            "2. Check sales\n" \
            "3. Exit")

            sales_option = input("\nChoose an option: ")

             # I verify that the option is not text. --> Verifico que la entrada no sea un texto
            if not sales_option.isdigit():
                print(">>>Error! Text is NOT allowed.!\n") 
                continue 

             # I convert the option to an integer so that I can use it in if statements. --> Convierto la opción a número entero para poder usarla en los if
            sales_option = int(sales_option)

            # I verify that the option is within the allowed range (1 or 2). --> Verifico que la opción esté dentro del rango permitido (1-5)
            if sales_option < 1 or sales_option > 3:
                print(">>>Error! Please enter a valid option!\n")
                continue
            
            # Register sales
            if sales_option == 1:   

                # I request the sales details.--> Pido los datos de la venta
                customer = input("Enter the customer's name: ")
                product_sold = input("Enter the title of the book sold: ")
                quantity = input("Enter the quantity sold: ")
                date = input("Date of sale (dd/mm/yyyy): ")

                # Create a dictionary with the sales data -->  Creo un diccionario con los datos de venta
                product_sales = {"customer": customer, "product_sold": product_sold, "quantity": quantity, "date": date}

                # I call the function that adds the sales record to the list. --> Llamo a la función que agrega el registro de la venta a la lista
                register_sales(sales_inventory, product_sales)
                
                while True:

                    # Validation if you want to continue adding sales Validación si desea continuar añadiendo ventas
                    continue_option_sales = input("Do you want to continue adding products? (s/n): ").lower()

                    # If it says “s” we keep adding. --> Si dice "s", seguimos agregando
                    if continue_option_sales == "s":
                        continuar = True  
                        break

                    # If it says “n” I exit the loop. --> Si dice "n", salgo del ciclo
                    elif continue_option_sales == "n":
                        continuar = False  
                        break
                    
                        # I do not allow numbers in this question. -->  No permito números en esta pregunta
                    elif continue_option_sales.isdigit():                           
                        print(">>>Opción incorrecta, no se admiten números")

                    else:
                        # I reject any input other than “y” or “n.” --> Cualquier otro ingreso que no sea "s" o "n" lo rechazo
                        print(">>>Opción incorrecta, ingresa 's' o 'n'")

                    # If I don't want to continue, I exit the product addition cycle.--> Si no quiero continuar, salgo del ciclo de agregar productos
                if not continuar:
                    break
            
            #Check sale 
            elif sales_option == 2:
               
                book_title = input("Enter the title of the book you want to sherch: ")
                print(check_sales(sales_inventory, book_title))
            
             # Exit
            elif sales_option == 3:           
                print(">>> Leaving the sales registry <<<")
                break
        





