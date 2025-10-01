from flask import Flask, render_template, request
import random

app = Flask(__name__)
random_num = random.randint(1, 100)
lives = 3
turns = 0

@app.route("/", methods=["GET", "POST"])
def index():
    global random_num, lives, turns
    feedback = ""

    if request.method == "POST":
        user_input = request.form.get("gok").strip().lower()

        if user_input == "stop":
            feedback = f"You stopped the game. The number was {random_num}."
            random_num = random.randint(1, 100)
            lives = 3
            turns = 0
        elif not user_input.isdigit():
            feedback = "Invalid input. Please enter a number or type 'stop'."
        else:
            user_num = int(user_input)
            turns += 1

            if user_num < 1 or user_num > 100:
                feedback = "The number must be between 1 and 100. Game over."
                random_num = random.randint(1, 100)
                lives = 3
                turns = 0
            elif user_num == random_num:
                feedback = f"Congratulations! You guessed the number in {turns} turns."
                random_num = random.randint(1, 100)
                lives = 3
                turns = 0
            elif user_num > random_num:
                feedback = "Too high!"
                lives -= 1
            else:
                feedback = "Too low!"
                lives -= 1

            if lives == 0:
                feedback += f" No lives left. You lost! The number was {random_num}."
                random_num = random.randint(1, 100)
                lives = 3
                turns = 0

    return render_template("index.html", feedback=feedback, lives=lives, turns=turns)

if __name__ == "__main__":
    app.run(debug=True)
