import test_module as test

radius = test.number_input()

print(test.get_circumference(radius))
print(test.get_circle_area(radius))

# print("메인의 __name__을 출력하기")
# print(__name__)
# print()

# test_module 모듈 활용 가이드
print("get_circumference(10) : ", get_circumference(10))
print("get_circle_area(10) : ", get_circle_area(10))