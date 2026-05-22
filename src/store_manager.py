"""
Store manager application
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""
import sys
from views.user_view import UserView
from views.product_view import ProductView

if __name__ == '__main__':
    while True:
        print("===== LE MAGASIN DU COIN =====")
        print("\n1. Utilisateur" "\n2. Produit" "\n3. Quitter")
        choice = input("Choisissez une option: ")

        if choice == '1':
            main_menu = UserView()
            main_menu.show_options()
        elif choice == '2':
            main_menu = ProductView()
            main_menu.show_options()
        elif choice == '3':
            sys.exit()
        else:
            print("Cette option n'existe pas.")