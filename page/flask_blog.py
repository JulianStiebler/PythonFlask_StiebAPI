from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'author': 'Max Mustermann',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'Yesterday'
    },
    {
        'author': 'Max Mustermann',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'Today'
    }
]

@app.route("/") # -> MAIN ROUTE
def routes_main():
    return render_template('pages/home.html', posts=posts)

@app.route("/legal/tos") # -> MAIN ROUTE
def routes_legal_tos():
    return render_template('pages/legal/tos.html')

@app.route("/legal/privacy") # -> MAIN ROUTE
def routes_legal_privacy():
    return render_template('pages/legal/privacy.html')

@app.route("/legal/impressum") # -> MAIN ROUTE
def routes_legal_impressum():
    return render_template('pages/legal/impressum.html')

@app.route("/legal/cookies") # -> MAIN ROUTE
def routes_legal_cookies():
    return render_template('pages/legal/cookies.html')


if __name__ == "__main__":
    app.run(debug=True)

