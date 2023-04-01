#Q1
def my_func(x1,x2,x3):
    if x1+x2+x3 == 0 :
        print("Not a number – denominator equals zero")
    elif type(x1) == int or type(x2) == int or type(x3) == int:
        print("Error: parameters should be float")
    elif type(x1) != float or type(x2) != float or type(x3) != float:
        print("None")
    else:
       numerator = (x1+x2+x3)*(x2+x3)*x3
       answer = numerator/(x1+x2+x3)
       print(answer)
       
my_func(3.0,4.0,5.3)


#Q2
def revword(words:str): 
    words = words.lower()[::-1]
    return words
        
        
def countword():
    text = open("text.txt","r")
    count = 1
    for i in text:
        row_list = i.split(" ")
        if len(row_list) == 1:
            word = row_list[0].strip()
        else:
            for x in row_list :
                word1 = revword(x).strip()
                if word1 == word:
                    count += 1
    print(count)

countword()



