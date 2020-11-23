# 1419 : love 2

# 영어 문장이 입력된다.
# 그 문장에서 love가 몇 번 나오는지 출력하시오.

string = input()

count = 0

for i in range(0, len(string)-4):
  if string[i:i+4] == 'love':
    count += 1

print(count)
