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

