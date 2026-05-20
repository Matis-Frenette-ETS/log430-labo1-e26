from models.product import Product
from controllers.product_controller import ProductController

class ProductView:
    @staticmethod
    def show_options():
        """ Show menu with operation options which can be selected by the product """
        controller = ProductController()
        while True:
            print("\n1. Montrer la liste d'items" \
            "\n2. Ajouter un item" \
            "\n3. Modifier les informations d'un item" \
            "\n4. Supprimer un item, selon son id" \
            "\n5. Supprimer tous les items"\
            "\n6. Quitter l'appli")
            choice = input("Choisissez une option: ")

            if choice == '1':
                products = controller.list_products()
                ProductView.show_products(products)
            elif choice == '2':
                name, email = ProductView.get_inputs()
                product = Product(None, name, email)
                controller.create_product(product)
            elif choice == '3':
                id, name, email = ProductView.get_inputs_update()
                product = Product(id, name, email)
                controller.update_product(product)
            elif choice == '4':
                product_id = ProductView.get_inputs_delete()
                controller.delete_product(product_id)
            elif choice == '5':
                controller.delete_all_products()
            elif choice == '6':
                controller.shutdown()
                break
            else:
                print("Cette option n'existe pas.")

    @staticmethod
    def show_products(products):
        """ List products """
        print("\n".join(f"{product.id}: {product.name} | {product.brand} | {product.price}" for product in products))

    @staticmethod
    def get_inputs():
        """ Prompt product for inputs necessary to add a new product """
        name = input("Nom d'utilisateur : ").strip()
        email = input("Adresse courriel : ").strip()
        return name, email
    
    @staticmethod
    def get_inputs_update():
        """ Prompt product for inputs necessary to update a product """
        id = input("Id du product a modifier : ").strip()
        name = input("Nouveau Nom d'utilisateur : ").strip()
        email = input("Nouvelle Adresse courriel : ").strip()
        return id, name, email
    
    @staticmethod
    def get_inputs_delete():
        """ Prompt product for inputs necessary to delete a product """
        id = input("Product id : ").strip()
        return id