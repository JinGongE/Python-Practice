import pickle

file1 = open("value.pickle", "wb")      #데이터 파일 저장
valuelist = {"A":90, "B":80, "C":70}
print(valuelist)
pickle.dump(valuelist, file1)
file1.close()

print()

file1 = open("value.pickle", "rb")      #데이터 파일 읽기
print(pickle.load(file1))
file1.close()

with open("score.txt", "w", encoding="utf8") as score:      #close 없이 사용
    score.write("나는 100점이다!!")
    