# """
# <파일 입출력>
# - 데이터를 계속 저장하려면 파일로 저장
# - 코드는 프로그램이 종료되면 사라짐

# <파일 입출력에서 배우는 핵심>
# 1. 파일 쓰기 - w(기존 내용 있으면 덮어씀)
# 2. 파일 읽기 - r
# 3. 파일에 추가하기 - a
# 4. 파일 데이터를 가공해서 자료구조로 바꾸기

# <파일 쓰기 기존 : w>

# """

# file=open("test.txt","w",encoding="utf-8")
# file.write("안녕하세요\n")
# file.close()

# "권장 방식 - with open()" # close()를 안 써도 됨
# with open("test.txt","a",encoding="utf-8")as file:
# 	file.write("안녕하세요\n")

# """ 
# open()은 파일을 여는 함수.
# "test.txt"는 파일 이름.
# "w"는 쓰기 모드.
# encoding="utf-8"은 한글이 깨지지 않도록 설정.
# with를 사용하면 파일을 자동으로 닫아줍니다. 
# """

# """
# 파일을 특정 폴더에 저장하려면 경로를 사용해야 합니다.
# 그런데 폴더가 없으면 오류가 발생합니다.
# 폴더를 자동으로 만들려면 이후에 os 라이브러리를 사용합니다.
# """

# # 여러줄 저장
# with open("memo.txt","w",encoding="utf-8")as file:
# 	file.write("1일차 학습\n")
# 	file.write("2일차 학습\n")
# 	file.write("3일차 학습\n")

# # 파일 불러올 때 공백 제거에 유의해야함!

# # 파일 읽기
# # with open("memo.txt","r",encoding="utf-8")as file:
# # 	content=file.read().rstrip()
# # 	# content=file.read()
# # print(content)

# """
# read()는 파일 전체 내용을 하나의 문자열로 읽어옵니다.
# readline()  - 한 줄씩 읽습니다. (for문과 잘 어울림)
# readlines()  - 여러 줄을 읽습니다.
# """

# with open("memo.txt","r",encoding="utf-8")as file:
# 	lines=file.readlines()

# print(lines) # 공백이 거슬림

# # 문자열 메서드와 연결
# for line in lines:
# 	print(line.strip())

# """
# readlines()는 파일 내용을 줄 단위 리스트로 가져옵니다.
# 각 줄 끝에는 줄바꿈 문자 \n이 포함될 수 있습니다.
# strip()으로 줄바꿈과 공백을 제거할 수 있습니다.
# """

# # 파일에 내용 추가
# with open("memo.txt","a",encoding="utf-8")as file:
# 	file.write("4일차 학습\n")

# # 사용자 입력 메모장에 저장
# memo=input("메모를 입력하세요: ")

# with open("memo.txt","w",encoding="utf-8")as file:
# 	file.write(memo)

# # 여러 메모를 계속 추가하기
# while True:
# 	memo=input("메모를 입력하세요. 종료하려면 q 입력: ").strip()

# 	if memo.lower()=="q":
# 		break
	
# 	with open("memo.txt","a",encoding="utf-8")as file:
# 		file.write(memo+"\n")
	
# 	print("메모 저장이 완료되었습니다.")

# "주의) 메모장에 적힌 모든 내용은 다 문자열 / 숫자 가져올 때 주의"

# students= [
#     {"name":"민수","score":85},
#     {"name":"지수","score":92},
#     {"name":"영희","score":55}
# ]

# with open("students.txt","w",encoding="utf-8")as file:
# 	for student in students:
# 		file.write(f"{student['name']},{student['score']}\n")

# students = []

# with open("students.txt", "r", encoding="utf-8") as file:
#     lines = file.readlines()

# for line in lines:
#     data = line.strip().split(",")

#     student = {
#         "name": data[0],
#         "score": int(data[1])
#     }

#     students.append(student)

# print(students)


# # 예외처리와 연결하기

# try:
#     with open("students.txt", "r", encoding="utf-8") as file:
#         content = file.read()

# except FileNotFoundError:
#     print("파일을 찾을 수 없습니다.")

# else:
#     print(content)

import os

경로 = os.getcwd() # 현재 나의 위치가 출력이 됨
print("경로 :", 경로)

# os.path.exists() # 파일이 있으면 T / 없으면 F 뱉음 
# try,except와 응용

with open("ranking.txt", "a", encoding="utf-8") as file:
    file.write(f"name,count\n")

# 파일이 없다고 오류가 나지 않음(a를 썼을 때)
