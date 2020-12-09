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
    medDosage = str(medDosage)

    try:
        newMedDosage = int(''.join(filter(str.isdigit, medDosage)))
    except ValueError or TypeError:
        newMedDosage = "0mg"

    myCursor.execute("SELECT dosageId, dosageDesc FROM dosage")
    for (dosageId, dosageDesc) in myCursor:
        medDict[dosageId] = dosageDesc

    for key, value in medDict.items():
        if value == newMedDosage:
            return key

    return False

def insertDiagnosis(medDiagnosis, medDiagnosisDesc):
    myCursor.execute("INSERT INTO diagnosis (diagnosisName, diagnosisDesc) VALUES (%s, %s)",
                     (medDiagnosis, medDiagnosisDesc))
    return db.commit()

def insertDosage(medDosage):
    try:
        newMedDosage = int(''.join(filter(str.isdigit, medDosage)))
    except ValueError or TypeError:
        newMedDosage = "0mg"

    if not convertMedDosageToKey(newMedDosage):
        myCursor.execute("INSERT INTO dosage (dosageDesc) VALUES (%s)", (newMedDosage,))
        return db.commit()

    return convertMedDosageToKey(newMedDosage)

def insertMedication(medName, medDesc, medDiagnosis):
    pass


