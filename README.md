# Star Wars Character Generator

Welcome to the Star Wars Character Generator! This project allows users to generate a unique Star Wars character by selecting random attributes such as species, home planet, starship, and weapon. 

## Table of Contents
- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Character Generator in the Terminal](#Running-the-Character-Generator-in-the-Terminal)
- [Usage](#usage)

## Getting Started
These instructions will guide you to run the Star Wars Character Generator on your local machine for development and testing purposes.

### Prerequisites
This project is built with Python 3. You will need Python 3 installed on your local system. You can download Python [here](https://www.python.org/downloads/).

In addition, you will need the following Python packages:
- Flask
- Requests

You can install these packages using pip (or pip3):
```bash
pip install flask requests
```
or
```bash
pip3 install flask requests
```

### Installation
1. Clone this repository:
    ```bash
    git clone git@github.com:alinikan/star-wars-character-generator.git
    ```
2. Navigate to the project directory:
    ```bash
    cd star-wars-character-generator
    ```
3. Run the API scrape script to gather Star Wars data:
    ```bash
    python3 api_scrape.py
    ```
4. Run the Flask application:
    ```bash
    python3 app.py
    ```
5. Open a web browser and visit `http://127.0.0.1:5000`.

### Running the Character Generator in the Terminal
If you prefer to run the character generator directly in the terminal without the Flask application, you can simply run:
```bash
python3 main.py
```
This script will ask for your input, and generates a new Star Wars character for you based on the data scraped from the SWAPI.

## Usage

The Star Wars Character Generator is a simple Flask web application. When you run the application, it will start a local web server and you can interact with the application through your web browser.

### Web Interface
1. Open your web browser and navigate to `http://127.0.0.1:5000`.
2. You will see a text box asking for a name for your character.
3. Enter a name and click the `Generate` button.
4. Your character's information will be generated and displayed on the screen.

### Command Line Interface
If you run `main.py` from the command line, you will be able to interact with the Star Wars Character Generator in a text-based format.
1. Run the script using `python3 main.py`.
2. The program will prompt you to enter a name for your character.
3. Enter a name.
4. The program will generate a character and display the information in the terminal.
5. You can continue to generate characters by entering new names, or type 'quit' to exit the program.

