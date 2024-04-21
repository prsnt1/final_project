class Human: 
    def __init__(self, first_name, last_name, age, friends=None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.friends = friends if friends else []

    @property
    def full_name(self):
        """Return the full name, combining first name and last name. Using property decorator for encapsulation"""
        return f"{self.first_name} {self.last_name}"

    def add_friend(self, friend):
        """Add a friend to the list of friends if not already in the list."""
        if friend not in self.friends:
            self.friends.append(friend)

    def remove_friend(self, friend):
        """Remove a friend from the list of friends if in the list."""
        if friend in self.friends:
            self.friends.remove(friend)

    def celebrate_birthday(self):
        """Increase the age by 1 and print a birthday message."""
        self.age += 1
        print(f"Happy Birthday, {self.full_name}! You are now {self.age} years old.")

    @property
    def is_eligible_to_drink(self):
        """Checks if the person is eligible to drink in the USA. The age to drink is 21."""
        return self.age >=21