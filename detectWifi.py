import tkinter as tk
import subprocess

class WifiGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Wifi Networks Around You!")

        # create label for wifi networks and signal strength
        self.network_label = tk.Label(self.window, text="Wifi Networks and Signal Strength:")
        self.network_label.pack(anchor='w')

        # create a text widget to display the network info
        self.network_info = tk.Text(self.window, height=10000, width=100)

        # create a scrollbar for the text widget
        self.scrollbar = tk.Scrollbar(self.window)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # attach the scrollbar to the text widget
        self.network_info.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.network_info.yview)

        self.network_info.pack(anchor='w')

        # call the update_network_info() function every 5 seconds to update the wifi networks and signal strength
        self.window.after(5000, self.update_network_info)

        self.window.mainloop()

    def update_network_info(self):
        # run the command to get the wifi networks and signal strength
        output = subprocess.check_output(["netsh", "wlan", "show", "network", "mode=Bssid"])

        # decode the output from bytes to string
        output = output.decode("utf-8")

        # clear the text widget
        self.network_info.delete('1.0', tk.END)

        # insert the new output into the text widget
        self.network_info.insert(tk.END, output)

        # call the update_network_info() function again after 5 seconds to keep updating the wifi networks and signal strength
        self.window.after(5000, self.update_network_info)

if __name__ == "__main__":
    gui = WifiGUI()
