from django.db import models

# Create your models here.
class Choristes(models.Model):
    id=models.AutoField(primary_key=True)
    nom=models.CharField(max_length=24)
    prenom=models.CharField(max_length=24)
    voice=models.CharField(max_length=10)
    
    def __str__(self) -> str:
        return f"{self.nom} {self.prenom}"

class Attendance(models.Model):
    id=models.AutoField(primary_key=True)
    date=models.DateField(auto_now=True)
    is_present=models.BooleanField()
    choriste=models.ForeignKey(Choristes, on_delete=models.PROTECT)
    
    