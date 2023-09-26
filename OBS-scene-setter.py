import tkinter as tk
from tkinter import filedialog
from screeninfo import get_monitors

# Create an empty list to store items
items = []

# Function to get number of monitors
def get_number_of_monitors():
    return len(get_monitors())

# Function to add an item
def add_item():
    if len(items) < 5:
        print("Available types: Browser, Display Capture, Game Capture, Image, Media Source, Video Capture Device, Window Capture")
        item_type = input("Enter the type of item from the above list: ")
        
        if item_type == 'Image' or item_type == 'Media Source':
            root = tk.Tk()
            root.withdraw()
            file_path = filedialog.askopenfilename()
            item_id = file_path
            
        elif item_type == 'Browser':
            item_id = input("Enter the URL: ")
        
        elif item_type == 'Display Capture':
            monitors = get_monitors()
            num_monitors = len(monitors)
            print(f"Number of monitors available: {num_monitors}")
            for i, monitor in enumerate(monitors):
                print(f"Monitor {i+1}: {monitor.name}")
            monitor_choice = input("Enter the monitor number you'd like to capture: ")
            item_id = f"Monitor {monitor_choice}"

        else:
            item_id = input(f"Enter the ID or location for {item_type}: ")
        
        items.append({"type": item_type, "id": item_id})
    else:
        print("You've reached the maximum number of items (5).")

# Function to display items
def display_items():
    for index, item in enumerate(items):
        print(f"Item {index + 1}: Type = {item['type']}, ID = {item['id']}")

# Main loop
while True:
    action = input("Would you like to add an item or display items? (add/display/quit): ")
    
    if action.lower() == "add":
        add_item()
    elif action.lower() == "display":
        display_items()
    elif action.lower() == "quit":
        break
