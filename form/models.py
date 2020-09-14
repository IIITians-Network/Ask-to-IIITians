from django.db import models
class Form(models.Model):
    INSTITUTE_CHOICES = (
        ('general', 'General'),
        ('kalyani','IIIT Kalyani'),
        ('guwhati','IIIT Guwhati'),
        ('bhagalpur','IIIT Bhagalpur'),
        ('bhopal', 'IIIT Bhopal'),
        ('dharwad', 'IIIT Dharwad'),
        ('gwalior', 'IIIT Gwalior'),
        ('jabalpur', 'IIIT Jabalpur'),
        ('kancheepuram', 'IIIT Kancheepuram'),
        ('kota', 'IIIT Kota'),
        ('kurnool', 'IIIT Kurnool'),
        ('lucknow', 'IIIT Lucknow'),
        ('nagpur', 'IIIT Nagpur'),
        ('pune', 'IIIT Pune'),
        ('raichur', 'IIIT Raichur'),
        ('ranchi', 'IIIT Ramchi'),
        ('sonepat', 'IIIT Sonepat'),
        ('sricity', 'IIIT Sricity'),
        ('surat', 'IIIT Surat'),
        ('tiruchirapalli', 'IIIT Tiruchirapalli'),
        ('una', 'IIIT Una'),
        ('vadodara', 'IIIT Vadodara'),
        ('kottayam', 'IIIT Kottayam'),
        ('manipur', 'IIIT Manipur'),
        ('agartala', 'IIIT Agartala'),
        ('allahabad', 'IIIT Allahabad')
    )

    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    query = models.TextField(null=True)
    institute = models.CharField(max_length=20,choices=INSTITUTE_CHOICES,default='kalyani')
    created = models.DateTimeField(auto_now_add=True)
    replied = models.BooleanField(default=False)
    reply = models.TextField(null=True)
    replied_by = models.CharField(max_length=200)
    secret_code_value = models.CharField(max_length=10)
    secret_code = models.CharField(max_length=10)

   

    def __str__(self):
        return f"{self.name}_{self.email}"


