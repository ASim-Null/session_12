import requests
import json


def display_availability(records):
    # Print the names of the columns.
    print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} ".format(
        'NAME', '12-13', '13-14', '14-15', '15-16', '16-17', '17-18'))
    print('-' * 105)

    # print each data item.
    for item in records:
        print("{:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} ".format(
            item['name'], item['12-13'], item['13-14'], item['14-15'], item['15-16'], item['16-17'], item['17-18']
        ))


def run():
    print('############################')
    print('Hello, welcome to our salon')
    print('############################')
    print()
    date = input('What date you would like to book your appointment for (YYYY-MM-DD): ')
    print()
    print('####### AVAILABILITY #######')


    print()
    print('See you soon!')


if __name__ == '__main__':
    run()
