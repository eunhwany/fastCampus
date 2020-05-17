# Section05-3
# 파이썬 흐름제어(제어문)
# 제어문 관련 퀴즈(정답은 영상)

# 1 ~ 5 문제 if 구문 사용
# 1. 아래 딕셔너리에서 '가을'에 해당하는 과일을 출력하세요.
q1 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}
print("> 1: ",''.join([q1[key] for key in q1 if key == "가을"]))

# 2. 아래 딕셔너리에서 '사과'가 포함되었는지 확인하세요.
q2 =  {"봄": "딸기", "여름": "토마토", "가을": "사과"}
print("> 2: ",("사과" in q2.values()))

# 3. 다음 점수 구간에 맞게 학점을 출력하세요.
# 81 ~ 100 : A학점
# 61 ~ 80 :  B학점
# 41 ~ 60 :  C학점
# 21 ~ 40 :  D학점
#  0 ~ 20 :  E학점
score = 10
grade = ''
if(score >= 81 and score <= 100 ):
    grade = 'A'
elif(score >= 61 and score <= 80 ):
    grade = 'B'
elif(score >= 41 and score <= 60 ):
    grade = 'C'
elif(score >= 21 and score <= 40 ):
    grade = 'D'
elif(score >= 0 and score <= 20 ):
    grade = 'E'
print("> 3: ", grade)
# 4. 다음 세 개의 숫자 중 가장 큰수를 출력하세요.(if문 사용) : 12, 6, 18
a, b, c = 12, 6, 18
best = a
if(b > a):
    best = b
elif(c > b):
    best = c
print("> 4: ", best)

# 5. 다음 주민등록 번호에서 7자리 숫자를 사용해서 남자, 여자를 판별하세요. (1,3 : 남자, 2,4 : 여자)
ihgno = '871025-2079118'
sex = ''
if(int(ihgno[7]) % 2 == 1):
    sex = '남자'
else:
    sex = '여자'
print("> 5: ", sex)

# 6 ~ 10 반복문 사용(while 또는 for)

# 6. 다음 리스트 중에서 '정' 글자를 제외하고 출력하세요.
q3 = ["갑", "을", "병", "정"]

for a in q3:
    if(a == "정"):
        continue
    else:
        print("> 6: ",a)

print("> 6: ",''.join([a for a in q3 if a != "정"]))

# 7. 1부터 100까지 자연수 중 '홀수'만 한 라인으로 출력 하세요.
result = ""
for a in range(1,101,2):
    result = result + str(a) + "/"
print("> 7: ", result)

print("> 7: ",','.join([str(a) for a in range(1,101,2)]))

# 8. 아래 리스트 항목 중에서 5글자 이상의 단어만 출력하세요.
q4 = ["nice", "study", "python", "anaconda", "!"]
result_list = []
for a in q4:
    if len(a) >= 5:
        result_list.append(a)
print("> 8: ", result_list)
print("> 8: ",[a for a in q4 if len(a) >= 5])

# 9. 아래 리스트 항목 중에서 소문자만 출력하세요.
q5 = ["A", "b", "c", "D", "e", "F", "G", "h"]
result_list = []
for a in q5:
    if(a.islower()):
        result_list.append(a)
print("> 9: ", result_list)
print("> 9: ", [a for a in q5 if a.islower()])

# 10. 아래 리스트 항목 중에서 소문자는 대문자로 대문자는 소문자로 출력하세요.
q6 = ["A", "b", "c", "D", "e", "F", "G", "h"]
result_q6 = []
for a in q6:
    if(a.islower()):
        result_q6.append(a.upper())
    else:
        result_q6.append(a.lower())
print("> 10: ", result_q6)
print("> 10: ", [a.upper() if a.islower() else a.lower() for a in q6])
