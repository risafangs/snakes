"""snakes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from .views import display_question, SMSFormView, EmailFormView, PaymentFormView

urlpatterns = [
    url(r'^question/(?P<question_id>[0-9]+)/$', display_question, name='display_question'),
    url(r'^choice/(?P<choice_id>[0-9]+)/$', SMSFormView.as_view(), name='choice'),
    url(r'^email/(?P<choice_id>[0-9]+)/$', EmailFormView.as_view(), name='email'),
    url(r'^braintree/(?P<choice_id>[0-9]+)/$', PaymentFormView.as_view(), name='braintree'),
    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
