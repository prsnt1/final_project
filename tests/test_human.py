import sys
from pathlib import Path

# Add the project root to the sys.path
# Assuming this script is in the 'tests' directory,
# the project root is one level up.
root_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(root_dir))
from beings.human import Human 

def test_init():
    human =  Human("Prashant", "Sharma", 28)
    assert human.full_name == "Prashant Sharma"