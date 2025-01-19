# Game Controller Logger

## Overview
The Game Controller Logger is a Python application designed to capture and log button presses from various game controllers (PS4, Xbox, and generic controllers) during gameplay. It records the player's name, the button pressed, and the timestamp of each action, saving this data in a CSV file for further analysis and training of deep learning models.
At the moment it just has a current version working for GNU/Linux Debian based operative systems, but we expect to liberate a working version for windows in the near future.

## Buttons

The program has the next button distribution, it is based on a generic xbox 360 controller, due to its compatibility with a wide variety of videogames.

How to read the list: [button name] = [numeric value] -> [corresponding axis].

The last entry only appear if the button is related to two or more axis, an example of this are the analog sticks, these inputs use the X and Y axis.

### Frontal buttons
1. A = 0
2. B = 1
3. X = 2
4. Y = 3

### Shoulder buttons
1. LB = 4
2. RB = 5

### Central Buttons
1. Back = 6
2. Start = 7
3. Home = 8

### Thumbstick Buttons
1. L3 = 9
2. R3 = 10

### D-pad
1. Right = 11 -> (1, 0) : axis_6
2. Left = 12 -> (-1, 0) : axis_6
3. Up =    13 -> (0, 1) : axis_7
4. Down = 14 -> (0, -1) : axis_7

### Analog sticks
1. LS_x = 15 -> axis_0
2. LS_y = 16 -> axis_1
3. RS_x = 17 -> axis_3
4. RS_y = 18 -> axis_4

### Triggers
1. LT = 19 -> axis_2
2. RT = 20 -> axis_5

### Others combinations of the D-pad
1. Up-left = 21 -> (-1, 1)
2. Up-right = 22 -> (1, 1)
3. Down-left = 23 -> (-1, -1)
4. Down-right = 24 -> (1, -1)
5. Dpad_no_use = 25 -> (0, 0)

## Project Structure
```
log_controller_buttons
├── main.py              # Entry point of the application
├── requirements.txt     # Lists project dependencies
└── README.md            # Project documentation
```

## Setup Instructions
1. Clone the repository:
   ```
   git clone <repository-url>
   cd game-controller-logger
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:

   ```
   python LOG_CONTROLLER_BUTTONS/main.py or python3 LOG_CONTROLLER_BUTTONS/main.py
   if you are using any GNU/Linux operative system. 

   Additionally, if you want to use the software in an easier way just download
   the 'log_buttons_controller' executable. It works for GNU/Linux Debian based operative systems. 
   ```

2. It is necessary to connect the controller to your PC before running the apliccation, otherwise it won't work. Follow the prompts to enter your name and start playing with your game controller. The application will log all button presses along with timestamps.



## Dependencies
- `pygame` or `inputs`: Libraries for handling game controller input.

## Contributing
Feel free to submit issues or pull requests to improve the functionality of the Game Controller Logger.