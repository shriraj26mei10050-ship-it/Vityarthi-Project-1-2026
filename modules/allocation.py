from database.mock_db import rooms_db

def get_all_rooms():
    return rooms_db

def allocate_room(student_name, preferred_type):
    if student_name == "" or preferred_type == "":
        return {"status": "error", "message": "Fields cannot be empty"}

    for room in rooms_db:
        if room["type"].lower() == preferred_type.lower():
            current_occupants = len(room["occupied_by"])
            max_capacity = room["capacity"]
            
            if current_occupants < max_capacity:
                room["occupied_by"].append(student_name)
                return {"status": "success", "message": "Room allocated successfully"}

    return {"status": "error", "message": "No available rooms found"}
