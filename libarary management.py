print(  "      welcome to libary       "    )
print("what sould you like to do :")
print('''1.view book 
      2.borrow book
      3.return book
      4.exit''')

books = {
    "Harry Potter": True,
    "LOTR": True,
    "The Hobbit": False
}
aviable=print(f"{books}")

while True:
    option=int(input("enter your option:"))
    if option == 1:
        print(books)
    elif option==2:
        book_name=input("which book you want to pick:")
        if book_name in books:
            if books[book_name]==True:
             books[book_name]=False
            else:
                print(f"{book_name } is taken by some one")
        else:
            print("books is not avialbe")
    elif option==3:
        choose=input("do you want to return book (yes/no)? ")
        if choose.lower() =="yes":
            question=input("which book did you tooK:")
            if question in books:
                if books[question]==False:
                    books[question]=True
                else:
                    print("you havent taken the book:")
            else:
                print("i think the book is not ours")
        else:
            print("you must return the book after some day:")
    elif option == 4 :
        print(f"ok have a good day ")
        print(books)
        quit()
                

                 
