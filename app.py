# שיעורי בית - כתבו תוכנית של יעדי טיול. 
# * קלטו יעד טיול . לכל יעד שם,  ציון,  תיאור. 
# * Barcelona, 9.5, "Barcelona is a great city"
# * בצעו חיפוש של יעד לפי שם. 
# * חיפוש לפי ציון (כל מי שגדול מציון מסוים). 
# * קראו ושמרו את היעדים בקובץ json.

from menu.menu import destinations_menu

file_path = 'data.json'

if __name__ == "__main__":
    print("&&&&&&&", __name__)
    destinations_menu()



