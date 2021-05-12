import sqlite3
import Hangman_readone

#The delete functino deletes an item
def delete():
    item = ""
    quantity = ""
    item, quantity = Hangman_readone.getWord()
    if item == "-1":
        print("Word not found")
    else:
        sure = input('Are you sure you want to delete this item? (y/n)')
        if sure.lower() == 'y':
            num_deleted = delete_row(item)
            print(f'{num_deleted} row(s) deleted')

#The delete_row function deletes an existing item
#The number of rows deleted is returned
def delete_row(item):
    conn = None
    num_deleted = 0
    try:
        conn = sqlite3.connect('inventory.db')
        cur = conn.cursor()
        cur.execute('''DELETE FROM food WHERE item == ?''', (item,))
        conn.commit()
        num_deleted = cur.rowcount
    except sqlite3.Error as err:
        print('Database Error', err)
    finally:
        if conn != None:
            conn.close()
    return num_deleted

#Execute the main function
if __name__ == '__main__':
    delete()


