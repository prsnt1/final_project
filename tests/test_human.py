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

def test_full_name_property_returns_correct_full_name_for_prashant_sharma():
    person = Human("Prashant", "Sharma", 28)
    assert person.full_name == "Prashant Sharma"

def test_add_friend_adds_new_friend_to_prashant_sharma():
    person = Human("Prashant", "Sharma", 28)
    person.add_friend("Amit")
    assert "Amit" in person.friends

def test_add_friend_does_not_duplicate_friend_for_ankita_budhraja():
    person = Human("Ankita", "Budhraja", 31, ["Hrishikesh"])
    person.add_friend("Hrishikesh")
    assert person.friends.count("Hrishikesh") == 1

def test_remove_friend_removes_existing_friend_from_prashant_sharma():
    person = Human("Prashant", "Sharma", 28, ["Aarzoo"])
    person.remove_friend("Aarzoo")
    assert "Aarzoo" not in person.friends

def test_remove_friend_does_nothing_if_friend_not_found_for_sushrey_nepal():
    person = Human("Sushrey", "Nepal", 30, ["Aadriana"])
    person.remove_friend("Rupesh")
    assert "Aadriana" in person.friends
    assert len(person.friends) == 1

def test_celebrate_birthday_increases_age_by_one_and_prints_message_for_prashant_sharma(capsys):
    person = Human("Prashant", "Sharma", 28)
    person.celebrate_birthday()
    captured = capsys.readouterr()  # Capture the printed output
    assert person.age == 29
    assert "Happy Birthday, Prashant Sharma! You are now 29 years old." in captured.out
