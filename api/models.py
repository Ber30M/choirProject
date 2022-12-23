from django.db import models

# Create your models here.
class Choriste(models.Model):
    id=models.AutoField(primary_key=True)
    nom=models.CharField(max_length=24)
    prenom=models.CharField(max_length=24)
    voice=models.CharField(max_length=10)

    
    def __str__(self) -> str:
        return f"{self.nom} {self.prenom}"
class Publication(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=50)
    moment_liturgique=models.CharField(max_length=50)
    temps_liturgique=models.CharField(max_length=50)
    author=models.CharField(max_length=50)
    lyrics=models.TextField
    date_added=models.DateField(auto_now=True)
    verified=models.BooleanField()
    posted_by=models.ForeignKey(Choriste, on_delete=models.PROTECT)
    
    def __str__(self) -> str:
        return f"{self.title} {self.Author}"
    
class Attendance(models.Model):
    id=models.AutoField(primary_key=True)
    date=models.DateField(auto_now=True)
    is_present=models.BooleanField()
    choriste=models.ForeignKey(Choriste, on_delete=models.PROTECT)
class Event(models.Model):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    date=models.DateField()
    lieu=models.CharField(max_length=50)
    is_present=models.BooleanField()
    choriste=models.ForeignKey(Choriste, on_delete=models.PROTECT)
    attendances=models.ForeignKey(Attendance, on_delete=models.PROTECT)
    
