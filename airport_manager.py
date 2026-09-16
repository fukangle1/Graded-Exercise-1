######################## IMPORTANT ########################
""" Do not rename the variables or functions.
Do not change the function parameters.
Do not add input() calls inside airport_manager.py.
The file must be importable by the tests. """
###########################################################


airport_info = ("OUL", "1", "14-09-2026")
allowed_gates = {"A1", "A2", "A3", "A4", "B1", "B2"}
restricted_destinations = {"Moscow", "Pyongyang"}
flights = {
    "AY450": {
        "destination": "Helsinki",
        "departure": "08:30",
        "gate": "A2",
        "capacity": 5,
        "passengers": ["Alice Wong", "David Kim", "Fatima Ali"]
    },
    "SK271": {
        "destination": "Stockholm",
        "departure": "10:15",
        "gate": "B1",
        "capacity": 4,
        "passengers": ["Chen Wei", "George Smith"]
    },
    "LH2491": {
        "destination": "Munich",
        "departure": "12:40",
        "gate": "A4",
        "capacity": 5,
        "passengers": ["Hana Lee", "Maria Garcia", "Noah Wilson"]
    }
}

## Logic to find if a flight exists
def find_flight(flights, flight_number):
    if flight_number is None:
        return None
    key = flight_number.strip().upper()
    if key in flights:
        return key
    return None

## Logic to find if a passenger exists
def passenger_exists(passengers, passenger_name):
    if passenger_name is None:
        return False
    target = passenger_name.strip().lower()
    for p in passengers:
        if p.strip().lower() == target:
            return True
    return False


## Logic to check in a passenger
def check_in_passenger(
    flights,
    flight_number,
    passenger_name,
    restricted_destinations
):
    key = find_flight(flights, flight_number)
    if key is None:
        return "FLIGHT_NOT_FOUND"

    if passenger_name is None or passenger_name.strip() == "":
        return "EMPTY_NAME"

    flight = flights[key]
    passengers = flight["passengers"]

    if passenger_exists(passengers, passenger_name):
        return "DUPLICATE"

    if len(passengers) >= flight["capacity"]:
        return "FULL"

    dest = flight["destination"].strip().lower()
    for r in restricted_destinations:
        if r.strip().lower() == dest:
            return "RESTRICTED"

    passengers.append(passenger_name.strip().title())
    return "OK"

## Logic to remove a passenger from a flight
def remove_passenger(
    flights,
    flight_number,
    passenger_name
):
    key = find_flight(flights, flight_number)
    if key is None:
        return "FLIGHT_NOT_FOUND"

    passengers = flights[key]["passengers"]
    target = passenger_name.strip().lower()

    for i in range(len(passengers)):
        if passengers[i].strip().lower() == target:
            passengers.pop(i)
            return "OK"

    return "PASSENGER_NOT_FOUND"



# Logic to change the gate of a flight
def change_gate(
    flights,
    flight_number,
    new_gate,
    allowed_gates
):
    key = find_flight(flights, flight_number)
    if key is None:
        return "FLIGHT_NOT_FOUND"

    if new_gate is None:
        return "INVALID_GATE"

    gate = new_gate.strip().upper()
    if gate not in allowed_gates:
        return "INVALID_GATE"

    flights[key]["gate"] = gate
    return "OK"


# Logic to get the status of a flight
def flight_status(flight):
    num = len(flight["passengers"])
    cap = flight["capacity"]
    percentage = num / cap * 100

    if num >= cap:
        return "FULL"
    elif percentage >= 75:
        return "ALMOST FULL"
    else:
        return "AVAILABLE"


# Logic to get the sorted manifest of a flight
def sorted_manifest(
    flights,
    flight_number
):
    key = find_flight(flights, flight_number)
    if key is None:
        return None
    return sorted(flights[key]["passengers"])

# Logic to get the total number of passengers across all flights
def total_passengers(flights):
    total = 0
    for f in flights.values():
        total += len(f["passengers"])
    return total

# Logic to check if any flight is full
def any_full_flight(flights):
    for f in flights.values():
        if len(f["passengers"]) >= f["capacity"]:
            return True
    return False


# Logic to check if all flights have at least one passenger
def all_flights_have_passengers(flights):
    for f in flights.values():
        if len(f["passengers"]) == 0:
            return False
    return True