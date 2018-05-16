from django.db import models
import datetime as dt

# Create your models here.

class Editor(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    phone_number = models.CharField(max_length =10,blank = True)

    def __str__(self):
        return self.first_name

    def save_editor(self):
        self.save()
    class Meta:
        ordering = ['first_name']


class tags(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name


class Location(models.Model):
   location = models.CharField(max_length=70)

   def __str__(self):
       return self.location

   def save_location(self):
       self.save()

   def delete_location(self):
       self.delete()


class Category(models.Model):
   name = models.CharField(max_length=25)

   def __str__(self):
       return self.name

   def save_category(self):
       self.save()

   def delete_category(self):
       self.delete()


class Article(models.Model):
    title = models.CharField(max_length =60)
    post = models.TextField()
    editor = models.ForeignKey(Editor)
    tags = models.ManyToManyField(tags)
    pub_date = models.DateTimeField(auto_now_add=True)
    article_image = models.ImageField(upload_to = 'articles/')
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)

    @classmethod
    def todays_pics(cls):
        today = dt.date.today()
        pics = cls.objects.filter(pub_date__date = today)
        return pics

    @classmethod
    def days_pics(cls,date):
        pics = cls.objects.filter(pub_date__date = all)
        return pics

    @classmethod
    def search_by_title(cls,search_term):
        pics = cls.objects.filter(title__icontains=search_term)
        return pics

def save_image(self):
       self.save()

       def delete_image(self):
           self.delete()

           @classmethod
           def get_image_by_id(cls, id):
               pass

               @classmethod
               def filter_by_location(cls, location):
                   pass

                   @classmethod
                   def get_images(cls):
                       return cls.objects.all()

                       @classmethod
                       def search_category(cls, search_term):
                           category = cls.objects.filter(category__name__icontains=search_term)
                           return category
