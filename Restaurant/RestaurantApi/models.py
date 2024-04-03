from django.db import models

# Create your models here.




class Rating(models.IntegerChoices):
    ONE_STAR = 1, '1 Star'
    TWO_STARS = 2, '2 Stars'
    THREE_STARS = 3, '3 Stars'
    FOUR_STARS = 4, '4 Stars'
    FIVE_STARS = 5, '5 Stars'



class Restaurant(models.Model):
    CUISINE_CHOICES = [
        ('AFRICAN', 'African'),
        ('INDIAN', 'Indian'),
        ('CHINESE', 'Chinese'),
        ('WEST_AFRICAN', 'West African'),
        ('ITALIAN', 'Italian'),
        ('EUROPEAN', 'European'),
        ]
    name = models.CharField(max_length=100)
    cuisine_type = models.CharField(max_length=50, choices=CUISINE_CHOICES)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    rating = models.IntegerField(choices=Rating.choices)
    owner = models.ForeignKey('RestaurantOwner', on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class RestaurantOwner(models.Model):
    Gender_Choices=[
        ('Male','Male'),
        ('Female','Female'),
    ]
    FirstName=models.CharField(max_length=100)
    LastName=models.CharField(max_length=100)
    Gender=models.CharField(max_length=100,choices=Gender_Choices)
    PhoneNumber=models.CharField(max_length=13)
    Nationality=models.CharField(max_length=20)


    def __str__(self):
        return self.FirstName
