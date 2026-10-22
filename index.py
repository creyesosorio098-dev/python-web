from flask import Flask, render_template

app = Flask(__name__)
PRODUCTOS = [
    {"id": 1, "nombre": "Urea", "categoria": "nitrogenado", "formula": "46-00-00", "precio": 450,  "imagen": "img/Foto urea.jpeg"},
    {"id": 2, "nombre": "Sulfato de amonio", "categoria": "nitrogenado", "formula": "21-00-00", "precio": 380, "imagen": "img/urea.jpeg"},
    {"id": 3, "nombre": "Triple 17", "categoria": "completo", "formula": "17-17-17", "precio": 520,  "imagen": "img/urea.jpeg"},
    {"id": 4, "nombre": "Composta orgánica", "categoria": "organico", "formula": "Orgánico", "precio": 250,  "imagen": "img/urea.jpeg"},
]

@app.route('/')
def home():
    return render_template('home.html', productos=PRODUCTOS)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)