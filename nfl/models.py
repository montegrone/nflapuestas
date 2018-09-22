from django.db import models



class Todo(models.Model):

    descripcion=models.TextField()
    terminado=models.BooleanField()


    def __str__(self):
        return self.descripcion
    
