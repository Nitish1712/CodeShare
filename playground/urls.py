from django.urls import path
from . import views

urlpatterns = [
	path('',views.home_view0,name="home0"),
	path('user/<str:name>',views.home_view1,name="home1"),
	path('signup',views.signup_view,name="signup"),
	path('login',views.login_view,name="login"),
	path('logout',views.logout_view,name="logout"),
	path('modify',views.modify_view,name="modify"),
	path('initialise',views.initialise,name='initialise'),
	path('update',views.update_view,name='update'),
]