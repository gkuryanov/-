import random

print('Это игра - виселица')
print('Вы знаете правила?')
while True:
    answer = str(input())
    otvet = answer.lower()
    if otvet == 'да':
        print('Тогда начинаем игру')
        break
    elif otvet == "ок":
        print('Тогда начинаем игру')
        break
    elif otvet == "yes":
        print('Тогда начинаем игру')
        break
    elif otvet == "конечно":
        print('Тогда начинаем игру')
        break
    elif otvet == "sui":
        print('Тогда начинаем игру')
        break
    elif otvet == "no":
        print(' Игроку загадывается слово, которое он должен угадать, используя буквы алфавита и возможность совершить ограниченное количество ошибок.Всего доступно 10 ошибок.')
        break
    elif otvet == "nah":
        print(' Игроку загадывается слово, которое он должен угадать, используя буквы алфавита и возможность совершить ограниченное количество ошибок.Всего доступно 10 ошибок.')
        break
    elif otvet == "nope":
        print(' Игроку загадывается слово, которое он должен угадать, используя буквы алфавита и возможность совершить ограниченное количество ошибок.Всего доступно 10 ошибок.')
        break
    elif otvet == "net":
        print(' Игроку загадывается слово, которое он должен угадать, используя буквы алфавита и возможность совершить ограниченное количество ошибок.Всего доступно 10 ошибок.')
        break
    elif otvet == "не":
        print(' Игроку загадывается слово, которое он должен угадать, используя буквы алфавита и возможность совершить ограниченное количество ошибок.Всего доступно 10 ошибок.')
        break
    elif otvet == "нет":
        print(' Игроку загадывается слово, которое он должен угадать, используя буквы алфавита и возможность совершить ограниченное количество ошибок.Всего доступно 10 ошибок.')
        break
    
    else:
        print('Вы ввели что-то неправильно, попробуйте снова!')
    

words = ['собака', 'жираф', 'змея', 'барсук', 'кот', 'рысь', 'тигр', 'лев', 'медведь', 'лань', 'олень', 'лось', 'зебра','мышь','свинья','корова',
         'кит', 'акула', 'обезьяна','альбинос', 'бегемот', 'як' , 'цапля', 'лама' , 'попугай', 'страус' , 'бобер', 'ягуар' , 'панда' , 'утка' , 
         'утконос', 'аист' , 'петух' , 'курица']
word = random.choice(words)

print('все слова связаны с животными!')
hp = 10
len_word = len(word)
print('длина слова :' , len_word)
used_letter = ""
true_word = []
for i in range(len(word)):
    true_word += "_"

while len_word != 0 and hp != 0:
    game = False
    while True:
        letter1 = input("введите букву: ")
        letter = letter1.lower()
        if letter in used_letter or len(letter) > 1:
            print("Эта буква была уже использована или вы использовали больше одного символа, попробуйте ещё раз!")
        else:
            break
    count = 0
    for i in word:
        if letter in i:
            len_word -= 1
            game = True
            true_word[count] = letter
        count += 1

    if not game:
        hp -= 1
        print("Неверно")
    else:
        print("Верно")
        print(true_word)

    print("HP = ", hp)

if len_word == 0:
    print("Победа! Слово: ", word)
else:
    print("Вас повесили :-( ")
