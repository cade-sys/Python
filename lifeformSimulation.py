# Cade Kirkpatrick
# 02/28/2023
import random
import math
import matplotlib.pyplot as plt

# Constants 
DETECTION_LIMIT = 1000  # Distance for detection in light years raised due to inaccurate results
NUM_SIMULATIONS = 15000 # Number of simulations to run
MIN_LIFEFORMS = 1000 # Minimum number of life-bearing planets
MAX_LIFEFORMS = 10000 # Maximum number of life-bearing planets
STEP_SIZE = 500 # Step size for the number of life-bearing planets


def generate_planet(): # Generates a random life-bearing planet in the Milky Way
    """Generates a random life-bearing planet in the Milky Way"""
    r = random.uniform(15000, 50000) # Generates a random distance from the center of the Milky Way
    theta = random.uniform(0, 2*math.pi) # Generates a random angle
    z = random.uniform(0,1000) # Generates a random height
    x = r * math.cos(theta) # Finds x coordinate of the life-bearing planet
    y = r * math.sin(theta) # Finds y coordinate of the life-bearing planet
    return x, y, z

def squared_distance(x1, y1, z1, x2, y2, z2): # Computes the squared distance between two points in 3D space
    """Computes the squared distance between two points in 3D space"""
    return ((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)

def main(): # Runs the simulation
    x_values = []
    y_values = []
    for lifeforms in range(MIN_LIFEFORMS, MAX_LIFEFORMS, STEP_SIZE): # Runs the simulation for a range of life-bearing planets
        detections = 0
        for _ in range(NUM_SIMULATIONS): # Runs the simulation NUM_SIMULATIONS times
            for _ in range(lifeforms): # Runs the simulation for a given number of life-bearing planets
                planet_x, planet_y, planet_z = generate_planet() # Generates a random life-bearing planet
                earth_x, earth_y, earth_z = generate_planet() # Generates Earth at a random location in the Milky Way
                distance_sq = squared_distance(earth_x, earth_y, earth_z, planet_x, planet_y, planet_z) # Computes the squared distance between Earth and the life-bearing planet
                if distance_sq <= DETECTION_LIMIT**2: # Checks if the life-bearing planet is within the detection limit
                    detections += 1 # Increases the number of detected life-bearing planets
                    break # Breaks out of the loop to avoid double counting
        detection_prob = detections / NUM_SIMULATIONS * 100 # Computes the detection probability
        x_values.append(lifeforms) # Stores the number of life-bearing planets
        y_values.append(detection_prob) # Stores the detection probability
        print(f"Lifeforms: {lifeforms}, Detection Probability: {detection_prob} %") # Prints the results of the simulation
    plt.plot(x_values, y_values)
    plt.xlabel("Number of Life-bearing Planets")
    plt.ylabel("Probability of Detection [%]")
    plt.title("Fermi Paradox Simulation")
    plt.show()

if __name__ == '__main__':
    main()