import tkinter as tk
import tkinter.font as font
import datetime as dt
import med_diary_database as db


# Functions
def submit():
    currentTime = dt.datetime.now()
    medNameInput = medName.get()
    medDosageInput = medDosage.get()
    medNoteInput = medNote.get("1.0", "end-1c")

    convertedMedName = db.convertMedNameToKey(medNameInput)
    convertedMedDosage = db.convertMedDosageToKey(medDosageInput)

    return db.insertToDiary(currentTime, convertedMedName, convertedMedDosage, medNoteInput)


# Interface
master = tk.Tk()
master.geometry("350x200")
master.title("Med Diary")

master.configure(background="lemon chiffon")


tk.Label(master, text=f"{dt.datetime.now():%b %d, %H:%M}", fg="white", bg="black", font=("Verdana", 11)).grid(row=0)

tk.Label(master, text="Medication Name", bg="lemon chiffon", font=("Verdana", 8)).grid(row=1)
tk.Label(master, text="Medication Dosage", bg="lemon chiffon", font=("Verdana", 8)).grid(row=2)
tk.Label(master, text="Medication Note", bg="lemon chiffon", font=("Verdana", 8)).grid(row=3)

medName = tk.Entry(master)
medDosage = tk.Entry(master)
medNote = tk.Text(master, wrap="word", width=20, height=5)

medName.grid(row=1, column=1, pady=3)
medDosage.grid(row=2, column=1, pady=3)
medNote.grid(row=3, column=1, pady=3)

medName.config({"background": "ivory"})
medDosage.config({"background": "ivory"})
medNote.config({"background": "ivory"})

Submit = tk.Button(master, text='Submit', bg="blue", fg="ivory", font=("Verdana", 8),
                   command=submit, height=5, width=5).grid(row=3, column=3)

master.mainloop()
