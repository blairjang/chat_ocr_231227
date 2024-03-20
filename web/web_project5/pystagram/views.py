from django.shortcuts import render, redirect

def index(request):
      #로그인 되어있는 경우, 피드페이지
      if request.user.is_authenticated:
          return redirect("posts:feeds")
      
      #로그인 되어있지 않은 경우, 로그인페이지
      else:
          return redirect("users:login")
        

