FILENAME = 'freq.txt'

def get_words():
    word_list=[]
    with open(FILENAME, encoding='utf8') as text:
        for line in text:
            parts=line.split('|')
            words=parts[0]
            for word in words:
                word_list.append(word)
    return word_list


def task_01(wordlist):
    for word in wordlist:
        if len(word)>=2:
            if word[:1]==word[-2:]:
                print(word)
            else:
                continue
        else:
            continue
    #длина слова строго больше 2 символов
    #2 первые буквы слова равны двум последним буквам слова
    #'''Решение для первого задания, которое просто что-то печатает и ничего не возвращает'''
    #pass


#def task_02(words, defenitions, imp):
    
    
    #Программа должна распечатать через запятую все существительные женского рода единственного числа, ipm которых строго больше 100.
    #'''Решение для второго задания, которое просто что-то печатает и ничего не возвращает'''
    #pass


def task_03():
    i=1
    wordlist_=[]
    while i==1:
        a=input('input word: ')
        if a !='':
            wordlist_.append(a)
        else:
            i-=1
            with open(FILENAME, encoding='utf8') as text:
                for word_ in wordlist_:
                    if word

    #само слово
    #морфологическую информацию о слове
    #ipm слова
    #'''Решение для третьего задания, которое просто что-то печатает и ничего не возвращает'''
    #pass


_name_=input('input command: ')
if _name_=='__main__':
    get_words()
    wordlist=get_words()
    print(wordlist)

