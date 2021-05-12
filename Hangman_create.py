import sqlite3
import RestaurantConstants


def create():
    print('Create New Restaurant Item')
    item = input('Item Name: ')

    quantity = input('Quantity:')
    insert_row(item, quantity)


# The insert_row function inserts a row into the Inventory table.
def insert_row(item, quantity):
    conn = None
    try:
        conn = sqlite3.connect(f'{RestaurantConstants.DATABASE_NAME}.db')
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS food ( item TEXT PRIMARY KEY NOT NULL, quantity TEXT NOT NULL )''')
        cur.execute('''INSERT INTO words (item, quantity) VALUES (?,?,?)''', (item, quantity))
        conn.commit()
    except sqlite3.Error as err:
        print('Database Error', err)
    finally:
        if conn is not None:
            conn.close()

    # Execute the main function.


if __name__ == '__main__':
    create()
