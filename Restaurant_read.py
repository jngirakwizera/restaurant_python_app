import sqlite3




def read_data(searchString):
    print(searchString)
    conn = None
    results = []
    try:
        conn = sqlite3.connect('inventory.db')
        cur = conn.cursor()
        cur.execute(searchString)
        results = cur.fetchall()
        print(results)
    except sqlite3.Error as err:
        print('Database Error', err)
    finally:
        if conn != None:
            conn.close()
    return results


# The display_item function displays all items

def read_items():
    item = ""
    quantity = ""
    conn = None
    results = []
    try:
        conn = sqlite3.connect('inventory.db')
        cur = conn.cursor()
        cur.execute('''SELECT * FROM food ORDER BY item''')
        results = cur.fetchall()
        # print(results)
        # print(f'Hidden Word     Level     Hint')
        for row in results:
            item = row[0]
            quantity = row[1]
            # print(f'Item: {hiddenword}, Level: {level}, Hint: {hint}')
    except sqlite3.Error as err:
        print('Database Error', err)
    finally:
        if conn != None:
            conn.close()

    # Return the number of matching rows.
    return item, quantity
    # return results


def read_all_items():
    item = ""
    quantity = ""
    conn = None
    results = []
    try:
        conn = sqlite3.connect('inventory.db')
        cur = conn.cursor()
        cur.execute('''SELECT * FROM food ORDER BY itme''')
        results = cur.fetchall()
        # print(results)
        # print(f'Hidden Word     Level     Hint')
        for row in results:
            item = row[0]
            quantity = row[1]
            # print(f'Hidden Word: {hiddenword}, Level: {level}, Hint: {hint}')
    except sqlite3.Error as err:
        print('Database Error', err)
    finally:
        if conn != None:
            conn.close()

    # Return the number of matching rows.
    return results

if __name__ == '__main__':
    read_items()
