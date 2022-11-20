'''
Ex02-4-String.py
파일명 : Ex02-4-String.py
문자열(String)
     하나 이상 연속된 문자(character) 들의 나열.
     파이썬에서 문자열 자료형은 큰 따옴표(" ")
     또는 작은 따옴표 (' ') 사이에 위치.
# 'hello' 와"hello" 동일
print('hello' == "hello"
'''
'''
변수에 문자열 할당 
'''
a = "hello"
print(a)

'''
여러줄 문자열 
     세개의 따옴표를 사용한여 변수에 여러 줄 문자열 할당
'''
a= """피카츄, 라이츄, 파이리, 꼬부기
버터플, 야도런, 피존투, 또가스
"""
print(a)

'''
문자열 배열
      문자열 인덱싱(indexing)
     h   e   l   l   o <== 문자열
     0   1   2   3   4 <== 인덱스
    -5  -4  -3  -2  -1 <== 마이너스 인덱스
'''

a = "hello"
print(a[1])
print(a[1] == a[-4])

'''
문자열 슬라이싱 
     슬라이스 구문을 사용하여 문자범위를 반환할 수 있다.
     문자열의 일부를 반환하려면 시작 인덱스와 끝 인덱스 콜론으로 구분하여 지정한다.
'''
b = "hello, World"
print(b[2:5])
# 처음부터 슬라이스
print(b[:5])
# 끝까지 슬라이스
print(b[2:])

a = "hello,World"
# 대문자
print(a.upper())
# 소문자
print(a.lower())

# 문자열 바꾸기
a = "hello,World"
print(a.replace("H","J"))

# 문자열 연결
a = "hello"
b = "World"
c = a + b
print(c)

c = a + "" + b
print(c)

d = None
print(type(d))