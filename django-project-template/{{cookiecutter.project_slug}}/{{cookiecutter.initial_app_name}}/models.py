# Create your models here.

from django.db import models
import datetime

class Person(models.Model):
    birth_date = models.DateField()
    first_name = models.CharField(max_length=50)
    last_name  = models.CharField(max_length=50)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    # llm came up with these ranges 🤷
    def generation(self):
        year = self.birth_date.year
        if year < 1900:
            return "Before 20th Century"
        elif 1900 <= year <= 1927:
            return "The Greatest Generation"
        elif 1928 <= year <= 1945:
            return "Silent Generation"
        elif 1946 <= year <= 1964:
            return "Baby Boomer"
        elif 1965 <= year <= 1980:
            return "Generation X"
        elif 1981 <= year <= 1996:
            return "Millennial (Gen Y)"
        elif 1997 <= year <= 2012:
            return "Generation Z"
        elif year >= 2013:
            return "Generation Alpha"
        else:
            return "Unknown Generation"

