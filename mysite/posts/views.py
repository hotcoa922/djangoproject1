from django.shortcuts import get_object_or_404, render, redirect
from .models import Post
from .forms import PostForm

# Create your views here.
def post_list(request):
    posts = Post.objects.all()  #객체 전부를 담는다
    ctx = {'posts' : posts} #변수 모음
    return render(request, template_name='posts/list.html', context=ctx)

def post_create(request):
    if request.method == 'POST':    #글 작성을 할 때
        form = PostForm(request.POST)   #빈 form이 아니다
        if form.is_valid(): #유효한지
            post = form.save()  #저장
            return redirect('posts:list')   #리다이렉트 한다 list.url로 
    else:   #get방식 = url로 들어갔을때
        form = PostForm()   #빈 form 즉 글을 쓸 양식
        ctx = {'form':form} #creat.html 로 넘겨줌
    return render(request, template_name='posts/create.html', context=ctx)

def post_update(request, pk):
    post = get_object_or_404(Post, id=pk)   #글 목록에서 객체를 하나만 가져온다 즉 post변수에 글 하나를 넣어줌
    #post = Post.objects.get(pk=pk) #이렇게 써도 된다.

    #post방식일 때 : 저장하기 눌렀을 때, 굳이 id가 필요없음 , 즉 데이터 변경할 때 -> 변경이 핵심!
    if request.method=='POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid:
            form.save()
            return redirect('posts:list')

    #get 방식일 때 : 수정버튼 눌러서 들어간 것(링크로 직접 들어간 것), 데이터를 요청할 때만 쓰임 -> 변경이 아님
    else :
        form = PostForm(instance=post) #안에 내용이 있어야 수정한다
        ctx = {'form' : form}

    return render(request, template_name='posts/create.html', context=ctx)

#delete 만들어야 함 (템플릿 노필요)
def post_delete(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('posts:list')

    
    #근데 생각해보니 삭제 버튼 누르면 즉시 지워지니 get만 있으면 될듯??????????

    #post 방식일 때 : 삭제 버튼 눌렀을 때
    #if request.method=='POST':
       # form = PostForm(request.POST, instance=post)
       # if form.is_valid:
       #
    #get 방식일 때 : 삭제 버튼 누른 결과
   # else :
    #    return render(request, template_name='posts/')

   # return render(request, template_name='posts/')

#detail 만들기 인데 템플릿 필요함, 글 상세보기 페이지
def post_detail(request, pk):
    detail = Post.objects.get(pk=pk)   
    return render(request, 'posts/detail.html', {'post': detail }) 