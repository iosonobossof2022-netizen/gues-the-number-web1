from flask import Flask, render_template, request, session, redirect
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

@app.route("/", methods=["GET", "POST"])
def index():
    if 'random_num' not in session:
        session['random_num'] = random.randint(1, 100)
        session['lives'] = 3
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
                    return redirect("/win")
                elif user_num > session['random_num']:
                    feedback = "📈 Too high!"
                    session['lives'] -= 1
                else:
                    feedback = "📉 Too low!"
                    session['lives'] -= 1

                if session['lives'] == 0:
                    return redirect("/game-over")

    return render_template("index.html", feedback=feedback, lives=session['lives'], turns=session['turns'])

@app.route("/win")
def win():
    turns = session.get('turns', 0)
    number = session.get('random_num', '?')
    return render_template("win.html", turns=turns, number=number)

@app.route("/game-over")
def game_over():
    number = session.get('random_num', '?')
    turns = session.get('turns', 0)
    return render_template("game_over.html", number=number, turns=turns)

@app.route("/reset")
def reset():
    reset_game()
    return redirect("/")

def reset_game():
    session['random_num'] = random.randint(1, 100)
    session['lives'] = 3
    session['turns'] = 0

if __name__ == "__main__":
    app.run(debug=True)