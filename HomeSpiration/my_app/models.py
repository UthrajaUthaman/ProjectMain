from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# Image generation
class Image(models.Model):
    phrase = models.CharField(max_length=200)
    ai_image = models.ImageField(upload_to='images/')  # Ensure this matches your MEDIA_ROOT

    def __str__(self):
        return self.phrase

class User(AbstractUser):
    is_user = models.BooleanField(default=False)
    is_professional = models.BooleanField(default=False)
    is_painter = models.BooleanField(default=False)
    is_plumber = models.BooleanField(default=False)
    is_carpenter = models.BooleanField(default=False)
    is_electrician = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class NormalUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=30,null=True)
    last_name = models.CharField(max_length=30,null=True)
    phone_number = models.CharField(max_length=15, null=True)
    country = models.CharField(max_length=100, null=True)
    profile_photo = models.ImageField(blank=True, null=True, upload_to='profile_photos/')
    registration_date = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.user.username
    

class Professional(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    company_name = models.CharField(max_length=100)
    profile_photo = models.ImageField(upload_to='professional_profile_photos/', blank=True, null=True)
    cover_photo = models.ImageField(upload_to='professional_cover_photos/', blank=True, null=True)
    phone_number = models.CharField(max_length=15)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pincode = models.CharField(max_length=20)
    license_document = models.FileField(upload_to='license_documents/', blank=True, null=True)
    license_number = models.CharField(max_length=100)
    company_verified = models.BooleanField(default=False)  # Field for admin to verify the company

    class CompanyType(models.TextChoices):
        LOCAL_BUILDER = 'LB', 'Local Builder'
        LOCAL_RETAILER = 'LR', 'Local Retailer'
        INTERNATIONAL_BUILDER = 'IB', 'International Builder'
        INTERNATIONAL_RETAILER = 'IR', 'International Retailer'

    company_type = models.CharField(max_length=2, choices=CompanyType.choices)

    def __str__(self):
        return self.company_name
    

class ProfessionalDetails(models.Model):
    professional = models.OneToOneField(Professional, on_delete=models.CASCADE, primary_key=True)
    services_offered = models.CharField(max_length=255, blank=True)
    website_link = models.URLField(max_length=200, blank=True, null=True)
    professional_information = models.TextField(blank=True, null=True)
    business_description = models.TextField(blank=True, null=True)
    certifications_and_awards = models.TextField(blank=True, null=True)
    typical_job_cost = models.CharField(max_length=100, blank=True, null=True)
    number_of_projects = models.CharField(max_length=100)

    def __str__(self):
        return f"Details for {self.professional.company_name}"
    


    
class Project(models.Model):
    professional = models.ForeignKey(Professional, on_delete=models.CASCADE, related_name='projects',blank=True, null=True)
    project_id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=100)
    client_name = models.CharField(max_length=100)
    address = models.TextField()
    start_date = models.DateField()
    expected_end_date = models.DateField()
    total_expected_duration = models.DurationField(help_text="Expected duration in days.")
    cost_of_construction = models.DecimalField(max_digits=12, decimal_places=2)
    image_of_building = models.ImageField(upload_to='projects/buildings/', blank=True, null=True)
    image_of_map = models.ImageField(upload_to='projects/maps/', blank=True, null=True)
    square_feet = models.DecimalField(max_digits=10, decimal_places=2)
    engineer_name = models.CharField(max_length=100, blank=True, null=True)
    contact_number = models.CharField(max_length=20, default='0000000000')

    status = models.CharField(max_length=20, choices=[
        ('Not Started', 'Not Started'),
        ('In Progress', 'In Progress'),
        ('Completed', 'Completed'),
    ], default='Not Started')
    description = models.TextField(blank=True, null=True)
    additional_notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.project_name} ({self.client_name})"

    class Meta:
        ordering = ['start_date']
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'


    
