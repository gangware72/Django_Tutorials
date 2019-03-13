from django.views.generic import TemplateView #renders a given template with the context containing parameters captured in the URL

class HomePageView(TemplateView): #This is what inheritance looks like in python we  are inheriting from the TemplateView
    template_name = 'home.html'

class AboutPageView(TemplateView): #(1) We already created the template for the about page, so the next step is (2) create this view
    template_name = 'about.html'
