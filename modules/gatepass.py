from database.mock_db import outpass_db

def request_outpass(student_name, destination):
    if student_name == "" or destination == "":
        return {"status": "error", "message": "Fields cannot be empty"}
        
    next_pass_id = len(outpass_db) + 101
    new_pass = {
        "pass_id": next_pass_id,
        "student": student_name,
        "destination": destination,
        "status": "Pending Approval"
    }
    outpass_db.append(new_pass)
    return {"status": "success", "message": "Outpass requested successfully"}

def get_outside_report():
    return outpass_db
