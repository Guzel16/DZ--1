# определитель душевной боли
a = float(input('Оцените силу вашей душевной боли по шкале от 0 до 10: '))

if a <= 1.5:
    print('Легкая встревоженность, будто вы уронили ключи перед заходом домой')
elif 1.5 < a <= 2.7:
    print('Кажется, вы испытываете легкое огорчение. Как человек в короткой поездке в метро, забывший дома наушники')
elif 2.7 < a <= 4.2:
    print('Вы встревожены - почти как человек, которому придется звонить по телефону, и это в эпоху мессенджеров! То самое чувство, когда начинаете нервно репетировать в голове диалог...')
elif 4.2 < a <= 6.5:
    print('У вас серьезное огорчение, как у человека, который только что потерял свой кошелек в общественном месте')
elif 6.5 < a <= 9:
    print('Вы испытываете глубокую боль, как будто вас только что бросили в середине дождливой ночи без зонта')
elif 9 < a <= 10:
    print('Это катастрофа! Ваша душевная боль настолько сильна, что сравнить её можно разве что с тем, что чувствует человек, у которого только что разбилось сердце.')
else:
    print('Ужас! Такая боль, будто все люди мира разбивают вам сердце каждую секунду...')