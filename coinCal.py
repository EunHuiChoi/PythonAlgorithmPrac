# 최소개의 동전 조합

coin_dic = {'1q': 25, '1d': 10, '1n': 5, '1p': 1}

print('Enter your coin:')
my_cent = int(input())          # 내가 가진 동전
print('Recheck you coin:', my_cent)
final_cent = 0                  # 얻고자 하는 최소개의 동전

for i in coin_dic.values():
    # print('>>>>>>', i)          # 25, 10, 5, 1
    my_remain = my_cent % i     # 남은 동전의 수
    my_cent = int(my_cent / i)  # 동전의 갯수
    # print(my_remain)
    # print(my_cent)
    final_cent = final_cent + my_cent   # coin_dic 으로 나눈 my_cent 값 누적 더하기
    my_cent = my_remain                 # 나머지값을 이용하여 다시 나눠야 함; 나머지 값은 즉 남은 코인의 갯수를 의미하므로 다시 코인이 되어야 한다.

print('Minimum coin combination:', final_cent)     # 누적된 coin 값만 출력

