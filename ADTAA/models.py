from django.db import models
# from django_mysql.models import ListCharField

class Course(models.Model):
    courseNumber = models.CharField(max_length=20)
    courseTitle = models.CharField(max_length=50)
    courseDays = models.CharField(max_length =10)
    courseTime = models.CharField(max_length=30)
    # courseDiscipline = ListCharField(
    #     base_field=models.CharField(max_length=50),
    #     size=6,
    #     max_length=(6*50)
    # )
    courseDiscipline_01 = models.CharField(max_length=40)
    courseDiscipline_02 = models.CharField(max_length=40)
    courseDiscipline_03 = models.CharField(max_length=40)




class Instructor(models.Model):
    lastName = models.CharField(max_length=20)
    maxLoad = models.IntegerField()
    # disciplineArea = ListCharField(
    #     base_field=models.CharField(max_length=50),
    #     size=6,
    #     max_length=(6*50)
    # )
    instructorDiscipline_01=models.CharField(max_length=40)
    instructorDiscipline_02 = models.CharField(max_length=40)
    instructorDiscipline_03 = models.CharField(max_length=40)