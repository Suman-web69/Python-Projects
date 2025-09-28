import json
import os

# if os.path.exists("diary.json"):
    
#     with open("diary.json","r") as y :
#         read=json.load(y)
#         for items in read:
#             self.en

entries=[]
# if os.path.exists("diary.json"):
#     with  open("diary.json","r") as f :
#         read=json.load(f)
#         for items in read:
#             entries.append(items)
# if not os.path.exists("diary.json"):
#     with  open("diary.json","r") as f :
#         read=json.load(f)
#         for items in read:
#             entries.append(items)        

class DiaryEntry:
    def __init__(self,title,date,note,mood):
        self.title=title
        self.date=date
        self.note=note
        self.mood=mood
        
    
    def to_Dict(self):
        return {"Title":self.title,"Date":self.date,"Note":self.note,"mood":self.mood}
    
    
    def __str__(self):
        return f"I noted {self.note} in {self.date} in mood {self.mood}.Topic was {self.title}"
    
note1=DiaryEntry("Work","2 Sep","I am coding","normal")
entries.append(note1.to_Dict())
print(note1)

class Diarymanager:
    # def __init__(self):
    #     self.entries=[]
        
    

       

    def add(self,title,date,note,mood):
          entry = DiaryEntry(title, date, note, mood)  # make object
          entries.append(entry.to_Dict())
        # self.title0=title0
        # self.date0=date0
        # self.note0=note0
        # self.mood0=mood0
        # self.entries.append((title0,date0,note0,mood0))

    def delete(self,title2):
        self.title2=title2
        global entries
        entries = [n for n in entries if n["Title"].lower() != self.title2.lower()]

                 

    def view(self):
        for notes2 in entries:
            print(notes2) 

    def search(self,title3):
        self.title3=title3
        notes3=[k for k in entries if k["Title"].lower()==self.title3.lower() ]
        print(notes3)  

    def addinjson(self):
      
        with open("diary.json","w") as o :
          json.dump(entries,o)


print("1.Add\n2.Delete\n3.View\n4.Search")
choice=input("Enter your Choice:")
if choice=="1":
 manager=Diarymanager()
 title=input("Enter title:")
 date=input("Enter date:")
 note=input("Enter note:")
 mood=input("Enter mood:")
 a1=manager.add(title,date,note,mood)
elif choice=='2':
  title2=input("Enter title:")
  manager=Diarymanager()
  d1=manager.delete(title2)
elif choice=="3":
    manager=Diarymanager()
    v1=manager.view()

elif choice=="4":
    title4=input("Enter title:")
    manager=Diarymanager()
    s1=manager.search(title4)
else:
    print('Choice is incorrect.')

manager=Diarymanager()
manager.addinjson()    

            

    

        


    


        







