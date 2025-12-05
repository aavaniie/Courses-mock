from django.db import models

# Create your models here.
class Times(models.Model):
    time = models.CharField()

    def __str__(self):
        return self.time
    

class Course(models.Model):
    name = models.CharField(max_length=20)
    tutor = models.CharField(max_length=20)
    credits = models.IntegerField()
    students = models.IntegerField()
    times = models.ForeignKey(Times, on_delete = models.CASCADE)
    image = models.ImageField(upload_to='std_image/', null=True, blank=True)

    def __str__(self):
        return self.name
    
