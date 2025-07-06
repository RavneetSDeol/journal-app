import json
import os
from datetime import datetime
from entry import Journal_Entry

JOURNAL_FILE = "journal.json"

def load_entries():
    if os.path.exists(JOURNAL_FILE):
        with open(JOURNAL_FILE, 'r') as file:
            data = json.load(file)
            return [Journal_Entry.from_dict(entry) for entry in data]
    return []

def save_entries(entries):
    with open(JOURNAL_FILE, 'w') as file:
        json.dump([entry.to_dict() for entry in entries], file, indent=4)

def write_entry():
    title = input("\nEnter the title of your journal entry: ")
    body = input("Enter the body of your journal entry: ")
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    new_entry = Journal_Entry(date, title, body)

    entries = load_entries()
    entries.append(new_entry)
    save_entries(entries)

    print("Journal entry saved successfully!\n")

def view_entries():
    entries = load_entries()
    if not entries:
        print("No journal entries found.\n")
        return

    print("\n--- Journal Entries ---")
    for entry in entries:
        print(f"Date: {entry.date}")
        print(f"Title: {entry.title}")
        print(f"Body: {entry.body}")
        print("-" * 20)
    print("End of entries.\n")

def delete_entry():
    entries = load_entries()
    if not entries:
        print("No journal entries found.\n")
        return

    print("\n--- Journal Entries ---")
    for i, entry in enumerate(entries):
        print(f"{i + 1}. {entry.title} (Date: {entry.date})")
    
    try:
        index = int(input("Enter the number of the entry you want to delete: ")) - 1
        if 0 <= index < len(entries):
            deleted_entry = entries.pop(index)
            save_entries(entries)
            print(f"Deleted entry: {deleted_entry.title}\n")
        else:
            print("Invalid entry number.\n")
    except ValueError:
        print("Invalid input. Please enter a number.")

def view_specific_entry():
    entries = load_entries()
    if not entries:
        print("No journal entries found.\n")
        return

    print("\n--- Journal Entries ---")
    for i, entry in enumerate(entries):
        print(f"{i + 1}. {entry.title} (Date: {entry.date})")

    try:
        index = int(input("Enter the number of the entry you want to view: ")) - 1
        while (index < 0 or index >= len(entries)):
            print("Invalid entry number. Please try again.")
            index = int(input("Enter the number of the entry you want to view: ")) - 1
        entry = entries[index]
        print(f"\nTitle: {entry.title}")
        print(f"Date: {entry.date}")
        print(f"Body: {entry.body}\n")
    except ValueError:
        print("Invalid input. Please enter a number.")

def edit_entry():
    entries = load_entries()
    if not entries:
        print("No journal entries found.\n")
        return

    print("\n--- Journal Entries ---")
    for i, entry in enumerate(entries):
        print(f"{i + 1}. {entry.title} (Date: {entry.date})")

    try:
        index = int(input("Enter the number of the entry you want to edit: ")) - 1
        if 0 <= index < len(entries):
            entry = entries[index]
            new_title = input(f"Enter new title (current: {entry.title}): ")
            new_body = input(f"Enter new body (current: {entry.body}): ")
            entry.title = new_title
            entry.body = new_body
            save_entries(entries)
            print("Entry updated successfully!\n")
        else:
            print("Invalid entry number.\n")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    while True:
        print("1. Write a new journal entry")
        print("2. View all journal entries")
        print("3. Delete a journal entry")
        print("4. View specific entry")
        print("5. Edit a journal entry")
        print("6. Exit")
        
        choice = input("Choose an option: ")

        if choice == '1':
            write_entry()
        elif choice == '2':
            view_entries()
        elif choice == '3':
            delete_entry()
        elif choice == '4':
            view_specific_entry()
        elif choice == '5':
            edit_entry()
        elif choice == '6':
            print("Exiting the journal application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()