from django.db import models
from pip import locations
from django.contrib.auth.models import User

class Event(models.Model):
    venue = models.CharField(max_length=200)
    date_of_event = models.DateField()
    TOUR = 'T'
    SOCIETY = 'S'
    EVENT_TYPE_CHOICES = (
        (TOUR, 'Tour'),
        (SOCIETY, 'Society'),
    )
    event_type = models.CharField(
        max_length=1,
        choices=EVENT_TYPE_CHOICES,
        default=SOCIETY
    )

    # Function to return a title for the model
    def __str__(self):
        return self.venue + " " + str(self.date_of_event)

    class Meta:
        unique_together = ("venue", "date_of_event")

# Link table to join new members to players who already exist in the dataset.
class User_Player_Link(models.Model):
    user = models.ForeignKey(User, unique=True)

class Results(models.Model):
    player = models.ForeignKey(User_Player_Link)
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

    # Function to calculate the scores from only the Front 9 and Back 9 Score
    def derived_scores(self):
        total_score = self.front_9_score + self.back_9_score
        # derived score for countback scenaries, ie 36pts with 15 on the back 9 would
        # result in a derived score of 36.15
        derived_score = self.front_9_score + self.back_9_score + (self.back_9_score / 100)

        return derived_scores(total_score, derived_score)

#    def date_of_event_short(self):
    # Short function to transform the date into a shorter date
    #    return self.date_of_event.strftime('%b %e %Y')
