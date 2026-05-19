"""
User view
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""
from models.user import User
from controllers.user_controller import UserController

class UserView:
    @staticmethod
    def show_options():
        """ Show menu with operation options which can be selected by the user """
        controller = UserController()
        while True:
            print("\n1. Montrer la liste d'utilisateurs" \
            "\n2. Ajouter un utilisateur" \
            "\n3. Update user's information" \
            "\n4. Delete user from from user_id" \
            "\n5. Delete all users"\
            "\n6. Quitter l'appli")
            choice = input("Choisissez une option: ")

            if choice == '1':
                users = controller.list_users()
                UserView.show_users(users)
            elif choice == '2':
                name, email = UserView.get_inputs()
                user = User(None, name, email)
                controller.create_user(user)
            elif choice == '3':
                id, name, email = UserView.get_inputs_update()
                user = User(id, name, email)
                controller.update_user(user)
            elif choice == '4':
                user_id = UserView.get_inputs_delete()
                controller.delete_user(user_id)
            elif choice == '5':
                controller.delete_all_users()
            elif choice == '6':
                controller.shutdown()
                break
            else:
                print("Cette option n'existe pas.")

    @staticmethod
    def show_users(users):
        """ List users """
        print("\n".join(f"{user.id}: {user.name} ({user.email})" for user in users))

    @staticmethod
    def get_inputs():
        """ Prompt user for inputs necessary to add a new user """
        name = input("Nom d'utilisateur : ").strip()
        email = input("Adresse courriel : ").strip()
        return name, email
    
    @staticmethod
    def get_inputs_update():
        """ Prompt user for inputs necessary to update a user """
        id = input("Id du user a modifier : ").strip()
        name = input("Nouveau Nom d'utilisateur : ").strip()
        email = input("Nouvelle Adresse courriel : ").strip()
        return id, name, email
    
    @staticmethod
    def get_inputs_delete():
        """ Prompt user for inputs necessary to add a new user """
        id = input("User id : ").strip()
        return id