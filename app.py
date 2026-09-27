import sys
from modules import allocation, tickets, gatepass

def display_menu():
    while True:
        print("\n--- HOSTEL SYSTEM MENU ---")
        print("1. View Rooms")
        print("2. Book a Room")
        print("3. View Complaints")
        print("4. File a Complaint")
        print("5. Update Complaint Status")
        print("6. Request Gate Outpass")
        print("7. View Gate Pass Report")
        print("8. Exit")
        
        user_choice = input("Select an option (1-8): ")
        
        if user_choice == "1":
            all_rooms = allocation.get_all_rooms()
            for r in all_rooms:
                print("Room Number: " + r["room_number"] + " | Type: " + r["type"] + " | Occupants: " + str(r["occupied_by"]))
                
        elif user_choice == "2":
            s_name = input("Enter student name: ")
            r_type = input("Enter room type (AC/Non-AC): ")
            result = allocation.allocate_room(s_name, r_type)
            print(result["message"])
            
        elif user_choice == "3":
            all_tickets = tickets.get_all_tickets()
            for t in all_tickets:
                print("ID: " + str(t["id"]) + " | Room: " + t["room"] + " | Problem: " + t["issue"] + " | Status: " + t["status"])
                
        elif user_choice == "4":
            room_no = input("Enter room number: ")
            problem = input("Enter problem details: ")
            result = tickets.create_ticket(room_no, problem)
            print(result["message"])
            
        elif user_choice == "5":
            t_id = input("Enter ticket ID: ")
            t_status = input("Enter new status: ")
            result = tickets.update_ticket_status(t_id, t_status)
            print(result["message"])
            
        elif user_choice == "6":
            name = input("Enter your name: ")
            place = input("Enter destination: ")
            result = gatepass.request_outpass(name, place)
            print(result["message"])
            
        elif user_choice == "7":
            active_passes = gatepass.get_outside_report()
            print("\n--- Current Hostel Outpasses ---")
            for p in active_passes:
                print("Pass ID: " + str(p["pass_id"]) + " | Name: " + p["student"] + " | Destination: " + p["destination"] + " | Status: " + p["status"])
                
        elif user_choice == "8":
            print("Closing the system.")
            sys.exit()
            
        else:
            print("Invalid input. Try again.")

if __name__ == '__main__':
    display_menu()
