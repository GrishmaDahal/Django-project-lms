from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.
SUBJECT = [ 
           ('BCT001','Software engineering'),
           ('BCT002','System Analysis and Design'),
           ('BCT003','Operating Systems'),
           ('BCT004','Object Oriented Programming'),
           ('BCT005','Electronics and Instrumentation')
        ]

class Student(models.Model):
    SEMESTER= [
        ('SEM_ONE','Semester One'),
        ('SEM_TWO','Semester Two'),
        ('SEM_THREE','Semester Three'),
        ('SEM_FOUR','Semester Four'),
        ('SEM_FIVE','Semester Five'),
        ('SEM_SIX','Semester Six'),
        ('SEM_SEVEN','Semester Seven'),
        ('SEM_EIGHT','Semester Eight'),
    ]
    full_name = models.CharField(max_length=200, null=False, blank= False,verbose_name = "Student Full Name")
    email = models.CharField(max_length=200, unique =True ,null=False, blank= False,verbose_name = "Student Email")
    semester = models.CharField(max_length=20,choices=SEMESTER,default='N/A', null=True, blank= False,)
    phone_no = models.IntegerField(null=False, blank= False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "student"
        verbose_name_plural = "students"
        ordering = ['-full_name']
        
    def __str__(self):
        return self.full_name
    
class Teacher(models.Model):
    DEPARTMENT = [
        ('BCA','Bachelor of Computer Application'),
        ('BCT','Bachelor of Computer Engineering'),
        ('BEI','Bachelor of Electronics and Information'),
        ('BCE','Bachelor of Civil Engineering')
    ]
    full_name = models.CharField(max_length=200, null=False, blank= False,verbose_name = "Teacher Full Name")
    email = models.CharField(max_length=200, unique =True ,null=False, blank= False,verbose_name = "Teacher Email")
    department = models.CharField(max_length=20,choices=DEPARTMENT,default='N/A', null=True, blank= False,)
    phone_no = models.IntegerField(null=False, blank= False)
    join_date = models.DateField(default='Join Date')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "teacher"
        verbose_name_plural = "teachers"
        ordering = ['-full_name']  
    
    def __str__(self):
        return self.full_name

class Assignment(models.Model):
    title= models.CharField(max_length=100,  null=False, blank=False, verbose_name= "")
    start_date = models.DateField(default='Start Date', null=False, blank=False, verbose_name='Start Date')
    end_date = models.DateField(default='End Date', null=False, blank=False, verbose_name='End Date')
    question_file = models.FileField(upload_to='assignment/questions/', null=True, blank=False, verbose_name='Select Assignment File')
    question = models.FileField(null=True, blank=True,verbose_name='Assignment Question')
    remark =  models.CharField(max_length=100, null=False,blank=False,verbose_name='Assignment Details')
    full_marks = models.FloatField(blank=False, null=False)
    teacher = models.ForeignKey(Teacher,on_delete= models.CASCADE,verbose_name='Uploaded By')
    subject = models.CharField(max_length = 20, choices = SUBJECT, default='N/A',verbose_name='Subject')    
    
    class Meta:
        verbose_name = 'assignment'
        verbose_name_plural = 'assignments'
        ordering= ['-title']
        
    def __str__(self):
        return self.title
        
#model banaune materials haru, slides haru rakhera 
#teachers ko ma aaye jastai gari material ko ni banaune 
class Materials(models.Model):
    MATERIALS = [
        ('SLIDES', 'Chapter Slides'),
        ('TEXT_BOOK', 'Text Book'),
        ('REFERENCE_BOOK', 'Word files'),
        ('OLD_QUESTIONS', 'Question Collections'),
        ('AUDIO_BOOK','An Audio Book')
    ]
    title= models.CharField(max_length=100, blank=False, null=True, verbose_name = "Chapter Full Name")
    Materials = models.CharField(max_length=50, choices=MATERIALS, default='N/A', null=True, blank= True ,verbose_name ="Materials")
    descriptions = models.CharField(max_length=255, null=False, blank=False, default='N/A',verbose_name='Description ')
    subject = models.CharField(max_length = 20, choices = SUBJECT,default='N/A', verbose_name='Subject') 
    material_file = models.FileField(upload_to='material/', null=False,blank= False, default='N/A', verbose_name='Select File')
    upload_date = models.DateTimeField(default=datetime.now(), verbose_name='Upload Time')
    teacher = models.ForeignKey(Teacher, on_delete= models.CASCADE, default='N/A')
    class Meta:
        verbose_name='material' 
        verbose_name_plural = "materials"
        ordering = ['-title']

    def __str__(self):
        return self.chapter_name
  