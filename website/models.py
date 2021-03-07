from django.db import models

class Created(models.Model):
    rua = models.CharField(max_length=100)
    bairro = models.CharField(max_length=50)
    telefone = models.CharField(max_length=15)
    email = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)

    def __str__(self): return f"{self.rua}\n{self.bairro}\n{self.telefone}\n{self.email}\n{self.estado}"

class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    message = models.TextField()

class Categorias(models.TextChoices):
    TECH = 'TC' , 'Tecnologia'
    CR = 'CR', 'Curiosidades'
    GR = 'GR', 'Geral'

class Post(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=200)
    content = models.TextField()
    categories = models.CharField(max_length=2,
                 default=Categorias.GR, choices=Categorias.choices)
    deleted = models.BooleanField(default=True)
    image = models.ImageField(upload_to='post', blank=True, null=True)

    def __str__(self):
        return self.title

    def full_name(self):
        return self.title +' '+ self.subtitle

    def get_categories_label(self):
        return self.get_categories_display()

    full_name.admin_order_field = 'id'