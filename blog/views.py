from django.http import HttpResponseRedirect
from django.shortcuts import render
# для отображения записей блога
# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post, Category
from django.shortcuts import render
from .forms import ImageForm, EditForm
from django.urls import reverse_lazy


class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
    # ordering = ['-id']
    ordering = ['-post_date']

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(BlogListView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context


def CategoryView(request, Cats):
    category_posts = Post.objects.filter(category=Cats)
    return render(request, 'categories.html', {'Cats': Cats, 'category_posts': category_posts})


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


class AddPostView(CreateView):
    model = Post
    form_class = ImageForm
    template_name = 'add_post.html'
    #fields = '__all__'
    # fields = ('title', 'author', 'body')


class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    # fields = ('title', 'author', 'image', 'body')


class AddCategoryView(CreateView):
    model = Category
    # form_class = EditForm
    template_name = 'add_category.html'
    fields = '__all__'
    # fields = ('title', 'author', 'image', 'body')

