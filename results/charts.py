
#from django_google_charts import charts
from .models import Result

class HandicapChart(charts.Chart):
    chart_slug = 'handicap_chart'
    columns = (
        ('datetime', "Date"),
        ('number', "Handicap"),
    )

    def get_data(self,pk):

        player = get_object_or_404(Player,id=pk)
        eventdate = Result.objects.filter(player_id=pk).order_by('-date_of_event').values('date_of_event')
        handicap = Result.objects.filter(player_id=pk).order_by('-date_of_event').values('handicap')

        return HandicapChart.objects.values_list('eventdate', 'handicap')
