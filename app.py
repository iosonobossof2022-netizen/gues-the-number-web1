from flask import Flask, render_template, request, session, redirect
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

@app.route("/", methods=["GET", "POST"])
def index():
    if 'random_num' not in session:
        session['random_num'] = random.randint(1, 100)
        session['lives'] = 10
        session['turns'] = 0

    feedback = ""

    if request.method == "POST":
        user_input = request.form.get("guess", "").strip().lower()

        if user_input == "stop":
            feedback = f"You stopped the game. The number was {session['random_num']}."
            reset_game()

        elif not user_input.isdigit():
            feedback = "Invalid input. Please enter a number or type 'stop'."

        else:
            user_num = int(user_input)

            if user_num < 1 or user_num > 100:
                feedback = "The number must be between 1 and 100."
            else:
                session['turns'] += 1

                if user_num == session['random_num']:
                    session['won'] = True
                    return redirect("/win")
                elif user_num > session['random_num']:
                    feedback = "📈 Too high!"
                    session['lives'] -= 1
                else:
                    feedback = "📉 Too low!"
                    session['lives'] -= 1

                if session['lives'] == 0:
                    session['lost'] = True
                    return redirect("/game-over")

    return render_template("index.html", feedback=feedback, lives=session['lives'], turns=session['turns'])

@app.route("/win")
def win():
    if not session.get('won'):
        return redirect("/")
    session.pop('won', None)
    turns = session.get('turns', 0)
    number = session.get('random_num', '?')
    lives = session.get('lives', 0)
    return render_template("win.html", turns=turns, number=number, lives=lives)

@app.route("/game-over")
def game_over():
    if not session.get('lost'):
        return redirect("/")
    session.pop('lost', None)
    number = session.get('random_num', '?')
    turns = session.get('turns', 0)
    lives = session.get('lives', 0)
    return render_template("game_over.html", number=number, turns=turns, lives=lives)

@app.route("/retry")
def retry():
    session['random_num'] = random.randint(1, 100)
    session['lives'] = 10
    session.pop('won', None)
    session.pop('lost', None)
    return redirect("/")

@app.route("/reset")
def reset():
    reset_game()
    return redirect("/")

def reset_game():
    session['random_num'] = random.randint(1, 100)
    session['lives'] = 10
    session['turns'] = 0
    session.pop('won', None)
    session.pop('lost', None)

@app.route("/buy-lives", methods=["GET", "POST"])
def buy_lives():
    if request.method == "POST":
        session['lives'] = session.get('lives', 0) + 3
        return redirect("/")
    return render_template("buy_lives.html")

if __name__ == "__main__":
    app.run(debug=True)