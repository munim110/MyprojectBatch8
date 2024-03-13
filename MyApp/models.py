from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()
    photo = models.ImageField(upload_to='contacts', null=True, blank=True)
    
    

    # equivalted DDL command
    # create table contact(
    #     id int primary key auto_increment,
    #     name varchar(122),
    #     email varchar(122),
    #     phone varchar(12),
    #     desc text,
    #     date date
    # );

    # A character field, for small- to large-sized strings.
    # A text field, for large amounts of text.
    # A date field, for a date.
    # A datetime field, for a date and time.
    # An integer field, for whole numbers.
    # A float field, for floating-point numbers.
    # A boolean field, for true/false values.
    # A file field, for file uploads.
    # Image field, for image uploads.


    # the __str__ method is used to display the name of the object in the admin panel
    
    def __str__(self):
        return self.name
    


# Create a model named Product with the following fields:
# product_id (auto increment)
# product_name (charfield)
# product_desc (textfield)
# product_price (floatfield)
    
class Product(models.Model):
    name = models.CharField(max_length=122)
    desc = models.TextField()
    price = models.FloatField()
    photo = models.ImageField(upload_to='products', null=True, blank=True)
    
    def __str__(self):
        return self.name
