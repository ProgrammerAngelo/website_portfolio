from flask import Flask, render_template, request, jsonify
from link_list import LinkedList
from stack import ShuntingYard
from queue_page import Node, Deque_App
from binary_tree_page import BinaryTree
import networkx as nx
from stations import stations_coordinates, connections
from selection_sort import selection_sort
from insertion_sort import insertion_sort
from flask import Flask, render_template, request, redirect, url_for
from merge_sort import merge_sort
from quick_sort import quick_sort_algorithm
import os

# ========================
# || ROOT ||
app = Flask(__name__, static_folder='static')

linked_list = LinkedList()
deque_app = Deque_App()  # Instantiate the Queue_App object
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

@app.route('/queue_page')  # Route for accessing the queue page
def queue_page():
    return render_template('queue_page.html')  # Render the queue HTML page

# ----------------------------
# Simple Queue Operations
# ----------------------------
@app.route('/enqueue', methods=['POST'])
def enqueue():
    data = request.form.get('data')
    if not data:
        return jsonify({"status": "error", "message": "No data provided"}), 400
    deque_app.enqueue(data)  # Call enqueue (adds to the rear)
    return jsonify({"status": "success", "queue": deque_app.view_deque()})

@app.route('/dequeue', methods=['POST'])
def dequeue():
    dequeued = deque_app.dequeue()  # Call dequeue (removes from the front)
    if dequeued is None:
        return jsonify({"status": "error", "message": "Queue is empty!"}), 400
    return jsonify({"status": "success", "dequeued": dequeued, "queue": deque_app.view_deque()})

# ----------------------------
# Double-Ended Queue Operations
# ----------------------------
@app.route('/push', methods=['POST'])
def push():
    data = request.form.get('data')
    if not data:
        return jsonify({"status": "error", "message": "No data provided"}), 400
    deque_app.push(data)  # Call push (adds to the front)
    return jsonify({"status": "success", "queue": deque_app.view_deque()})

@app.route('/pop', methods=['POST'])
def pop():
    popped = deque_app.pop()  # Call pop (removes from the front)
    if popped is None:
        return jsonify({"status": "error", "message": "Deque is empty!"}), 400
    return jsonify({"status": "success", "popped": popped, "queue": deque_app.view_deque()})

@app.route('/inject', methods=['POST'])
def inject():
    data = request.form.get('data')
    if not data:
        return jsonify({"status": "error", "message": "No data provided"}), 400
    deque_app.inject(data)  # Call inject (adds to the rear)
    return jsonify({"status": "success", "queue": deque_app.view_deque()})

@app.route('/eject', methods=['POST'])
def eject():
    ejected = deque_app.eject()  # Call eject (removes from the rear)
    if ejected is None:
        return jsonify({"status": "error", "message": "Deque is empty!"}), 400
    return jsonify({"status": "success", "ejected": ejected, "queue": deque_app.view_deque()})

# ----------------------------
# View Queue / Deque State
# ----------------------------
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    @staticmethod
    def from_infix(expression):
        def build_tree(tokens):
            ops = []  # Stack for operators
            nodes = []  # Stack for operands
            precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

            def attach_operator():
                if len(nodes) < 2:
                    raise ValueError("Invalid expression: missing operands.")
                operator = ops.pop()
                right = nodes.pop()
                left = nodes.pop()
                operator_node = TreeNode(operator)
                operator_node.left = left
                operator_node.right = right
                nodes.append(operator_node)

            for token in tokens:
                if token.isalnum():  # Operand (A, B, C, etc.)
                    nodes.append(TreeNode(token))
                elif token in precedence:  # Operator (+, -, *, /)
                    while (ops and ops[-1] != '(' and
                           precedence.get(ops[-1], 0) >= precedence[token]):
                        attach_operator()
                    ops.append(token)
                elif token == '(':  # Opening parenthesis
                    ops.append(token)
                elif token == ')':  # Closing parenthesis
                    while ops and ops[-1] != '(':
                        attach_operator()
                    if not ops:
                        raise ValueError("Invalid expression: unmatched parenthesis.")
                    ops.pop()  # Remove the '('

            while ops:  # Attach remaining operators
                attach_operator()

            if len(nodes) != 1:
                raise ValueError("Invalid expression: too many operands or operators.")
            return nodes[0]

        # Tokenize the expression by splitting on parentheses and spaces
        tokens = expression.replace('(', ' ( ').replace(')', ' ) ').split()
        return build_tree(tokens)

    # Build a binary tree from postfix expression
    @staticmethod
    def from_postfix(expression):
        stack = []
        for token in expression.split():
            if token.isalnum():  # Operand
                stack.append(TreeNode(token))
            else:  # Operator
                right = stack.pop()
                left = stack.pop()
                operator_node = TreeNode(token)
                operator_node.left = left
                operator_node.right = right
                stack.append(operator_node)
        return stack[0]

    # Build a binary tree from prefix expression
    @staticmethod
    def from_prefix(expression):
        stack = []
        for token in reversed(expression.split()):
            if token.isalnum():  # Operand
                stack.append(TreeNode(token))
            else:  # Operator
                left = stack.pop()
                right = stack.pop()
                operator_node = TreeNode(token)
                operator_node.left = left
                operator_node.right = right
                stack.append(operator_node)
        return stack[0]

    # Serialize the tree into JSON-compatible format
    @staticmethod
    def serialize_tree(root):
        if not root:
            return None
        return {
            "value": root.value,
            "left": BinaryTree.serialize_tree(root.left),
            "right": BinaryTree.serialize_tree(root.right),
        }

    # Convert a tree to a prefix expression
    @staticmethod
    def to_prefix(root):
        if not root:
            return ""
        return f"{root.value} {BinaryTree.to_prefix(root.left)} {BinaryTree.to_prefix(root.right)}".strip()


