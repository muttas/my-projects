import os
import pandas as pd
import tkinter as tk
from tkinter import ttk, messagebox
#import sys
root = tk.Tk()

user = os.getlogin()

root.title("Business Reviews Quality Metrics")
root.geometry("1200x600+0+0")
root.pack_propagate(False) # tells the root to not let the widgets inside it determine its size.
root.resizable(0, 0)


frame1 = tk.LabelFrame(root, text=f"Audit Data for {user}", bg="White", font =(("times new roman", 25)))
frame1.place(x=0, y=0.65, width = 1200, height=500)

my_tree = ttk.Treeview(frame1)
my_tree.place(relheight=1, relwidth=1)

treescrolly = tk.Scrollbar(frame1, orient="vertical", command=my_tree.yview) # command means update the yaxis view of the widget
treescrollx = tk.Scrollbar(frame1, orient="horizontal", command=my_tree.xview) # command means update the xaxis view of the widget
my_tree.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set) # assign the scrollbars to the Treeview Widget
treescrollx.pack(side="bottom", fill="x") # make the scrollbar fill the x axis of the Treeview widget
treescrolly.pack(side="right", fill="y") # make the scrollbar fill the y axis of the Treeview widget




frame2 = tk.Frame(root, bg= "White")
frame2.place(x=0, y=501, width =1200, height = 99)

button = tk.Button(frame2, text = 'Get Audit Details', font = ("times new roman", 15),bg='DarkCyan', fg='white', cursor="hand2", command=lambda: auditDetails()).place(x=500, y= 35, width = 200)          

def clear_data():
    my_tree.delete(*my_tree.get_children())
    return None

def auditDetails():
    
    clear_data()
    
    team = ["pokkus", "izharmi", "ammshiv", "ksnehalb", "awaipsh", "rayyanms", "kprudhvi", "mutta"]
    file = r"\\ant.amazon.com\dept-as\HYD11\GroupData\ABSC-HYD\ABSC-Ops-Team\Business Reviews\audit_details.xlsx"
    if user in team:
        try:
            df = pd.read_excel(file)
            
            df = df.loc[df["Classifier Login"]==user]
            
            my_tree["column"] = list(df.columns)
            my_tree["show"] = "headings"

            for column in my_tree["column"]:
                my_tree.heading(column, text = column)
            
            df_rows = df.to_numpy().tolist()
            
            for row in df_rows:
                my_tree.insert("", "end", values = row)
            
        except Exception as es:
            messagebox.showerror("Error",f"Error due to:{str(es)}", parent = root)
        

        






root.mainloop()