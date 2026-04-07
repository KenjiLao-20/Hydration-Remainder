# Water Intake Calculator

A Flask web app that calculates daily water intake needs based on body weight and activity level, with hourly hydration reminders.

---

## How It Works

1. Enter your weight in pounds
2. Select your activity level
3. Get your daily water requirement
4. Receive hourly reminders to drink water for 12 hours

---

## Formula Used

Base Water = Weight (lbs) x 0.5 oz

Additional Water by Activity:
- None: +0 oz
- Low: +12 oz
- Moderate: +24 oz
- High: +36 oz

Total Daily Water = Base Water + Additional Water
Water Per Hour = Total Daily Water / 12 hours

---

## Example

Weight: 150 lbs
Activity: Moderate

Base Water = 150 x 0.5 = 75 oz
Total = 75 + 24 = 99 oz per day
Water per hour = 99 / 12 = 8.25 oz

---

## Installation

pip install flask
python app.py

---

## Project Structure

water-calculator/
├── app.py
├── templates/
│   └── index.html
└── README.md

---

## Routes

/ (GET) - Shows calculator form
/ (POST) - Calculates water intake

---

## Built With

- Flask (Python)
- HTML/CSS
- JavaScript (for notifications)

---

## License

MIT
