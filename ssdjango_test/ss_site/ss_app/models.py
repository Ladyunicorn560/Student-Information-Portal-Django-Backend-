from django.db import models

class Student(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    rollno = models.IntegerField()
    department = models.CharField(max_length=50, null=True)
    course = models.CharField(max_length=50, null=True)

    @classmethod
    def create(cls, fname, lname, rollno, department):
        student = cls(fname=fname, lname=lname, rollno=rollno, department=department)
        student.save()
        return student
    
    def delete_student(self):
        self.delete()
