# Number of worker processes
workers = 2

# Number of worker threads per process
threads = 4

# Listen on all network interfaces on port 8000
bind = '0.0.0.0:8000'

# Specify the Python module that contains your Flask application
# Replace 'backend' with the name of your Python module
# Replace 'app' with the name of your Flask application object
# For example, if your Flask app is defined in 'backend.py' and the
# app object is named 'app', then use 'backend:app'
app = 'backend:app'
