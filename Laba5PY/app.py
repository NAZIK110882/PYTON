from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# Налаштування бази даних SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Модель таблиці для бази даних
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)

# Створення бази даних перед першим запитом
with app.app_context():
    db.create_all()

# --- МАРШРУТИ ---

# Головна сторінка (Форма + Список)
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        if task_content:
            new_task = Task(content=task_content)
            try:
                db.session.add(new_task)
                db.session.commit()
                return redirect(url_for('index'))
            except:
                return 'Помилка при додаванні завдання'
            
    # GET-запит: відображення завдань
    tasks = Task.query.all()
    welcome = "Вітаю у Flask-додатку!"
    return render_template('index.html', tasks=tasks, welcome_text=welcome)

# Сторінка "Про автора"
@app.route('/about')
def about():
    return render_template('about.html', author="Якимчук Назарій")

# Сторінка з параметром у URL
@app.route('/hello/<name>')
def hello(name):
    return render_template('hello.html', user_name=name)

# Видалення завдання (Додаткова фіча)
@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Task.query.get_or_404(id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect(url_for('index'))
    except:
        return 'Виникла помилка при видаленні'

# Обробка помилки 404 (сторінка не знайдена)
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(debug=True)