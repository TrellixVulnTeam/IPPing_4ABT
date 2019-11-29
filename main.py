import ipfunc as ipfunc
import tkinter as tk


class GUIframeworkmain(ipfunc.IPfunctions):
<<<<<<< HEAD
    """This class communicates with ipfunc.py using the IPfunctions class"""
=======
    """This class communicates with ipfunc.py file using the IPfunctions class and objects"""

>>>>>>> version-0.1.0
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.l_sep = tk.Label(self, text="___________").grid(row=1)
        self.iptxt = tk.Label(self, text="Enter IP:", font=("Arial Bold", 9)).grid(row=2)

        tk.Button(self, bg="green", text='Add New IP', command=self.newip).grid(row=0, column=0, pady=2),
        tk.Button(self, text='Open IPlist', command=self.contents).grid(row=0, column=1, sticky=tk.SE, pady=2),
        tk.Button(self, text='Open Reports', command=self.reports).grid(row=0, column=2, sticky=tk.SE, pady=2),
        tk.Button(self, text='Ping All IPs', command=self.scanlist).grid(row=0, column=3, sticky=tk.SE, pady=2),
        tk.Button(self, text='Exit', command=self.quit).grid(row=0, column=4, pady=2)

        self.e1 = tk.Entry(self, bg='grey', fg='white', font=("Arial Bold",))
        self.e1.grid(row=2, column=1)


class App(tk.Tk):
    """This class uses the Tkinter module and its used to call buttons labels change
    certain settings with in Tkinter module etc... onto the the GUI"""
<<<<<<< HEAD
    def __init__(self):
         super().__init__()
=======

    def __init__(self):
        super().__init__()

        self.title("IPPing")
        self.geometry("450x100+900+300")
>>>>>>> version-0.1.0

        # calls the GUIframework class onto Tkinter GUI module
        self.ip_function = GUIframeworkmain(self)
        self.ip_function.grid()



if __name__ == '__main__':
    """this function runs the App class which is using the Tkinter module"""
    App().mainloop()
