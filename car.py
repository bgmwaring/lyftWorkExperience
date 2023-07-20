import engine
import battery


class Car(engine, battery):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self):
        if self.engine.needs_service() == True:
            return True
        if self.battery.needs_service() == True:
            return True
        else:
            return False