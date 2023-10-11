from django.contrib import admin
from .models import MenuItem , BannerVideo, GalleryImage, FooterItem, Service, Item, About, Contact
#from django.core.files import File
#from tempfile import NamedTemporaryFile
#from PIL import Image
#from resizeimage import resizeimage


@admin.register(MenuItem)
class menuAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')


# class VideoFileInline(admin.StackedInline):
#     model = VideoFile
#     extra = 1  # Isso permite que você adicione apenas um vídeo por vez


# class BannerVideoAdmin(admin.ModelAdmin):
#     inlines = [VideoFileInline]


admin.site.register(BannerVideo)


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['titulo']


@admin.register(FooterItem)
class footerAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'telefone', 'email', 'instagram')


@admin.register(GalleryImage)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao',)


# class GalleryAdmin(admin.ModelAdmin):
#     list_display = ('titulo', 'descricao')
#     readonly_fields = ['image_cropped']

#     def save_model(self, request, obj, form, change):
#         # Salvar a imagem original
#         super().save_model(request, obj, form, change)

#         # Verificar se o produto possui uma imagem
#         if obj.image:
#             # Abrir a imagem original usando o Pillow
#             original_image = Image.open(obj.image.path)

#             # Determinar as dimensões da miniatura desejada
#             target_size = (500, 500)

#             # Redimensionar a imagem mantendo a proporção, preenchendo e cortando
#             cropped_image = resizeimage.resize_cover(original_image, target_size)

#             # Criar um arquivo temporário para a miniatura
#             with NamedTemporaryFile(delete=True) as temp_file:
#                 cropped_image.save(temp_file, format='JPEG')
#                 temp_file.seek(0)

#                 # Salvar o arquivo temporário no campo 'image_cropped'
#                 obj.image_cropped.save(f'{obj.titulo}_thumb.jpg', File(temp_file))

# admin.site.register(GalleryImage, GalleryAdmin)


admin.site.register(Service)


@admin.register(Contact)
class contactAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email')


# class ItemInline(admin.TabularInline):
#     model = Service.itens.through
#     extra = 1

#@admin.register(Service)
#class ServiceAdmin(admin.ModelAdmin):
    # list_display = ['itens']
#    inlines = [ItemInline]

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['nome']


