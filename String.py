sentence = "My name is JinGongE!"

print(sentence.lower())                     #문자열 전부 소문자
print(sentence.upper())                     #문자열 전부 대문자
print(sentence[0].isupper())                #0번째 문자가 대문자인가
print(len(sentence))                        #문자열 길이
print(sentence.replace("JinGongE", "JG"))   #문자열 바꾸기

print("나는 %d살입니다. 그리고 나는 %s학생입니다." % (18, "고등"))              #문자열 포멧 1

print("나는 {}살입니다. 그리고 나는 {}학교 학생입니다.".format(18, "고등"))     #문자열 포멧 2

print("나는 {1}살입니다. 그리고 나는 {0}학교 학생입니다.".format("고등", 18))     #문자열 포멧 3(순서)

print("제 이름은 \"진공이\"입니다.")            #탈출문자