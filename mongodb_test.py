from pymongo import MongoClient

# 🔹 Connexion à MongoDB et création de la base de données
client = MongoClient("mongodb://localhost:27017")
db = client["ensa"]  # Création de la base de données ENSA
collection = db["etudiant"]  # Création de la collection Etudiant

# 🔹 1. CREATE - Ajouter des étudiants
def create_student(nom, prenom, age, filiere):
    student = {"nom": nom, "prenom": prenom, "age": age, "filiere": filiere}
    result = collection.insert_one(student)
    print(f"Étudiant ajouté avec l'ID : {result.inserted_id}")

# 🔹 2. READ - Lire les étudiants
def read_students():
    students = collection.find()
    print("\n📌 Liste des étudiants :")
    for student in students:
        print(student)

# 🔹 3. UPDATE - Modifier l'âge d'un étudiant
def update_student(nom, new_age):
    result = collection.update_one({"nom": nom}, {"$set": {"age": new_age}})
    print(f"Documents modifiés : {result.modified_count}")

# 🔹 4. DELETE - Supprimer un étudiant
def delete_student(nom):
    result = collection.delete_one({"nom": nom})
    print(f"Documents supprimés : {result.deleted_count}")

# 🚀 TESTS
if __name__ == "__main__":
    print("\n📚 Création de la base de données 'ensa' et de la collection 'etudiant'...")

    print("\n📌 Ajout de quelques étudiants...")
    create_student("El Mehdi", "Bennani", 21, "Informatique")
    create_student("Fatima", "Zahra", 22, "Génie Civil")
    create_student("Omar", "Tazi", 20, "Télécommunications")

    read_students()

    print("\n🔄 Mise à jour de l'âge de 'El Mehdi'...")
    update_student("El Mehdi", 23)

    read_students()

    print("\n❌ Suppression de 'Omar'...")
    delete_student("Omar")

    read_students()
