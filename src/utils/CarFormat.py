class CarFormat:
    @classmethod
    def car_format(self, car_id):
        if car_id == 1:
            return "Carro a Gasolina (até 1.4)"
        elif car_id == 2:
            return "Carro a Gasolina (1.5 até 2.0)"
        elif car_id == 0:
            return ""
