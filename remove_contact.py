from save_all_contact import save_all_contact 

def remove_book_by_number(all_contact):
    number_to_remove = input("Enter the number of the contact to remove: ")
    
    contact_to_remove = None
    for contact in all_contact:
        if str(contact["number"]) == number_to_remove:
            contact_to_remove = contact
            break

    if contact_to_remove:
        all_contact.remove(contact_to_remove)
        print(f"contact with number {number_to_remove} has been removed.")
        save_all_contact(all_contact)
        
    else:
        print(f"No contact found with number {number_to_remove}.")
    
    return all_contact
