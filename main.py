
def load_tasks():
    try:
        with open('tasks.txt',"r") as file:
            tasks = file.readlines()
            return [task.strip() for task in tasks]
    except FileNotFoundError:
        return []

def show_list(tasks):
    if not tasks:
        print("No Tasks.")
    for i,task in enumerate(tasks,1):
        print(f'{i}. {task}')

def save_task(tasks):
    with open('tasks.txt','w') as file:
        for task in tasks:
            file.write(task + '\n')

def main():
    tasks = load_tasks()
    while True:
        print('-' * 40)
        print("1. Show List")
        print("2. Add Task")
        print("3. Delete a Task")
        print("4. Exit")

        choice = input('Enter your option number(1-4): ')
        print('-' * 40)

        if choice == '1':
            show_list(tasks)
        elif choice == '2':
            task = input('Enter the task: ').strip()
            if len(task) > 1:
                tasks.append(task)
                save_task(tasks)
            print('Enter at least one word...')

        elif choice == '4':
            print('GoodBye👋')
            break
        else:
            print('Invalid Choice!')


if __name__=='__main__':
    main()