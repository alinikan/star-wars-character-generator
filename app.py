from flask import Flask, render_template, request
import main  # Assuming the file is in the same directory

app = Flask(__name__, static_folder='static')


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # If the request method is POST, it means the user has submitted the form.
        # Fetches the name input from the form.
        name = request.form.get('name')

        # Loads data from the JSON file and builds a Star Wars character using the user's input name.
        # Passes the character to the template.
        character = main.build_character(main.load_data('sw_database.json'), name)
        return render_template('index.html', character=character)

    # If the request method is GET, it means the user is accessing the page for the first time.
    # Returns the template without a character.
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
