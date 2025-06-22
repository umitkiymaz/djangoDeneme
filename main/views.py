from django.shortcuts import render,redirect
from .models import Post
from .forms import PostForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

@login_required
def anasayfa(request):
    yazilar = Post.objects.all().order_by('-yayin_tarihi')
    return render(request, 'main/anasayfa.html', {'yazilar': yazilar})

@login_required
def yazi_ekle(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('anasayfa')
    else:
        form = PostForm()
    return render(request, 'main/yazi_ekle.html', {'form': form})


@login_required
def yazi_duzenle(request, pk):
    yazi = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=yazi)
        if form.is_valid():
            form.save()
            return redirect('anasayfa')
    else:
        form = PostForm(instance=yazi)
    return render(request, 'main/yazi_ekle.html', {'form': form})

@login_required
def yazi_sil(request, pk):
    yazi = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        yazi.delete()
        return redirect('anasayfa')
    return render(request, 'main/yazi_sil.html', {'yazi': yazi})
