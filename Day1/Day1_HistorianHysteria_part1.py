list1 = []
list2 = []
while True:
    user_input = input()
    if not user_input:
        break
    int1, int2 = map(int, user_input.split())
    list1.append(int1)
    list2.append(int2)
sorted1 = (sorted(list1))
sorted2 = (sorted(list2))

distances = []
for i in range(len(sorted1)):
    distances.append(abs(sorted1[i] - sorted2[i]))

print(sum(distances))
