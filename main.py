from tqdm import tqdm



def most_propable(word_lista):
    word = ''
    word_count = 0
    for i in tqdm(word_lista):
        count_question = calculate_word_cut(i,word_lista)
        if count_question > word_count:
            word_count = count_question
            word = "".join(i)
    return str(word) +" " + str(word_count)
                 
        
def word_list_cuter(query, word_lista):             #0 - no info  
    querry_lista = []
    iteri = 0
    while iteri < len(query):
        if query[iteri] == "0":
            querry_lista.append("0" + query[iteri + 1])
            iteri += 2
        else:
            querry_lista.append(query[iteri])
            iteri += 1
    print(querry_lista)
    query = querry_lista

    for i in range(len(query)):                     #lower case letter (abcdefghaijk....)   -   letter is in word
        if "0" in query[i]:                                  #upper case letter (ABCDEFG...)     - letter in word on position  
            for j in range(len(word_lista)-1,-1,-1):
                if query[i][1] in word_lista[j]:
                    word_lista.pop(j)
            continue
        if query[i].islower():
            for j in range(len(word_lista)-1,-1,-1):
                if query[i] not in word_lista[j]:
                    word_lista.pop(j)
        else:
            for j in range(len(word_lista)-1,-1,-1):
                if query[i].lower() != word_lista[j][i]:
                    word_lista.pop(j)
    return word_lista
        
                     
        
def calculate_word_cut(word,word_list):
    working_w_list = word_list.copy()
    for i in range(len(word)):
        for j in range(len(word_list)):
            try:    
                if word[i] == word_list[j][i]:
                    working_w_list.remove(word_list[j])
            except:    
                pass
    return len(word_list) - len(working_w_list)
    
def data_prepare(path,sep):
    with open(path,"r") as f:
        output = []
        for i in f.read().split("\n"):
            output.append(",".join(list(i.lower()))) 

    with open(path,"w") as f:    
        for line in output:
            f.write(line + "\n") 

            


def data_parse(path, sep):
    output_list = []
    with open(path,"r") as f: 
       for i in  f.read().split("\n"):
           output_list.append(i.split(sep))
    return output_list



def main_loop():
    print(r"""
          ⣀⣤⣤⣴⣤⣤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣰⣾⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⡿⠋⠉⠉⠛⠛⠛⠋⠉⠙⢿⡆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣼⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣧⠀⠀⠀⠀⠀⠀
⡰⠉⠉⠁⠉⡙⠹⢠⢾⣛⠛⢶⢀⡶⠛⣛⠳⡄⡏⢋⠉⠉⠉⠉⢢
⢹⠶⠶⠶⣾⠡⣾⠈⠸⡿⠷⠀⠀⠀⢾⣿⠇⠁⡶⡌⢷⠶⠶⠶⡏
⢸⠀⠀⠀⠆⠀⢻⡀⠀⠀⡀⠀⠀⠀⢀⢀⡀⠀⡟⠀⠸⡀⠀⠀⡇
⢸⠀⠀⢸⠀⠀⠈⡇⣠⠒⠓⠤⣀⠤⠘⠀⡘⢰⠃⠀⠀⡇⠀⠀⡇
⢸⠀⠀⡎⠀⠀⠀⢻⠀⠙⣶⣶⣒⣶⣶⠋⢀⡏⠀⠀⠀⢸⠀⠀⡇
⢸⠀⠀⡇⠀⠀⠀⠘⣧⡀⠈⠿⣿⡿⠁⢀⢮⠃⠀⠀⠀⢸⠀⠀⡇
⢸⠀⠀⡇⠀⠀⠀⠀⢰⠑⠄⣀⠀⢀⡠⠊⡌⠀⠀⠀⠀⢸⠀⠀⡇
⢸⠀⠀⠘⢄⠀⠀⠀⠀⠆⠀⠀⠀⠀⠀⠰⠀⠀⠀⠀⡠⠃⠀⠀⡇
⠈⠦⣀⣔⠂⠋⠒⠲⠶⠾⠤⠤⠤⠤⠤⠷⠶⠖⠒⠉⠒⢢⣀⠴⠃
⠀⠀⠀⠅⠉⠉⠉⠉⠉⠒⠒⠒⠒⠒⠒⠊⠉⠉⠉⠉⠉⠨⡀⠀⠀
⠀⠀⠀⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠁⠀⠀
⠀⠀⠀⠳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡜⠀⠀⠀
⠀⠀⠀⠀⠱⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠎⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠢⢄⣀⡀⢀⠀⡀⢀⠀⣀⣀⡠⠔⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⡌⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠸⠤⠠⠀⢀⣀⣀⣀⠀⠀⠤⠤⠖⠀
          """)
    print("type path to word_list")
    path = input()
    wl = data_parse(path,",")
    print("best_word: "+ "sores")
    print("""type your question:
              0a0b0c0d.... - letter not known

              abcdefg... - letter in word
              ABCDEFG... - letter in word on given position              
              """)
    while True:
        print("""type your question:              
              """)
        question = input()
        wl = word_list_cuter(question,wl)
        print("best_word: "+ most_propable(wl))
   

if __name__ == '__main__':
    #data_prepare("words.csv","'") 
    # for i in data_parse("words.csv",","):
    #     print(i) 
        
    # print(calculate_word_cut(['z', 'o', 'w', 'i', 'e'],data_parse("words.csv",",")))
    # print(most_propable(data_parse("words.csv",",")))
    #print(word_list_cuter("A0a0a0a0a",data_parse("words.csv",",")))
    main_loop()

