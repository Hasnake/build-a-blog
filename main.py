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

    def __init__ (self, name, body):
        self.name = name
        self.body = body


def get_blogList():
    return Blog.query.all()

@app.route("/newpost", methods=["POST", "GET"])
def newpost_page():
    if request.method == "GET":
        return render_template('newpost.html')

    if request.method == "POST":
        # Save our post
        # TODO: Put save logic here
        blog_title = request.form['blog_Title']
        blog_content = request.form['blog_NewEntry']

        error_title=""
        error_content=""

        if len(blog_title) >= 120 or len(blog_title)==0:
            error_title = "Limit message under 120 characthers"
            blog_title="" #displays empty title instead of the the error content
        if len(blog_content) >=1000 or len(blog_content)==0:
            error_content = "Limit message under 1000 characthers"
            blog_content=""
        if len(error_title)>0 or len(error_content)>0:
            posts = Blog.query.all()
            return render_template(
                'newpost.html',page_name="Build A Blog!", posts=posts,
                title="Blog title", content="Blog content", error_title=error_title,
                error_content=error_content)

        newpost = Blog(blog_title, blog_content)
        db.session.add(newpost)
        db.session.commit()
        return redirect("/")


@app.route('/blog')
def blogPage():

    return render_template('blog.html',blogList=get_blogList())

@app.route("/")
def index():
    return redirect('/blog')


if __name__ == "__main__":
    app.run()
