from database.mock_db import tickets_db

def get_all_tickets():
    return tickets_db

def create_ticket(room_number, issue_description):
    if not room_number or not issue_description:
        return {"error": "Missing fields"}, 400
        
    new_id = len(tickets_db) + 1
    new_ticket = {
        "id": new_id,
        "room": room_number,
        "issue": issue_description,
        "status": "Pending"
    }
    tickets_db.append(new_ticket)
    return {"message": "Ticket created successfully", "ticket": new_ticket}, 201

def update_ticket_status(ticket_id, new_status):
    for ticket in tickets_db:
        if ticket["id"] == int(ticket_id):
            ticket["status"] = new_status
            return {"message": f"Ticket {ticket_id} updated to {new_status}"}, 200
    return {"error": "Ticket not found"}, 404
