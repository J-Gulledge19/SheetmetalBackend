from django.db import models

# Create your models here.
class Job(models.Model):
    name = models.CharField(max_length=20, unique=True)
    number = models.IntegerField(unique=True)
    
    def __str__(self):
        return self.name
   
class Download(models.Model):
    dlName = models.CharField(max_length=50)
    done = models.BooleanField()
    dateTurnedIn = models.CharField(max_length=40)
    dateDue = models.CharField(max_length=40)
    receivedBy = models.CharField(max_length=20)
    fittings = models.IntegerField()
    cutOut = models.BooleanField()
    duct = models.IntegerField()
    active = models.BooleanField()
    weight = models.IntegerField()
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='downloads')
    
    def __str__(self):
        return self.dlName
    
# class Weight(models.Model):
#     galv = models.IntegerField()
#     ss = models.IntegerField()
#     blackIron = models.IntegerField()
#     pl = models.IntegerField()
#     alum = models.IntegerField()
#     dl = models.OneToOneField(Download, on_delete=models.CASCADE, related_name='weight', null=True, blank=True)
    
#     def __str__(self):
#         return self.galv
    