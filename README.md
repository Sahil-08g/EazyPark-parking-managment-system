# EazyPark-parking-managment-system
EasyPark - Parking Management System
Overview
EasyPark is an advanced Parking Management System developed with Python using the Tkinter library for graphical user interfaces (GUIs). This system offers a comprehensive solution for managing parking spaces in real-time, catering to both users (car owners) and administrators (parking lot managers). The system enables efficient parking management, fee calculations, advanced bookings, and dynamic pricing models to meet modern parking demands.

This application was designed to streamline the parking process, reduce time spent searching for parking spots, and improve overall user and administrative experiences. EasyPark also features dynamic parking fees based on parking duration and vehicle types, making it suitable for modern urban environments with fluctuating demand.

Features

User Features:
Login/Logout: Users can securely log in with their credentials to access the system.
View Available Slots: Users can check real-time availability of parking slots and select a slot that suits their needs.
Park a Car: Users can park their vehicle in an available slot, specifying the car ID and vehicle type (e.g., 2-wheeler or 4-wheeler).
Checkout Car: Users can check out from a parking slot, view parking duration, and calculate the parking fee based on dynamic pricing.
Advanced Booking: Users can book parking slots in advance for specific times or dates.
Dynamic Pricing: Real-time dynamic pricing based on vehicle type, duration, and time of parking. Discounts apply for extended parking durations.

Admin Features:
Login/Logout: Admins can log in with their credentials to manage the parking lot.
Add Parking Slot: Admins can add new parking slots to the parking lot, increasing capacity as demand rises.
Remove Parking Slot: Admins can remove parking slots from the system, provided they are not in use.
View Parked Cars: Admins can view detailed information about all currently parked vehicles, including car IDs, slot IDs, parking duration, and outstanding fees.
View Advanced Bookings: Admins can manage advanced bookings made by users, ensuring availability at specified times.
Force Remove Car: Admins can forcefully remove a vehicle from a parking slot if necessary (e.g., for illegal parking or other issues).

Dynamic Pricing:
2-Wheeler: ₹30 per hour.
4-Wheeler: ₹50 per hour.

After 1 hour:
2-Wheeler: 60% of the base rate.
4-Wheeler: 60% of the base rate.

After 3 hours:
2-Wheeler: 30% of the base rate.
4-Wheeler: 30% of the base rate.

This dynamic pricing ensures fairness and optimizes revenue for parking lot owners while encouraging turnover for high-demand spaces.

Market Demand and Needs

1. Urbanization and Traffic Congestion
As cities grow and more people move into urban areas, parking has become a critical problem. In highly populated cities, finding parking can take a long time, creating traffic congestion. EasyPark offers a solution to this issue by providing real-time availability of parking slots.

Problem: Lack of available parking, especially in densely populated areas, leads to increased traffic congestion and frustration.
Solution: EasyPark optimizes parking usage by displaying available slots in real-time and reducing the time spent searching for parking spaces.

2. Increase in Vehicle Ownership
With the rise in personal vehicle ownership and the growing number of cars on the road, there is a greater need for efficient parking management systems.

Problem: The sheer number of vehicles in urban areas is overwhelming parking facilities, creating competition for limited spaces.
Solution: EasyPark allows users to park more efficiently by providing dynamic pricing, which optimizes the use of available slots and ensures fair usage.

3. Parking Fees and Revenue Management
Parking lot owners often struggle to manage parking fees and ensure they charge fairly for the duration vehicles are parked. EasyPark addresses this by implementing a dynamic pricing model that adjusts fees based on factors like parking duration and vehicle type.

Problem: Fixed parking fees may not reflect usage patterns or market demand, potentially leading to underutilized parking spaces.
Solution: With dynamic pricing, EasyPark maximizes revenue by adjusting fees based on parking duration and vehicle type. Users who park for extended periods get discounted rates, encouraging turnover.

4. Need for Convenience and Efficiency
Users increasingly demand convenience, and parking is no exception. The manual process of looking for a parking spot, paying the fee, and leaving can be time-consuming and stressful.

