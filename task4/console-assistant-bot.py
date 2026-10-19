# Handle input errors raised by command handlers.
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return 'Input is incorrect. It should include a contact name as a first argument, and a phone number as a second argument.'
        except KeyError:
            return 'Contact with the given name was not found.'
        except IndexError:
            return 'Input is incorrect. It should include a contact name as a first argument.'

    return inner


# Parse the user input and split it into command
# and arguments.
def parse_input(user_input: str) -> tuple:
    # Split user input into command and arguments.
    user_input_parts = user_input.split()

    if not user_input_parts:
        return '', []

    cmd, *args = user_input_parts
    cmd = cmd.strip().lower()
    return cmd, *args

# Add the contact name and phone number.
@input_error
def add_contact(args: list, contacts: dict) -> str:
    name, phone = args

    # Check whether a contact with the given name
    # already exists.
    if name in contacts:
        return f'Contact "{name}" already exists.'

    contacts[name] = phone
    return 'Contact has been added.'

# Update the phone number of the contact.
@input_error
def change_contact(args: list, contacts: dict) -> str:
    name, phone = args

     # Raise an error if the contact does not exist.
    if name not in contacts:
        raise KeyError()

    contacts[name] = phone
    return 'Contact has been updated.'

# Display the phone number of the contact.
@input_error
def display_contact_phone(args: list, contacts: dict) -> str:
    name = args[0]
    return f'Contact "{name}" has phone number {contacts[name]}.'

# Display all existing contacts.
@input_error
def display_all_contacts(contacts: dict) -> str:
    if not contacts:
        return 'No contacts found.'

    return '\n'.join(f'{name}: {phone}' for name, phone in contacts.items())

def main():
    contacts = {}

    print('Welcome to the assistant bot!')
    
    while True:
        user_input = input('Enter a command: ')
        command, *args = parse_input(user_input)

        if not command:
            print('Please enter a command.')
            continue

        if command in ['close', 'exit']:
            print('Good bye!')
            break

        elif command == 'hello':
            print('How can I help you?')

        elif command == 'add':
            print(add_contact(args, contacts))

        elif command == 'change':
            print(change_contact(args, contacts))

        elif command == 'phone':
            print(display_contact_phone(args, contacts))

        elif command == 'all':
            print(display_all_contacts(contacts))

        else:
            print('Invalid command.')

if __name__ == "__main__":
    main()
