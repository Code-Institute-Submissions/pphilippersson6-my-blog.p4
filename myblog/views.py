from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, EditForm
from django.urls import reverse_lazy

# def home(request):
#    return render(request, 'home.html', {})


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']

    def get_context_data(self, *args, **kwargs):
        categ_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["categ_menu"] = categ_menu
        return context

def CategoryView(request, categ):
    category_posts = Post.objects.filter(category=categ.replace('-', ' '))
    return render (request, 'categories.html', {'categ':categ.title().replace('-', ' '), 'category_posts':category_posts})

class ArticleDetailView(DetailView):
    model = Post
    template_name = 'blogpost_details.html'


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_blogpost.html'

class AddCategoryView(CreateView):
    model = Category
    template_name = 'add_category.html'
    fields = ['name', 'name']

class EditPostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'edit_post.html'

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')