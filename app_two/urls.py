from django.urls import path
from app_two import views

#Template tagging
app_name = "app_two"

urlpatterns = [
    # path(r'^$',views.index, name="index"),
    # path(r'^admin/', admin.site.urls),

    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('users', views.users, name='users'),
    path('form_page', views.form_name_view, name='form_name'),
    path('input_user', views.input_user_view, name='input_user'),
    path('other', views.other, name='other'),
    path('relative_urls', views.relative_urls, name='relative_urls'),
    path('user_login', views.user_login, name='user_login'),

]
