# Game Controller Logger

## Overview
The Game Controller Logger is a Python application designed to capture and log button presses from various game controllers (PS4, Xbox, and generic controllers) during gameplay. It records the player's name, the button pressed, and the timestamp of each action, saving this data in a CSV file for further analysis and training of deep learning models.
At the moment it just has a current version working for GNU/Linux Debian based operative systems, but we expect to liberate a working version for windows in the near future. 

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