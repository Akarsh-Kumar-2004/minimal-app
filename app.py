from flask import Flask, render_template
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
    



@app.route("/")
def hello_world():
    site=Site(title="todo site", desc="this is a todo site")
    db.session.add(site)
    db.session.commit()
    all_sites=Site.query.all()
    print(all_sites)
    return render_template("index.html",all_sites=all_sites)
    #return "<p>Hello, World!</p>"


@app.route("/show")
def products():
    all_sites = Site.query.all()
    print(all_sites)
    return 'this is products page'
if __name__ == "__main__":
    app.run(debug=True)