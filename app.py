from flask import Flask, render_template, request, redirect
import Hangman_create, Hangman_read, Hangman_update, Hangman_readone, Hangman_delete

app = Flask(__name__)
wordinfo = []


@app.route("/")
def homePage():
    return render_template("index.html")


@app.route("/hangman")
def playGame():
    allwords = []
    alllevels = []
    allhints = []
    results = []

    wordinfo = ""
    results = Hangman_read.read_all_items()

    for row in results:
        print(f'Hidden Word: {row[0]}, Level: {row[1]}, Hint: {row[2]}')
        allwords.append(row[0])
        alllevels.append(row[1])
        allhints.append(row[2])



    return render_template("hangman.html", allwords=allwords, alllevels=alllevels, allhints=allhints)


@app.route("/add", methods=['POST', 'GET'], )
def add():
    errormsg = ""
    wordinfo = ""
    if request.method == 'POST':
        word = request.form['word'].upper()
        if not word:
            errormsg = "Enter a Word"
        else:
            errormsg = ""
            if len(word) > 10:
                level = "H"
            elif len(word) > 5:
                level = "M"
            else:
                level = "E"
            hint = request.form['hint']
            success_code = Hangman_create.insert_row(word, level, hint)
            if success_code == 0:
                errormsg = "Data added successfully"
                wordinfo.append(f"(word) | (level) | (hint)")
            else:
                errormsg = "Database error =- Word already exists"
    return render_template("add.html", wordinfo=wordinfo, errormsg=errormsg)


@app.route("/read/<string:flag>")
def read(flag):
    print(flag)
    wordinfo = ""
    search = ""
    if flag == "all":
        search = "SELECT * FROM  words ORDER BY hiddenword"
    elif flag == "E":
        search = "SELECT * FROM  words WHERE level = 'E' ORDER BY hiddenword"
    elif flag == "M":
        search = "SELECT * FROM  words WHERE level = 'M' ORDER BY hiddenword"
    elif flag == "H":
        search = "SELECT * FROM  words WHERE level = 'H' ORDER BY hiddenword"

    wordinfo = Hangman_read.read_data(search)
    return render_template("read.html", wordinfo=wordinfo)


@app.route("/update", methods=['POST', 'GET'])
def update():
    if request.method == 'POST':
        word = ""
        level = ""
        hint = ""
        if request.form['btn_id'] == 'Search':
            word = request.form['word'].lower()
            if not word:
                errormsg = "You must enter a word"
            else:
                errormsg = ""
                word, level, hint = Hangman_readone.read_item(word)
                print(word)
                if not word:
                    errormsg = "Database error == Word not found"
                else:
                    errormsg = ""
            return render_template("update.html", word=word, level=level, hint=hint,errormsg=errormsg)
        elif request.form['btn_id'] == 'Update':
            print("processing update")
            word = request.form['hiddenword'].lower()
            if not word:
                errormsg = "You must enter a word"
                return render_template("update_html",errormsg=errormsg)
            else:
                errormsg = ""
                hint = request.form['hint']
                print(hint)
                level = request.form['level'].upper()
                print('level')
                if level != "H" and level != "M" and level != 'E':
                    errormsg = "Enter E, M or H for level"
                else:
                    errormsg = ""
                    print(level, hint)
                    num_updated = Hangman_update.update_row(word, level, hint)
                    print(num_updated)
                    if num_updated == 0:
                        errormsg = "Database error"
                    else:
                        errormsg = "Record updated"
            return render_template("update.html", word=word, level=level, hint=hint,errormsg=errormsg)
    else:
        return render_template("update.html")


@app.route("/delete/<string:word>", methods=['POST', 'GET'])
def delete(word):
    Hangman_delete.delete_row(word)
    return redirect('/read_delete')


@app.route("/read_delete")
def read_delete():
    search = "SELECT * FROM  words ORDER BY hiddenword"
    wordinfo = ""
    wordinfo = Hangman_read.read_data(search)
    return render_template("delete.html", wordinfo=wordinfo)
