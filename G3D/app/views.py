from django.shortcuts import render, redirect
from .models import MenuItem, BannerVideo, GalleryImage, FooterItem, About, Service, Item, Contact
from django.http import JsonResponse
from django.core.mail import send_mail
from .forms import EmailForm


def index(request):
    template_name = 'index.html'
    menu_items = MenuItem.objects.all()
    banner_video = BannerVideo.objects.first()
    gallery_images = GalleryImage.objects.all()
    footer_items = FooterItem.objects.all()
    about = About.objects.all()
    item_services = Item.objects.all()
    service = Service.objects.all()

    email_form = EmailForm()

    context_data = {
        'menu_items': menu_items,
        'banner_video': banner_video,
        'gallery_images': gallery_images,
        'footer_items': footer_items,
        'about': about,
        'item_services': item_services,
        'service': service,
        'email_form': email_form,
    }

    return render(request, template_name, context_data)



def enviar_mensagem(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            mensagem = form.cleaned_data['mensagem']

            # Salvar o nome e o e-mail no banco de dados
            contato = Contact(nome=nome, email=email)
            contato.save()

            # Enviar e-mail para o cliente
            send_mail('Assunto do E-mail', mensagem, 'alexandre.lambertini@gmail.com', [email], fail_silently=False)
        else:
            print(form.errors)
            return redirect('index.html')  # Redirecione para uma página de sucesso após enviar o e-mail

    else:
        form = EmailForm()
        print(form.errors)

    return render(request, 'form.html', {'form': form})



def load_more_images(request):

    page = request.GET.get('page', 1)  # Página padrão é 1
    items_per_page = 5  # Número de imagens por página

    start_index = (int(page) - 1) * items_per_page
    end_index = start_index + items_per_page

    next_images = GalleryImage.objects.all()[start_index:end_index]

    images_data = [
        {
            "image_url": image.image.url, 
            "get_500x500_crop": image.get_500x500_crop, 
            "title": image.titulo, 
            "description": image.descricao
        } 

        for image in next_images]
    
    return JsonResponse(images_data, safe=False)

    