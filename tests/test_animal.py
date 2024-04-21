import sys
from pathlib import Path

# Add the project root to the sys.path
# Assuming this script is in the 'tests' directory,
# the project root is one level up.
root_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(root_dir))
from beings.animal import Animal

def test_animal_initialization_sets_correct_scientific_name():
    """
    Test Case 1: Ensure that the Animal instance is initialized with the correct scientific name.
    """
    leo = Animal("Leo", "Panthera", "leo", True, 5)
    assert leo.scientific_name == "Panthera leo"

def test_celebrating_birthday_increases_age_by_one():
    """
    Test Case 2: Verify that celebrating a birthday correctly increments the animal's age by 1.
    """
    leo = Animal("Leo", "Panthera", "leo", True, 5)
    leo.celebrate_birthday()
    assert leo.age == 6
