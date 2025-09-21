import time
from flask import Flask, render_template, request, redirect, url_for, flash
from sqlalchemy import text
from models.db import db, User, Product

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "supersecret"  # Needed for flash messages
db.init_app(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/product_page', methods=['GET', 'POST'])
def product_page():
    if request.method == 'POST':
        username = request.form['login']
        password = request.form['password']

        query = f"SELECT * FROM user WHERE username = '{username}' AND password_hash = '{password}'"
        result = db.session.execute(text(query)).fetchall()

        if result:
            return redirect(url_for('admin_page'))
        else:
            return "Login failed. Try again."

    products = Product.query.all()
    return render_template('product_page.html', products=products)

@app.route('/admin_page')
def admin_page():
    products = Product.query.all()
    users = User.query.all()
    return render_template('admin_page.html', products=products, users=users)

@app.route('/level2', methods=['POST'])
def level2():
    product_id_input = request.form['product_id']

    if "DELETE" in product_id_input.upper():
        try:
            prod_id = int(product_id_input.split()[0])
            product = Product.query.get(prod_id)
            if product:
                db.session.delete(product)
                db.session.commit()
                flash(f"Product '{product.name}' deleted using SQL injection.")
            else:
                flash("Product not found.")
        except:
            flash("Malformed input.")

    elif "UPDATE" in product_id_input.upper():
        try:
            parts = product_id_input.split()
            prod_id = int(parts[0])
            new_price = float(parts[2])
            product = Product.query.get(prod_id)
            if product:
                product.price = new_price
                db.session.commit()
                flash(f"Product '{product.name}' price updated to ₹{new_price}!")
            else:
                flash("Product not found.")
        except:
            flash("Malformed input.")

    elif "OR" in product_id_input.upper() or "1=1" in product_id_input:
        Product.query.delete()
        db.session.commit()
        flash("All products deleted! You exploited the SQL injection vulnerability.")

    else:
        flash("No effect. Try using: '2 DELETE' or '1 UPDATE 9.99' or '1 OR 1=1'.")

    return redirect(url_for('admin_page'))

@app.route('/level2_user', methods=['POST'])
def level2_user():
    user_input = request.form['user_input']

    if "DELETE" in user_input.upper():
        try:
            user_id = int(user_input.split()[0])
            user = User.query.get(user_id)
            if user:
                db.session.delete(user)
                db.session.commit()
                flash(f"User '{user.username}' deleted using SQL injection.")
            else:
                flash("User not found.")
        except:
            flash("Malformed input.")

    elif "UPDATE" in user_input.upper():
        try:
            parts = user_input.split()
            user_id = int(parts[0])
            new_status = parts[2].lower() == 'true'
            user = User.query.get(user_id)
            if user:
                user.is_admin = new_status
                db.session.commit()
                flash(f"User '{user.username}' admin status updated to {new_status}.")
            else:
                flash("User not found.")
        except:
            flash("Malformed input.")

    elif "OR" in user_input.upper() or "1=1" in user_input:
        User.query.delete()
        db.session.commit()
        flash("All users deleted! You exploited the SQL injection vulnerability.")

    else:
        flash("No effect. Try using: '2 DELETE' or '1 UPDATE True' or '1 OR 1=1'.")

    return redirect(url_for('admin_page'))

@app.route('/level3', methods=['GET', 'POST'])
def level3():
    result = None
    response_time = None

    if request.method == 'POST':
        user_guess = request.form['user_guess']
        start_time = time.time()

        try:
            matching_users = User.query.filter(User.username.like(f"{user_guess}%")).all()
            if matching_users:
                time.sleep(5)
                result = "True condition – something exists!"
            else:
                result = "False condition – nothing found."
        except Exception as e:
            result = f"Error in query simulation: {str(e)}"

        response_time = time.time() - start_time

        if response_time > 3:
            result += " (This took longer to respond, try to analyze the time!)"

    return render_template('level3.html', result=result, response_time=response_time)

if __name__ == "__main__":
    app.run(debug=True)
