import add_contact
import view_all_contact
import update_contact
import remove_contact
import search_contact
import load_file

all_contacts = load_file.load_all_contacts()

while True:
    print("Welcome to Contact Book")
    print("0. View all Contact")
    print("1. Search Contact")
    print("2. Add Contact")
    print("3. Delete Contact")
    print("4. Update Cobtact")
    print("5. exit")

    menu = input("Select Any Operation: ")

    if menu == "0":
        view_all_contact.view_all_contact(all_contacts)

    elif menu == "1":
        all_contacts = search_contact.search_contact_by_number(all_contacts)
        
    elif menu == "2":
        all_contacts = add_contact.add_contact(all_contacts)
    
    elif menu == "3":
       all_contacts = remove_contact.remove_contact_by_number(all_contacts)
        
    elif menu == "4":
        all_contacts= update_contact.update_contact_by_isbn(all_contacts)

    elif menu == "5":
        print("Thanks for using Contact Book\n Have good day!") 
        break
    else:
        print("Invalid operation")            