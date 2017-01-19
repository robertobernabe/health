from health import (
    GENDER_MALE, GENDER_FEMALE, UNDERWEIGHT, NORMAL_WEIGHT,
    PRE_ADIPOSITY,    ADIPOSITY_I, ADIPOSITY_II,
    ADIPOSITY_III)


class BmiCalculator(object):
    RANGE_UNDERWEIGHT = (0.00, 18.4)
    RANGE_NORMAL_WEIGHT = (18.5, 24.9)
    RANGE_PRE_ADIPOSITY = (25.0, 29.9)
    RANGE_ADIPOSITY_I = (30.0, 34.9)
    RANGE_ADIPOSITY_II = (35.0, 39.9)
    RANGE_ADIPOSITY_III = (40, float('inf'))

    RATING_MAP = [
        (RANGE_UNDERWEIGHT, UNDERWEIGHT),
        (RANGE_NORMAL_WEIGHT, NORMAL_WEIGHT),
        (RANGE_PRE_ADIPOSITY, PRE_ADIPOSITY),
        (RANGE_ADIPOSITY_I, ADIPOSITY_I),
        (RANGE_ADIPOSITY_II, ADIPOSITY_II),
        (RANGE_ADIPOSITY_III, ADIPOSITY_III)
    ]


    def __init__(self, age, height, weight, gender):
        self.age = age
        self.height = float(height) / 100
        self.weight = float(weight)
        self.gender = gender
        self._bmi = None

    @property
    def bmi(self):
        if self._bmi:
            return self._bmi
        return self.calculate()

    def calculate(self):
        self._bmi = self.weight / pow(self.height, 2)
        return self._bmi

    def rate(self, bmi=None):
        if bmi is None:
            bmi = self.bmi

        for _range, rate in self.RATING_MAP:
            if bmi >= _range[0] and bmi <= _range[1]:
                return rate




if __name__ == '__main__':
    print(BmiCalculator(30, 173, 67, GENDER_MALE).calculate())
    print(BmiCalculator(30, 173, 67, GENDER_MALE).rate())