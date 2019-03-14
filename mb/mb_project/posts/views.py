from django.views.generic import ListView
from .models import Post

class HomePageView(ListView):
    model = Post #model name
    template_name = 'home.html' #what model were using, this is template reference
    context_object_name = 'all_posts_list'
    #list view returns and object_list
# Create your views here.
