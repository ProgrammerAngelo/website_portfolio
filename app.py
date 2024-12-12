# || IMPORTS ||
from flask import Flask, render_template, request, jsonify
from link_list import LinkedList
from stack import ShuntingYard

# ========================
# || ROOT ||
app = Flask(__name__)

# ========================
# || INITIALIZE A GLOBAL LINKED LIST INSTANCE ||
linked_list = LinkedList()

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
# - Rendering the linked list html
@app.route('/link_list')
def link_list():
    linked_list_content = linked_list.printLinkedList()
    return render_template('link_list.html', linked_list_content=linked_list_content)

# - Linked list API routes
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
# - Rendering the stack.html
@app.route('/stack')
def stack():
    return render_template('stack.html')

# - Stack API routes
@app.route('/convert', methods=['POST'])
def convert():
    infix_expression = request.form['infix']  
    converter = ShuntingYard(infix_expression)  
    postfix = converter.convert()  
    steps = converter.get_steps()  
    return render_template('stack.html', steps=steps, postfix=postfix)

# ========================
# - QUEUE SYNTAX
@app.route('/queue')
def queue():
    return render_template('queue.html')

# ========================
# - BINARY TREE SYNTAX

# ========================
# - GRAPH SYNTAX



if __name__ == "__main__":
    app.run(debug=True)
