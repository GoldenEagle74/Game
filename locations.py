import text
import sys
import getpass
import titles
import game_map
import random
from time import sleep
from os import system
from sys import platform
if platform == 'linux': clr = 'clear'
if platform == 'win32': clr = 'cls'
CURSOR_UP_ONE = '\x1b[1A'
ERASE_LINE = '\x1b[2K'
partner = False
nun = False
keys = False
boy = False
localname = ''
inventory = {}
location = '0'


def output(text):
    for i in text:
        if i != "*":
            sleep(0.033)
            sys.stdout.write(i)
            sys.stdout.flush()
        else:
            getpass.getpass(prompt='')
            print(CURSOR_UP_ONE, end="")

def error():
    output('Неверный ввод, попробуйте еще раз*')
    print(ERASE_LINE, CURSOR_UP_ONE, ERASE_LINE, end='', sep='')

def choose_location(name='',part = '',inv = {}):
    global partner, inventory, location, localname
    if part != '': partner = part
    if name != '': localname = name
    if inv: inventory |= inv
    a = {
        '1': square,
        '2': playground,
        '3': dark_alley,
        '4': old_square,
    }
    system(clr)
    print('''Выберите действие:
[1] Перейти на главную площадь
[2] Перейти на детскую площадку
[3] Перейти на тёмный переулок
[4] Перейти на старую площадь

Просмотреть инвентарь (Ctrl+X)
Выйти из игры (ESC)''')
    choice = input()
    while choice not in ['1','2','3','4','\x18','\x1b']:
        error()
        choice = input()
    print(CURSOR_UP_ONE)
    if choice == '\x18': text.inv(inventory)
    elif choice == '\x1b': exit()
    else:
        game_map.char(location)
        for i in range(2): game_map.char(choice)
        location = choice
        a[choice]()
    system(clr)

def r_p_s():
    win = 0
    lose = 0
    a = {
        '1': 'Камень',
        '2': 'Ножницы',
        '3': 'Бумага'
    }
    system(clr)
    output('Начнём игру!*')
    while win < 3 and lose < 3:
        print('''Выберите действие:
[1] Камень
[2] Ножницы
[3] Бумага    
        ''')
        choice = input()
        while choice not in ['1','2','3']:
            error()
            choice = input()
        print(CURSOR_UP_ONE, f'Ваш выбор: {a[choice]}',sep='')
        for i in range(3):
            print(f'Ожидаем выбор противника: {3-i}')
            sleep(1)
            print(CURSOR_UP_ONE, ERASE_LINE, end='',sep='')
        enemy_choice=random.choice(['1','2','3'])
        print(f'Выбор противника: {a[enemy_choice]}')
        success = 'Вы выиграли*\n'
        failure = 'Вы проиграли*\n'
        if (choice == '1' and enemy_choice == '2') or (choice == '2' and enemy_choice == '3') or (choice == '3' and enemy_choice == '1'):
            win += 1
            output(success)
        elif choice == enemy_choice: output('Ничья*\n')
        else:
            lose += 1
            output(failure)
        output(f'''Побед: {win}
Поражений: {lose}*
''')
        system(clr)
    if lose == 3: return False
    if win == 3: return True

    
