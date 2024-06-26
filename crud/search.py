
def search_by_score(destinations):
    print("list of destinations with score by choice: ")
    if destinations:
        score_to_search = int(input("enter destination score to search: "))
        for dest in destinations:
            if dest['score'] == score_to_search:
                 print(f"Name: {dest['name']}, Score: {dest['score']}, Description: {dest['description']}")
    else:
        print("No destinations available.")

def search_by_name(destinations):
    if destinations:
        name_to_search = input("enter destination name to search: ")
        for dest in destinations:
            if dest['name'] == name_to_search:
                 print(f"Name: {dest['name']}, Score: {dest['score']}, Description: {dest['description']}")
    else:
        print("No destinations available.")

def search_contains(destinations):
    print("list of destinations containing a word: ")
    if destinations:
        name_to_search = input("enter search word: ").lower()
        for dest in destinations:
            if name_to_search in dest['name'].lower():
                 print(f"Name: {dest['name']}, Score: {dest['score']}, Description: {dest['description']}")
    else:
        print("No destinations available.")


def serch_score_above_80(destinations):
    print("list of destinations with score by choice: ")
    if destinations:
        for dest in destinations:
            if dest['score'] > 80 :
                 print(f"Name: {dest['name']}, Score: {dest['score']}, Description: {dest['description']}")
    else:
        print("No destinations available.")
