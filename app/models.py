from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50,unique=True,verbose_name="Kategoriya")

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"
    
class Tags(models.Model):
    name = models.CharField(max_length=30,verbose_name="Tag nomi")

    def __str__(self) -> str:
        return self.name     

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Taglar"       

class News(models.Model):
    name = models.CharField(max_length=255, verbose_name  =  "Nomi")
    slug = models.SlugField(max_length=255, verbose_name ="Slug")
    deskription = models.TextField(blank=True, null=True, verbose_name="Matni")
    image = models.ImageField(blank=True, null=True, verbose_name="Rasmi")
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tags, verbose_name="Taglar")
    views = models.IntegerField(default=0, verbose_name="Kurishlar soni")
    is_active = models.BooleanField(default=True, verbose_name="Saytga chiqarish")
    is_banner = models.BooleanField(default=False, verbose_name="Bannerga chiqarish")
    is_weekly = models.BooleanField(default=False, verbose_name="Haftalik yangilk")
    

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = "Yangilik"
        verbose_name_plural = "Yangiliklar"
    
