from django.db import models


class ContactMessage(models.Model):
    SERVICE_CHOICES = [
        ('general', 'General enquiry'),
        ('new_plant', 'New flour mill project setup'),
        ('flow_design', 'Mill flow sheet & design'),
        ('commissioning', 'Erection & commissioning'),
        ('performance', 'Mill performance improvement'),
        ('chakki_sattu', 'Chakki atta / Sattu plant'),
        ('training', 'Quality control & staff training'),
    ]

    STAGE_CHOICES = [
        ('idea', 'Idea / planning stage'),
        ('construction', 'Under construction'),
        ('running_upgrade', 'Running mill – want to upgrade'),
        ('running_problem', 'Running mill – facing problems'),
    ]
    MACHINERY_CHOICES = [
        ('not_decided', 'Not decided yet'),
        ('buhler', 'Buhler'),
        ('indian', 'Indian make'),
        ('other', 'Other / mixed'),
    ]
    CONTACT_CHOICES = [
        ('phone', 'Phone call'),
        ('whatsapp', 'WhatsApp'),
        ('email', 'Email'),
    ]

    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    company = models.CharField('Company / Mill name', max_length=150, blank=True)
    location = models.CharField('City / State', max_length=120, blank=True)
    service = models.CharField(max_length=30, choices=SERVICE_CHOICES, default='general')
    project_stage = models.CharField(max_length=30, choices=STAGE_CHOICES, default='idea')
    capacity_tpd = models.PositiveIntegerField('Plant capacity (TPD)', null=True, blank=True)
    machinery = models.CharField('Machinery make', max_length=20, choices=MACHINERY_CHOICES, default='not_decided')
    preferred_contact = models.CharField('Preferred contact', max_length=20, choices=CONTACT_CHOICES, default='phone')
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Enquiry'
        verbose_name_plural = 'Enquiries'

    def __str__(self):
        return f'{self.name} – {self.get_service_display()}'
