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