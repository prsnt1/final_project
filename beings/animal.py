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
