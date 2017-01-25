from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.
class FoodItem(models.Model):
    name = models.CharField(max_length=200)

    # Would be better to define this in the admin app
    FOOD_TYPES = (
        ('FISH','FISH'),
        ('MEAT','MEAT'),
        ('VEG','VEGETABLE'),
        ('OTH','OTHER')
    )

    type = models.CharField(max_length=5,choices=FOOD_TYPES)

    timer = models.DurationField()

    temperature = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    def get_timer(self):
        time = 0
        times = self.timer.__str__().split(":")
        time += int(times[0])*(60*60)+int(times[1])*(60) + int(times[2])*1
        return time

    def get_temperature(self):
        temp = self.temperature
        degree_sign = u'\N{DEGREE SIGN}'
        if temp == "HIGH":
            temp += " HEAT"
        elif temp == "MEDIUM":
            temp += " HEAT"
        elif temp == "LOW":
            temp += " HEAT"
        else:
            temp += " "+degree_sign+"F"
        return temp

    def get_absolute_url(self):
        return reverse('fooditem_edit',kwargs={'pk':self.pk})




