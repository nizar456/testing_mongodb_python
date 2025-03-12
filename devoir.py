from pymongo import MongoClient

#  Connexion à MongoDB
client = MongoClient("mongodb://localhost:27017")

#  1. Afficher toutes les bases de données
def list_databases():
    databases = client.list_database_names()
    print("\n Bases de données existantes :", databases)

#  2. Créer une base de données
def create_database(db_name):
    db = client[db_name]
    db["temp_collection"].insert_one({"temp": "delete me"})  # Hack pour créer la BD
    db["temp_collection"].drop()
    print(f"\n Base de données '{db_name}' créée avec succès.")

#  3. Supprimer une base de données
def delete_database(db_name):
    client.drop_database(db_name)
    print(f"\n Base de données '{db_name}' supprimée.")

#  4. Afficher toutes les collections d’une BD
def list_collections(db_name):
    db = client[db_name]
    collections = db.list_collection_names()
    print(f"\n Collections de la BD '{db_name}' :", collections)

#  5. Créer une collection
def create_collection(db_name, collection_name):
    db = client[db_name]
    db.create_collection(collection_name)
    print(f"\n Collection '{collection_name}' créée dans la BD '{db_name}'.")

#  6. Supprimer une collection
def delete_collection(db_name, collection_name):
    db = client[db_name]
    db.drop_collection(collection_name)
    print(f"\n Collection '{collection_name}' supprimée de la BD '{db_name}'.")

#  7. Ajouter un document à une collection
def add_document(db_name, collection_name, data):
    db = client[db_name]
    collection = db[collection_name]
    result = collection.insert_one(data)
    print(f"\n Document ajouté avec l'ID : {result.inserted_id}")

#  8. Afficher tous les documents d’une collection
def list_documents(db_name, collection_name):
    db = client[db_name]
    collection = db[collection_name]
    documents = collection.find()
    print(f"\n Documents dans '{collection_name}':")
    for doc in documents:
        print(doc)

#  9. Mettre à jour un document spécifique
def update_document(db_name, collection_name, filter_criteria, new_data):
    db = client[db_name]
    collection = db[collection_name]
    result = collection.update_one(filter_criteria, {"$set": new_data})
    print(f"\n Documents mis à jour : {result.modified_count}")

#  10. Supprimer un document spécifique
def delete_document(db_name, collection_name, filter_criteria):
    db = client[db_name]
    collection = db[collection_name]
    result = collection.delete_one(filter_criteria)
    print(f"\n Documents supprimés : {result.deleted_count}")

#  11. Autre requête - Recherche avancée
def search_documents(db_name, collection_name, search_criteria):
    db = client[db_name]
    collection = db[collection_name]
    results = collection.find(search_criteria)
    print(f"\n Résultats de la recherche dans '{collection_name}':")
    for doc in results:
        print(doc)

#  TESTS
if __name__ == "__main__":
    print("\n Connexion réussie à MongoDB")

    # Tests
    list_databases()
    create_database("testDB")
    list_databases()
    list_collections("testDB")
    create_collection("testDB", "students")
    list_collections("testDB")

    student_data = {"nom": "Ali", "prenom": "Mehdi", "age": 22, "filiere": "Informatique"}
    add_document("testDB", "students", student_data)
    
    list_documents("testDB", "students")
    
    update_document("testDB", "students", {"nom": "Ali"}, {"age": 23})
    list_documents("testDB", "students")
    
    search_documents("testDB", "students", {"age": {"$gt": 20}})

    delete_document("testDB", "students", {"nom": "Ali"})
    list_documents("testDB", "students")

    delete_collection("testDB", "students")
    delete_database("testDB")
    list_databases()