def square():
    titles.square()
    system(clr)
    d = {
        'text': '''Главная площадь. Главное место для проведения всех праздников в деревне.*
Она была украшена в кроваво-красных тонах. Столбы увешаны красно-чёрными гирляндами из бумаги.*
Дети изображали из себя вампиров и пугали других детей, которые являлись “Жертвами”.*

''',
    'Frod': f'''Фрод: "стоял буквально у сцены и ждал своего друга"*
Фрод: Ну где ты там, {localname}?!*
''',
    'text_2': f'''{localname}: "Всё-таки как-то протиснулся через толпу людей ближе к сцене и устремил свой взгляд на ведущего на сцене"*
Ведущий: Дамы и господа, прошу капельку внимания!*
Ведущий: Хочу вас всех поздравить с праздником нашего уголка - день Красной Аллеи!*
Ведущий: И начинает наш праздник - приглашенная звезда. Прошу ваших аплодисментов!*
Звезда: " уже на сцене появилась его фигура "*
Звезда: Добрый день, милые дамы и юноши! Я рад сегодня быть на вашем празднике!*
''',
    'choice_1': '''Выбор действий:
[1] Сразу залезть на сцену и накинуться на звезду
[2] Дождаться конца его выступления и поймать в гримёрке
''',
    'result_1': f'''
{localname}: {CURSOR_UP_ONE}Вот и ты!*
Не долго думая, парень залез на сцену под кучу недоумевающих взглядов.*
Уже через пару секунд детектив был над звездой сегодняшнего вечера и впечатал его в деревяшки пола сцены.*
{localname}: Живо! Я знаю что ты виновен в пропаже людей! Отвечай куда ты их увел!*
Однако пока тот пытался выпытать из звезды хоть какие-то слова, охрана взяла под руки детектива и выперла со сцены уже к разъяренной толпе*
После этого жители деревни выгоняют детектива из деревни за испорченный праздник.*
''',
    'result_2': f'''{CURSOR_UP_ONE}Когда уже звезда закончила своё выступление и спокойно ушёл со сцены, детектив незаметно проследовал за ним к гримёрке.*
Благодаря ключу от продавщицы вы спокойно зашли в гримёрку*
{localname}: Извини что без стука!
Звезда: " уставился уже на детектива и хотел вызвать охрану, как детектив закрыл дверь "*
{localname}: Не приятно познакомиться! Я - детектив! И ты подозреваемый в деле по продаже людей в этой деревне!*
Звезда: Ты чего это себе позволяешь...*
" Светловолосый уже не на шутку начинал злиться "*
{localname}: А то. Что на тебе много что сходится и ты главный подозреваемый!*
Звезда: Да ты! Ничего такого!*
Звезда: Да как ты смеешь вообще?!*
" Звезда не долго думая обнажил свои клыки и накинулся на детектива "*
''',
    'choice_2(no_p)': '''Выбор действий:
[1] Открыть быстро дверь  
''',
    'choice_2': '''Выбор действий:
[1] Открыть быстро дверь
[2] Позвать помощника (если имеется)    
''',
    'result_2_1': f'''{CURSOR_UP_ONE}Быстро среагировав, детектив открывает дверь, из-за чего звезда вылетает в целую толпу своих фанатов.*
Люди быстро заметили кто в них влетел и испугались, ибо перед ними буквально был их любимец, но он был вампиром!*
Вампирёныш же быстро утолил свою жажду убить детектива и просто принял участь быть выгнанным из города.*
Жители продолжили праздновать свой праздник, а Фрод вместе с детективом уже отмечали победу в доме детектива.*

''',
    'result_2_2': f'''{localname}: {CURSOR_UP_ONE}ФРОООООД!*
Будто услышав “команду”, друг быстро выломал замок и уже встал перед своим детективом.*
Фрод: Отошёл от моего друга!*
Звезда уже накинулась на Фрода, широко открыв рот и желая укусить того.*
Однако, железная труба, которую так преподнес Фрод, помешала ему это сделать.*
Быстрым рывком, вампир вылетел из гримёрки, как пробка из шампанского.*
Люди быстро заметили кто в них влетел и испугались, ибо перед ними буквально был их любимец, но он был вампиром!*
Вампирёныш же быстро утолил свою жажду убить детектива и просто принял участь быть выгнанным из города.*
Жители продолжили праздновать свой праздник, а Фрод вместе с детективом уже отмечали победу в доме детектива*

'''
    }
    if nun == False or keys == False or boy == False:
        output('Тут нечего делать*')
        system(clr)
        choose_location()
    else:
        output(d['text'])
        if partner: output(d['Frod'])
        output(d['text_2'])
        output(d['choice_1'])
        choice = input()
        while choice not in ['1','2']:
            error()
            choice = input()
        if choice == '1':
            output(d['result_1'])
            output('Открыта плохая концовка! <З*')
            return 0
        if choice == '2':
            output(d['result_2'])
            if partner: output(d['choice_2'])
            else: output(d['choice_2(no_p)'])
            choice = input()
            while choice not in ['1','2']:
                error()
                choice = input()
            if choice == '1':
                output(d['result_2_1'])
                output('Открыта хорошая концовка! <З*')
            if choice == '2':
                output(d['result_2_2'])
                output('Открыта обалденная концовка! :D*')

def playground():
    global boy
    titles.playground()
    system(clr)
    d = {
        'text': f'''{localname}: «Замечает ребёнка на детской площадке и подходит к нему»*
{localname}: Привет, я здешний детектив, веду расследование. Можешь мне помочь и ответить на пару вопросов?*
Ребёнок: Хорошо, я помогу. Но только если выиграешь меня в камень-ножницы-бумага!*
{localname}: Отлично, давай сыграем!*
''',
        'win': f'''Ребёнок: Воу! А вы выиграли, дядя детектив! Хорошо! Помогу чем смогу!*
{localname}: Чудно! Скажи, ты встречал в деревне светловолосого парня?*
Ребёнок: Да! Я часто вижу его гуляющим по ночам, также я знаю что он будет завтра выступать на главной площади!*
{localname}: Чудесно! Спасибо тебе большое!*
''',
        'lose': f'''Ребёнок: Видно не судьба, дядя детектив!*
{localname}: Блиин... Как я мог проиграть ребёнку...*
Ребёнок: Я держу своё обещание, но скажу лишь одно - тот светловолосый парень очень подозрительный*
Ребёное: Увидимся на главной площади на концерте, дядя детектив!*
'''
    }
    if nun == False or keys == False:
        output('Тут нечего делать*')
        system(clr)
        choose_location()
    else:
       output(d['text'])
       if r_p_s(): output(d['win'])
       else: output(d['lose'])
       boy = True
       system(clr)
       choose_location()


