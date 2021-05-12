import sqlite3

# The read function reads an existing item
def getWord():
    name = input('Enter word to search for: ')
    item, quantity = read_item(name)
    if item == "":
        item = "-1"
    else:
        print(f'Item: {item:<20} Quantity: {quantity:<3}')
    return item, quantity

# The display_item function displays all items
# with a matching ItemName
def read_item(name):
    item = ""
    quantity = ""
    conn = None
    results = []
    try:
        conn = sqlite3.connect('inventory.db')
        cur = conn.cursor()
        cur.execute('''SELECT * FROM food WHERE lower(item) == ?''', (name.lower(),))
        results = cur.fetchall()
        print(results)
        for row in results:
            item = row[0]
            quantity = row[1]
    except sqlite3.Error as err:
        print('Database Error', err)
    finally:
        if conn != None:
            conn.close()

    #Return the number of matching rows.
    return item, quantity

if __name__ == '__main__':
    getWord()