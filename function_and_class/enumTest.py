# -*- coding: utf-8 -*-
from enum import Enum


class CarType(Enum):
    Male = 0
    Female = 1


male = CarType.Male
print(male)
print(male.name)
print(male.value)
