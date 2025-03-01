from django.urls import path

from django.conf import settings
from django.conf.urls.static import static


from games.views import HomeView, ContactView, MathFactsView, AnagramHuntView, GameScoresView, ReviewView, record_score

app_name = 'games'
urlpatterns = [

    path('', HomeView.as_view(), name='homepage'),
    path('math-facts/', MathFactsView.as_view(), name='math-facts'),
    path('anagram-hunt/', AnagramHuntView.as_view(), name='anagram-hunt'),
    path('record-score/', record_score, name="record-score"),
    path('game-scores/', GameScoresView.as_view(), name="game-scores"),
    path('contact-us/', ContactView.as_view(), name='contact-us'),
    path('review-us/', ReviewView.as_view(), name='review-us'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)