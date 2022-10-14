from flask import Flask
import random

app = Flask(__name__)


@app.route("/")
def main():
    return "<h1>Guess a number between 0 to 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"


def random_num():
    return random.randint(1, 10)

rand_num = random_num()

@app.route("/<int:num>")
def check_response(num):
    if num < rand_num:
        return "<h2>Too low, try again!</h2>" \
               "<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    elif num > rand_num:
        return "<h2>Too high, try again!</h2>" \
               "<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"
    else:
        return "<h2>You found me!</h2>" \
               "<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"



if __name__ == "__main__":
    app.run()
