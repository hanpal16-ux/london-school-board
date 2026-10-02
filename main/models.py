from django.db import models

# Create your models here.

class Student(models.Model):
    student_name=models.CharField(max_length=150)
    student_age=models.IntegerField()
    student_city=models.CharField(max_length=150)
    student_email=models.EmailField()
    student_phone=models.CharField(max_length=20)
    student_subject=models.CharField(max_length=100)
    student_grade=models.IntegerField()
    student_hobby=models.CharField(max_length=150)
    student_address=models.CharField(max_length=100)
    enrollment_year= models.IntegerField()
    
    def __str__(self):
        return self.student_name
    
class Teacher(models.Model):
    teacher_name=models.CharField(max_length=150)
    teacher_age=models.IntegerField()
    teacher_city=models.CharField(max_length=150)
    teacher_email=models.EmailField()
    teacher_phone=models.CharField(max_length=20)
    teacher_subject=models.CharField(max_length=100)
    teacher_grade=models.IntegerField()
    teacher_hobby=models.CharField(max_length=150)
    teacher_address=models.CharField(max_length=100)
    enrollment_year= models.IntegerField()
    
    def __str__(self):
        return self.teacher_name

class Products_table(models.Model):
    product_name = models.CharField(max_length=150)
    product_description = models.TextField()
    product_amount = models.DecimalField(max_digits=6, decimal_places=2)
    product_image = models.ImageField(upload_to='products/')
    product_category= models.CharField(max_length=100)


    def __str__(self):
        return self.product_name + "-" + self.product_description