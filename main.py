class Vehicle:
    def __init__(self, name, capacity, base_fare_per_person):
        self.name = name
        self.capacity = capacity
        self.base_fare_per_person = base_fare_per_person

    def vehicle_info(self):
        return f"Vehicle Name: {self.name}, Capacity: {self.capacity}, Base Fare: {self.base_fare_per_person}"

class Bus(Vehicle):
    def calculate_total_fare(self):
        base_total = self.capacity * self.base_fare_per_person
        maintenance_charge = 0.1 * base_total  # 10% maintenance charge
        total_fare = base_total + maintenance_charge
        return total_fare

# Example usage:
if __name__ == "__main__":
    # Create a Bus object
    school_bus = Bus(name="School Bus", capacity=50, base_fare_per_person=20)

    # Display vehicle info
    print(school_bus.vehicle_info())

    # Calculate and display total fare
    total_fare = school_bus.calculate_total_fare()
    print(f"Total Fare (including maintenance): ${total_fare:.2f}")