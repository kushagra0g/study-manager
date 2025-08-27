from app.database import add_subject, add_task, fetch_tasks, fetch_all_subjects
from app.run_gui import main as run_gui


def temporary():
    while True:
        # temporary for testing if database operations work well
        print("options : \n"
              "1. add a subject\n"
              "2. add a task\n"
              "3. show all tasks for a subject\n"
              "4. list all subjects\n"
              "5. exit\n"
              "enter the index number of the action you wanna perform\n")

        choice = int(input())
        if choice==1:
            subject =  input("what subject do you want to add : ")
            add_subject(subject)
            print("DONE!")

        elif choice==2:
            task_name = input("Enter the task name : ")
            task_description = input("Enter the task description : ")
            due_date = input("Enter the due date (DD / MM / YYYY): ")
            subject = input("Enter the subject : ")
            add_task(task_name, task_description, due_date, subject)
            print("DONE SUCCESSFULLY")

        elif choice==3:
            subject = input("Enter the subject you wanna check tasks of : ")
            print(fetch_tasks(subject))

        elif choice==4:
            print(fetch_all_subjects())

        elif choice==5:
            break

        else:
            print("invalid input. try again.\n\n")

if __name__ == "__main__":
    #temporary()
    run_gui()