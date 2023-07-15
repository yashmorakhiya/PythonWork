qlist =[]#dic
print("Quiz Application-:")
print('''Select Your Choice:
1. Attempt Quiz
2. Add Question
3. Exit''')
ch=0
while(ch != 3):
    ch=int(input("Enter Your Choice"))
    rans=0
    wans=0
    if ch == 1:
        print("Attempt Quiz Now")
        for a in qlist:
            print(a['qt'])
            print(a['A'])
            print(a['B'])
            print(a['C'])
            print(a['D'])
            ans= input("Answer")
            if a['CAns']==ans:
                rans=rans+1               
            else:
                wans=wans+1
        print("total right ans ",rans)
        print("total wrong ans ",wans)
                
    if ch == 2:
        q={}
        q['qt']=input("Enter Question")
        q['A']=input("Option A")
        q['B']=input("Option B")
        q['C']=input("Option C")
        q['D']=input("Option D")
        q['CAns']=input("Correct Option")
        qlist.append(q)
        print("Add New Question Here:")