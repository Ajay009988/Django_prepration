from django.db import models



class Employee(models.Model):
    name=models.CharField(max_length=80)
    city=models.CharField(max_length=70)
    salary=models.IntegerField()
    email=models.EmailField()

    def __str__(self):
        return self.name


class Student(models.Model):
    name=models.CharField(max_length=80)
    subject=models.CharField(max_length=80)
    fees=models.IntegerField()
    location=models.CharField(max_length=70)

    def __str__(self):
        return self.name