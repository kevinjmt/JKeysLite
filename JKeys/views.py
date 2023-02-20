from msilib.schema import ListView
from django.views import generic
from JKeys.models import Id
from django.shortcuts import render

# View for the Website Home Page
class WebSite(generic.ListView):
    # HTML link to file
    template_name = "jkeys/home.html"
    # objectname in the HTML file
    context_object_name = "websitelist"

    # Function to get all objects in the database and
    # show them thanks to the forloop
    def get_queryset(self):
        return Id.objects.all()

# View for the Detail Page of an Element
class Element(generic.DetailView):
    # HTML link to file
    template_name = "jkeys/element.html"
    # Takes Id Model
    model = Id

# View for the Create Page of an Element
class CreateElement(generic.CreateView):
    # HTML link to file
    template_name = "jkeys/create.html"
    # Fields ready to be filled in the CreateView
    fields = ["name", "mail", "password", "link"]
    # Takes Id Model
    model = Id
    # On success (of creating an object), go to Home Page
    success_url = "/"

    # Save element when 'Save' Button clicked
    def save_element(request):
        # Each field saved in a new Id if POSTed
        # (if the user created a new Id)
        if request.method == "POST":
            name= request.POST.get('name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            link = request.POST.get('link')

            # Create object directly from the texts field
            # stored in the variables as on top
            Id.objects.create(name=name,email=email,password=password,link=link)
        # Return the render of the Home Page when finished saving
        return render(request,'jkeys/home.html')


# View for the Delete Page of an Element
class DeleteElement(generic.DeleteView):
    # HTML link to file
    template_name = "jkeys/delete.html"
    # On success (of deleting), go to Home Page
    success_url = "/"
    # Takes Id Model
    model = Id


# View for the Edit Page of an Element
class EditElement(generic.UpdateView):
    # HTML link to file
    template_name = "jkeys/edit.html"
    # Fields ready to be filled in the EditView
    fields = ["name", "mail", "password", "link"]
    # Takes Id Model
    model = Id
    # On success (of editing), go to Home Page
    success_url = "/"

    # Save element when 'Save' Button clicked
    def save_element(request):
        # Each field saved in a new Id if POSTed
        # (if the user created a new Id)
        if request.method == "POST":
            name= request.POST.get('name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            link = request.POST.get('link')

            # Create object directly from the texts field
            # stored in the variables as on top
            Id.objects.create(name=name,email=email,password=password,link=link)

        # Return the render of the Home Page when finished saving
        return render(request,'jkeys/element.html')