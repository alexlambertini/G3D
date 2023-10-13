import os
from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from cloudinary.models import CloudinaryField


# Itens do Menu
class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name} {self.url}"
    
    class Meta:
        verbose_name_plural = "Menu"



# Vídeo de background do banner
class BannerVideo(models.Model):
    video_file = CloudinaryField(
        resource_type='video',
        folder='media/videos/'
    )

    def __str__(self):
        return "video"

    class Meta:
        verbose_name_plural = "Video Banner"


class VideoFile(models.Model):
    banner_video = models.OneToOneField(BannerVideo, on_delete=models.CASCADE)



# Texto Sobre
class About(models.Model):
    titulo = models.CharField(max_length=100, blank=False, unique=True)
    texto = models.TextField(blank=False)
    image = models.ImageField(upload_to='about_images/', blank=False)

    def __str__(self):
        return self.titulo
    
    class Meta:
        verbose_name_plural = "About"



# Cadastro de imagem da Galeria
class GalleryImage(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    image = CloudinaryField('image', folder='media/gallery')

    def __str__(self):
        return f"{self.titulo} {self.descricao}"

    class Meta:
        verbose_name_plural = "Portfolio"

    @property
    def get_500x500_crop(self):
        transformed_image = self.image.build_url(
            transformation=[
                {'width': 500, 'height': 500, 'crop': "fill"},
                {'fetch_format': "auto"}
            ]
        )
        return transformed_image



# Cadastro de Serviços
class Item(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Services Items"


class Service(models.Model):
    titulo = models.CharField(max_length=100)
    itens = models.ManyToManyField(Item, blank=True)
    image = models.ImageField(upload_to='service/', verbose_name='Capa do vídeo')
    youtube_url = models.URLField()

    def image_url(self):
        return self.image.url

    def __str__(self):
        return self.titulo



# Contato
class FooterItem(models.Model):
    titulo = models.CharField(max_length=100, blank=False)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    instagram = models.URLField()

    def __str__(self):
        return f"Dados do Footer"
    
    class Meta:
        verbose_name_plural = 'Contact area'


class Contact(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'Emails received'



@receiver(pre_delete, sender=VideoFile)
def delete_video_file(sender, instance, **kwargs):
    # Exclui o arquivo de mídia associado quando o objeto VideoFile é excluído
    if instance.video_file:
        if os.path.isfile(instance.video_file.path):
            os.remove(instance.video_file.path)    
