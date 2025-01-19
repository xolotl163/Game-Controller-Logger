import csv
import time
import json
import pygame
import tkinter as tk
from datetime import datetime
from tkinter import simpledialog, messagebox, filedialog, scrolledtext

def get_controllers_list():
    """Lista los controles detectados por pygame."""
    controles = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]
    for i, control in enumerate(controles):
        control.init()
        print(f"Control {i}: {control.get_name()}")
    return controles

def save_user_info(player_name, current_game, file_path):
    user_info = {
        "player_name": player_name,
        "current_game": current_game,
        "file_path": file_path
    }
    with open("user_info.json", "w") as json_file:
        json.dump(user_info, json_file)

def main():

    #variables creation

    """
        The internal index of the buttons is as follows:
        [0] -> real value
        [1] -> given value
    """
    controller_buttons = {

        'A': [0, 0], 'B': [1,1 ], 'X': [2, 2], 'Y': [3, 3],
        'LB': [4, 4], 'RB': [5, 5],
        'Back': [6, 6], 'Start': [7, 7], 'Home': [8, 8],
        'L3': [9, 9], 'R3': [10, 10],
        'Right': [(1,0), 11], 'Left': [(-1,0), 12], 'Up': [(0,1), 13], 'Down': [(0,-1), 14],
        'LS_x': ['axis_0', 15], 'LS_y': ['axis_1', 16], 'RS_x': ['axis_3',17], 'RS_y': ['axis_4', 18],
        'LT': ['axis_2', 19], 'RT': ['axis_5', 20],
        'Up-left': [(-1,1), 21], 'Up-right': [(1,1), 22], 'Down-left': [(-1,-1), 23], 'Down-right': [(1,-1), 24],
        'DPad_no_use': [(0,0), 25]
    }

    # Initialize Pygame
    pygame.init()
    pygame.joystick.init()

    # Create the main window
    root = tk.Tk()
    root.title("Controlador de Juego")
    root.geometry("600x400")

    # Create a text widget to display log information
    log_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=20)
    log_text.pack(pady=10)

    # Get player's name
    player_name = simpledialog.askstring("Nombre del Jugador", "Ingrese su nombre:", parent=root)
    if not player_name:
        messagebox.showerror("Error", "Debe ingresar un nombre.")
        return

    # Get the name of the game
    current_game = simpledialog.askstring("Nombre del Juego", "Ingrese el nombre del juego:", parent=root)
    if not current_game:
        messagebox.showerror("Error", "Debe ingresar el nombre del juego.")
        return

    # Select the file path to save CSV files
    file_path = None
    while not file_path:
        file_path = filedialog.askdirectory(title="Seleccione la carpeta para guardar los archivos CSV")
        if not file_path:
            messagebox.showerror("Error", "Debe seleccionar una carpeta.")
    
    # Save user information to JSON
    save_user_info(player_name, current_game, file_path)

    # Initialize controller
    controllers = get_controllers_list()
    if not controllers:
        messagebox.showerror("Error", "No se detectaron controles.")
        return

    current_controller = controllers[0]
    messagebox.showinfo("Controlador", f"Usando control: {current_controller.get_name()}\nPresione botones en el control. Presione ESC para salir.")

    # Open CSV file for logging
    csv_file_name = f"{file_path}/{player_name}_buttons_pressed.csv"
    initial_time = time.perf_counter()
    with open(csv_file_name, mode='a', newline='') as csv_file:
        fieldnames = [
            'date', 
            'player_name', 
            'game', 
            'controller', 
            
            'event_type',
            'event_name',
            'event_real_value',
            'event_given_value',
            'elapsed_time'
        ]

        writer = csv.writer(csv_file)

        # Write header only if the file is new
        if csv_file.tell() == 0:
            log_text.insert(tk.END, "Writing header to CSV file.\n")
            writer.writerow(fieldnames)

        # Main loop
        running = True
        sensitivity_threshold = 0.1  # Adjust this value as needed

        def process_events():
            nonlocal running

            controller_buttons_keys = list( controller_buttons.keys() )
            controller_buttons_realValues = [ controller_buttons[key][0] for key in controller_buttons_keys ]

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

                elif event.type == pygame.JOYBUTTONDOWN:

                    pressed_button = event.button
                    event_name = None
                    event_given_value = None

                    timestamp = datetime.now().strftime("%Y-%m-%d")
                    current_time = time.perf_counter() - initial_time
                    current_time = round(current_time, 4)

                    match pressed_button:
                        case value if value in controller_buttons_realValues:
                            event_name = controller_buttons_keys[ controller_buttons_realValues.index(value) ]
                            event_given_value = controller_buttons[event_name][1]

                    data = [

                        #player info
                        timestamp, 
                        player_name, 
                        current_game, 
                        current_controller.get_name(), 
                        
                        #event info
                        'button', #event type
                        event_name, #event name
                        pressed_button, #event real value
                        event_given_value, #event given value 
                        current_time #elapsed time
                    ]
                    
                    writer.writerow(data)
                    csv_file.flush()
                    log_text.insert(tk.END, f"[{timestamp}] Botón {pressed_button} presionado en {current_controller.get_name()}.\n")
                    log_text.yview(tk.END)
                
                elif event.type == pygame.JOYAXISMOTION:

                    axis = event.axis
                    axis_name = f'axis_{axis}'
                    axis_value = round( event.value, 4)
                    event_name = None
                    event_given_value = None

                    if abs(axis_value) > sensitivity_threshold:  # Only register significant movements

                        timestamp = datetime.now().strftime("%Y-%m-%d")
                        current_time = time.perf_counter() - initial_time
                        current_time = round(current_time, 4)

                        match axis_name:
                            case value if value in controller_buttons_realValues:
                                event_name = controller_buttons_keys[ controller_buttons_realValues.index(value) ]
                                event_given_value = controller_buttons[event_name][1]

                        data = [

                            #player info
                            timestamp, 
                            player_name, 
                            current_game, 
                            current_controller.get_name(), 
                            
                            #event info
                            f'axis_{axis}', #event type
                            event_name, #event name 
                            axis_value, #event real value
                            event_given_value, #event given value 
                            current_time #elapsed time
                        ]
                        
                        writer.writerow(data)
                        csv_file.flush()
                        log_text.insert(tk.END, f"[{timestamp}] Movimiento en el eje {axis} con valor {value} en {current_controller.get_name()}.\n")
                        log_text.yview(tk.END)
                
                elif event.type == pygame.JOYHATMOTION:

                    hat = event.hat
                    hat_name = f'hat_{hat}'
                    value = event.value
                    event_name = None
                    event_given_value = None
                    
                    timestamp = datetime.now().strftime("%Y-%m-%d")
                    current_time = time.perf_counter() - initial_time
                    current_time = round(current_time, 4)

                    match value:
                            case value if value in controller_buttons_realValues:
                                event_name = controller_buttons_keys[ controller_buttons_realValues.index(value) ]
                                event_given_value = controller_buttons[event_name][1]

                    data = [
                        
                        #player info
                        timestamp, 
                        player_name, 
                        current_game, 
                        current_controller.get_name(), 
                        
                        #event info
                        f'hat_{hat}', #event type
                        event_name, #event name
                        value, #event real value
                        event_given_value, #event given value
                        current_time #elapsed time
                    ]
                    
                    writer.writerow(data)
                    csv_file.flush()
                    log_text.insert(tk.END, f"[{timestamp}] Movimiento en la cruceta {hat} con valor {value} en {current_controller.get_name()}.\n")
                    log_text.yview(tk.END)
            
            if running:
                root.after(100, process_events)  # Schedule the next call to process_events

        process_events()  # Start processing events
        root.mainloop()  # Start the Tkinter main loop

    pygame.quit()
    try:
        root.destroy()
    except tk.TclError:
        pass

if __name__ == "__main__":
    main()