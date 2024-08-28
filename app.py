todos = []

def show_todos():
    print("\nYour To-Do List:")
    for index, todo in enumerate(todos, 1):
        print(f"{index}. {todo}")
    print("\n")

def add_todo():
    todo = input("Enter a new To-Do: ")
    todos.append(todo)
    print(f"'{todo}' has been added to your list.\n")

def remove_todo():
    show_todos()
    index = int(input("Enter the number of the To-Do to remove: ")) - 1
    if 0 <= index < len(todos):
        removed = todos.pop(index)
        print(f"'{removed}' has been removed from your list.\n")
    else:
        print("Invalid number.\n")

def main():
    while True:
        print("1. Show To-Do List")
        print("2. Add To-Do")
        print("3. Remove To-Do")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            show_todos()
        elif choice == "2":
            add_todo()
        elif choice == "3":
            remove_todo()
        elif choice == "4":
            break
        else:
            print("Invalid choice, please try again.\n")

if __name__ == "__main__":
    main()
