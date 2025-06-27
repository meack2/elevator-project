# Elevator Project

This project simulates an elevator that moves between requested floors and reports the total travel time and the order of floors visited.

## Features

- Simple elevator simulation in Python
- Calculates total travel time assuming 10 seconds per floor
- Visits floors in the given input order
- Command-line interface for easy testing

## Assumptions

- The elevator starts at the specified start floor.
- Each destination is visited in the order provided (no route optimization).
- Travel time is strictly calculated as 10 seconds per floor.
- No delays for opening/closing doors or loading/unloading passengers.
- Only a single elevator is simulated.

## Usage

### Requirements

- Python 3.x

### How to Run

1. Clone or download this repository
2. Open your terminal and navigate to the project folder
3. Run the script using:

```bash
python elevator_simulator.py <start_floor> <floor_list>
```