D1={
    "Brand":"Ford",
    "Model":"swift",
    "year":1990
}
print(D1)
print(D1.get("Model"))
print(D1["year"])
D1["Year"]=2000
print(D1)
for x,y in D1.items():
    print(x,y)
D1.pop("Model")
print(D1)