from flask import Flask, render_template, request, session, redirect
import random

app = Flask(__name__)
app.secret_key = 'myapppythonhtmlcss'

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
            session['turns'] += 1

            if user_num < 1 or user_num > 100:
                feedback = "The number must be between 1 and 100. Game over."
                reset_game()
            elif user_num == session['random_num']:
                feedback = f"Correct! You guessed it in {session['turns']} turns."
                reset_game()
            elif user_num > session['random_num']:
                feedback = "Too high!"
                session['lives'] -= 1
            else:
                feedback = "Too low!"
                session['lives'] -= 1

            if session['lives'] == 0:
                feedback += f" No lives left. You lost! The number was {session['random_num']}."
                reset_game()

    return render_template("index.html", feedback=feedback, lives=session.get('lives', 3), turns=session.get('turns', 0))

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