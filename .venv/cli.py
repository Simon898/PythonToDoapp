import function
import time
import os

if not os.path.exists('todos.txt'):
    with open('todos.txt', 'w') as file:
        pass

now = time.strftime("%d %b %Y - %H:%M:%S")
print("It's " + now)

while True:
    user_action = input("Enter add, show, edit, complete or exit: ")
    user_action = user_action.strip()

    #match user_action:
    if user_action.startswith('add'):
        todo = user_action[4:] + "\n"

        todos = function.get_todos('todos.txt')

        todos.append(todo)

        function.write_todos('todos.txt', todos)

    elif user_action.startswith('show'):
        todos = function.get_todos('todos.txt')

        new_todos = [item.strip('\n') for item in todos]

        for index,todo in enumerate(new_todos):
            row = f"{index+1}. {todo}"
            print(row)
    elif user_action.startswith('edit'):
        try:
            #number = int(input("Enter number to be edited: "))
            number = int(user_action[5:])
            #new_todo = input("Enter new todo: ")
            #todos[number - 1] = new_todo

            with open("todos.txt", "r") as file:
                todos = file.readlines()
                #print('Here are existing todos: ', todos)

                new_todo = input("Enter new todo: ")
                todos[number-1] = new_todo + '\n'
                #print("Here are updated todos: ", todos)

            function.write_todos('todos.txt', todos)
        except ValueError:
            print("Your command is invalid!")
        #except IndexError:
            #print(f"Your input {number} is not in list!")

    elif user_action.startswith('complete'):
        number = int(input("Number of the todo to complete: "))

        todos = function.get_todos('todos.txt')
        index = number - 1
        todo_to_complete = todos[index].strip('\n')
        todos.pop(index)

        function.write_todos('todos.txt', todos)

        message = f"Todo {todo_to_complete} was removed from your list!"
        print(message)
    elif user_action.startswith('exit'):
        break

print('Bye!')