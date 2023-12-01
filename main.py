import random
import logging

logging.basicConfig( filename = 'log.log', level = logging.INFO )

while True:

    try:
        n = int( input( "😉 Введите натуральное число: " ) )
        assert n > 0
        logging.info( 'correct number input, n = {}'.format( n ) )
        break

    except AssertionError:
        print( '❗  Вы ввели число которое не является натуральным!' )
        logging.exception( "num isn't natural" )

    except ValueError:
        print( '❗  Неправильно!' )
        logging.exception( 'wrong num input' )

num_list = [ i for i in range( 1, n + 1 ) ]
random.shuffle( num_list )

print( '🤝 Нажимайте на ENTER и вы увидите числа 🥰', end='' )

for element in num_list:
    a = input()
    print( element, end='' )