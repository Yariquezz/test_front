from django.urls import reverse_lazy
from django.views import generic
from .forms import CreatePostForm, EditPostForm
from .models import Post
from django.db.models import Q
import logging


logger = logging.getLogger(__name__)


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'posts/posts.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['top_post'] = Post.objects.latest(
                'created_on', '-updated_on')
            context['featured_post'] = Post.objects.filter(
                status=1).order_by('created_on')[:2]
        except Exception as err:
            logger.error(err)

        return context


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'posts/post_detail.html'


class CreatePost(generic.CreateView):
    model = Post
    form_class = CreatePostForm
    template_name = 'posts/create.html'


class EditPost(generic.UpdateView):
    model = Post
    form_class = EditPostForm
    template_name = 'posts/edit.html'


class DeletePost(generic.DeleteView):
    model = Post
    success_url = reverse_lazy('posts:posts')


class SearchResultsView(generic.ListView):
    model = Post
    template_name = 'posts/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list = Post.objects.filter(
            Q(content__icontains=query)
            | Q(title__icontains=query)
            | Q(category__icontains=query)
        )
        return object_list
