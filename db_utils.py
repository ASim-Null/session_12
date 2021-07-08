import mysql.connector
from config import USER, PASSWORD, HOST


class DbConnectionError(Exception):
    pass


def _connect_to_db(db_name):
    cnx = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=db_name
    )
    return cnx


def _map_values(schedule):
    mapped = []
    for item in schedule:
        mapped.append({
            'name': item[0],
            '12-13': 'Not Available' if item[1] else 'Available',
            '13-14': 'Not Available' if item[2] else 'Available',
            '14-15': 'Not Available' if item[3] else 'Available',
            '15-16': 'Not Available' if item[4] else 'Available',
            '16-17': 'Not Available' if item[5] else 'Available',
            '17-18': 'Not Available' if item[6] else 'Available',
        })
    return mapped


# EXAMPLE 1
def get_all_booking_availability(_date):
    pass


if __name__ == '__main__':
    get_all_booking_availability('2020-12-15')
