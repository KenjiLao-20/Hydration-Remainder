from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None
    water_per_hour = None  # Variable to hold water per hour
    if request.method == "POST":
        try:
            weight = float(request.form["weight"])
            if weight <= 0:
                error = "Invalid Input! Only Numbers 1 and Above!"
            else:
                activity_level = request.form["activityLevel"]
                base_required_water = weight * 0.5  # 0.5 oz per pound

                # Calculate additional water intake based on activity level
                if activity_level == "none":
                    required_water = base_required_water
                elif activity_level == "low":
                    required_water = base_required_water + 12  # 12 oz for low activity
                elif activity_level == "moderate":
                    required_water = base_required_water + 24  # 24 oz for moderate activity
                elif activity_level == "high":
                    required_water = base_required_water + 36  # 36 oz for high activity
                else:
                    error = "Please select a valid activity level."
                    required_water = None

                if required_water is not None:
                    water_per_hour = required_water / 12  # Calculate water per hour
                    result = f"Required Water Intake: <strong>{required_water:.2f} oz</strong> (8 oz = 1 Glass of Water)<br>A Notification Will Pop Up Every Hour Reminding you to Drink Water For The Next 12 Hours"
                    # Prepare the message for the popup
                    notification_message = f"Drink {water_per_hour:.2f} oz of Water! Stay Hydrated! (8 oz = 1 Glass of Water)"
                    return render_template("index.html", result=result, error=error, notification_message=notification_message)
        except ValueError:
            error = "Please enter a valid input."

    return render_template("index.html", result=result, error=error)

if __name__ == "__main__":
    app.run(debug=True)