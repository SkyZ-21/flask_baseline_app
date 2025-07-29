# Flask Baseline App

A minimal Flask application with simplicity and scalabitily in mind. Best suited for APIs or small we apps with room to grow into production-level services.

# Features

- Basic Flask app factory pattern  -----for enviroment aware instatiation
- Blueprint structure  -----to keep routes modual and organized 
- Environment variable support with `.env` via 'python-dotenv'
- integrated 'Health' and 'status' check endpoints
- Easy to deploy, to extend, or dockerize

## Project Structure

flask_baseline_app/
│
├── app/
│ ├── init.py # App factory
│ ├── routes.py # All app routes
│ └── config.py # Config using environment variables
│
├── venv/ # Virtual environment (should be in .gitignore)
├── .env # Secret keys and enviroment config (not commited)
├── .gitignore
├── run.py # app entry point
├── requirements.txt
└── README.md

## Setup Instructions:

### 1. Clone the repo

Bash-

git clone https://github.com/YOUR_USERNAME/flask_baseline_app.git
cd flask_baseline_app

2. Create and activate virtual environment
   
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

Availiable Routes():Route, Method, Desc

(/)	     GET   Home route;
(/health)  GET  Health check;
(/status)  GET	 App status;
(/about)	 GET About this app;

Future intentions:
Add units via pytest
EC2 deoloyment config w/ Nginx + Gunicorn
add Docker support

License:
MIT — free to modify and use for any purpose.
