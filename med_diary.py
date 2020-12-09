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

def insert():
    medNameInsInput = medNameIns.get()
    medDosageInsInput = medDosageIns.get()
    medDescInsInput = medDescIns.get()
    medDiagnosisInsInput = medDiagnosisIns.get()
    medDiagnosisDescInsInput = medDiagnosisDescIns.get()

    db.insertDosage(medDosageInsInput)
    db.insertMedication(medNameInsInput, medDescInsInput, medDiagnosisInsInput, medDiagnosisDescInsInput)

    return "Inserted"


# Interface
master = tk.Tk()
master.title("Med Diary")

master.configure(background="lemon chiffon")


tk.Label(master, text=f"{dt.datetime.now():%b %d, %H:%M}", fg="white", bg="black", font=("Verdana", 11)).grid(row=0)
tk.Label(master, text="Insert Medication", fg="white", bg="black", font=("Verdana", 11)).grid(row=5)

tk.Label(master, text="Medication Name", bg="lemon chiffon", font=("Verdana", 8)).grid(row=1)
tk.Label(master, text="Medication Dosage (mg)", bg="lemon chiffon", font=("Verdana", 8)).grid(row=2)
tk.Label(master, text="Medication Note", bg="lemon chiffon", font=("Verdana", 8)).grid(row=3)
tk.Label(master, text="Medication Name", bg="lemon chiffon", font=("Verdana", 8)).grid(row=6)
tk.Label(master, text="Medication Dosage (mg)", bg="lemon chiffon", font=("Verdana", 8)).grid(row=7)
tk.Label(master, text="Medication Description", bg="lemon chiffon", font=("Verdana", 8)).grid(row=8)
tk.Label(master, text="Medication Used For", bg="lemon chiffon", font=("Verdana", 8)).grid(row=9)
tk.Label(master, text="Diagnosis Description", bg="lemon chiffon", font=("Verdana", 8)).grid(row=10)




medName = tk.Entry(master)
medDosage = tk.Entry(master)
medNote = tk.Text(master, wrap="word", width=20, height=5)
medNameIns = tk.Entry(master)
medDosageIns = tk.Entry(master)
medDescIns = tk.Entry(master)
medDiagnosisIns = tk.Entry(master)
medDiagnosisDescIns = tk.Entry(master)


medName.grid(row=1, column=1, pady=3)
medDosage.grid(row=2, column=1, pady=3)
medNote.grid(row=3, column=1, pady=3)
medNameIns.grid(row=6, column=1, pady=3)
medDosageIns.grid(row=7, column=1, pady=3)
medDescIns.grid(row=8, column=1, pady=3)
medDiagnosisIns.grid(row=9, column=1, pady=3)
medDiagnosisDescIns.grid(row=10, column=1, pady=3)

medName.config({"background": "ivory"})
medDosage.config({"background": "ivory"})
medNote.config({"background": "ivory"})
medNameIns.config({"background": "ivory"})
medDosageIns.config({"background": "ivory"})
medDiagnosisIns.config({"background": "ivory"})
medDiagnosisDescIns.config({"background": "ivory"})

Submit = tk.Button(master, text='Submit', bg="blue", fg="ivory", font=("Verdana", 8),
                   command=submit, height=1, width=8).grid(row=4, column=1)
Insert = tk.Button(master, text='Insert', bg="blue", fg="ivory", font=("Verdana", 8),
                   command=insert, height=1, width=8).grid(row=11, column=1)

master.mainloop()
