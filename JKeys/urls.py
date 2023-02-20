"""JKeys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    # Link to Home Page (Listview), called "home" in buttons
    # Pattern : url
    path('', views.WebSite.as_view(), name="home"),

    # Link to Create Page (Createview), called "createelement" in buttons
    # Pattern : url/id/create
    path('create', views.CreateElement.as_view(), name="createelement"),

    # Link to Details Page (Detailsview), called "element" in buttons
    # Pattern : url/id
    path('<int:pk>', views.Element.as_view(), name="element"),

    # Link to Edit Page (Updateview), called "elementedit" in buttons
    # Pattern : url/id/edit
    path('<int:pk>/edit', views.EditElement.as_view(), name="elementedit"),

    # Link to Delete Page (Deleteview), called "elementdelete" in buttons
    # Pattern : url/id/delete
    path('<int:pk>/delete', views.DeleteElement.as_view(), name="elementdelete"),

    # Default admin page
    # Pattern : url/admin
    path('admin/', admin.site.urls),
]
