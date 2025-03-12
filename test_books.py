from pymongo import MongoClient

# Connexion à MongoDB
client = MongoClient("mongodb://localhost:27017")
db = client["Db_GI"]  # Utilisation de ta base de données
collection = db["books"]  # Utilisation de ta collection

# 🔹 1. CREATE (Ajouter un livre)
def create_book(title, author, year):
    book = {"title": title, "author": author, "year": year}
    result = collection.insert_one(book)
    print(f"Livre ajouté avec l'ID : {result.inserted_id}")

# 🔹 2. READ (Lire les livres)
def read_books():
    books = collection.find()
    for book in books:
        print(book)

# 🔹 3. UPDATE (Modifier un livre)
def update_book(title, new_year):
    result = collection.update_one({"title": title}, {"$set": {"year": new_year}})
    print(f"Livres modifiés : {result.modified_count}")

# 🔹 4. DELETE (Supprimer un livre)
def delete_book(title):
    result = collection.delete_one({"title": title})
    print(f"Livres supprimés : {result.deleted_count}")

# 🚀 TESTS
if __name__ == "__main__":
    print("\n📚 Ajout de livres...")
    create_book("Python pour débutants", "Jean Dupont", 2021)
    create_book("Mastering MongoDB", "Alice Martin", 2019)
    
    print("\n📌 Liste des livres :")
    read_books()
    
    print("\n🔄 Mise à jour de l'année de 'Python pour débutants'...")
    update_book("Python pour débutants", 2023)
    
    print("\n📌 Liste après mise à jour :")
    read_books()
    
    print("\n❌ Suppression de 'Mastering MongoDB'...")
    delete_book("Mastering MongoDB")
    
    print("\n📌 Liste après suppression :")
    read_books()
