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

## Replacing plant-card illustrations with real photos
The "Plants we specialise in" cards on the home page use illustrations from
`website/static/website/img/industries/`. To use a real photo for a card, save it in that
folder with the card's name, and it replaces the illustration automatically:

`flour-mill`, `chakki-plant`, `sattu-plant`, `grain-storage`, `cleaning-section`,
`milling-section`, `plansifter`, `plc-automation` (+ `.jpg`, `.png` or `.webp`)

## Editing content
- Phone, email, address, founder name, established year → `website/context_processors.py`
- Services, experience, flour-mill industry content → `website/data.py`
- Colours and styling → `website/static/website/css/style.css` (`:root` variables)
- Page layouts → `website/templates/website/`

## Deploy on Railway

The repo is ready for [Railway](https://railway.com): `railway.json` sets the start command
(migrate → collectstatic → gunicorn), and `requirements.txt` includes gunicorn, WhiteNoise
(serves CSS/JS/images) and Postgres support.

1. In Railway, open the service → **Variables** and add:
   - `DJANGO_SECRET_KEY`: a long random string. Generate one with
     `python -c "import secrets; print(secrets.token_urlsafe(50))"`. **Required**; the site refuses to start without it.
   - `DJANGO_ALLOWED_HOSTS` (optional): extra domains, comma-separated. `*.up.railway.app` and
     `rpconsultant.online` are already allowed.
2. **Keep enquiries between deploys:** Railway's disk is wiped on every deploy, so the SQLite file does not
   persist. Add a **Postgres** database to the project and connect it to this service; Railway sets
   `DATABASE_URL` and the site uses it automatically.
3. Create an admin login once: open the service's shell and run `python manage.py createsuperuser`.

Debug mode is off automatically on Railway (set `DJANGO_DEBUG=true` only to troubleshoot).
