class CarriganTire():
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear

    def need_service(self):
        for i in range(4):
            if self.tire_wear[i] <= 0.9:
                return True
        
        return False
