class Octoprime():
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear

    def need_service(self):
        sum = 0
        for i in range(4):
            sum += self.tire_wear[i]
        
        if sum <= 3:
            return True
        else:
            return False