Problem: Users waste time finding parking, and administrators struggle with managing availability, enforcement, and fees.
Solution: EasyPark streamlines the process, allowing users to find, reserve, and park in available spaces instantly while automating fee calculation and collection.

5. Technological Integration in Parking
Many parking systems still rely on manual or outdated methods for slot management and fee calculation. EasyPark leverages technology to enhance user experience and automate parking lot operations.

Problem: Outdated systems lead to inefficiency, errors, and difficulties for both users and administrators.
Solution: EasyPark modernizes parking lot management with automated slot booking, fee calculation, and advanced booking systems, all through an intuitive interface.


Requirements

Prerequisites:
Python 3.x (Python 3.6 or later recommended)
Tkinter (for GUI, comes pre-installed with Python)
pytz (for timezone management)

How It Works
Login: Upon launching the application, the user is presented with a login screen. The user can log in with either admin or user credentials:

Admin Credentials: Username: admin, Password: adminpass
User Credentials: Username: user, Password: userpass
User Dashboard: Once logged in as a user, they are presented with options:

View Available Slots: Displays available parking slots in real-time.
Park a Car: Allows users to park their car by specifying a car ID and vehicle type.
Checkout Car: Checkout the car and calculates the fee based on duration.
Advanced Booking: Reserve a slot for future use.
Show Dynamic Pricing: View the dynamic pricing model for different vehicle types.
Admin Dashboard: After logging in as an admin, the following options are available:

Add Parking Slot: Add a new parking slot to increase parking capacity.
Remove Parking Slot: Remove an unused or underperforming parking slot.
View Parked Cars: View the list of currently parked cars and their details.
View Advanced Bookings: See all the advanced bookings made by users.
Force Remove Car: Forcefully remove a parked car from a slot if necessary.
Exit: Users and admins can log out from the system at any time.

Code Structure
1. ParkingSlot Class
Manages the state of individual parking slots.

Attributes: slot_id, is_occupied, car, vehicle_type, amount_due, in_time, out_time, booking_time
Methods:
park(car, vehicle_type): Parks a vehicle in the slot.
leave(): Removes the car from the slot and calculates the parking fee.
get_status(): Returns whether the slot is occupied or available.
calculate_parking_fee(duration_minutes): Calculates the fee based on parking duration.
mark_paid(): Resets the parking fee after payment.
get_current_time(): Returns the current time in IST.
2. ParkingLot Class
Manages the entire parking lot and its slots.

Attributes: slots, advanced_bookings
Methods:
display_available_slots(): Displays all available slots.
park_car(car, vehicle_type): Parks a car in an available slot.
checkout_car(car): Checks out a car and calculates the fee.
get_parked_cars_info(): Retrieves details of all parked cars.
advanced_booking(slot_id, booking_time): Allows for advanced booking of slots.
3. User and Admin Classes
User Class: Manages user credentials and login process.
Admin Class: Inherits from User and provides additional administrative functionalities (e.g., adding/removing slots, viewing parked cars, managing advanced bookings).
4. ParkingManagementSystemGUI Class
Manages the graphical user interface (GUI) for both the user and admin.

Methods:
create_login_screen(): Displays the login interface.
create_user_dashboard(): Displays the user dashboard with parking and checkout options.
create_admin_dashboard(): Displays the admin dashboard with management

Screenshots

Login Screen
<img width="594" alt="Screenshot 2024-11-17 at 9 04 37 PM" src="https://github.com/user-attachments/assets/4d41f780-b947-45e6-8c8e-99c3726d299b">

User Dashboard
<img width="594" alt="Screenshot 2024-11-17 at 9 06 09 PM" src="https://github.com/user-attachments/assets/055675da-4613-4133-99a8-7477a60ab43b">


Admin Dashboard
<img width="594" alt="Screenshot 2024-11-17 at 9 05 05 PM" src="https://github.com/user-attachments/assets/30bba938-5a2c-4bbc-af33-e4be6b1b3953">

Contributing
We welcome contributions to the project! To contribute:

Fork the repository.
Create a new branch.
Implement your changes.
Create a pull request.
License
This project is licensed under the MIT License - see the LICENSE file for more details.


