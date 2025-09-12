from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, permission_required
from .models import Article
from .forms import ArticleForm

@login_required
@permission_required('accounts.can_view_article', raise_exception=True)
def article_list(request):
    articles = Article.objects.all()
    return render(request, 'articles/article_list.html', {'articles': articles})

@login_required
@permission_required('accounts.can_create_article', raise_exception=True)
def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            art = form.save(commit=False)
            art.author = request.user
            art.save()
            return redirect('article_list')
    else:
        form = ArticleForm()
    return render(request, 'articles/article_form.html', {'form': form})

@login_required
@permission_required('accounts.can_edit_article', raise_exception=True)
def article_edit(request, pk):
    art = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=art)
        if form.is_valid():
            form.save()
            return redirect('article_list')
    else:
        form = ArticleForm(instance=art)
    return render(request, 'articles/article_form.html', {'form': form})

@login_required
@permission_required('accounts.can_delete_article', raise_exception=True)
def article_delete(request, pk):
    art = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        art.delete()
        return redirect('article_list')
    return render(request, 'articles/article_confirm_delete.html', {'article': art})
