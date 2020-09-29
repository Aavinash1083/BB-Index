from flask import *
import sqlite3

app = Flask(__name__)
DATABASE = 'BB.db'


# Handlers ==>

def calculate_loss(amount, duration, working_time):
    yourprofit = (working_time/duration)*100
    yourloss = 100 - (working_time/duration)*100
    amountloss = amount*(yourloss/100)
    return yourloss


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/add")
def add():
    return render_template("add.html")


@app.route("/savedetails", methods=["POST"])
def saveDetails():
    msg = "msg"
    name = request.form["name"]
    amount = int(request.form["amount"])
    duration = int(request.form["duration"])
    working_time = int(request.form["working_time"])
    loss = int(calculate_loss(amount, duration, working_time))
    with sqlite3.connect("BB.db") as con:
        try:
            cur = con.cursor()
            cur.execute("INSERT into BBINDEX_LOSS_PERCENT (name, amount, duration,working_time,loss_percent) values (?,?,?,?,?)",
                        (name, amount, duration, working_time, loss))
            con.commit()
            msg = "Name successfully Added"
        except:
            con.rollback()
            msg = "We can not add the name to the list"
        finally:
            return render_template("success.html", msg=msg)
            con.close()


@app.route("/view")
def view():
    con = sqlite3.connect(DATABASE)
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    cur.execute("select * from BBINDEX_LOSS_PERCENT")
    rows = cur.fetchall()
    return render_template("view.html", rows=rows)


@app.route("/delete")
def delete():
    return render_template("delete.html")


@app.route("/deleterecord", methods=["POST"])
def deleterecord():
    id = request.form["id"]
    print(id)
    with sqlite3.connect(DATABASE) as con:
        try:
            cur = con.cursor()
            cur.execute(
                'delete from BBINDEX_LOSS_PERCENT where name = "{}" '.format(id))
            msg = "Record successfully deleted"
        except:
            msg = "can't be deleted"
        finally:
            return render_template("delete_record.html", msg=msg)


if __name__ == "__main__":
    app.run(debug=True)
