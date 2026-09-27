from flask import Flask, jsonify, request
from modules import allocation, tickets, gatepass

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return jsonify({"system": "CampusLive API", "status": "Online"}), 200

@app.route('/api/rooms', methods=['GET'])
def view_rooms():
    return jsonify(allocation.get_all_rooms()), 200

@app.route('/api/rooms/allocate', methods=['POST'])
def book_room():
    data = request.get_json() or {}
    name = data.get('student')
    room_type = data.get('type')
    response, status_code = allocation.allocate_room(name, room_type)
    return jsonify(response), status_code

@app.route('/api/tickets', methods=['GET'])
def view_tickets():
    return jsonify(tickets.get_all_tickets()), 200

@app.route('/api/tickets', methods=['POST'])
def add_ticket():
    data = request.get_json() or {}
    room = data.get('room')
    issue = data.get('issue')
    response, status_code = tickets.create_ticket(room, issue)
    return jsonify(response), status_code

@app.route('/api/tickets/<int:id>', methods=['PUT'])
def patch_ticket(id):
    data = request.get_json() or {}
    status = data.get('status', 'Resolved')
    response, status_code = tickets.update_ticket_status(id, status)
    return jsonify(response), status_code

@app.route('/api/outpass/request', methods=['POST'])
def file_pass():
    data = request.get_json() or {}
    name = data.get('student')
    dest = data.get('destination')
    response, status_code = gatepass.request_outpass(name, dest)
    return jsonify(response), status_code

@app.route('/api/outpass/report', methods=['GET'])
def guard_report():
    return jsonify(gatepass.get_outside_report()), 200

if __name__ == '__main__':
    app.run(debug=True)
