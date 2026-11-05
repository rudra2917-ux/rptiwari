"""Business details shown across every page. Edit these values to update the whole site."""

SITE = {
    'name': 'R.P. Consultant & Engineers',
    'short_name': 'RPCE',
    'tagline': 'Flour Milling Consultant',
    'founder': 'R.P. Tiwari',
    'founder_full': 'Ratan Prakash Tiwari',
    'founder_title': 'Technical Consultant',
    'phone_display': '+91 88877 08386',
    'phone_raw': '+918887708386',
    'whatsapp': '918887708386',
    'email': 'rptiwari755@gmail.com',
    'address': 'Hanuman Mandir, Ajat Nagar, Badatpur, Varanasi, Uttar Pradesh',
    'city': 'Varanasi, Uttar Pradesh',
    'experience_years': '24+',
    # Year the firm was established. Leave blank to hide it on the site.
    'established': '',
}


def site_info(request):
    return {'site': SITE}
