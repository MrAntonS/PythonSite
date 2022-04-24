from django.db import models


class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='Title')
    content = models.TextField(blank=True, verbose_name="Content")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Time Created")
    updated_at = models.DateTimeField(auto_now=True, blank=True, verbose_name='Last Update')
    photo = models.ImageField(upload_to = 'photos/%Y/%m/%d/', verbose_name='Photo', blank=True)
    is_published = models.BooleanField(default=False, verbose_name="Publised")
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)


    def __str__(self):
        return self.title
    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"
        ordering = ['-created_at', 'title']

class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True, verbose_name="Category Name")
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['title']
