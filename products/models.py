from django.db import models
from django.utils.text import slugify
from django_smalluuid.models import SmallUUIDField, uuid_default
from django.contrib.contenttypes.fields import GenericRelation

# Create your models here.
class Product(models.Model):
    uuid = SmallUUIDField(default=uuid_default)
    title = models.CharField(unique=True)
    slug = models.SlugField(default="", null=False)
    features = models.JSONField(default=dict, verbose_name="features of product")
    descriptions = models.TextField(verbose_name="descriptions of product")
    discount = models.SmallIntegerField(default=0)
    price = models.IntegerField()
    count = models.PositiveIntegerField(default=0)
    is_special = models.BooleanField(default=False)
    cover = models.ForeignKey("core.Gallery", on_delete=models.SET_DEFAULT, default=1, related_name="cover_of")
    category = models.ForeignKey("Category", on_delete=models.SET_DEFAULT, default=1, related_name="products")
    brand = models.ForeignKey("Brand", on_delete=models.SET_DEFAULT, default=1, related_name="products")
    user = models.ForeignKey('users.User', on_delete=models.SET_NULL, blank=True, null=True)
    color = models.ManyToManyField("Color")
    gallery = models.ManyToManyField("core.Gallery")
    comments = GenericRelation('hub.Comment')
    likes = GenericRelation('hub.Activity')
    points = GenericRelation('hub.point')


    @property
    def final_price(self):
        return self.price - (self.price * self.discount)

    @property
    def average_points(self):
        result = self.points.aggregate(total_points=models.Sum('value'))
        total_points = result['total_points'] or 0
        return total_points / 5
    

    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = slugify(f"{self.title}-{self.uuid}")
        return super().save(*args, **kwargs)

class Category(models.Model):
    name = models.CharField(unique=True)
    parent = models.ForeignKey("self", on_delete=models.SET_NULL, null=True, blank=True, related_name="children")
    slug = models.SlugField(default="", null=False)
    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

class Brand(models.Model):
    name = models.CharField(unique=True)
    parent = models.ForeignKey("self", on_delete=models.PROTECT, related_name="children", null=True, blank=True)
    categories = models.ManyToManyField('Category', related_name="brands")
    slug = models.SlugField(default="", null=False)
    def save(self, *args, **kwargs) -> None:
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class Color(models.Model):
    name = models.CharField(unique=True)
    hexcode = models.CharField(max_length=7, unique=True)


