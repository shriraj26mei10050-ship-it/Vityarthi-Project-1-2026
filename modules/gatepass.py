from database.mock_db import outpass_db

def request_outpass(student_name, destination):
    if not student_name or not destination:
        return {"error": "Invalid details"}, 400
        
    new_pass = {
        "pass_id": len(outpass_db) + 101,
        "student": student_name,
        "destination": destination,
        "status": "Pending Approval"
    }
    outpass_db.append(new_pass)
    return {"message": "Out-pass requested", "data": new_pass}, 201

def get_outside_report():
    approved_leaves = [p for p in outpass_db if p["status"] == "Approved"]
    return {
        "total_outside": len(approved_leaves),
        "student_list": approved_leaves
    }
