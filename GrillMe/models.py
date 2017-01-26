from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.
class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)
    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value':self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)

class FoodItem(models.Model):
    name = models.CharField(max_length=200)

    # Would be better to define this in the admin app
    FOOD_TYPES = (
        ('MEAT', 'MEAT'),
        ('FISH','FISH'),
        ('VEG','VEGETABLE'),
        ('OTH','OTHER')
    )

    type = models.CharField(max_length=5,choices=FOOD_TYPES, default=FOOD_TYPES[0])

    hours = models.PositiveIntegerField(default=0)

    minutes = IntegerRangeField(default=0, min_value=0, max_value=60)

    seconds = IntegerRangeField(default=0, min_value=0, max_value=60)

    temperature = models.CharField(max_length=200)

    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    def get_timer(self):
        time = 0
        time += self.hours*(60*60)+self.minutes*60 + self.seconds
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




