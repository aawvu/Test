from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'practiceproject1'

posts = [
    {
        'author':'Naveen',
        'title' : 'life',
        'date_posted' : 'jan 7 2024',
        'content' : 'first post'
    },
    {
        'author':'Kavin',
        'title' : 'Survive',
        'date_posted' : 'jan 8 2024',
        'content' : 'second post'
    },
]

@app.route("/")
@app.route("/home")
def home():
    return render_template ("home.html", posts=posts)

@app.route("/about")
def about():
    return render_template ("about.html", title="About")

@app.route("/register")
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template ("register.html", title="Register", form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template ("login.html", title="login", form=form)

if __name__ == "__main__":
    app.run(debug=True)