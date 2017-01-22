from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.
class FoodItem(models.Model):
    name = models.CharField(max_length=200)

    # Would be better to define this in the admin app
    FOOD_TYPES = (
        ('F','FISH'),
        ('M','MEAT'),
        ('V','VEGETABLE'),
        ('O','OTHER')
    )

    type = models.CharField(max_length=1,choices=FOOD_TYPES)

    timer = models.DurationField()

    def __str__(self):
        return self.name

    def __unicode__(self):
        return self.name

    def get_timer(self):
        return self.timer

    def get_absolute_url(self):
        return reverse('fooditem_edit',kwargs={'pk':self.pk})

    ##Will need a start timer method I think





