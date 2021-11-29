from django.db import models
from  django.contrib.auth.models import User

class post(models.Model):
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
    contenido = models.TextField()
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.contenido


class usuario(models.Model):
    id = models.BigAutoField(primary_key=True)
    usuario_fk = models.ForeignKey(User, on_delete=models.CASCADE, null=True,   default=None)
    posts = models.ForeignKey(post , on_delete=models.CASCADE, null=True,default=None)
    comentarios = models.ForeignKey(comentario , on_delete=models.CASCADE, null=True, default=None)
    tipo_usuario = models.CharField(max_length=10)

    def __str__(self):
        salida = '{} {} {}'.format(self.id, self.usuario_fk, self.tipo_usuario)
        return salida
# Create your models here.
