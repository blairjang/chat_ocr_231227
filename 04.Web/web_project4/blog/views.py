from django.shortcuts import render, redirect
from blog.models import Post, Comment

# Create your views here.
def index(request):
    return render(request, "index.html")

def post_list(request):
    posts = Post.objects.all()
    
    print("전체 POST", posts) # 아래 코딩란에 내가 찾은 posts 프린트됨

    # 템플릿에 전달할 딕셔너리 context = {키 : 데이터}
    context = {
        "posts" : posts,
    }
    return render(request, "post_list.html", context)

def post_detail(request, post_id):
    post = Post.objects.get(id = post_id) 
    # id값이 url에서 받은 post_id값인 Post 객체
    # print(post) # 가져온 객체 print 함수로 확인
    if request.method == "POST":
        # textarea의 name속성값(comment)가져옴
        comment_content = request.POST["comment"]
        print(comment_content)
        
        Comment.objects.create(
            post=post,
            content = comment_content,
            )
        #1. GET 요청으로 글 상세페이지 보여주거나
        #2. POST 요청으로 댓글 생성되거나
        #3. 두경우 모두, 이 글의 상세페이지 보여주면 됨

    context = {
        "post" : post,
    }

    return render(request, "post_detail.html", context)

def post_add(request):
    if request.method == "POST": # method가 POST일 때
        title = request.POST["title"]
        content = request.POST["content"]
        thumbnail = request.FILES.get("thumbnail", None) #이미지 파일

        post = Post.objects.create(
            title=title,
            content= content,
            thumbnail=thumbnail, # 이미지 파일을 게시글 객체 생성시에 전달            
        )
        return redirect(f"/posts/{post.id}/")
        # 해당 글의 상세보기 페이지로 이동
    
    return render(request, "post_add.html")