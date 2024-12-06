from flask import Flask, render_template, request, jsonify
from link_list import LinkedList

app = Flask(__name__)

# Initialize a global linked list instance
linked_list = LinkedList()

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
    linked_list_content = linked_list.printLinkedList()
    return render_template('link_list.html', linked_list_content=linked_list_content)
# Linked list API routes
@app.route('/insert_at_beginning', methods=['POST'])
def insert_at_beginning():
    data = request.json.get('data', '').strip()
    if not data:
        return jsonify({'message': 'Invalid input!'}), 400
    linked_list.insert_at_beginning(data)
    return jsonify({'message': f"Inserted '{data}' at the beginning."})

@app.route('/insert_at_end', methods=['POST'])
def insert_at_end():
    data = request.json.get('data', '').strip()
    if not data:
        return jsonify({'message': 'Invalid input!'}), 400
    linked_list.insert_at_end(data)
    return jsonify({'message': f"Inserted '{data}' at the end."})

@app.route('/remove_beginning', methods=['POST'])
def remove_beginning():
    removed_data = linked_list.remove_beginning()
    if removed_data is None:
        return jsonify({'message': 'List is empty!'}), 400
    return jsonify({'message': f"Removed '{removed_data}' from the beginning."})

@app.route('/remove_at_end', methods=['POST'])
def remove_at_end():
    removed_data = linked_list.remove_at_end()
    if removed_data is None:
        return jsonify({'message': 'List is empty!'}), 400
    return jsonify({'message': f"Removed '{removed_data}' from the end."})

@app.route('/remove_at', methods=['POST'])
def remove_at():
    data = request.json.get('data', '').strip()
    if not data:
        return jsonify({'message': 'Invalid input!'}), 400
    removed_data = linked_list.remove_at(data)
    if removed_data is None:
        return jsonify({'message': f"Data '{data}' not found in the list."}), 404
    return jsonify({'message': f"Removed '{removed_data}' from the list."})

@app.route('/print_linked_list', methods=['GET'])
def print_linked_list():
    linked_list_content = linked_list.printLinkedList()
    return jsonify({'list': linked_list_content})

@app.route('/stack')
def stack():
    return render_template('stack.html')

@app.route('/queue')
def queue():
    return render_template('queue.html')

if __name__ == "__main__":
    app.run(debug=True)
