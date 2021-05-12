import sqlite3
import Hangman_readone

# The update function updates an exiting item's data
def update():
    item = ""
    quantity = ""
    item, quantity = Hangman_readone.getWord()
    if item == "-1":
        print("Word not found")
    else:
        # Get the new values for item name and price
        quantity = input('Quantity: ')

        # Update the row
        num_updated = update_row(item, quantity)
        print(f'{num_updated} row(s) updated')

#The update row function updates an existing row with a new
#ItemName and Price. The number of rows updated is returned
def update_row(item, quantity):
    conn = None
    num_updated = 0
    try:
        conn = sqlite3.connect('inventory.db')
        cur = conn.cursor()
        cur.execute('''UPDATE food
        SET quantity = ? WHERE lower(item) == ?''',
                    ( quantity, item.lower()))
        conn.commit()
        num_updated = cur.rowcount
    except sqlite3.Error as err:
        print('Database Error', err)
    finally:
        if conn != None:
            conn.close()
    return num_updated

#Execute the main function
if __name__ == '__main__':
    update()
