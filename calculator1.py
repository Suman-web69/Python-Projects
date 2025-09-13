import json
data=[
    {"task": "Finish Python homework", "done":False},
    {"task": "Buy groceries", "done":True},
    {"task": "Read 10 pages of Atomic Habits", "done":False}

]

with open("chice.json","w") as f:
    save=json.dump(data,f)
try:
 with open("chice.json","r") as g:
    lo=json.load(g)
except FileNotFoundError:
        lo=[]
add=input("Enter new task:")
status = input("Is it done? (yes/no): ")
lo.append( {"task":add,"done":True if status.lower() == "yes" else False})

with open("chice.json","w") as i:
    json.dump(lo,i)

   