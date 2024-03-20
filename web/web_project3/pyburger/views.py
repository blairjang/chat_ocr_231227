from django.http import HttpResponse 
# Httpresponse:Django가 반환한 값을 브라우저가 읽을 수 있도록 적절한 처리를 해주는 역할 
from django.shortcuts import render
from burgers.models import Burger


def main(request):
    return render(request, "main.html")

def burger_list(request):
    burgers = Burger.objects.all()
    print("전체 햄버거 목록 :", burgers)

    # Template 전달해줄 dict 객체
    context = {
        "burgers": burgers, # burgers키에 burgers 변수(QuerySet객체)전달
    }
    return render(request, "burger_list.html", context)

def burger_search(request):
    # GET방식으로 전달된 데이터 출력
    keyword = request.GET.get("keyword", None)
    print(keyword)

    if keyword: # 키워드값이 있다면
    # 이름에 전달받은 키워드 값이 포함된 버거 검색
        burgers = Burger.objects.filter(name__contains=keyword)

    else: # 키워드 값이 없어서 none 할당
        burgers = Burger.objects.none() # 빈 QuerySet할당

    context = {
        "burgers" : burgers,
    }
    return render(request, "burger_search.html", context)
