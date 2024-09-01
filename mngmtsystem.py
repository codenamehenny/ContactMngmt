import re

contacts = {}

def add_contact():
    phone = input("Enter the contact's phone number: ")
    contact_name = input("Enter the contact's name: ")
    email = input("Enter the email: ")
    address = input("Enter the address: ")
    note = input("Enter any notes here: ")
    contacts[phone] = {phone: {"Name": contact_name, "Phone Number": phone, "Email": email, 
                               "Additional Info": {"Address": address, "Notes": note}}}
    with open('contact_list.txt', 'w') as file:  # export to contact_list.txt
        for identifier, details in contacts.items():  # loops for name, phone and email
            file.write(f"Unique Identifier: {identifier}")
            file.write(f"Name: {details["Name"]}")
            file.write(f"Phone Number: {details["Phone Number"]}")
            file.write(f"Email: {details["Email"]}")
            for key, value in details["Additional Info"].items(): # loops for address and notes
                file.write(f"{key}: {value}")
    return print(f"{contact_name} successfully added to your contacts list")

