file1 = open("number.txt", "w", encoding="utf8")    #파일 작성
print("A = 90", file=file1)
print("B = 80", file=file1)     
print("c = 70", file=file1)
file1.close()


file2 = open("number.txt", "a", encoding="utf8")    #파일 추가 작성
print("D = 60", file=file2)
file2.close()

file3 = open("number.txt", "r", encoding="utf8")    #파일 읽기
# print(file3.read())
print()
print(file3.readline())
file3.close()