def dark_alley():
    global keys, inventory
    titles.dark_alley()
    system(clr)
    d = {
        'text': f'''Вдалеке виднеется магазин*
{localname}: "совершенно случайно заметил в круглой тьме яркий огонёк, тлеющей сигареты"*
{localname}: Ага! Ещё один свидетель!*
Продавщица: Чертила, я не буду так просто тебе давать показания. Ты вылез из ниоткуда и уже стал детективом.*
''',
    'choice_1': '''Выберите действие:
[1] Отправить своего помощника с ней поговорить
[2] Пойти самому
''',

    'choice_2': '''Выберите действие:
[1] Пойти самому
''',
    'result_1': '''Фрод: Ты мне конечно друг, но твоё исследование дорого стоит - целая пачка сигарет!*
Фрод: Грабёж! Но всё-таки! Я нашёл кое-что стоящее!!!*
''',
    'choice_2_1': '''Выберите действие:
[1] Предложить что-то взамен на информацию
''',
    'result_2_1':f'''{localname}: Ну… Могу свою лупу дать взамен на вашу информацию!*
{localname}: Конечно бесполезный обмен, ибо я даже не знаю что у вас, но в какой-то мере он логичный!* 
"Детектив улыбнулся во все 32 зуба, дабы показать свои добрые намерения (плохо выходит)"* 
Продавщица: " скептически уже осмотрела лупу, а потом детектива " Ладно, ты не глупый.*
Продавщица: Держи ключи, они остались от того светловолосого парня*
''',
    'success': '''Вы получили ключи с брелком*
''',
    'success_2': '''Вы получили ключи с брелком но потеряли лупу*
'''
    }
    if nun == False:
        output('Тут нечего делать*')
        system(clr)
        choose_location()

    else:
        output(d['text'])
        if partner: output(d['choice_1'])
        else: output(d['choice_2'])
        choice = input()
        while choice not in ['1','2']:
            error()
            choice = input()
        print(CURSOR_UP_ONE, end="")
        if partner and choice == '1':
            output(d['result_1'])
            output(d['success'])
            inventory |= {'Ключи с брелком': 'На брелке надпись "гримёрка"'}
            keys = True
            choose_location()
        elif partner and choice == '2' or choice == '1':
            output(d['choice_2_1'])
            choice = input()
            while choice != '1':
                error()
                choice = input()
            print(CURSOR_UP_ONE, end="")
            if choice == '1':
                output(d['result_2_1'])
                output(d['success_2'])
                del inventory['Лупа']
                inventory |= {'Ключи с брелком': 'На брелке надпись "гримёрка"'}
                keys = True
                choose_location()
    
def old_square():
    global nun
    titles.old_square()
    system(clr)
    d = {
    'text':  f'''Вы встретили монашку*
{localname}: Хэээй!*
Монашка: АААА ЗАБИРАЙ ЧТО УГОДНО, НО МЕНЯ НЕ ТРОГАЙ*
Тут от монашки и след простыл*
''',

    'choice_1': '''Выберите действие:
[1] Отправить своего помощника с ней поговорить
[2] Пойти самому
''',

    'choice_2': '''Выберите действие:
[1] Пойти самому
''',

    'result_1': '''Фрод: Короче. Я с ней всё обсудил. Ну ты её и напугал до чёртиков! Всё выдала! Ну слушай.*
Фрод: В деревню приплёлся ещё какой-то светловолосый парень, как она упомянула - певец на нашем концерте тут.*
''',

    'choice_2_1': '''Выберите действие:
[1] Надавить на неё
[2] Спокойно всё обсудить
''',

    'result_2_1_1': f'''{localname}: Слушай, если ты сейчас же не выдашь мне информацию о чём либо, я тебя лично сдам в руки тому вору, чтобы из тебя сделали куклу!*
Монашка: "Дрожит как кленовый лист и смотрит куда угодно, но никак не на детектива. Потом вовсе убегает от вас, не издав и звука"*
''',

    'result_2_1_2': f'''{localname}: Я не причиню тебе вреда и не сделаю плохо. Просто расскажи что ты знаешь. Это очень нам поможет в деле.*
Монашка: "всё-таки посмотрела на детектива"*
Монашка: Ну после вас сюда приехал ещё один человек…*
Монашка: Он со светлыми волосами, с таким же готическим стилем и он вроде певец у нас на концерте…*
''',
    'success': 'Вы получили необходимую информацию*',
    'failure': 'Вы не смогли получить необходимую информацию*'
}
    output(d['text'])
    if partner: output(d['choice_1'])
    else: output(d['choice_2'])
    choice = input()
    while choice not in ['1','2']:
        error()
        choice = input()
    print(CURSOR_UP_ONE, end="")
    if partner and choice == '1':
        output(d['result_1'])
        output(d['success'])
        nun = True
        choose_location()
    elif partner and choice == '2' or choice == '1':
        output(d['choice_2_1'])
        choice = input()
        while choice not in ['1','2']:
            error()
            choice = input()
        print(CURSOR_UP_ONE, end="")
        if choice == '1':
            output(d['result_2_1_1'])
            output(d['failure'])
            choose_location()
        if choice == '2':
            output(d['result_2_1_2'])
            output(d['success'])
            nun = True
            choose_location()