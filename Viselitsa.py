import random

print('Это игра - виселица')
print('Вы знаете правила?')
while True:
    answer = str(input())
    if answer == ('да' or 'Да' or 'Yes' or 'yes'):
        print('Тогда начинаем игру')
        break
    elif answer == ('нет' or 'Нет' or 'no' or 'No'):
        print(' Игроку загадывается слово, которое он должен угадать, используя буквы алфавита и возможность совершить ограниченное количество ошибок.Всего доступно 10 ошибок.')
        break
    else:
        print('Вы ввели что-то неправильно, попробуйте снова!')
    

words = ['собака', 'жираф', 'змея', 'барсук', 'кот', 'рысь', 'тигр', 'лев', 'медведь', 'лань', 'олень', 'лось', 'зебра','мышь','свинья','корова',
         'кит', 'акула', 'обезьяна','альбинос', 'бегемот', 'як' , 'цапля', 'лама' , 'попугай', 'страус' , 'бобер', 'ягуар' , 'панда' , 'утка' , 
         'утконос', 'аист' , 'петух' , 'курица']
word = random.choice(words)


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
        letter = input("введите букву: ")
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