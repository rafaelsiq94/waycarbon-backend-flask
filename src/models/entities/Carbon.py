from utils.DateFormat import DateFormat
from utils.TcoFormat import TcoFormat
from utils.CarFormat import CarFormat


class Carbon:
    def __init__(
        self,
        id,
        car_id=None,
        km=None,
        eletricity=None,
        gas=None,
        total_tco2_monthly=None,
        total_tco2_yearly=None,
        trees=None,
        creation_date=None,
    ) -> None:
        self.id = id
        self.car_id = car_id
        self.km = km
        self.eletricity = eletricity
        self.gas = gas
        self.total_tco2_monthly = total_tco2_monthly
        self.total_tco2_yearly = total_tco2_yearly
        self.trees = trees
        self.creation_date = creation_date

    def to_JSON(self):
        return {
            "id": self.id,
            "car_id": CarFormat.car_format(self.car_id),
            "km": self.km,
            "eletricity": self.eletricity,
            "gas": self.gas,
            "total_tco2_monthly": TcoFormat.convert_tco(self.total_tco2_monthly),
            "total_tco2_yearly": TcoFormat.convert_tco(self.total_tco2_yearly),
            "trees": self.trees,
            "creation_date": DateFormat.convert_date(self.creation_date),
        }
