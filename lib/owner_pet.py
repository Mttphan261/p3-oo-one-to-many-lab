class Pet:

    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner = ''):
        self.name = name
        if pet_type in self.PET_TYPES:
            self.pet_type = pet_type
        else:
            raise Exception
        self.owner = owner
        if owner:
            owner.add_pet(self)
        Pet.add_pet_to_all(self)

    @classmethod
    def add_pet_to_all(cls, pet):
        cls.all.append(pet)

class Owner:

    def __init__(self, name):
        self.name = name
        self.owners_pets = []

    def pets(self):
        return self.owners_pets
    
    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner = self
            self.owners_pets.append(pet)
        else:
            raise Exception
    
    def get_sorted_pets(self):
        return sorted(self.owners_pets, key=lambda pet: pet.name)
    
# owner = Owner("Ben")
# pet1 = Pet("Fido", "dog", owner)
# pet2 = Pet("Clifford", "dog", owner)
    
# print(owner.get_sorted_pets())