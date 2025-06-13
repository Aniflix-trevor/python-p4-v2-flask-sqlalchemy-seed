#!/usr/bin/env python3
#server/seed.py
from random import choice as rc
from faker import Faker

from app import app
from models import db, Pet

with app.app_context():
    faker = Faker()

    Pet.query.delete()  # Clear the Pet table before seeding

    # Create an empty list
    pets = []

    species = ["Dog", "Cat", "Hamster",  "Turtle", "Chicken"]

    for n in range(10):
        # Create a new Pet instance with random data
        pet = Pet(
            name=faker.first_name(),
            species=rc(species),
        )
        # Append the new Pet instance to the list
        pets.append(pet)
    # Add some Pet instances to the list
    # pets.append(Pet(name = "Fido", species = "Dog"))
    # pets.append(Pet(name = "Whiskers", species = "Cat"))
    # pets.append(Pet(name = "Hermie", species = "Hamster"))
    # pets.append(Pet(name = "Slither", species = "Snake"))


    # Insert each Pet in the list into the database table
    db.session.add_all(pets)

    # Commit the transaction
    db.session.commit()