@app.route('/binary_tree_page', methods=['GET'])
def binary_tree_page():
    return render_template('binary_tree_page.html')


@app.route('/build_tree', methods=['POST'])
def build_tree():
    data = request.json
    expression = data.get('expression', '').strip()
    expr_type = data.get('type', 'infix').lower()

    if not expression:
        return jsonify({"error": "Expression cannot be empty!"}), 400

    try:
        if expr_type == 'infix':
            root = BinaryTree.from_infix(expression)
        elif expr_type == 'postfix':
            root = BinaryTree.from_postfix(expression)
        elif expr_type == 'prefix':
            root = BinaryTree.from_prefix(expression)
        else:
            return jsonify({"error": f"Unsupported expression type: {expr_type}"}), 400

        tree_data = BinaryTree.serialize_tree(root)
        prefix_expression = BinaryTree.to_prefix(root)
        return jsonify({"tree": tree_data, "prefix": prefix_expression})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ========================
# GRAPH SYNTAX
@app.route('/graph')
def graph():
    # Pass the stations data to the template
    return render_template('graph.html', stations=stations_coordinates)

# Create a graph and add nodes and edges
G = nx.Graph()
for station in stations_coordinates.keys():
    G.add_node(station, pos=stations_coordinates[station])

for station1, station2 in connections:
    G.add_edge(station1, station2, weight=1)

# Function to find the shortest path
def find_shortest_path(start, end):
    if start not in G or end not in G:
        return None
    return nx.shortest_path(G, source=start, target=end, weight='weight')

@app.route('/find_path', methods=['POST'])
def find_path():
    start = request.form['start'].lower().strip()
    end = request.form['end'].lower().strip()

    # Find the shortest path
    shortest_path = find_shortest_path(start, end)

    if shortest_path is None:
        return jsonify({'error': 'Invalid stations or no path found.'})
    
    path_coords = [stations_coordinates[station] for station in shortest_path]
    return jsonify({'path': shortest_path, 'coordinates': path_coords})

#-----------
#Bubble sort

@app.route('/bubble_sort')
def bubble_sort():

    return render_template('bubble_sort.html')

#--------------
#Selection sort
@app.route('/selection_sort')
def selection_sort():
    # Your view logic here
    return render_template('selection_sort.html')

@app.route('/selection_sort', methods=['GET', 'POST'])
def sort():
    if request.method == 'POST':
        try:
            input_numbers = request.form['numbers']  # Get the input from the form
            numbers = list(map(int, input_numbers.split(',')))  # Convert the input into a list of integers
            sorted_numbers = selection_sort(numbers)  # Sort the numbers using the selection sort algorithm
            return render_template('selection_sort.html', numbers=numbers, sorted_numbers=sorted_numbers)
        except ValueError:
            return render_template('selection_sort.html', error="Please enter a valid list of integers separated by commas.")
    return render_template('selection_sort.html')  # GET request renders the form

#--------------
#Insertion sort

sorted_list = []
steps = []

@app.route("/insertion_sort", methods=["GET", "POST"])
def insertion_sort_page():
    global sorted_list, steps  # Declare the variables as global
    if request.method == "POST":
        try:
            # Get the input from the form
            numbers = request.form.get("number")  # Retrieve the input as a string
            # Split the input by commas and convert to integers
            number_list = [int(num.strip()) for num in numbers.split(",")]
            
            # Call insertion sort function (ensure it's modified to return sorted list and steps)
            sorted_list, steps = insertion_sort(number_list)  # Update both variables
            
        except ValueError:
            # Handle invalid input (e.g., non-integer values)
            return render_template(
                "insertion_sort.html", 
                sorted_list=sorted_list, 
                steps=steps, 
                error="Invalid input! Please enter a comma-separated list of integers."
            )
    
    return render_template("insertion_sort.html", sorted_list=sorted_list, steps=steps)

@app.route("/reset_sorted_list", methods=["POST"])
def reset_sorted_list():
    global sorted_list, steps
    sorted_list = []  # Clear the sorted list
    steps = []  # Clear the step-by-step process
    return redirect(url_for("insertion_sort_page"))
#-----------
#Merge Sort
def home():
    return render_template('merge_sort.html')

@app.route('/merge_sort_page', methods=['GET', 'POST'])  # Allow both GET and POST
def merge_sort_page():
    if request.method == 'POST':
        numbers_input = request.form['numbers']
        
        try:
            numbers = [int(num.strip()) for num in numbers_input.split(',')]
        except ValueError:
            return render_template('merge_sort.html', error="Please enter valid numbers.")
        
        sorted_numbers, steps = merge_sort(numbers)
        return render_template('merge_sort.html', sorted_numbers=sorted_numbers, steps=steps)
    
    # Handle GET request to render the page initially
    return render_template('merge_sort.html')


#quick sort Logic
@app.route("/quick_sort.html", methods=["GET", "POST"])
def quick_sort():
    sorted_list = None
    steps = []  # List to hold step-by-step process
    error = None

    if request.method == "POST":
        try:
            # Get input from form
            user_input = request.form.get("number")
            if not user_input:
                raise ValueError("Please enter numbers to sort.")

            # Convert input to a list of integers
            data = list(map(int, user_input.split(",")))

            # Perform quick sort and track steps
            quick_sort_algorithm(data, 0, len(data) - 1, steps)
            sorted_list = data

        except ValueError as e:
            error = str(e)

    return render_template("quick_sort.html", sorted_list=sorted_list, steps=steps, error=error)

if __name__ == "__main__":
    app.run(debug=True)
