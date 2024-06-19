# שיעורי בית - כתבו תוכנית של יעדי טיול. 
# * קלטו יעד טיול . לכל יעד שם,  ציון,  תיאור. 
# * Barcelona, 9.5, "Barcelona is a great city"
# * בצעו חיפוש של יעד לפי שם. 
# * חיפוש לפי ציון (כל מי שגדול מציון מסוים). 
# * קראו ושמרו את היעדים בקובץ json.
import json
from pathlib import Path
file_path = 'data.json'

destinations = [
    {"name": "aaa", "score": 77, "description": "aaa"},
    {"name": "bbb", "score": 88, "description": "bbb"},
    {"name": "ccc", "score": 99, "description": "ccc"}
]

def save_file():
    with open(file_path, 'w') as f:  
        json.dump(destinations, f)

def read_file():
    global destinations
    if Path(file_path).exists() and Path(file_path).is_file():
        with open(file_path, 'r') as f:
            destinations = json.load(f)

def add_destination():
    new_dest_name = input("enter destination name: ")
    new_dest_description = input("enter description: ")
    new_dest_score = int(input("enter destination score: "))
    new_destination = {
        "name": new_dest_name,
        "description": new_dest_description,
        "score": new_dest_score
    }
    destinations.append(new_destination)
    print("destination added")

def edit_destination():
    name = input("Enter the name of the destination to edit: ")
    for destination in destinations:
        if destination["name"] == name:
            new_name = input(f"Enter the new name of the destination (current: {destination['name']}): ")
            new_score = int(input(f"Enter the new score of the destination (current: {destination['score']}): "))
            new_description = input(f"Enter the new description of the destination (current: {destination['description']}): ")
            destination["name"] = new_name
            destination["score"] = new_score
            destination["description"] = new_description
            print(f"Destination '{name}' updated successfully.")
            return
    print(f"Destination '{name}' not found.")

def dest_list():
    print("list of all destinations:  ")
    if destinations:
        for dest in destinations:
            print(f"Name: {dest['name']}, Score: {dest['score']}, Description: {dest['description']}")
    else:
        print("No destinations available.")

def search_by_score():
    print("list of destinations with score by choice: ")
    if destinations:
        score_to_search = int(input("enter destination score to search: "))
        for dest in destinations:
            if dest['score'] == score_to_search:
                 print(f"Name: {dest['name']}, Score: {dest['score']}, Description: {dest['description']}")
    else:
        print("No destinations available.")

def serch_score_above_80():
    print("list of destinations with score by choice: ")
    if destinations:
        for dest in destinations:
            if dest['score'] > 80 :
                 print(f"Name: {dest['name']}, Score: {dest['score']}, Description: {dest['description']}")
    else:
        print("No destinations available.")


def delete_destination():
    print("****** Deleting destination ******")
    name = input("Please enter the name of the destination to delete: ")
    found = False
    i = 0
    
    while i < len(destinations):
        if destinations[i]["name"] == name:
            del destinations[i]
            found = True
            print(f"Destination '{name}' deleted successfully.")
            break  
        i += 1
    
    if not found:
        print(f"Destination '{name}' not found.")


def destinations_menu():
    read_file()
    while True:
        print ("please choose an option:  ")
        print ("1. Add destination")
        print ("2. Edit destination")
        print ("3. Delete destination")
        print ("4. Search destination by score")
        print ("5. search score above 80")
        print ("6. List of all destinations")
        print ("7. Exit menue")
        select = input("please enter your choice:  ")
        if select == "1":           
            print("add destination is selected")
            add_destination()
            save_file()
        elif select == "2":
            print("edit destination is selected")
            edit_destination()
            save_file()
        elif select == "3":
            print("delete destination is selected")
            delete_destination()
            save_file()
        elif select == "4":
            print("search by score is selected")
            search_by_score()
        elif select == "5":
            print("search score above 80")
            serch_score_above_80()
        elif select == "6":
            print("list of all destinations is selected")
            dest_list()
        elif select == "7":
            print("exit is selected")
            exit()

destinations_menu()

