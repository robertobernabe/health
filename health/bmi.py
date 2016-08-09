from health import GENDER_MALE, GENDER_FEMALE

class BmiCalculator(object):

    def __init__(self, age, height, weight, gender):
        self.age = age
        self.height = height
        self.weight = weight
        self.gender = gender

