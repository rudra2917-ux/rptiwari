from pathlib import Path

from django.contrib import messages
from django.shortcuts import redirect, render

from . import data
from .forms import ContactForm

GALLERY_DIR = Path(__file__).resolve().parent / 'static' / 'website' / 'img' / 'gallery'
IMAGE_EXTS = {'.jpg', '.jpeg', '.png', '.webp', '.gif'}


def gallery_images():
    """Photos dropped into static/website/img/gallery/ appear on the site automatically."""
    if not GALLERY_DIR.is_dir():
        return []
    photos = []
    for f in sorted(GALLERY_DIR.iterdir()):
        if f.suffix.lower() in IMAGE_EXTS:
            caption = f.stem.replace('-', ' ').replace('_', ' ').strip().capitalize()
            photos.append({'path': f'website/img/gallery/{f.name}', 'caption': caption})
    return photos


INDUSTRY_DIR = Path(__file__).resolve().parent / 'static' / 'website' / 'img' / 'industries'


def industries():
    """Use a real photo for a card when one exists, otherwise the SVG illustration."""
    items = []
    for item in data.INDUSTRIES:
        image = f"website/img/industries/{item['slug']}.svg"
        for ext in ('.jpg', '.jpeg', '.png', '.webp'):
            if (INDUSTRY_DIR / f"{item['slug']}{ext}").exists():
                image = f"website/img/industries/{item['slug']}{ext}"
                break
        items.append({**item, 'image': image, 'is_photo': not image.endswith('.svg')})
    return items


def home(request):
    return render(request, 'website/home.html', {
        'services': data.SERVICES,
        'stats': data.STATS,
        'experience': data.EXPERIENCE,
        'india_facts': data.INDIA_FACTS,
        'expertise': data.EXPERTISE,
        'process': data.CONSULT_PROCESS,
        'flow_strip': data.FLOW_STRIP,
        'faqs': data.FAQS[:4],
        'gallery': gallery_images()[:6],
        'industries': industries(),
        'field_to_flour': data.FIELD_TO_FLOUR,
        'core_services': data.CORE_SERVICES,
        'active': 'home',
    })


def about(request):
    return render(request, 'website/about.html', {
        'experience': data.EXPERIENCE,
        'training_trips': data.TRAINING_TRIPS,
        'stats': data.STATS,
        'gallery': gallery_images(),
        'active': 'about',
    })


def services(request):
    return render(request, 'website/services.html', {
        'services': data.SERVICES,
        'process': data.CONSULT_PROCESS,
        'expertise': data.EXPERTISE,
        'faqs': data.FAQS,
        'active': 'services',
    })


def flour_mills(request):
    return render(request, 'website/flour_mills.html', {
        'india_facts': data.INDIA_FACTS,
        'steps': data.MILLING_STEPS,
        'products': data.PRODUCTS,
        'plant_types': data.PLANT_TYPES,
        'wheat_states': data.WHEAT_STATES,
        'machinery': data.MACHINERY,
        'compliance': data.COMPLIANCE,
        'trends': data.TRENDS,
        'flow_strip': data.FLOW_STRIP,
        'grain_parts': data.GRAIN_PARTS,
        'calc_defaults': data.CALC_DEFAULTS,
        'active': 'flour_mills',
    })


def photo_credits(request):
    return render(request, 'website/photo_credits.html', {'credits': data.PHOTO_CREDITS})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you! Your enquiry has been received. We will contact you shortly.')
            return redirect('contact')
    else:
        initial = {}
        service = request.GET.get('service')
        if service in dict(ContactForm.base_fields['service'].choices):
            initial['service'] = service
        form = ContactForm(initial=initial)
    return render(request, 'website/contact.html', {'form': form, 'active': 'contact'})
