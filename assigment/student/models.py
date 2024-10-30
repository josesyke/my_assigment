from django.db import models




# Create your models here.
student_types = [
    ('leader', 'cohort leader'),
    ('deputy', 'deputy leader'),
    ('member', 'member')
    
    
]




class Student(models.Model):
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    status = models.BooleanField(default=True)
    student_types = models.CharField(max_length=100,choices= student_types, default='member')
    date_join = models.DateTimeField(auto_now_add=True)

    class meta:
        ordering = ['-date_join']




def __str__(self):
        return f"{self.first_name} {self.last_name}"
    




class Student_Profile(models.Model):
    student = models.OneToOneField(Student,on_delete=models.CASCADE)
    bio = models.TextField()
    date_of_birth =models.DateField()
    address = models.CharField(max_length=300)
    rating = models.FloatField(default=0.0)
    profile_picture = models.ImageField(upload_to='student_profile')
    date_join = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f"{self.student.username} {self.student.first_name}"
    
    
    



class Program(models.Model):
    courses = models.CharField(max_length=500)
    grade = models.IntegerField(default=0.0)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
   
    def __str__(self):
        return f"{self.courses}"

    

   
    



class CohortGroup(models.Model):
    name = models.CharField(max_length=200)
    date_join = models.DateTimeField(auto_now_add=True)
    students = models.ManyToManyField(Student)
    def __str__(self):
       return f"{self.name}"
    