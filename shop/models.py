from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=200)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name'])
        ]
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])


class SubCategory(models.Model):
    category = models.ForeignKey(Category,
                                 related_name='sub_categories',
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    slug = models.SlugField(unique=True, max_length=250)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name'])
        ]
        verbose_name = 'subcategory'
        verbose_name_plural = 'subcategories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_sub_category', args=[self.slug])


class Product(models.Model):
    sub_category = models.ForeignKey(SubCategory,
                                 related_name='products',
                                 on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, max_length=200)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    old_price = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    top_selling = models.BooleanField(default=False)
    new_product = models.BooleanField(default=False)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['-created']),
        ]
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id,
                                                    self.slug])


class Slide(models.Model):
    first_title = models.CharField(max_length=200)
    second_title = models.CharField(max_length=300)
    image = models.ImageField(upload_to='slides', blank=False)
    index_number = models.IntegerField(unique=True, blank=False)
    link = models.URLField(max_length=200, blank=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['index_number']
        verbose_name = 'slide'
        verbose_name_plural = 'slides'
