from customtkinter import *
from app.database import add_subject, add_task, fetch_tasks, fetch_all_subjects

def main():
    def render_subject_frame():
        for widget in subject_frame.winfo_children():
            widget.destroy()
        subjects = fetch_all_subjects()
        for subject in subjects:
            b = CTkButton(master=subject_frame,
                          text=subject[0],
                          font=("Bahnschrift", 17),
                          command=lambda name=subject: show_tasks_for_subject(name))
            b.pack(padx=30, pady=10)

        CTkButton(master=subject_frame, text="New Subject", font=("Bahnschrift", 17), fg_color="black",
                  command=add_subject_button_handler).pack(padx=30, pady=40,
                                                           side="bottom")

    def show_tasks_for_subject(subject_name: tuple):
        subject_name = subject_name[0]
        for widget in task_frame.winfo_children():
            widget.destroy()
        print(subject_name)

        tasks = fetch_tasks(
            subject_name)  # each task is a tuple / list, index :  0 - task id, 1 - task name, 2 - task description, 3 - due date
        print(tasks)
        if tasks is not None:
            for task in tasks:
                t = CTkFrame(master=task_frame)
                t.pack(fill="x", padx=10, pady=6)
                CTkLabel(master=t, text=task[1]).pack(padx=2, pady=2)
                CTkLabel(master=t, text=task[2]).pack(padx=2, pady=2)
                CTkLabel(master=t, text=task[3]).pack(padx=2, pady=2)

    def add_subject_button_handler():
        def handle_add_subject():
            subject_name = entry.get().strip()
            if subject_name:
                add_subject(subject_name)
                entry.delete(0, "end")
                CTkLabel(master=task_frame, text=f"New subject added successfully ", text_color="green",
                         font=("Arial", 20)).pack(padx=20, pady=20)
                render_subject_frame()
                show_tasks_for_subject(subject_name)

            else:
                CTkLabel(master=task_frame, text="Subject name cannot be empty! ", text_color="red",
                         font=("Arial", 20)).pack(padx=20, pady=20)

        entry = CTkEntry(master=task_frame, placeholder_text="Enter New subject name")
        entry.pack(padx=20, pady=20)
        CTkButton(master=task_frame, text="Add Subject", command=handle_add_subject).pack(padx=20, pady=20)

    def add_task_button_handler():
        # to make
        ...
    app = CTk()
    app.title("Study Manager")
    set_appearance_mode("dark")
    app.geometry("700x500")

    # Configuring grids for easier placement,
    app.grid_columnconfigure(0, weight=1)
    app.grid_rowconfigure(0, weight=1)
    app.grid_columnconfigure(2, weight=1)

    # Setting up Subjects frame
    subject_frame = CTkScrollableFrame(master=app)
    subject_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nsw")

    # Setup of tasks frame
    task_frame = CTkFrame(master=app)
    task_frame.grid(row=0, column=2, padx=20, pady=20, sticky="nsew")

    render_subject_frame()

    app.mainloop()