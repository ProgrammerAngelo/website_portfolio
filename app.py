from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/works')
def works():
    return render_template('works.html')

@app.route('/link_list')
def link_list():
    return render_template('link_list.html')

@app.route('/stack')
def stack():
    return render_template('stack.html')

@app.route('/queue')
def queue():
    return render_template('queue.html')

if __name__ == "__main__":
    app.run(debug=True)