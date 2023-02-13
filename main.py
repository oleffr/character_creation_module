from random import randint

from graphic_arts.start_game_banner import run_screensaver


def attack(char_name: str, char_class: str) -> str:
    """Характеризует атаку."""
    if char_class == 'warrior':
        points = randint(3, 5)
        return (f'{char_name} нанёс урон противнику равный {5 + points}')
    if char_class == 'mage':
        points = randint(5, 10)
        return (f'{char_name} нанёс урон противнику равный {5 + points}')
    if char_class == 'healer':
        points = randint(-3, -1)
        return (f'{char_name} нанёс урон противнику равный {5 + points}')
    return (f'{char_name} не нанёс урон противнику')


def defence(char_name: str, char_class: str) -> str:
    """Характеризует урон."""
    if char_class == 'warrior':
        return (f'{char_name} блокировал {10 + randint(5, 10)} урона')
    if char_class == 'mage':
        return (f'{char_name} блокировал {10 + randint(-2, 2)} урона')
    if char_class == 'healer':
        return (f'{char_name} блокировал {10 + randint(2, 5)} урона')
    return (f'{char_name} не блокировал урон')


def special(char_name: str, char_class: str) -> str:
    """Характеризует специальные умения."""
    if char_class == 'warrior':
        return (f'{char_name} применил специальное умение «Выносливость 105»')
    if char_class == 'mage':
        return (f'{char_name} применил специальное умение «Атака 45»')
    if char_class == 'healer':
        return (f'{char_name} применил специальное умение «Защита 40»')
    return (f'{char_name} не применил специальное умение')


def start_training(char_name: str, char_class: str) -> str:
    """Характеризует тренировку."""
    if char_class == 'warrior':
        print(f'{char_name}, ты Воитель — отличный боец ближнего боя.')
    if char_class == 'mage':
        print(f'{char_name}, ты Маг — превосходный укротитель стихий.')
    if char_class == 'healer':
        print(f'{char_name}, ты Лекарь — чародей, способный исцелять раны.')
    print('Потренируйся управлять своими навыками.')
    command1 = 'attack — чтобы атаковать противника,'
    command2 = 'defence — чтобы блокировать атаку противника'
    command3 = 'или special — чтобы использовать свою суперсилу.'
    print('Введи одну из команд: ', command1, command2, command3)
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd: str = ''
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        if cmd == 'defence':
            print(defence(char_name, char_class))
        if cmd == 'special':
            print(special(char_name, char_class))
    return 'Тренировка окончена.'


def choice_char_class() -> str:
    """Характеризует выбор класса персонажа."""
    approve_choice: str = ''
    char_class: str = ''
    while approve_choice != 'y':
        message1 = 'Введи название персонажа, за которого хочешь играть: '
        message2 = 'Воитель — warrior, Маг — mage, Лекарь — healer:'
        print(message1, message2)
        char_class = input()
        if char_class == 'warrior':
            warrior_message1 = 'Воитель — дерзкий воин ближнего боя.'
            warrior_message2 = 'Сильный, выносливый и отважный.'
            print(warrior_message1, warrior_message2)
        if char_class == 'mage':
            mage_message1 = 'Маг — находчивый воин дальнего боя.'
            mage_message2 = 'Обладает высоким интеллектом.'
            print(mage_message1, mage_message2)
        if char_class == 'healer':
            healer_message1 = 'Лекарь — могущественный заклинатель.'
            healer_message2 = 'Черпает силы из природы, веры и духов.'
            print(healer_message1, healer_message2)
        approve_m = 'Нажми (Y), чтобы подтвердить выбор,'
        approve_m += 'или любую другую кнопку, чтобы выбрать другого персонажа'
        approve_choice = input(approve_m).lower()
    return char_class


if __name__ == '__main__':
    run_screensaver()
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name: str = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class: str = choice_char_class()
    print(start_training(char_name, char_class))
