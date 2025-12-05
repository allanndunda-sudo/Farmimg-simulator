from farm_database import SessionLocal
from models.animal import Animal
from models.category import Category

def register_animal():
    session = SessionLocal()

    name = input("Animal name: ")
    gender = input("Gender (male/female): ")
    species = input("Species: ")

    animal = Animal(name=name, gender=gender, species=species)
    session.add(animal)
    session.commit()

    print("Animal saved!")

if __name__ == "__main__":
    register_animal()
