# Flask Baseline App

A minimal Flask application with basic routes and environment configuration. Designed for simple Flask-based APIs or web apps with scalable structure.

# Features

- Basic Flask app factory pattern
- Blueprint structure
- Environment variable support with `.env`
- Health and status check endpoints
- Easy to deploy and extend

## Project Structure

flask_baseline_app/
│
├── app/
│ ├── init.py # App factory
│ ├── routes.py # All app routes
│ └── config.py # Config using environment variables
│
├── venv/ # Virtual environment (should be in .gitignore)
├── .env # Environment variables (should be in .gitignore)
├── .gitignore
├── run.py # Entry point to start the app
├── requirements.txt
└── README.md

## Setup Instructions

### 1. Clone the repo

Bash-

git clone https://github.com/YOUR_USERNAME/flask_baseline_app.git
cd flask_baseline_app

2. Create a virtual environment
   
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows

4. Install dependencies

pip install -r requirements.txt

5. Set environment variables

Create a .env file:
ini
Copy
Edit
SECRET_KEY=your_secret_key_here -----critical for session management and CSRF protections

5. Run the app

python run.py

Routes:

Route	Method	Description
/	GET	Home route
/health	GET	Health check
/status	GET	App status
/about	GET	About this app

Up next:
-Formatting for AWS EC2
-Unit test

 License
MIT — free to modify and use for any purpose.
