

def search_contact_by_number(all_contact):
    number_to_update = int(input("\nEnter phone number: "))

    for contact in all_contact:
        if int(contact['number']) == number_to_update:
            print(f"\n number found: {contact}")