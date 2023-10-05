class CarAgent:
    """
    The `CarAgent` class represents an agent that can control a car in a simulation.
    It has methods to perceive the current distance to an obstacle and to take action
    based on that perception.

    Constructor:
        def __init__(self, initial_distance: float = 10.0, initial_velocity: float = 20.0)

        Initializes a `CarAgent` object with an initial distance and velocity.

        Parameters:
            - `initial_distance` (float): The initial distance to the obstacle in meters. Default is 10.0.
            - `initial_velocity` (float): The initial velocity of the car in meters per second. Default is 20.0.

    Methods:
        def percept(self, current_distance: float)

        Updates the perception of the current distance to the obstacle.

        Parameters:
            - `current_distance` (float): The current distance to the obstacle in meters.

        def act(self)

        Takes action based on the current perception of the distance.
        If the time to collision is less than 5.0 seconds, it prints "Brake!" and decreases the velocity by 10.0.
        Otherwise, it prints "Add throttle." and increases the velocity by 5.0.

    Example usage:
        agent = CarAgent()
        agent.percept(8.0)
        agent.act()
    """
    def __init__(self, initial_distance = 10.0, initial_velocity = 20.0):
        self.distance = initial_distance
        self.velocity = initial_velocity

    def percept(self, current_distance):
        self.distance = current_distance

    def act(self):
        time_to_collision = self.distance / self.velocity if self.velocity != 0 else float('inf')
        if time_to_collision < 5.0:
            print("Brake!")
            self.velocity -= 10.0
        else:
            print("Add throttle.")
            self.velocity += 5.0

def main():
    # Initialize the agent
    agent = CarAgent(initial_distance=20, initial_velocity=30)

    # scenarios
    distances = [30, 20, 10, 5]  # distances to the car ahead

    # Sensor measurements and actions
    for current_distance in distances:
        agent.percept(current_distance)
        print(f"Car ahead is {current_distance}m far.")
        agent.act()
        print(f"Current velocity: {agent.velocity} m/s\n")

if __name__ == "__main__":
    main()