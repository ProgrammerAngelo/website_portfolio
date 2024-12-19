# || IMPORTS ||
from flask import Flask, render_template, request, jsonify
from link_list import LinkedList
from stack import ShuntingYard
from queue_page import Queue_App
from binary_tree_page import BinaryTree

# ========================
# || ROOT ||
app = Flask(__name__)
linked_list = LinkedList()
queue_app = Queue_App()  # Instantiate the Queue_App object
binary_tree = BinaryTree()

# ========================
# || INITIALIZE A GLOBAL LINKED LIST INSTANCE ||

# ========================
# || RENDERING THE TABS ||
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/profiles')
def profiles():
    return render_template('profiles.html')

@app.route('/works')
def works():
    return render_template('works.html')

@app.route('/chin_profile')
def chin_profile():
    return render_template('chin_profile.html')

@app.route('/kei_profile')
def kei_profile():
    return render_template('kei_profile.html')

@app.route('/ryl_profile')
def ryl_profile():
    return render_template('ryl_profile.html')

@app.route('/ed_profile')
def ed_profile():
    return render_template('ed_profile.html')

@app.route('/gab_profile')
def gab_profile():
    return render_template('gab_profile.html')

@app.route('/gelo_profile')
def gelo_profile():
    return render_template('gelo_profile.html')

@app.route('/ris_profile')
def ris_profile():
    return render_template('ris_profile.html')

# ========================
# || LINKED LIST SYNTAX ||
@app.route('/link_list')
def link_list():
    linked_list_content = linked_list.printLinkedList()
    return render_template('link_list.html', linked_list_content=linked_list_content)

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
    return jsonify({'message': f"Removed '{removed_data}' at the beginning."})

@app.route('/remove_at_end', methods=['POST'])
def remove_at_end():
    removed_data = linked_list.remove_at_end()
    if removed_data is None:
        return jsonify({'message': 'List is empty!'}), 400
    return jsonify({'message': f"Removed '{removed_data}' at the end."})

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

# ========================
# STACK SYNTAX
@app.route('/stack')
def stack():
    return render_template('stack.html')

@app.route('/convert', methods=['POST'])
def convert():
    infix_expression = request.form['infix']  
    converter = ShuntingYard(infix_expression)  
    postfix = converter.convert()  
    steps = converter.get_steps()  
    return render_template('stack.html', steps=steps, postfix=postfix)

# ========================
# QUEUE SYNTAX

@app.route('/queue')  # Route for accessing the queue page
def queue_page():
    return render_template('queue_page.html')  # This will render your queue page (HTML)

@app.route('/enqueue', methods=['POST'])
def enqueue():
    data = request.form.get('data')  # Use .get() to safely retrieve the 'data' value
    if not data:
        return jsonify({"status": "error", "message": "No data provided"}), 400
    queue_app.enqueue(data)  # Call the method on the instance of Queue_App
    return jsonify({"status": "success", "queue": queue_app.view_queue()})  # View updated queue after enqueue

@app.route('/dequeue', methods=['POST'])
def dequeue():
    dequeued = queue_app.dequeue()  # Call the method on the instance of Queue_App
    if dequeued is None:
        return jsonify({"status": "error", "message": "Queue is empty!"}), 400
    return jsonify({"status": "success", "dequeued": dequeued, "queue": queue_app.view_queue()})  # Return the dequeued value and updated queue

@app.route('/view', methods=['GET'])
def view_queue():
    return jsonify({"queue": queue_app.view_queue()})  # View current state of the queue

# ========================
# BINARY TREE SYNTAX
@app.route('/binary_tree', methods=['GET', 'POST'])
def binary_tree_page():
    status_message = ""
    traversals = {}

    if request.method == "POST":
        # Get the tree node values as comma-separated input
        node_values = request.form.get("tree", "").split(',')
        
        # Clean up the values (strip spaces and filter out empty strings)
        node_values = [value.strip() for value in node_values if value.strip()]

        # Insert values into the binary tree
        if node_values:
            for value in node_values:
                try:
                    binary_tree.insert(int(value))  # Insert each value into the binary tree
                except ValueError:
                    status_message = f"'{value}' is not a valid integer and was skipped."

            # Get current traversals after insertions
            traversals = {
                'in_order': binary_tree.in_order_traversal(),
                'pre_order': binary_tree.pre_order_traversal(),
                'post_order': binary_tree.post_order_traversal(),
            }
        else:
            status_message = "No valid input provided."

    return render_template('binary_tree_page.html', traversals=traversals, status_message=status_message)

if __name__ == "__main__":
    app.run(debug=True)
