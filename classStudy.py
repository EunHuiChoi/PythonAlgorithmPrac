# class 이름은 보통 대문자로 시작한다.
# 마치 과자 틀과 같은 설계도

import sys
sys.path.append("")

import moduleTest
# from moduleTest import addthis


class FourCalTest:
    pass


# 생성자는 가장 처음 쓰는 것이 일반적
# 부모 클래스
class FourCal:
    def __init__(self, first, second):  # 생성자
        self.first = first
        self.second = second

    def setData(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def div(self):
        result = self.first / self.second
        return result


class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second


class Calculator:
    def __init__(self):
        self.result = 0

    # 클래스 내 함수
    def add(self, num):
        self.result += num
        return self.result


class Family:
    lastname = "김"


# 전역 변수들 선언 이 쯤>?


# 마치 함수처럼 찍어낸다.
cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(4))
print(cal1.add(3))
print(cal1.add(7))

# <class '__main__.FourCal'>
a = FourCalTest()
print(type(a))

# 선언한 클래스 내부의 함수 찍어내기
b = FourCal(1, 2)
b.setData(1, 2)
print(b.first)
print(b.second)

c = FourCal(4, 2)
c.setData(4, 2)
print(c.add())

d = MoreFourCal(4, 2)
print(d.add())

d = MoreFourCal(4, 0)
print('>>>>>>>', d.div())

Family.lastname = "박"
print(Family.lastname)

e = Family()
f = Family()
print(e.lastname)
print(f.lastname)

# 모듈 활용 부분
print('현진님 애정해요', moduleTest.addThis(1, 2))