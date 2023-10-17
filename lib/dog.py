#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name='fido', breed='Pug'):
        if isinstance(name, str) and (1 <= len(name) <= 25):
            self.dog_name = name
        else:
            print("Name must be string between 1 and 25 characters.")
        if breed in APPROVED_BREEDS:
            self.dog_breed = breed
        else:
            print("Breed must be in list of approved breeds.")

    @property
    def name(self):
        return self.dog_name

    @name.setter
    def name(self, name='Rex'):
        if isinstance(name, str) and (1 <= len(name) <= 25):
           self.dog_name = name 
        else:
            print("Name must be string between 1 and 25 characters.")

    @property
    def breed(self):
        return self.dog_breed

    @breed.setter
    def breed(self, breed='Pug'):
        if breed in APPROVED_BREEDS:
            self.dog_breed = breed
        else:
            print("Breed must be in list of approved breeds.")

