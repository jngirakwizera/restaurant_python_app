from flask import Flask, render_template, request, redirect
import Restaurant_create, Restaurant_read, Restaurant_update, Restaurant_readone, Restaurant_delete

app = Flask(__name__)
wordinfo = []


@app.route("/")
def homePage():
    search = "SELECT * FROM  orders ORDER BY item"
    wordinfo = ""
    wordinfo = Restaurant_read.read_data(search)
    return render_template("index.html", wordinfo=wordinfo)


@app.route("/hangman")
def playGame():
    allwords = []
    alllevels = []
    allhints = []
    results = []

    wordinfo = ""
    results = Restaurant_read.read_all_items()

    for row in results:
        print(f'Hidden Word: {row[0]}, Level: {row[1]}, Hint: {row[2]}')
        allwords.append(row[0])
        alllevels.append(row[1])
        allhints.append(row[2])



    return render_template("hangman.html", allwords=allwords, alllevels=alllevels, allhints=allhints)


@app.route("/add", methods=['POST', 'GET'])
def add():
    errormsg = ""
    wordinfo = ""
    if request.method == 'POST':
        food = request.form['food'].upper()
        if not food:
            errormsg = "Enter a food"
        else:
            errormsg = ""

            quantity = request.form['quantity']
            print("food is" + food)
            print("quanity is" + quantity)
            success_code = Restaurant_create.insert_row(food, quantity)
            print(success_code)
            if success_code == 0:
                errormsg = "Data added successfully"
                wordinfo.append(f"(food) | (quantity)")
                print("word info is " + wordinfo)
            else:
                errormsg = "Database error =- Food already exists"
    return render_template("add.html", wordinfo=wordinfo, errormsg=errormsg)


@app.route("/read/<string:flag>")
def read(flag):
    print(flag)
    wordinfo = ""
    search = "SELECT * FROM  food ORDER BY item"


    wordinfo = Restaurant_read.read_data(search)
    return render_template("read.html", wordinfo=wordinfo)

@app.route("/order", methods=['POST', 'GET'])
def order():
    search = "SELECT * FROM  food ORDER BY item"
    wordinfo = ""
    wordinfo = Restaurant_read.read_data(search)
    if request.method == 'POST':
        food = ""
        quantity = ""
        if request.form['btn_id'] == 'Order':
            print("processing update")


            food = request.form['food'].lower()
            currentQuantity = 0
            found = False

            for row in wordinfo:
                item = row[0]
                quantity = row[1]
                if food == item.lower():
                    print("found food")
                    currentQuantity = quantity
                    found = True


            if not found:
                errormsg = "You must enter a correct food"
                return render_template("orderFood.html",errormsg=errormsg)
            else:
                errormsg = ""
                quantity = request.form['quantity']
                print(quantity)

                name = request.form['name']
                print(name)



                if name == "" and quantity == ""  and name == "":
                    errormsg = "Enter food, name and quantity"
                else:
                    errormsg = ""
                    quantityInt = int(currentQuantity) - int(quantity)
                    quantityDecremented = str(quantityInt)
                    num_updated = Restaurant_update.update_row(food, quantityDecremented)
                    Restaurant_create.insert_order_row(food, quantity, name)
                    print(num_updated)
                    if num_updated == 0:
                        errormsg = "Database error"
                    else:
                        errormsg = "Order placed successfully"
            return render_template("orderFood.html", wordinfo=wordinfo, errormsg=errormsg)
    else:
        return render_template("orderFood.html", wordinfo=wordinfo)

@app.route("/update", methods=['POST', 'GET'])
def update():
    if request.method == 'POST':
        food = ""
        quantity = ""
        if request.form['btn_id'] == 'Search':
            food = request.form['food'].lower()
            if not food:
                errormsg = "You must enter a food"
            else:
                errormsg = ""
                food, quantity = Restaurant_readone.read_item(food)
                print(food)
                if not food:
                    errormsg = "Database error == Word not found"
                else:
                    errormsg = ""
            return render_template("update.html", food=food, quantity=quantity,errormsg=errormsg)
        elif request.form['btn_id'] == 'Update':
            print("processing update")
            food = request.form['food'].lower()
            if not food:
                errormsg = "You must enter a food"
                return render_template("update_html",errormsg=errormsg)
            else:
                errormsg = ""
                quantity = request.form['quantity']
                print(quantity)
                print(food)

                print(len(quantity))
                print(len(food))

                if len(food) == 0 and len(quantity) == 0:
                    errormsg = "Enter food and quantity"
                else:
                    errormsg = ""
                    print(food, quantity)
                    num_updated = Restaurant_update.update_row(food, quantity)
                    print(num_updated)
                    if num_updated == 0:
                        errormsg = "Database error"
                    else:
                        errormsg = "Record updated"
            return render_template("update.html", food=food, quantity=quantity,errormsg=errormsg)
    else:
        return render_template("update.html")


@app.route("/delete/<string:word>", methods=['POST', 'GET'])
def delete(word):
    Restaurant_delete.delete_row(word)
    return redirect('/read_delete')




@app.route("/read_delete")
def read_delete():
    search = "SELECT * FROM  food ORDER BY item"
    wordinfo = ""
    wordinfo = Restaurant_read.read_data(search)
    return render_template("delete.html", wordinfo=wordinfo)
