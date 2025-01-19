from flask import Flask, render_template,  request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

users = [
    {"email": "zhengpou@gmail.com", "password": "cjinthehood", "username": "muhammad.ashar"},
    {"email": "abbax.momi@gmail.com", "password": "Cjinthehood316716", "username": "muhammad.abbas"}
]

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         email_or_username = request.form.get('email')
#         password = request.form.get('password')

#         # Check email or username
#         for user in users:
#             if user["email"] == email_or_username or user["username"] == email_or_username:
#                 if user["password"] == password:
#                     flash(f"Welcome back {user['username']}!", "success")
#                     return redirect(('home'))
#                 else:
#                     flash("Incorrect password!", "danger")
                    
#         flash("No account found with those credentials!", "danger")
#     return render_template('login.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email_or_username = request.form.get('email')
        password = request.form.get('password')

        # Check email or username
        for user in users:
            if user["email"] == email_or_username or user["username"] == email_or_username:
                if user["password"] == password:
                    flash(f"Welcome back {user['username']}!", "success")
                    return redirect(url_for('home'))
                else:
                    flash("Incorrect password!", "danger")
                    return redirect(url_for('login'))
                    
        flash("No account found with those credentials!", "danger")
    return render_template('login.html')




@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')

        # Add new user to the database
        users.append({"email": email, "password": password, "username": username})
        flash("Registration successful! You can now log in.", "success")
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
