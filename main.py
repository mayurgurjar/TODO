from flask import Flask ,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"
db = SQLAlchemy(app)

class todo(db.Model):
    Sno = db.Column(db.Integer , primary_key = True)
    title = db.Column(db.String(200) , nullable = False)
    description = db.Column(db.String(200) , nullable = False)
    date = db.Column(db.DateTime , default = datetime.utcnow)
    
    # def __repr__(self):
    #     return f"{self.Sno}-{self.title}"

@app.route("/" , methods = ["GET" , "POST"])
def hello():
    if request.method=="POST":
        title = request.form['formGroupExampleInput']
        description = request.form["formGroupExampleInput2"]
        tt = todo(title = title , description = description)
        db.session.add(tt)
        db.session.commit()
    all = todo.query.all()
    return render_template("index.html" , tdo = all)

@app.route("/delete/<int:Sno>")
def delete(Sno):
    al = todo.query.filter_by(Sno=Sno).first()
    db.session.delete(al)
    db.session.commit()
    return redirect("/")
    


if __name__ == '__main__':
    app.run(debug = True)
    