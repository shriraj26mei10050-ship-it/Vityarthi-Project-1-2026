from database.mock_db import rooms_db

def get_all_rooms():
    return rooms_db

def allocate_room(student_name, preferred_type):
    if not student_name or not preferred_type:
        return {"error": "Student name and room type are required"}, 400

    for room in rooms_db:
        if room["type"].lower() == preferred_type.lower():
            if len(room["occupied_by"]) < room["capacity"]:
                room["occupied_by"].append(student_name)
                return {
                    "message": f"Success! {student_name} allocated to Room {room['room_number']}",
                    "room_details": room
                }, 201

    return {"error": f"No vacant {preferred_type} rooms available right now"}, 404
