# elevator_simulator.py

import sys

# Constants
FLOOR_TRAVEL_TIME = 10  # seconds per floor

def simulate_elevator(start, destinations):
    # Clean and convert destinations to integers
    try:
        floor_list = [int(floor.strip()) for floor in destinations.split(",")]
        current_floor = int(start)
    except ValueError:
        return "Invalid input. Please enter integer values only."

    visited_floors = [current_floor]
    total_time = 0

    for floor in floor_list:
        travel = abs(current_floor - floor)
        total_time += travel * FLOOR_TRAVEL_TIME
        current_floor = floor
        visited_floors.append(current_floor)

    return total_time, visited_floors

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python elevator_simulator.py <start_floor> <floor_list>")
        print("Example: python elevator_simulator.py 12 2,9,1,32")
        sys.exit(1)

    start_floor = sys.argv[1]
    destination_floors = sys.argv[2]

    time, visited = simulate_elevator(start_floor, destination_floors)
    print(f"{time} {','.join(map(str, visited))}")
