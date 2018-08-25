from django.db import models

# Create your models here.
class Equipo(models.Model):

    nombre = models.CharField(max_length=100)

    def __str__(self):
        return(self.nombre)


class Fixture(models.Model):

    fecha=models.IntegerField
    local=models.ForeignKey(Equipo,on_delete=models.CASCADE)
    visitante=models.ForeignKey(Equipo,on_delete=models.CASCADE,related_name='relacion1')
    gana_local=models.FloatField        #campo para guardar la probabilidad de que gane el local
    gana_visitante = models.FloatField  #campo para guardar la probabilidad de que gane el visitante

    def __str__(self):
        return '{} {} {} {} {}'.format(self.fecha,self.local,self.gana_local,self.visitante,self.gana_visitante)
