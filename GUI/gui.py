# gui.py
import tkinter as tk
import student
import file_operations


def write_record():
    try:
        roll = int(roll_entry.get())
        name = name_entry.get()
        per = float(per_entry.get())

        student_obj = student.Student()
        student_obj.add_record(roll, name, per)

        result_label.config(text=file_operations.write_record(student_obj))

    except Exception as e:
        result_label.config(text=str(e))


def display_all():
    result_text.delete(1.0, tk.END)

    records = file_operations.display_all_records()

    for record in records:
        result_text.insert(tk.END, record + "\n\n")


app = tk.Tk()
app.title("Student Record Management")

frame = tk.Frame(app)
frame.pack(padx=20, pady=20)

tk.Label(frame, text="Roll Number:").grid(row=0, column=0)
tk.Label(frame, text="Name:").grid(row=1, column=0)
tk.Label(frame, text="Percentage:").grid(row=2, column=0)

roll_entry = tk.Entry(frame)
name_entry = tk.Entry(frame)
per_entry = tk.Entry(frame)

roll_entry.grid(row=0, column=1)
name_entry.grid(row=1, column=1)
per_entry.grid(row=2, column=1)

add_button = tk.Button(frame, text="Add Record", command=write_record)
add_button.grid(row=3, column=0, columnspan=2)

display_button = tk.Button(frame, text="Display All Records", command=display_all)
display_button.grid(row=4, column=0, columnspan=2)

result_label = tk.Label(frame, text="", wraplength=300)
result_label.grid(row=5, column=0, columnspan=2)

result_text = tk.Text(frame, height=10, width=40)
result_text.grid(row=6, column=0, columnspan=2)

app.mainloop()
