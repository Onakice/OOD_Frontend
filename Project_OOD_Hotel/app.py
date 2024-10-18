import tkinter as tk
from tkinter import messagebox, simpledialog, Toplevel, Label, Entry, Button
from HilbertsHotel import HilbertsHotel

class HotelUI:
    def __init__(self, hotel):
        self.hotel = hotel
        self.root = tk.Tk()
        self.root.title("Rond-mayer-du-Sieur Hotel Management")
        self.root.geometry("400x500")  # Set a fixed size for the window
        self.create_widgets()

    def create_widgets(self):
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=20)

        title_label = tk.Label(self.root, text="Rond-mayer-du-Sieur Hotel Management", font=("Helvetica", 16))
        title_label.pack(pady=10)

        self.add_room_button = tk.Button(button_frame, text="Add Room", command=self.show_add_room_dialog, width=20)
        self.add_room_button.grid(row=0, column=0, pady=5)

        self.add_multiple_rooms_button = tk.Button(button_frame, text="Add Multiple Rooms", command=self.show_add_multiple_rooms_dialog, width=20)
        self.add_multiple_rooms_button.grid(row=1, column=0, pady=5)

        self.remove_room_button = tk.Button(button_frame, text="Remove Room", command=self.remove_room, width=20)
        self.remove_room_button.grid(row=2, column=0, pady=5)

        self.sort_rooms_button = tk.Button(button_frame, text="Sort Rooms", command=self.sort_rooms, width=20)
        self.sort_rooms_button.grid(row=3, column=0, pady=5)

        self.find_room_button = tk.Button(button_frame, text="Find Room", command=self.find_room, width=20)
        self.find_room_button.grid(row=4, column=0, pady=5)

        self.save_data_button = tk.Button(button_frame, text="Save Data", command=self.save_data, width=20)
        self.save_data_button.grid(row=5, column=0, pady=5)

        self.empty_rooms_button = tk.Button(button_frame, text="Show Empty Rooms", command=self.show_empty_rooms, width=20)
        self.empty_rooms_button.grid(row=6, column=0, pady=5)

        self.status_label = tk.Label(self.root, text="", font=("Helvetica", 10), fg="green")
        self.status_label.pack(pady=10)

    def show_add_room_dialog(self):
        self.dialog = Toplevel(self.root)
        self.dialog.title("Add Room")
        
        # Create labels and entry fields
        Label(self.dialog, text="Fleet Number:").grid(row=0, column=0, padx=10, pady=5)
        self.fleet_entry = Entry(self.dialog)
        self.fleet_entry.grid(row=0, column=1, padx=10, pady=5)

        Label(self.dialog, text="Ship Number:").grid(row=1, column=0, padx=10, pady=5)
        self.ship_entry = Entry(self.dialog)
        self.ship_entry.grid(row=1, column=1, padx=10, pady=5)

        Label(self.dialog, text="Bus Number:").grid(row=2, column=0, padx=10, pady=5)
        self.bus_entry = Entry(self.dialog)
        self.bus_entry.grid(row=2, column=1, padx=10, pady=5)

        Label(self.dialog, text="Guest Number:").grid(row=3, column=0, padx=10, pady=5)
        self.guest_entry = Entry(self.dialog)
        self.guest_entry.grid(row=3, column=1, padx=10, pady=5)

        # Add Submit Button
        submit_button = Button(self.dialog, text="Add Room", command=self.add_room_from_dialog)
        submit_button.grid(row=4, columnspan=2, pady=10)

    def add_room_from_dialog(self):
        try:
            fleet = int(self.fleet_entry.get())
            ship = int(self.ship_entry.get())
            bus = int(self.bus_entry.get())
            guest = int(self.guest_entry.get())
            
            room_number = self.hotel.add_room(fleet, ship, bus, guest)
            messagebox.showinfo("Success", f"Room {room_number} added.")
            self.status_label.config(text=f"Room {room_number} added successfully.")
            self.dialog.destroy()  # Close the dialog after adding
        except ValueError:
            messagebox.showwarning("Input Error", "Please enter valid integers for all fields.")

    def show_add_multiple_rooms_dialog(self):
    # Create a new window for input
        self.dialog = Toplevel(self.root)
        self.dialog.title("Add Multiple Rooms")
    
    # Create labels and entry fields in the same row
        Label(self.dialog, text="Start Fleet Number:").grid(row=0, column=0, padx=10, pady=5)
        self.fleet_start_entry = Entry(self.dialog)
        self.fleet_start_entry.grid(row=0, column=1, padx=10, pady=5)

        Label(self.dialog, text="End Fleet Number:").grid(row=0, column=2, padx=10, pady=5)
        self.fleet_end_entry = Entry(self.dialog)
        self.fleet_end_entry.grid(row=0, column=3, padx=10, pady=5)

        Label(self.dialog, text="Start Ship Number:").grid(row=1, column=0, padx=10, pady=5)
        self.ship_start_entry = Entry(self.dialog)
        self.ship_start_entry.grid(row=1, column=1, padx=10, pady=5)

        Label(self.dialog, text="End Ship Number:").grid(row=1, column=2, padx=10, pady=5)
        self.ship_end_entry = Entry(self.dialog)
        self.ship_end_entry.grid(row=1, column=3, padx=10, pady=5)

        Label(self.dialog, text="Start Bus Number:").grid(row=2, column=0, padx=10, pady=5)
        self.bus_start_entry = Entry(self.dialog)
        self.bus_start_entry.grid(row=2, column=1, padx=10, pady=5)

        Label(self.dialog, text="End Bus Number:").grid(row=2, column=2, padx=10, pady=5)
        self.bus_end_entry = Entry(self.dialog)
        self.bus_end_entry.grid(row=2, column=3, padx=10, pady=5)

        Label(self.dialog, text="Start Guest Number:").grid(row=3, column=0, padx=10, pady=5)
        self.guest_start_entry = Entry(self.dialog)
        self.guest_start_entry.grid(row=3, column=1, padx=10, pady=5)

        Label(self.dialog, text="End Guest Number:").grid(row=3, column=2, padx=10, pady=5)
        self.guest_end_entry = Entry(self.dialog)
        self.guest_end_entry.grid(row=3, column=3, padx=10, pady=5)

        submit_button = Button(self.dialog, text="Add Rooms", command=self.add_multiple_rooms_from_dialog)
        submit_button.grid(row=4, columnspan=4, pady=10)

    def add_multiple_rooms_from_dialog(self):
        try:
            fleet_start = int(self.fleet_start_entry.get())
            fleet_end = int(self.fleet_end_entry.get())
            ship_start = int(self.ship_start_entry.get())
            ship_end = int(self.ship_end_entry.get())
            bus_start = int(self.bus_start_entry.get())
            bus_end = int(self.bus_end_entry.get())
            guest_start = int(self.guest_start_entry.get())
            guest_end = int(self.guest_end_entry.get())

            if all(v is not None for v in [fleet_start, fleet_end, ship_start, ship_end, bus_start, bus_end, guest_start, guest_end]):
                added_rooms = []
                for fleet in range(fleet_start, fleet_end + 1):
                    for ship in range(ship_start, ship_end + 1):
                        for bus in range(bus_start, bus_end + 1):
                            for guest in range(guest_start, guest_end + 1):
                                room_number = self.hotel.add_room(fleet, ship, bus, guest)
                                added_rooms.append(room_number)

                messagebox.showinfo("Success", f"Added rooms: {', '.join(map(str, added_rooms))}")
                self.status_label.config(text=f"Added rooms: {', '.join(map(str, added_rooms))}")
                self.dialog.destroy()  # Close the dialog after adding
        except ValueError:
            messagebox.showwarning("Input Error", "Please enter valid integers for all fields.")

    # def add_multiple_rooms(self):
    #     fleet_start = simpledialog.askinteger("Input", "Enter Start Fleet Number:")
    #     fleet_end = simpledialog.askinteger("Input", "Enter End Fleet Number:")
    #     ship_start = simpledialog.askinteger("Input", "Enter Start Ship Number:")
    #     ship_end = simpledialog.askinteger("Input", "Enter End Ship Number:")
    #     bus_start = simpledialog.askinteger("Input", "Enter Start Bus Number:")
    #     bus_end = simpledialog.askinteger("Input", "Enter End Bus Number:")
    #     guest_start = simpledialog.askinteger("Input", "Enter Start Guest Number:")
    #     guest_end = simpledialog.askinteger("Input", "Enter End Guest Number:")

    #     if all(v is not None for v in [fleet_start, fleet_end, ship_start, ship_end, bus_start, bus_end, guest_start, guest_end]):
    #         added_rooms = []
    #         for fleet in range(fleet_start, fleet_end + 1):
    #             for ship in range(ship_start, ship_end + 1):
    #                 for bus in range(bus_start, bus_end + 1):
    #                     for guest in range(guest_start, guest_end + 1):
    #                         room_number = self.hotel.add_room(fleet, ship, bus, guest)
    #                         added_rooms.append(room_number)

    #         messagebox.showinfo("Success", f"Added rooms: {', '.join(map(str, added_rooms))}")
    #         self.status_label.config(text=f"Added rooms: {', '.join(map(str, added_rooms))}")

    def remove_room(self):
        room_number = simpledialog.askinteger("Input", "Enter Room Number to Remove:")
        if room_number is not None:
            self.hotel.remove_room(room_number)
            self.status_label.config(text=f"Room {room_number} removed.")

    def sort_rooms(self):
        sorted_rooms = self.hotel.sort_rooms()
        messagebox.showinfo("Sorted Rooms", f"Sorted Rooms: {sorted_rooms}")
        self.status_label.config(text="Rooms sorted.")

    def find_room(self):
        room_number = simpledialog.askinteger("Input", "Enter Room Number to Find:")
        if room_number is not None:
            result = self.hotel.find_room(room_number)
            if result:
                messagebox.showinfo("Room Found", f"Room {room_number} details: {result}")
                self.status_label.config(text=f"Room {room_number} found.")
            else:
                messagebox.showwarning("Not Found", f"Room {room_number} not found.")
                self.status_label.config(text=f"Room {room_number} not found.")

    def save_data(self):
        file_name = simpledialog.askstring("Input", "Enter file name to save data:")
        if file_name:
            self.hotel.save_to_file(file_name)
            self.status_label.config(text=f"Data saved to {file_name}.")

    def show_empty_rooms(self):
        empty_count = self.hotel.empty_rooms()
        messagebox.showinfo("Empty Rooms", f"Number of empty rooms: {empty_count}")
        self.status_label.config(text=f"Number of empty rooms: {empty_count}")

    def run(self):
        self.root.mainloop()

# Initialize and run the UI
hotel = HilbertsHotel(100)
app = HotelUI(hotel)
app.run()