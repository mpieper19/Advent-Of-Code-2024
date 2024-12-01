list1 = []
list2 = []
while True:
    user_input = input()
    if not user_input:
        break
    int1, int2 = map(int, user_input.split())
    list1.append(int1)
    list2.append(int2)

similarity_score = []
for i in list1:
    if i in list2:
        score = i * (list2.count(i))
        similarity_score.append(score)

print(sum(similarity_score))
