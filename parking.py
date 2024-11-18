

import tkinter as tk
from tkinter import simpledialog, messagebox
import pytz
from datetime import datetime
import time


# ParkingSlot class
class ParkingSlot:
    def __init__(self, slot_id):
        self.slot_id = slot_id
        self.is_occupied = False
        self.car = None
        self.vehicle_type = None
        self.parked_at = None
        self.amount_due = 0.0
        self.in_time = None
        self.out_time = None
        self.booking_time = None  # For advanced bookings

    def park(self, car, vehicle_type):
        """Park the car in this slot."""
        if not self.is_occupied:
            self.is_occupied = True
            self.car = car
            self.vehicle_type = vehicle_type
            self.parked_at = time.time()
            self.in_time = self.get_current_time()
            return f"Car {car} parked in slot {self.slot_id}."
        return f"Slot {self.slot_id} is already occupied."

    def leave(self):
        """Remove the car from this slot and calculate the parking fee."""
        if self.is_occupied:
            parked_duration = time.time() - self.parked_at
            self.is_occupied = False
            self.car = None
            self.parked_at = None
            self.calculate_parking_fee(parked_duration / 60)  # Convert to minutes
            self.out_time = self.get_current_time()
            return f"Car {self.car} left from slot {self.slot_id}. Duration: {parked_duration / 60:.2f} mins. Amount Due: ₹{self.amount_due:.2f}"
        return f"Slot {self.slot_id} is empty."

    def get_status(self):
        """Get the status of the parking slot."""
        return 'Occupied' if self.is_occupied else 'Available'

    def calculate_parking_fee(self, duration_minutes):
        """Calculate parking fee based on dynamic pricing model."""
        if self.vehicle_type == '2-wheeler':
            rate_per_hour = 30  # 2-wheeler rate per hour in INR
        else:
            rate_per_hour = 50  # 4-wheeler rate per hour in INR

        if duration_minutes <= 60:
            self.amount_due = rate_per_hour
        elif 60 < duration_minutes <= 180:
            self.amount_due = rate_per_hour + ((duration_minutes - 60) / 60) * rate_per_hour * 0.6
        else:
            self.amount_due = rate_per_hour + 2 * rate_per_hour * 0.6 + ((duration_minutes - 180) / 60) * rate_per_hour * 0.3

    def mark_paid(self):
        """Mark the parking as paid."""
        self.amount_due = 0.0

    def get_current_time(self):
        """Get current time in IST."""
        tz = pytz.timezone('Asia/Kolkata')
        return datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")


# ParkingLot class
class ParkingLot:
    def __init__(self, num_slots):
        self.slots = [ParkingSlot(i + 1) for i in range(num_slots)]
        self.advanced_bookings = {}  # Store advanced bookings by slot_id

    def display_available_slots(self):
        available_slots = [f"Slot {slot.slot_id}" for slot in self.slots if not slot.is_occupied]
        return available_slots

    def park_car(self, car, vehicle_type):
        """Try to park a car in the first available slot."""
        for slot in self.slots:
            if not slot.is_occupied:
                return slot.park(car, vehicle_type)
        return "No available parking slots."

    def checkout_car(self, car):
        """Checkout a car from the parking lot."""
        for slot in self.slots:
            if slot.car == car:
                return slot.leave()
        return f"Car {car} not found in the parking lot."

    def get_parked_cars_info(self):
        """Get information of all parked cars."""
        parked_cars_info = []
        for slot in self.slots:
            if slot.is_occupied:
                parked_cars_info.append(f"Car {slot.car} in slot {slot.slot_id} - {slot.vehicle_type} | In: {slot.in_time} | Out: {slot.out_time} | Duration: {self.calculate_parked_duration(slot)} mins | Amount Due: ₹{slot.amount_due:.2f}")
        return parked_cars_info

    def calculate_parked_duration(self, slot):
        """Calculate the parked duration in minutes."""
        if slot.is_occupied:
            duration = time.time() - slot.parked_at
            return duration / 60  # Return in minutes
        return 0

    def advanced_booking(self, slot_id, booking_time):
        """Make an advanced booking for a slot."""
        for slot in self.slots:
            if slot.slot_id == slot_id:
                if not slot.is_occupied:
                    slot.booking_time = booking_time
                    self.advanced_bookings[slot_id] = booking_time
                    return f"Slot {slot_id} booked for {booking_time}."
                return f"Slot {slot_id} is already occupied."
        return "Invalid slot ID."


# User class
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def login(self, username, password):
        """Check if user credentials are correct."""
        return self.username == username and self.password == password


