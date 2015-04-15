from django.db import models
from tinymce_4.fields import TinyMCEModelField

# Create your models here.
class Tag(models.Model):
    title_en = models.CharField(max_length=100)
    title_fr = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title_en

class NewsEntry(models.Model):
    date = models.DateField('Date the newsEntry was published on')
    dateTime = models.DateTimeField('Testing DateTimeField')
    image = models.ImageField('Image for the NewsEntry', upload_to='uploads/newsentry/')
    title_en = models.CharField(max_length=100)
    title_fr = models.CharField(max_length=100)
    subtitle_en = models.CharField(max_length=300)
    subtitle_fr = models.CharField(max_length=300)
    content_en = TinyMCEModelField()
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title_en

class Publisher(models.Model):
    name = models.CharField(max_length=50)
    productImage_en = models.ImageField(upload_to='uploads/publisher/')
    logo_en = models.ImageField(upload_to='uploads/publisher/')
    logo_fr = models.ImageField(upload_to='uploads/publisher/')
    tags = models.ManyToManyField(Tag)

class Product(models.Model):
    publisher = models.ForeignKey(Publisher)
    name_en = models.CharField(max_length=100)
    name_fr = models.CharField(max_length=100)
    summary_en = models.CharField(max_length=300)
    summary_fr = models.CharField(max_length=300)
    description_en = models.TextField()
    description_fr = models.TextField()
    image_en = models.ImageField('Product Image - english version',upload_to='uploads/product/')
    image_fr = models.ImageField('Product Image - french version', upload_to='uploads/product/')
    tags = models.ManyToManyField(Tag)

class Job(models.Model):
    title_en = models.CharField(max_length=100)
    title_fr = models.CharField(max_length=100)
    location_en = models.CharField(max_length=200)
    description_en = models.TextField()
    description_fr = models.TextField()
    image_en = models.ImageField('Job Image - english version', upload_to='uploads/job/')
    image_fr = models.ImageField('Job Image - french version', upload_to='uploads/job/')
    date = models.DateField()
    tags = models.ManyToManyField(Tag)
