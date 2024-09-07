import re

contacts = {}
imported_contacts = {}

def add_contact():
    phone = input("Enter the contact's phone number: ")
    numbers_only = re.sub(r'\D','', phone) # removes dashes or extra characters
    contact_name = input("Enter the contact's name: ").capitalize()
    email = input("Enter the email: ").capitalize()
    address = input("Enter the address: ")
    note = input("Enter any notes here: ")
    if numbers_only not in contacts:
        contacts[numbers_only] = {"Name": contact_name, "Phone Number": phone, "Email": email, 
                               "Additional Info": {"Address": address, "Notes": note}}
        print(f"{contact_name} successfully added to your contacts list")
    elif numbers_only in contacts:
        (f"{numbers_only} already in contacts.")
    return contacts

def edit_contact(identifier, contact_option, new_info):
    contact_option = contact_option.capitalize()
    if identifier in contacts:
        if contact_option in contacts[identifier]: # outer dictionary details
            contacts[identifier][contact_option] = new_info
            print(f"{contact_option} has been updated for {contacts[identifier]["Name"]}")
        elif contact_option in contacts[identifier]["Additional Info"]: # inner dictionary details
            contacts[identifier]["Additional Info"][contact_option] = new_info
            print(f"\n{contact_option} has been updated for {contacts[identifier]["Name"]}")
        
def delete_contact(identifier):
    if identifier in contacts:
        removed_id = contacts.pop(identifier)
        print(f"\n{removed_id['Name']} has been deleted from your contacts.")
    return contacts

def search_contact(search_option, search_value):
    results = {}
    index = 0
    for identifier, details in contacts.items():
        if search_option in details and search_value in details[search_option]:
            results[identifier]= details
        else:
            print(f"\nNo matches found for {search_value}, you can add this contact to the list")
    if results:
        index += 1
        for identifier, details in results.items():
            print(f"\n{index}. -- Search Results For '{search_value}' --")
            print(f"Name: {details['Name']}\nPhone Number: {details["Phone Number"]}\nEmail: {details["Email"]}")
            print(f"~ Additional info ~")
            for key, value in details["Additional Info"].items(): # loops for inner dictionary
                print(f"{key}: {value}")  

def display_contacts():
    for identifier, details in contacts.items():
        print(f"-- Contact Info For Unique ID: {identifier} --")
        print(f"Name: {details['Name']}\nPhone Number: {details["Phone Number"]}\nEmail: {details["Email"]}")
        print(f"~ Additional Info ~")
        for key, value in details["Additional Info"].items(): # loops for inner dictionary
            print(f"{key}: {value}") 

def export_contacts():
    with open('contact_list.txt', 'w') as file:  # export to contact_list.txt
        for identifier, details in contacts.items():  # loops for outer dictionary
            file.write(f"Unique ID: {identifier}\nName: {details["Name"]}\nPhone Number: {details["Phone Number"]}\nEmail: {details["Email"]}\n~ Additional info ~")
            for key, value in details["Additional Info"].items(): # loops for inner dictionary
                file.write(f"\n{key}: {value}")

def main_user_system():
    while True:
        print("\nWelcome to the Contact Management System! \nMenu:")
        print("1. Add a new contact \n2. Edit an existing contact \n3. Delete a contact")
        print("4. Search for a contact \n5. Display all contacts \n6. Export contacts to a text file \n7. Quit")
        try:
            option = int(input("Enter option number: "))
            if option == 1:
                add_contact()
            elif option ==  2:
                unique_id = input("What's the contact's phone number (unique id)? ")
                identifier = re.sub(r'\D','', unique_id)
                contact_option = input("Which info are we updating? Name, Phone Number, Email, Address or Notes? ").capitalize()
                new_info = input("Enter the new info: ").capitalize()
                if identifier in contacts:
                    edit_contact(identifier, contact_option, new_info)
                else:
                    ("Contact Not Found")
            elif option == 3:
                identifier = input("Enter the phone number you wish to delete: ")
                if identifier in contacts:
                    delete_contact(identifier)
                else:
                    ("Contact Not Found")
            elif option == 4:
                search_option = input("What would you like to search by? Name, Phone Number or Email? ").capitalize()
                search_value = input("Enter search criteria: ").capitalize()
                search_contact(search_option, search_value)
            elif option == 5:
                if contacts:
                    display_contacts()
                else:
                    print("List empty")
            elif option == 6:
                if contacts:
                    print("Exporting contacts...")
                    export_contacts()
                else:
                    print("List Empty")
            elif option == 7:
                print("Quitting")
                break
        except ValueError:
            print("\nPlease follow the prompt carefully and try again with correct input type (text or number)")

main_user_system()