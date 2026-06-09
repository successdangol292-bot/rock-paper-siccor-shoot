sentence=input("enter a sentence for this code:")
word=sentence.split()
h=0
for i in word:
    if len(i)>h:
      h=len(i)
for i in word:
     if len(i)>h:
      print(i,"have the higest lengeth in word")


    