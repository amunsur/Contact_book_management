import csv

def load_all_contacts():
    contacts = []
    try:
        with open("all_contact.csv", mode="r") as fp:
            reader = csv.reader(fp)
            
            for row in reader:
                contact={
                    "name": row[0],"email": row[1],"number": row[2],"address": row[3]
                }
                contacts.append(contact)
                
    except FileNotFoundError:
        pass
    
    return contacts