from database.mock_db import tickets_db

def get_all_tickets():
    return tickets_db

def create_ticket(room_number, issue_description):
    if room_number == "" or issue_description == "":
        return {"status": "error", "message": "Fields cannot be empty"}
        
    next_id = len(tickets_db) + 1
    new_ticket = {
        "id": next_id,
        "room": room_number,
        "issue": issue_description,
        "status": "Pending"
    }
    tickets_db.append(new_ticket)
    return {"status": "success", "message": "Ticket logged successfully"}

def update_ticket_status(ticket_id, new_status):
    for ticket in tickets_db:
        if str(ticket["id"]) == str(ticket_id):
            ticket["status"] = new_status
            return {"status": "success", "message": "Status updated successfully"}
            
    return {"status": "error", "message": "Ticket ID not found"}
