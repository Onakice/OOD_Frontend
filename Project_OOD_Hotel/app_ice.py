import tkinter as tk
from tkinter import messagebox, simpledialog
from HilbertsHotel import HilbertsHotel

class HotelUI:
    def __init__(self, hotel):
        self.hotel = hotel
        self.setup_ui()

    def setup_ui(self):
        """ตั้งค่าหน้าต่างหลักของแอปพลิเคชัน"""
        self.root = tk.Tk()
        self.root.title("Hilbert's Hotel Management")
        self.root.geometry("400x400")
        self.create_widgets()

    def create_widgets(self):
        """สร้างปุ่มต่างๆ สำหรับการทำงาน"""
        buttons = [
            ("Add Room", self.add_room),
            ("Add Multiple Rooms", self.add_multiple_rooms),
            ("Remove Room", self.remove_room),
            ("Sort Rooms", self.sort_rooms),
            ("Find Room", self.find_room),
            ("Save Data", self.save_data),
            ("Show Empty Rooms", self.show_empty_rooms),
        ]
        
        for text, command in buttons:
            tk.Button(self.root, text=text, command=command).pack(pady=10)

    def add_room(self):
        """เพิ่มห้องเดี่ยวพร้อมข้อมูลจากผู้ใช้"""
        try:
            fleet, ship, bus, guest = self.get_room_input()
            self.hotel.add_room(fleet, ship, bus, guest)
            self.show_info("Room added successfully!")
        except ValueError:
            self.show_error("Invalid input, please enter valid numbers.")

    def add_multiple_rooms(self):
        """เพิ่มหลายห้องจาก Fleet เริ่มและจบ"""
        try:
            fleet_start, fleet_end = self.get_fleet_range()
            for fleet in range(fleet_start, fleet_end + 1):
                ship, bus, guest = self.get_room_input(fleet_only=False)
                self.hotel.add_room(fleet, ship, bus, guest)
            self.show_info("Multiple rooms added successfully!")
        except ValueError:
            self.show_error("Invalid input, please enter valid numbers.")

    def remove_room(self):
        """ลบห้องตามหมายเลขที่กำหนด"""
        try:
            room_number = self.get_number_input("Enter Room Number to Remove:")
            self.hotel.remove_room(room_number)
            self.show_info("Room removed successfully!")
        except ValueError:
            self.show_error("Invalid room number.")

    def sort_rooms(self):
        """เรียงลำดับห้อง"""
        self.hotel.sort_rooms()
        self.show_info("Rooms sorted successfully!")

    def find_room(self):
        """ค้นหาห้องตามหมายเลข"""
        try:
            room_number = self.get_number_input("Enter Room Number to Find:")
            room_info = self.hotel.find_room(room_number)
            if room_info:
                self.show_info(f"Room Info: {room_info}")
            else:
                self.show_info("Room not found.")
        except ValueError:
            self.show_error("Invalid room number.")

    def save_data(self):
        """บันทึกข้อมูลห้อง"""
        self.hotel.save_to_file()
        self.show_info("Data saved successfully!")

    def show_empty_rooms(self):
        """แสดงห้องว่าง"""
        empty_rooms = self.hotel.show_empty_rooms()
        self.show_info(f"Empty Rooms: {empty_rooms}")

    def get_room_input(self, fleet_only=True):
        """รับข้อมูลจากผู้ใช้เกี่ยวกับ Fleet, Ship, Bus, และ Guest"""
        fleet = int(simpledialog.askstring("Input", "Enter Fleet Number:"))
        if fleet_only:
            return fleet
        ship = int(simpledialog.askstring("Input", "Enter Ship Number:"))
        bus = int(simpledialog.askstring("Input", "Enter Bus Number:"))
        guest = int(simpledialog.askstring("Input", "Enter Guest Number:"))
        return fleet, ship, bus, guest

    def get_fleet_range(self):
        """รับค่า Fleet เริ่มและสิ้นสุดจากผู้ใช้"""
        fleet_start = int(simpledialog.askstring("Input", "Enter Start Fleet Number:"))
        fleet_end = int(simpledialog.askstring("Input", "Enter End Fleet Number:"))
        return fleet_start, fleet_end

    def get_number_input(self, prompt):
        """รับข้อมูลตัวเลขจากผู้ใช้"""
        return int(simpledialog.askstring("Input", prompt))

    def show_info(self, message):
        """แสดงข้อความข้อมูล"""
        messagebox.showinfo("Information", message)

    def show_error(self, message):
        """แสดงข้อความข้อผิดพลาด"""
        messagebox.showerror("Error", message)

    def run(self):
        """เริ่มต้น GUI"""
        self.root.mainloop()

# การใช้งาน UI กับคลาส Hotel
hotel = HilbertsHotel()  # สมมติว่าเรามีคลาส HilbertsHotel แล้ว
ui = HotelUI(hotel)
ui.run()
