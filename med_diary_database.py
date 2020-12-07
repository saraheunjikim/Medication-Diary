import mysql.connector


db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="med_diary"
)

myCursor = db.cursor()

def insertToDiary(datetime, medName, medDosage, medNote):
    insertSql = "INSERT INTO diary (datetime, medication, dosage, note) VALUES (%s, %s, %s, %s)"
    values = (datetime, medName, medDosage, medNote)
    myCursor.execute(insertSql, values)

    return db.commit()

def convertMedNameToKey(medName):
    medDict = {}
    medName = medName.replace(" ", "").lower()
    myCursor.execute("SELECT medicationId, medicationName FROM medication")
    for (medicationId, medicationName) in myCursor:
        medDict[medicationId] = (medicationName.replace(" ", "")).lower()

    for key, value in medDict.items():
        if value == medName:
            return key

    return False


def convertMedDosageToKey(medDosage):
    medDict = {}
    medDosage = int(''.join(filter(str.isdigit, medDosage)))
    myCursor.execute("SELECT dosageId, dosageDesc FROM dosage")
    for (dosageId, dosageDesc) in myCursor:
        medDict[dosageId] = dosageDesc

    for key, value in medDict.items():
        if value == medDosage:
            return key

    return False







