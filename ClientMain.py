import customtkinter as CTK
import os
os.system("") # Enables ANSI codes in terminal?

# Connect to server button
def ConnectCli2Ser():
    print(COLOUR["BLUE"] + "Attempting to connect to Server..." + COLOUR["ENDCOLOUR"])
    print(COLOUR["RED"] + "Failed to connect to server!" + COLOUR["ENDCOLOUR"])

# Takes input and retrieves input
def GetClientNameInputBTN():
    InputText = ClientNameInput.get()
    print(InputText)


# Main program
## Default values
COLOUR = {
    "BLUE": "\033[94m",
    "GREEN": "\033[92m",
    "RED": "\033[91m",
    "ENDCOLOUR": "\033[0m",
}

## Initialises app
App = CTK.CTk() # Creates a instance of a window with its own loop?
App.title("Chatbox") # Changes the title of the window
App.geometry("500x500") # Changes window size

# Window grid
App.columnconfigure(0, weight=1, uniform = "a") # Single column of 1, only column so 100%, uniform prevents CTK from expanding widgets to other areas
App.rowconfigure((0, 2), weight=1, uniform = "a")
App.rowconfigure(1, weight=8, uniform = "a")
# Window frame
InitializeFrame = CTK.CTkFrame(App)
InitializeFrame.grid(row = 0, column = 0, padx = 5, pady = 5, sticky = "nsew")
InitializeFrame.rowconfigure(0, weight = 1, uniform = "a")
InitializeFrame.columnconfigure((0, 1), weight = 2, uniform = "a")
InitializeFrame.columnconfigure(2, weight = 1, uniform = "a")


# Widgets
ConnectBTN = CTK.CTkButton(InitializeFrame, text="Connect to server", command = ConnectCli2Ser) # Creates a CTK button with window to blit on, text on button and can call a subroutine
ConnectBTN.grid(row=0, column=0, padx = 5, pady = 5, sticky = "nsew") # The "visual hitbox" of the button
ClientNameInput = CTK.CTkEntry(InitializeFrame, placeholder_text = "Client Name") # Takes in player's name
ClientNameInput.grid(row=0, column=1, padx = 5, pady = 5, sticky = "nsew") # The "visual hitbox" of the button
ClientNameInputBTN = CTK.CTkButton(InitializeFrame, text = "Client Name", command = GetClientNameInputBTN) # Takes in player's name
ClientNameInputBTN.grid(row=0, column=2, padx = 5, pady = 5, sticky = "nsew") # The "visual hitbox" of the button

## Main
App.mainloop() # Runs the App object which displays a window and loops through events?