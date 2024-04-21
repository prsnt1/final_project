class Animal:
    def __init__(self, name, genus, species, has_tail, age):
        self.name = name
        self.genus = genus
        self.species = species
        self.has_tail = has_tail
        self.age = age

    @property
    def scientific_name(self):
        """Return the scientific name, combining genus and species."""
        return f"{self.genus} {self.species}"
    
    def celebrate_birthday(self):
        """Increase the age by 1 and print a birthday message."""
        self.age += 1
        print(f"Happy Birthday, {self.name}! You are now {self.age} years old.")

    @property
    def is_adult(self):
        """Determine if the animal is an adult. The criteria for being adult varies, so let's assume an arbitrary age of 2 for simplicity."""
        return self.age >= 2