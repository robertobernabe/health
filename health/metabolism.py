from health import GENDER_FEMALE, GENDER_MALE

class MetaBolismCalculator(object):

    def __init__(self, age, height, weight, gender):
        self.weight = float(weight)
        self.height = float(height)
        self.age = age
        self.gender = gender

    def calculate_metabolism(self):
        _ = None
        if self.gender == GENDER_MALE:
            _ = self._calculate_metabolism_male()
        elif self.gender == GENDER_FEMALE:
            _ = self._calculate_metabolism_female()
        return round(_)

    def _calculate_metabolism_male(self):
        return 66.47 + (13.7 * self.weight) + (5 * self.height) - (6.8 * self.age)

    def _calculate_metabolism_female(self):
        return 655.1 + (9.6 * self.weight) + (1.8 * self.height) - (4.7 * self.age)


if __name__ == '__main__':
    assert MetaBolismCalculator(29, 172, 70, GENDER_FEMALE).calculate_metabolism() == 1500
