from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Sample project data
projects = [
    {"name": "Dwarfdash", "description": "Game Jam project."},
    {"name": "Quick Dive", "description": "Hackathon project."},
    {"name": "Dave's Nightmare", "description": "Game Jam project."}
]

# Serve the main page
@app.route('/')
def index():
    return render_template("index.html")

# API route to get projects
@app.route('/api/projects', methods=['GET'])
def get_projects():
    return jsonify(projects)

#API route to get about me page
@app.route('/about')
def about():
    return render_template('about.html')


# API route to handle contact form submissions
@app.route('/contact', methods=['POST'])
def contact():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')
    # Here, you could save the contact message to a database or send an email
    print(f"Received message from {name} ({email}): {message}")
    return jsonify({"message": "Thank you for your message! I'll get back to you soon."})

if __name__ == '__main__':
    app.run(debug=True)