# Admin class inherits from User
class Admin(User):
    def __init__(self, username, password):
        super().__init__(username, password)

    def add_parking_slot(self, parking_lot):
        """Admin can add a parking slot."""
        new_slot = ParkingSlot(len(parking_lot.slots) + 1)
        parking_lot.slots.append(new_slot)
        return f"New parking slot {new_slot.slot_id} added."

    def remove_parking_slot(self, parking_lot, slot_id):
        """Admin can remove a parking slot."""
        for slot in parking_lot.slots:
            if slot.slot_id == slot_id:
                if not slot.is_occupied:
                    parking_lot.slots.remove(slot)
                    return f"Slot {slot_id} removed."
                return f"Slot {slot_id} is occupied, cannot remove."
        return "Invalid slot ID."

    def force_remove_car(self, parking_lot, car):
        """Forcefully remove a car."""
        for slot in parking_lot.slots:
            if slot.car == car:
                slot.leave()
                return f"Car {car} has been forcefully removed."
        return f"Car {car} not found in the parking lot."

    def view_advanced_bookings(self, parking_lot):
        """View all advanced bookings."""
        bookings_info = []
        for slot_id, booking_time in parking_lot.advanced_bookings.items():
            bookings_info.append(f"Slot {slot_id} booked for {booking_time}")
        if bookings_info:
            return "\n".join(bookings_info)
        else:
            return "No advanced bookings."


