from django.test import TestCase
from .models import Editor,Article,tags,Location,Category
import datetime as dt

# Create your tests here.
class EditorTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.james= Editor(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')
# Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.james,Editor))

    # Testing Save Method
    def test_save_method(self):
        self.james.save_editor()
        editors = Editor.objects.all()
        self.assertTrue(len(editors) > 0)

class ArticleTestClass(TestCase):

    def setUp(self):
        # Creating a new editor and saving it
        self.james= Editor(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')
        self.james.save_editor()

        # Creating a new tag and saving it
        self.new_tag = tags(name = 'testing')
        self.new_tag.save()

        self.new_article= Article(title = 'Test Article',post = 'This is a random test Post',editor = self.james)
        self.new_article.save()

        self.new_article.tags.add(self.new_tag)

    def tearDown(self):
        Editor.objects.all().delete()
        tags.objects.all().delete()
        Article.objects.all().delete()

    def test_get_pics_today(self):
        today_pics = Article.todays_pics()
        self.assertTrue(len(today_pics)>0)

    def test_get_pics_by_date(self):
        test_date = '2017-03-17'
        date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
        pics_by_date = Article.days_pics(date)
        self.assertTrue(len(pics_by_date) == 0)

class LocationTestClass(TestCase):
   # set up method
   def setUp(self):
       self.location = Location(location='Nairobi,Kenya')

   def test_instance(self):
       self.assertTrue(isinstance(self.location, Location))

   def test_save_location(self):
       self.location.save_location()
       location = Location.objects.all()
       self.assertTrue(len(location) > 0)


class CategoryTestClass(TestCase):
   # set up method
   def setUp(self):
       self.category = Category(name='Cool')

   def test_instance(self):
       self.assertTrue(isinstance(self.category, Category))

   def test_save_category(self):
       self.category.save_category()
       category = Category.objects.all()
       self.assertTrue(len(category) > 0)


class ImageTestClass(TestCase):

   # set up method
   def setUp(self):
       # Location
       self.location = Location(location="Nairobi")
       self.location.save()

       # Category
       self.category = Category(category="Home Desktop")
       self.category.save()

       self.image = Image(image='', image_name='photo', image_description='Breif description', location=self.location)
       self.image.save()

       self.new_image.category.add(self.category)

   def tearDown(self):
       Location.objects.all().delete()
       Category.objects.all().delete()
       Image.objects.all().delete()
