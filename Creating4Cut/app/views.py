from django.shortcuts import render, redirect
from .models import Post, Photo
from datetime import timezone
# Create your views here.

def create(request):
    if(request.method == 'POST'):

        new_post= Post.objects.create(
            title = request.POST['title'],
            content = request.POST['content']
        )


        #name속성이 imgs인 input 태그로부터 받은 파일들을 반복문을 통해 하나씩 가져온다
        for img in request.FILES.getlist('imgs'):
            #Photo 객체를 하나 생성한다.
            photo=Photo()
            #외래키로 현재 생성한 Post의 기본키를 참조한다.
            photo.post = new_post
            #imgs로 부터 가져온 이미지 파일 하나를 저장한다.
            photo.image = img
            #데이터베이스에 저장
            photo.save()

        return redirect('detail',new_post.pk)
    return render(request, 'create.html' )

def detail(request, post_pk):
    post=Post.objects.get(pk=post_pk)
    return render(request, 'detail.html', {'post':post})