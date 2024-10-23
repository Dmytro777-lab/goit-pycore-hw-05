# Декоратор для обробки помилок
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except ValueError:
            return "Please provide name and phone."
        except IndexError:
            return "Not enough arguments."
    return inner

# Словник для контактів
contacts = {}

# Функція для додавання контакту
@input_error
def add_contact(args):
    name, phone = args[0], args[1]
    contacts[name] = phone
    return f"Added {name} with phone {phone}."

# Функція для отримання номера телефону
@input_error
def get_phone(args):
    name = args[0]
    return f"{name}'s phone is {contacts[name]}."

# Функція для показу всіх контактів
def show_all():
    return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()]) if contacts else "No contacts."

# Основна функція
def main():
    while True:
        command = input("Enter command (add, phone, all, exit): ").lower()
        
        if command == "exit":
            print("Goodbye!")
            break
        elif command == "add":
            args = input("Enter name and phone: ").split()
            print(add_contact(args))
        elif command == "phone":
            args = input("Enter name: ").split()
            print(get_phone(args))
        elif command == "all":
            print(show_all())
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
