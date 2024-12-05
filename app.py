from flask import Flask, render_template
from link_list import LinkedList

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
    # Creating a linked list and performing operations
    sushi_preparation = LinkedList()
    sushi_preparation.insert_at_beginning("prepare to assemble")
    sushi_preparation.insert_at_beginning("wash rice")
    sushi_preparation.insert_at_beginning("cut fish")
    sushi_preparation.insert_at_end("roll sushi")
    sushi_preparation.insert_at_end("eat sushi")

    # Get the current state of the linked list
    linked_list_content = sushi_preparation.printLinkedList()

    return render_template('link_list.html', linked_list_content=linked_list_content)

@app.route('/stack')
def stack():
    return render_template('stack.html')

@app.route('/queue')
def queue():
    return render_template('queue.html')

if __name__ == "__main__":
    app.run(debug=True)