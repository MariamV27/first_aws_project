from flask import Flask, render_template, request, redirect, url_for
import pymysql

app = Flask(__name__)

# Database connection configuration
DB_CONFIG = {
    'host': 'localhost',
    'user': 'root',
    'password': 'klsflskdjflsdkjglskjdiusdhgn86767',
    'db': 'data_base_01',
    'port': 3306,
    'charset': 'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor
}

def get_db_connection():
    return pymysql.connect(**DB_CONFIG)

@app.route('/')
def index():
    with get_db_connection() as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM aws_first_proyect")
            users = cursor.fetchall()
    return render_template('index.html', users=users)

@app.route('/add_user', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        nationality = request.form['nationality']
        
        with get_db_connection() as connection:
            with connection.cursor() as cursor:
                sql = "INSERT INTO aws_first_proyect (name, age, nationality) VALUES (%s, %s, %s)"
                cursor.execute(sql, (name, age, nationality))
            connection.commit()
        
        return redirect(url_for('index'))
    return render_template('add_user.html')

if __name__ == '__main__':
    app.run(debug=False)