from engine.engine import Engine

class CapuletEngine(Engine):
    def __init__(self, current_mileage, last_mileage):
        self.current__mileage = current_mileage
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_be_service(self):
        return self.current_mileage - self.last_service_mileage > 30000
