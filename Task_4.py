def parse_input(user_input):
        parts = user_input.split()
        cmd, *args = parts
        cmd = cmd.strip().lower()
        return cmd, args

def add_contact(args, contacts):
        if len(args) < 2:
            print("Invalid command.")
            return "Usage: add <name> <phone>"
        name, phone = args[0], args[1]
        if name in contacts:
            return "Contact already exists. Use 'change' to update the phone."
        contacts[name] = phone
        return f"Contact '{name}' added."

def change_contact(args, contacts):
        if len(args) < 2:
            return "Usage: change <name> <new_phone>"
        name, phone = args[0], args[1]
        if name not in contacts:
            return "Contact not found."
        contacts[name] = phone
        return f"Contact '{name}' updated."

def show_phone(args, contacts):
        if len(args) < 1:
            return "Usage: phone <name>"
        name = args[0]
        phone = contacts.get(name)
        if phone is None:
            return "Contact not found."
        return f"{name}: {phone}"

def show_all(contacts):
        if not contacts:
            return "No contacts yet."
        lines = [f"{name}: {phone}" for name, phone in contacts.items()]
        return "\n".join(lines)

def main():
        contacts = {}
        print("Welcome to the assistant bot!")
        while True:
            user_input = input("Enter a command: ")
            command, args = parse_input(user_input)

        if command in ["close", "exit", "goodbye", "bye"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "show":
            if args and args[0].lower() == "all":
                print(show_all(contacts))
            else:
                print("Usage: show all")
        else:
            print("Invalid command.")

if __name__ == "__main__":
        main()
