from flask import Flask, render_template, request
import main  # Assuming the file is in the same directory

app = Flask(__name__, static_folder='static')


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        character = main.build_character(main.load_data('sw_database.json'), name)
        return render_template('index.html', character=character)
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
