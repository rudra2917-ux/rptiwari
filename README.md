# R.P. Consultant & Engineers – Website

Django website for **R.P. Consultant & Engineers (RPCE)**, a flour milling consultancy.

## Pages
| URL | Page |
|-----|------|
| `/` | Home |
| `/about/` | About Us (company, founder profile, logo story, experience, training, gallery) |
| `/services/` | Services (6 detailed services, consulting process, FAQ) |
| `/flour-mills-in-india/` | Flour Mills in India (industry guide, wheat grain anatomy, Flour Yield Calculator) |
| `/contact/` | Contact Us (enquiry form, saved to database) |
| `/admin/` | Admin panel to read enquiries |

## Run locally (Windows PowerShell)
```powershell
cd "C:\Users\Rudra Narayan Tiwari\Desktop\rp"
pip install -r requirements.txt      # first time only
python manage.py migrate             # first time only
python manage.py runserver
```
Open http://127.0.0.1:8000 in your browser.

### See contact-form enquiries
```powershell
python manage.py createsuperuser     # first time only
```
Then log in at http://127.0.0.1:8000/admin/ → **Enquiries**.

## Logo
- `website/static/website/img/logo.svg`: emblem only (gear + wheat + RP), also used as the favicon
- `website/static/website/img/logo-full.svg`: emblem with company name
- `website/static/website/img/logo-full-white.svg`: version for dark backgrounds

## Adding real photos
Drop `.jpg` / `.png` / `.webp` photos into `website/static/website/img/gallery/`.
A **Gallery** section appears automatically on the Home and About pages, and the file name becomes the caption.

## Editing content
- Phone, email, address, founder name, established year → `website/context_processors.py`
- Services, experience, flour-mill industry content → `website/data.py`
- Colours and styling → `website/static/website/css/style.css` (`:root` variables)
- Page layouts → `website/templates/website/`
