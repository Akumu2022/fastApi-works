import json

thisDict = dict(Fname ="John", Lname ="Doe",Age =99, job="Software Dev")
print(thisDict)

x = json.dumps(thisDict)
print(x)

y = json.loads(x)
print(y)
