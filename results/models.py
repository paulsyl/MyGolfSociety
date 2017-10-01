from django.db import models
from pip import locations
from django.contrib.auth.models import User

class Event(models.Model):
    venue = models.CharField(max_length=200)
    date_of_event = models.DateField()
    TOUR = 'Tour'
    SOCIETY = 'Society'
    EVENT_TYPE_CHOICES = (
        (TOUR, 'Tour'),
        (SOCIETY, 'Society'),
    )
    event_type = models.CharField(
        max_length=100,
        choices=EVENT_TYPE_CHOICES,
        default=SOCIETY
    )

    # Function to return a title for the model
    def __str__(self):
        return self.venue + " " + str(self.date_of_event)

    class Meta:
        unique_together = ("venue", "date_of_event")

# Link table to join new members to players who already exist in the dataset.
class Player(models.Model):
    first_name = models.CharField(max_length=75, blank=False)
    last_name = models.CharField(max_length=75, blank=False)
    date_joined = models.DateField(blank=True)
    starting_handicap = models.DecimalField(max_digits=3, decimal_places=1)
    user = models.ForeignKey(User, unique=True, blank=True, null=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Result(models.Model):
    player = models.ForeignKey(Player, blank=False)
    event = models.ForeignKey(Event)
    handicap = models.DecimalField(max_digits=3, decimal_places=1)
    front_9_score = models.SmallIntegerField()
    back_9_score = models.SmallIntegerField()
    total_score = models.SmallIntegerField()
    derived_score = models.DecimalField(max_digits=4, decimal_places=2)
    event_rank = models.SmallIntegerField()
    event_3rd_place_score = models.SmallIntegerField()
    hc_increase_range = models.DecimalField(max_digits=3, decimal_places=1)
    hc_adjustment_percentage = models.DecimalField(max_digits=3, decimal_places=1)

    class Meta:
        unique_together = ("player", "event")

    def __str__(self):
        return self.player.first_name + " " + self.player.last_name + " " + self.event.venue + " " + str(self.event.date_of_event)