# Tkinter GUI for the Parking Management System
class ParkingManagementSystemGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Parking Management System")
        self.master.geometry("600x600")
        
        # Create parking lot and users (admin and user)
        self.parking_lot = ParkingLot(5)  # Start with 5 slots
        self.admin = Admin("admin", "adminpass")
        self.user = User("user", "userpass")
        
        self.current_user = None
        self.create_login_screen()

    def create_login_screen(self):
        """Create login screen."""
        self.clear_screen()

        # Add the project title at the top of the login screen
        self.project_title_label = tk.Label(self.master, text="EasyPark", font=("Helvetica", 24, "bold"))
        self.project_title_label.pack(pady=20)  # Added padding to give some space

        self.username_label = tk.Label(self.master, text="Username:")
        self.username_label.pack(pady=5)
        
        self.username_entry = tk.Entry(self.master)
        self.username_entry.pack(pady=5)
        
        self.password_label = tk.Label(self.master, text="Password:")
        self.password_label.pack(pady=5)
        
        self.password_entry = tk.Entry(self.master, show="*")
        self.password_entry.pack(pady=5)
        
        self.login_button = tk.Button(self.master, text="Login", command=self.login)
        self.login_button.pack(pady=10)

    def login(self):
        """Login the user."""
        username = self.username_entry.get()
        password = self.password_entry.get()

        if self.admin.login(username, password):
            self.current_user = self.admin
            self.create_admin_dashboard()
        elif self.user.login(username, password):
            self.current_user = self.user
            self.create_user_dashboard()
        else:
            messagebox.showerror("Invalid Credentials", "Username or Password is incorrect.")

    def create_user_dashboard(self):
        """Create the user dashboard."""
        self.clear_screen()

        self.welcome_label = tk.Label(self.master, text="Welcome User!")
        self.welcome_label.pack(pady=10)

        self.view_slots_button = tk.Button(self.master, text="View Available Slots", command=self.view_available_slots)
        self.view_slots_button.pack(pady=10)

        self.park_button = tk.Button(self.master, text="Park a Car", command=self.park_car)
        self.park_button.pack(pady=10)

        self.checkout_button = tk.Button(self.master, text="Checkout Car", command=self.checkout_car)
        self.checkout_button.pack(pady=10)
        
        self.advanced_booking_button = tk.Button(self.master, text="Advanced Booking", command=self.advanced_booking)
        self.advanced_booking_button.pack(pady=10)

        self.dynamic_pricing_button = tk.Button(self.master, text="Show Dynamic Pricing", command=self.show_dynamic_pricing)
        self.dynamic_pricing_button.pack(pady=10)

        self.logout_button = tk.Button(self.master, text="Logout", command=self.logout)
        self.logout_button.pack(pady=10)

    def show_dynamic_pricing(self):
        """Show dynamic pricing for 2-wheeler and 4-wheeler."""
        pricing_info = """
        Dynamic Pricing:
        - 2-wheeler: ₹30 per hour.
        - 4-wheeler: ₹50 per hour.
        - Discount for long duration:
            - After 1 hour: 60% of the base rate.
            - After 3 hours: 30% of the base rate.
        """
        messagebox.showinfo("Dynamic Pricing", pricing_info)

    def create_admin_dashboard(self):
        """Create the admin dashboard."""
        self.clear_screen()

        self.welcome_label = tk.Label(self.master, text="Welcome Admin!")
        self.welcome_label.pack(pady=10)

        self.add_slot_button = tk.Button(self.master, text="Add Parking Slot", command=self.add_parking_slot)
        self.add_slot_button.pack(pady=10)

        self.remove_slot_button = tk.Button(self.master, text="Remove Parking Slot", command=self.remove_parking_slot)
        self.remove_slot_button.pack(pady=10)

        self.view_parked_cars_button = tk.Button(self.master, text="View Parked Cars", command=self.view_parked_cars)
        self.view_parked_cars_button.pack(pady=10)

        self.view_advanced_bookings_button = tk.Button(self.master, text="View Advanced Bookings", command=self.view_advanced_bookings)
        self.view_advanced_bookings_button.pack(pady=10)

        self.force_remove_button = tk.Button(self.master, text="Force Remove Car", command=self.force_remove_car)
        self.force_remove_button.pack(pady=10)

        self.logout_button = tk.Button(self.master, text="Logout", command=self.logout)
        self.logout_button.pack(pady=10)

    def view_available_slots(self):
        """Display available parking slots for the user."""
        available_slots = self.parking_lot.display_available_slots()
        if available_slots:
            slots_info = "\n".join(available_slots)
            messagebox.showinfo("Available Slots", f"Available Slots:\n{slots_info}")
        else:
            messagebox.showinfo("Available Slots", "No available slots.")
    
    def park_car(self):
        """Allow the user to park their car."""
        car = simpledialog.askstring("Park a Car", "Enter your Car ID:")
        if car:
            vehicle_type = simpledialog.askstring("Vehicle Type", "Enter vehicle type (2-wheeler or 4-wheeler):")
            if vehicle_type in ['2-wheeler', '4-wheeler']:
                message = self.parking_lot.park_car(car, vehicle_type)
                messagebox.showinfo("Park Car", message)
            else:
                messagebox.showerror("Invalid Vehicle Type", "Please enter a valid vehicle type (2-wheeler or 4-wheeler).")
    
    def checkout_car(self):
        """Allow the user to checkout a parked car."""
        car = simpledialog.askstring("Checkout Car", "Enter your Car ID:")
        if car:
            result = self.parking_lot.checkout_car(car)
            messagebox.showinfo("Checkout Car", result)

    def advanced_booking(self):
        """Allow the user to make an advanced booking."""
        slot_id = simpledialog.askinteger("Advanced Booking", "Enter Slot ID for advanced booking:")
        booking_time = simpledialog.askstring("Booking Time", "Enter booking time (YYYY-MM-DD HH:MM:SS):")
        if slot_id and booking_time:
            result = self.parking_lot.advanced_booking(slot_id, booking_time)
            messagebox.showinfo("Advanced Booking", result)

    def add_parking_slot(self):
        """Admin adds a new parking slot."""
        result = self.admin.add_parking_slot(self.parking_lot)
        messagebox.showinfo("Add Slot", result)

    def remove_parking_slot(self):
        """Admin removes a parking slot."""
        slot_id = simpledialog.askinteger("Remove Slot", "Enter Slot ID to remove:")
        if slot_id:
            result = self.admin.remove_parking_slot(self.parking_lot, slot_id)
            messagebox.showinfo("Remove Slot", result)

    def view_parked_cars(self):
        """Admin views all parked cars."""
        parked_cars = self.parking_lot.get_parked_cars_info()
        if parked_cars:
            messagebox.showinfo("Parked Cars", "\n".join(parked_cars))
        else:
            messagebox.showinfo("Parked Cars", "No cars are currently parked.")

    def view_advanced_bookings(self):
        """Admin views advanced bookings."""
        bookings_info = self.admin.view_advanced_bookings(self.parking_lot)
        messagebox.showinfo("Advanced Bookings", bookings_info)

    def force_remove_car(self):
        """Admin forcefully removes a car."""
        car = simpledialog.askstring("Force Remove Car", "Enter Car ID to force remove:")
        if car:
            result = self.admin.force_remove_car(self.parking_lot, car)
            messagebox.showinfo("Force Remove Car", result)

    def logout(self):
        """Logout the current user."""
        self.current_user = None
        self.create_login_screen()

    def clear_screen(self):
        """Clear the current screen."""
        for widget in self.master.winfo_children():
            widget.destroy()

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = ParkingManagementSystemGUI(root)
    root.mainloop()
