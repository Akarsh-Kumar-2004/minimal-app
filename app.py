from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db=SQLAlchemy(app)

class Site(db.Model):
    sno=db.Column(db.Integer, primary_key=True)
    desc=db.Column(db.String(200), nullable=False)
    title=db.Column(db.String(200), nullable=False)
    date_created=db.Column(db.DateTime, default=datetime.utcnow)
    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"
    

@app.route("/",methods=["GET","POST"])
def hello_world():
    if request.method=="POST":
        title= request.form['title']
        desc= request.form['desc']
        site=Site(title=title, desc=desc)
        db.session.add(site)
        db.session.commit()
    all_sites=Site.query.all()
    print(all_sites)
    return render_template("index.html",all_sites=all_sites)



@app.route("/show")
def products():
    all_sites = Site.query.all()
    print(all_sites)
    return 'this is products page'


@app.route("/update")
def update():
    all_sites = Site.query.all()
    print(all_sites)
    return 'this is products page'

@app.route("/delete/<int:sno>")
def delete(sno):
    all_sites = Site.query.filter_by(sno=sno).first()
    db.session.delete(all_sites)
    db.session.commit()
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)