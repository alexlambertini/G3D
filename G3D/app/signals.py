import cloudinary
import cloudinary.uploader
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from .models import GalleryImage


# @receiver(pre_delete, sender=GalleryImage)
# def handle_image_deletion(sender, instance, **kwargs):
#     # Certifique-se de que há uma URL de imagem no modelo
#     if instance.cloudinary_url:
#         # Extrai o "public ID" da URL da imagem
#         public_id = instance.cloudinary_url.split("/")[-1].split(".")[0]
#         # Exclui a imagem do Cloudinary usando o "public ID"
#         cloudinary.uploader.destroy(public_id)