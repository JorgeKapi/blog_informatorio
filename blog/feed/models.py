from django.db import models
from  django.contrib.auth.models import User


class usuario(models.Model):
    tipo = [("reader","reader"), ("writer","writer"), ("admin","admin")]
    id = models.BigAutoField(primary_key=True)
    usuario_fk = models.ForeignKey(User, on_delete=models.CASCADE)
    tipo_usuario = models.CharField(max_length=10, choices=tipo )

    def __str__(self):
        salida = '{} {} {}'.format(self.id, self.usuario_fk, self.tipo_usuario)
        return salida

class post(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE) 
    titulo = models.CharField(max_length=100)
    contenido = models.TextField()
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)
    me_gusta = models.IntegerField(default=0)
    no_megusta = models.IntegerField(default=0)
    #imagen = models.ImageField(upload_to='post_images', blank=True)
    visitas = models.IntegerField(default=0)

    def __str__(self):
        return self.titulo

class comentario(models.Model):
    post = models.ForeignKey(post, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.TextField()
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.contenido


# Create your models here.
