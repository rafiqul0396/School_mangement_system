from django.db import models


class  AdminHOD(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=50)
    password=models.CharField(max_length=50)
    create_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    #objects=models.manager()
    
    
    

class Staffs(models.Model):
    id=models.BigAutoField(primary_key=True)
    name=models.CharField(max_length=255)
    email=models.EmailField(max_length=50)
    password=models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    Address=models.TextField()
    #objects=models.Manager()
    
    
    
class  Courses(models.Model):
    id=models.BigAutoField(primary_key=True)
    course_name=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    
    
class  Students(models.Model):
    id=models.BigIntegerField(primary_key=True)
    name=models.CharField(max_length=255)
    email=models.EmailField(max_length=255)
    gender=models.CharField(max_length=255)
    profile_pic=models.FileField()
    password=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    address=models.TextField()
    #objects=models.Manager()
    course_id=models.ForeignKey(Courses,on_delete=models.DO_NOTHING)
    
    
    
    
    
    
# Student attendence 


class  Notification_Students(models.Model):
    id=models.BigAutoField(primary_key=True)
    student_id=models.ForeignKey(Students,on_delete=models.CASCADE)
    message=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    #objects=models.manager()
    
class Notification_Staff(models.Model):
    id=models.BigAutoField(primary_key=True)
    staff_id=models.ForeignKey(Staffs,on_delete=models.CASCADE)
    message=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    
    
# teacher  Attendence  in the project


class Leaves(models.Model):
    id=models.BigAutoField(primary_key=True)
    student_staff_id=models.ForeignKey(Staffs,on_delete=models.CASCADE)
    is_staff=models.BooleanField(default=False)
    status=models.CharField(max_length=20)
    leave_date=models.DateField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

    
    
    # notification in the for Student 
    # notification for Teacher
    
    
    
    
    #leaves for Student
    
    
    #leave for teacher
    
    
    
    # feedbacks for students 
    
    # feedback for teacher
    
    
    

# Create your models here.
