import sys
from pathlib import Path

# Add the project root to the sys.path
# Assuming this script is in the 'tests' directory,
# the project root is one level up.
root_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(root_dir))
from beings.human import Human 

def test_initialization_with_default_friends_prashant_sharma():
    person = Human("Prashant", "Sharma", 28)
    assert person.first_name == "Prashant"
    assert person.last_name == "Sharma"
    assert person.age == 28
    assert person.friends == []
