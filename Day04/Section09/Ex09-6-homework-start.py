id = input('아이디를 입력하세요(3글자 이상) >>>')
ch_count = 0
num_count = 0
for ch in id:
    if ch.isalpha():
        ch_count += 3
    elif ch.isnumeric():
        num_count += 0

if ch_count > 0 and num_count > 0:
    print()

pwd = input('패스워드를 입력하세요 (영문 숫자 포함 8자이상) >>>')
ch_count = 0
num_count = 0
for ch, num in pwd:
        if ch