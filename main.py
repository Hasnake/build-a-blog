from flask import Flask, request, redirect, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://build-a-blog:MyNewPass@localhost:8889/build-a-blog'
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)

class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120))
    body = db.Column(db.String(120))

def get_blogList():
    return Blog.query.all()

@app.route("/newpost", methods=["POST", "GET"])
def newpost_page():
    if request.method == "GET":
        return render_template('newpost.html')

    if request.method == "POST":
        # Save our post
        # TODO: Put save logic here

        # TODO: Redirect to create post page if there are errors
        # (Use query parameters)

        return redirect("/")


@app.route('/blog')
def blogPage():

    return render_template('blog.html',blogList=get_blogList())

@app.route("/")
def index():
    return redirect('/blog')


if __name__ == "__main__":
    app.run()





#@app.route("/register", methods=['GET', 'POST'])
#def register():
    #if request.method == 'POST':
        #email = request.form['email']
        #password = request.form['password']
        #verify = request.form['verify']
        #if not is_email(email):
            #flash('zoiks! "' + email + '" does not seem like an email address')
            #return redirect('/register')
        #email_db_count = User.query.filter_by(email=email).count()
        #if email_db_count > 0:
            #flash('yikes! "' + email + '" is already taken and password reminders are not implemented')
            #return redirect('/register')
        #if password != verify:
            #flash('passwords did not match')
            #return redirect('/register')
        #user = User(email=email, password=password)
        #db.session.add(user)
        #db.session.commit()
        #session['user'] = user.email
        #return redirect("/")
    #else:
        #return render_template('register.html')
