from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Welcome to My Flask App</h1>
    <p>This is the home page.</p>
    <a href="/about">Go to About Page</a>
    """

@app.route('/about')
def about():
    return """
    <h1>About Us</h1>
    <p>This page is built using Flask.</p>
    <a href="/">Back to Home</a>
    """

if __name__ == '__main__':
    app.run(debug=True)
