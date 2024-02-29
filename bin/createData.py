import random
import string
from datetime import datetime, timedelta
import json

def generate_fantasy_name(universe):
    """Generates a fantasy name based on the given universe."""
    name_parts = random.sample(string.ascii_lowercase * 10 + " ", 3)
    name = "".join(name_parts).title()
    if universe == "harry_potter":
        name += " " + random.choice(["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin", "Potter", "Weasley", "Granger", "Dumbledore", "Malfoy", "Snape"])
    elif universe == "star_wars":
        name += " " + random.choice(["Jedi", "Sith", "Rebel", "Empire", "Skywalker", "Solo", "Kenobi", "Palpatine", "Amidala", "Organa"])
    return name

def generate_address(city):
    """Generates a random address based on the given city."""
    # Consider using external data sources (e.g., Google Maps API) for more diverse and realistic addresses.
    street_names = {
        "London": ["Baker Street", "Oxford Street", "Piccadilly Circus"],
        "New York": ["Fifth Avenue", "Wall Street", "Broadway"],
        "Hong Kong": ["Queen's Road Central", "Nathan Road", "Causeway Bay"],
        "Singapore": ["Orchard Road", "Marina Bay", "Sentosa Island"],
        "Frankfurt": ["Zeil", "Hauptwache", "Römerberg"],
    }
    street_name = random.choice(street_names[city])
    house_number = random.randint(1, 100)
    return f"{house_number} {street_name}, {city}"

def get_currency_for_country(city):
    """Retrieves the currency based on the given city."""
    # Consider external services or data sources for real-time or broader coverage.
    currency_map = {
        "London": "GBP",
        "New York": "USD",
        "Hong Kong": "HKD",
        "Singapore": "SGD",
        "Frankfurt": "EUR",
    }
    return currency_map[city]

def generate_postal_code(city):
    """Generates a postal code for the given city."""
    # Generating random postal code format based on country's format
    postal_code_formats = {
        "London": "WC{} {}{}".format(*random.choices(string.ascii_uppercase, k=1), *random.choices(string.digits, k=2)),
        "New York": "{}{}{}{}{}".format(*random.choices(string.digits, k=5)),
        "Hong Kong": "{}{}{}".format(*random.choices(string.digits, k=2), *random.choices(string.ascii_uppercase, k=1)),
        "Singapore": "{} {}{}".format(*random.choices(string.digits, k=3), *random.choices(string.digits, k=3)),
        "Frankfurt": "{}{}{}".format(*random.choices(string.digits, k=5)),
    }
    return postal_code_formats[city]

def get_country(city):
    """Retrieves the country based on the given city."""
    city_country_map = {
        "London": "United Kingdom",
        "New York": "United States",
        "Hong Kong": "China",
        "Singapore": "Singapore",
        "Frankfurt": "Germany",
    }
    return city_country_map[city]

def generate_firm(id):
    """Generates a random firm object with additional attributes."""
    firm_name = generate_fantasy_name(random.choice(["harry_potter", "star_wars"]))
    firm_type = random.choice(["bank", "investment bank", "asset manager", "wealth manager", "fund manager"])
    city = random.choice(["London", "New York", "Hong Kong", "Singapore", "Frankfurt"])
    country = get_country(city)
    aum = random.randint(10000000, 1000000000)

    established_at = datetime.now() - timedelta(days=random.randint(365 * 10, 365 * 30))
    address = generate_address(city)
    postal_code = generate_postal_code(city)

    # Add more relevant and diverse attributes (e.g., contact information, website, employees)
    suffix = random.choice(["fund", "plc", "ltd"])
    firm_name += f" {suffix}"

    return {
        "firm_id": id,
        "firm_name": firm_name,
        "firm_type": firm_type,
        "city": city,
        "country": country,
        "AUM": aum,
        "date_added": established_at.strftime("%Y-%m-%d"),
        "last_updated": datetime.now().strftime("%Y-%m-%d"),
        "established_at": established_at.strftime("%Y-%m-%d"),
        "address": address,
        "postal_code": postal_code
    }

def generate_commitments(firms):
    """Generates a list of commitments."""
    asset_classes = ["re", "pe", "pd", "inf", "hf", "nr"]
    commitments = []
    for _ in range(300):  # Generate 300 commitments
        firm_id = random.choice([2670, 2792, 332, 3611])  # Randomly choose from specified firm_ids
        asset_class = random.choice(asset_classes)
        amount = f"{random.randint(1, 100)}M"
        currency = random.choice(["GBP", "USD", "HKD", "SGD", "EUR"])
        id = random.randint(10000, 99999)
        commitment = {
            "id": id,
            "firm_id": firm_id,
            "asset_class": asset_class,
            "amount": amount,
            "currency": currency
        }
        commitments.append(commitment)
    return commitments

# Generate firm objects
firms = [generate_firm(i + 1) for i in range(10)]

# Generate commitments
commitments = generate_commitments(firms)

# Create a dictionary containing both firms and commitments
data = {
    "firms": firms,
    "commitments": commitments
}

# Write data to JSON file in a readable format
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=4)

print("Data written to data.json")
