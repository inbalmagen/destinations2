
from os import name


def add_destination(destinations):
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

def edit_destination(destinations):
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


def delete_destination(destinations):
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


def dest_list(destinations):
    print("list of all destinations:  ")
    if destinations:
        for dest in destinations:
            print(f"Name: {dest['name']}, Score: {dest['score']}, Description: {dest['description']}")
    else:
        print("No destinations available.")