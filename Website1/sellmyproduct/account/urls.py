from django.conf.urls import url

from account import views

urlpatterns = [
      	 url(r'^$',views.index,name='index'),
    	 url(r'login/',views.loginme,name='loginme'),
    	 url(r'register/',views.registerme,name='registerme'),

    	 url(r'registers/submit/',views.registerSub,name='registerSub'),

    	 url(r'logins/log/',views.loginSub, name='loginSub'),
         url(r'recover/(?P<token>.+)/$',views.recoverpass,name='recoverpass'),

    	 

    	 url(r'Post/',views.add,name='add'),
    	 url(r'profile/',views.myhome,name='profile'),
    	 url(r'logout/',views.logout,name="logout"),

         url(r'change-password/',views.changepass,name='changepass'),
         url(r'change-pass-submit/',views.changepasssubmit,name='changepasssubmit'),


         
         url(r'contact/',views.contactsub,name='contactsub'),
         url(r'forgot-password/',views.forgetpass,name='forgetpass'),
    	 url(r'FAQ/',views.freqaskd,name='freqaskd'),
         url(r'Privacypolicy/',views.privacy,name='privacy'),
         url(r'termsofuse/',views.terms,name='terms'),
]
