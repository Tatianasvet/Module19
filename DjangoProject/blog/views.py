from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Message


class BlogPage:
    per_page = 3

    def get_page(self, request):
        messages = Message.objects.all().order_by('-date')
        if request.method == 'POST':
            if request.POST.get('page_len') == 'all':
                self.per_page = len(messages)
            else:
                self.per_page = int(request.POST.get('page_len'))
        paginator = Paginator(messages, self.per_page)
        try:
            page_number = int(request.GET.get('page'))
        except TypeError:
            page_number = 1
        page_posts = paginator.get_page(page_number)
        num_page_list = []
        if page_number - 2 > 1:
            num_page_list.append(0)
        for i in range(max(1, page_number - 2), min(paginator.num_pages, page_number + 2) + 1):
            num_page_list.append(i)
        if page_number + 2 < paginator.num_pages:
            num_page_list.append(0)
        context = {'page_posts': page_posts,
                   'paginator': paginator,
                   'num_page_list': num_page_list}
        return render(request, 'blog_page.html', context)
