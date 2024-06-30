dic1={1:10, 4:30}
dic2={3:20, 2:40}
dic3={5:50, 6:60}

result = {}
for i in [dic1,dic2,dic3]:
    result.update(i)

print(result)

print(1 in result)

print(sorted(result.values()))
print(sorted(result.keys()))

print(10 in result.values())