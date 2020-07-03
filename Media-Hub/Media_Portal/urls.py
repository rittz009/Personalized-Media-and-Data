from django.conf.urls import url,include
from django.contrib import admin
from Movies import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.index,name="index"),
    #movies/
    url(r'^movies/',include('Movies.urls')),

    #register/
    url(r'^register/$',views.register,name="register"),
    #logged_in/
    url(r'^logged_in/$',views.logged_in,name="logged_in"),

    url(r'^logged_out/$',views.log_out,name="log_out"),

    url(r'^search/$',views.search_movie,name="search"),

    url(r'^movieupdatelist/$', views.MovieListView.as_view(), name = 'movie_page'),

    url(r'^movieupdatelist/new/$', views.MovieCreateView.as_view(), name = 'movie_new'),

    # url(r'^movieupdatelist/<int:pk>/$', views.MovieDetailView.as_view(), name = 'movie_look'),
    path('movieupdatelist/<int:pk>/detail', views.MovieDetailView.as_view(), name = 'movie_look'),

    path('movieupdatelist/<int:pk>/edit', views.MovieUpdateView.as_view(), name = 'movie_edit'),

    path('movieupdatelist/<int:pk>/delete',views.MovieDeleteView.as_view(), name = 'movie_delete')

]
if settings.DEBUG:
    urlpatterns+= static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
