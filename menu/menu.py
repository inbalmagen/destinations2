

from crud.actions import add_destination, delete_destination, dest_list, edit_destination
from crud.search import search_by_name, search_by_score, search_contains, serch_score_above_80
from load_save.load_save import read_file, save_file


def destinations_menu():
    destinations = read_file()
    while True:
        print ("please choose an option:  ")
        print ("1. Add destination")
        print ("2. Edit destination")
        print ("3. Delete destination")
        print ("4. Search destination by score")
        print ("5. Search score above 80")
        print ("6. Search by name")
        print ("7. Search destinations containing word")
        print ("8. List of all destinations")
        print ("x. Exit menu")
        choice = input("please enter your choice:  ")
        
        if choice == "1":           
            print("add destination is choiceed")
            add_destination(destinations)
            save_file(destinations)
        elif choice == "2":
            print("edit destination is choiceed")
            edit_destination(destinations)
            save_file(destinations)
        elif choice == "3":
            print("delete destination is choiceed")
            delete_destination(destinations)
            save_file(destinations)
        elif choice == "4":
            print("search by score is choiceed")
            search_by_score(destinations)
        elif choice == "5":
            print("search score above 80")
            serch_score_above_80(destinations)
        elif choice == "6":
            print("search destination by name")
            search_by_name(destinations)
        elif choice == "7":
            print("search destination containing word")
            search_contains(destinations)
        elif choice == "8":
            print("list of all destinations")
            dest_list(destinations)
        elif choice == "x":
            print("exit is choiceed")
            exit()