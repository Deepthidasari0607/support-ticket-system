from flask import Flask, request, jsonify

app = Flask(__name__)

tickets = []

@app.route('/create_ticket', methods=['POST'])
def create_ticket():
    data = request.json
    if not data or 'issue' not in data:
        return jsonify({"error": "Invalid input"}), 400

    ticket = {
        "id": len(tickets) + 1,
        "issue": data['issue'],
        "status": "Open"
    }
    tickets.append(ticket)
    return jsonify({"message": "Ticket created", "ticket": ticket})

@app.route('/tickets', methods=['GET'])
def get_tickets():
    return jsonify(tickets)

@app.route('/update_ticket/<int:id>', methods=['PUT'])
def update_ticket(id):
    for ticket in tickets:
        if ticket['id'] == id:
            ticket['status'] = "Resolved"
            return jsonify({"message": "Ticket resolved"})
    return jsonify({"message": "Ticket not found"})

if __name__ == '__main__':
    app.run(debug=True)
