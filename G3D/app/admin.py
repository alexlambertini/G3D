from django.contrib import admin
from PIL import Image
from .models import MenuItem, VideoFile, BannerVideo, GalleryImage, FooterItem, Service, Item, About, Contact
from django.core.files import File


@admin.register(MenuItem)
class menuAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')


class VideoFileInline(admin.StackedInline):
    model = VideoFile
    extra = 1  # Isso permite que você adicione apenas um vídeo por vez


class BannerVideoAdmin(admin.ModelAdmin):
    inlines = [VideoFileInline]


admin.site.register(BannerVideo, BannerVideoAdmin)


@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ['titulo']


@admin.register(FooterItem)
class footerAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'telefone', 'email', 'instagram')



class GalleryAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao')

    def save_model(self, request, obj, form, change):
        # Save the original picture
        super().save_model(request, obj, form, change)

        # Check if the product has a picture
        if obj.image:
            # Open the original image using Pillow
            original_image = Image.open(obj.image.path)
            cropped_image = original_image.crop((0, 0, 100, 100))
            cropped_image.seek(0)

            obj.image_cropped = File(cropped_image, name=f'{obj.titulo}_cropped.jpg')
            obj.image_cropped.save()

            #obj.image_cropped.save(f'{obj.titulo}_cropped.jpg',File(cropped_image, name=f'{obj.titulo}_cropped.jpg'))
    
            

admin.site.register(GalleryImage, GalleryAdmin)


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


