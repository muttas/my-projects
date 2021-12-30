from tkinter import*
from tkinter import ttk, messagebox
import datetime as dt
import openpyxl
import pandas as pd
import os
import csv
class dataEntry:
    def __init__(self,root):
        self.root = root
        self.root.title("Quality tracker")
        self.root.geometry("1000x800+0+0")
        self.root.pack_propagate(False) # tells the root to not let the widgets inside it determine its size.
        self.root.resizable(0, 0)

        self.user = os.getlogin()

        #self.bg=ImageTk.PhotoImage(file=r'C:\Users\mutta\Desktop\test1\wallpaper_tk1.jpg')
        #bg=Label(self.root,image=self.bg).place(relwidth = 1, relheight = 1)

        frame1 = Frame(self.root, bg= "DarkCyan")
        frame1.place(x=0.5, y=0.5, width =2000, height = 80)

        frame2 = Frame(self.root, bg= "White")
        frame2.place(x=0.5, y=80.5, width =2000, height = 1000)

        title = Label(frame1, text= "Business Reviews Audit Entry", font=("times new roman", 20, "bold"), bg = "DarkCyan", fg = 'white').place(x=30,y=30)
        
        date= dt.datetime.now()
        date = Label(frame2, text=f"{date:%A, %B %d, %Y}", font="Calibri, 10", bg='white', fg='black')
        date.place(x=600, y=2)


        Auditor_login = Label(frame2, text= "Auditor Login:", font=("times new roman", 15, "bold"), bg = "white", fg = 'black').place(x=50,y=30)
        self.txt_Auditor_login = Label(frame2, text= self.user, font = ("calibri", 15, "bold"), bg= "white", fg="black")
        self.txt_Auditor_login.place(x=250, y= 30, width =100)

        File_name = Label(frame2, text= "File Name:", font=("times new roman", 15, "bold"), bg = "white", fg = 'black').place(x=50,y=70)
        self.txt_File_name = Entry(frame2, font = ("times new roman", 10), bg= "lightgray")
        self.txt_File_name.place(x=250, y= 75, width =250)

        Marketplace = Label(frame2, text= "Marketplace:", font=("times new roman", 15, "bold"), bg = "white", fg = 'black').place(x=50,y=110)
        
        self.cmb_Marketplace = ttk.Combobox(frame2, font = ("times new roman", 12), state= "readonly", justify=CENTER)
        self.cmb_Marketplace['values']=("Select","EN","DE","FR","IT","JP","ES","UK","CA","IN","None")
        self.cmb_Marketplace.place(x=250, y= 115, width =100)
        self.cmb_Marketplace.current(0)


        Audit_sample = Label(frame2, text= "Audit Sample:", font=("times new roman", 15, "bold"), bg = "white", fg = 'black').place(x=50,y=150)
        self.txt_Audit_sample = Entry(frame2, font = ("times new roman", 15), bg= "lightgray")
        self.txt_Audit_sample.place(x=250, y= 155, width =100)

        Error_count = Label(frame2, text= "Error Count:", font=("times new roman", 15, "bold"), bg = "white", fg = 'black').place(x=50,y=190)
        self.txt_Error_count =Entry(frame2, font = ("times new roman", 15), bg= "lightgray")
        self.txt_Error_count.place(x=250, y= 195, width =100)

        Classifier_login = Label(frame2, text= "Classifier login:", font=("times new roman", 15, "bold"), bg = "white", fg = 'black').place(x=50,y=230)
        self.txt_Classifier_login = Entry(frame2, font = ("times new roman", 15), bg= "lightgray")
        self.txt_Classifier_login.place(x=250, y= 235, width =100)
        


        button = Button(text = 'Submit', font = ("times new roman", 15),bg='DarkCyan', fg='white', cursor="hand2", command = self.auditDetails).place(x=500, y= 450, width = 100)
    
    def clear(self):
        self.txt_File_name.delete(0,END)
        self.cmb_Marketplace.current(0)
        self.txt_Audit_sample.delete(0,END)
        self.txt_Error_count.delete(0,END)
        self.txt_Classifier_login.delete(0,END)    

    def auditDetails(self):
        if self.txt_Auditor_login=="" or self.txt_File_name.get()=="" or self.cmb_Marketplace.get()=="" or self.txt_Audit_sample.get()=="" or self.txt_Error_count.get()=="" or self.txt_Classifier_login.get()=="":
            messagebox.showerror("Oops, Error!","All fields are mandatory", parent=self.root)
        elif str(self.user)==str(self.txt_Classifier_login.get()):
            messagebox.showerror("Oops, Error!","Auditor ID can't be same as Classifier ID", parent=self.root)

        
            
        else:
            try:
                al =  self.user
                fn =  self.txt_File_name.get()
                mp = self.cmb_Marketplace.get()
                asc =self.txt_Audit_sample.get()
                ec =self.txt_Error_count.get()
                cl = self.txt_Classifier_login.get()
                dtn = dt.datetime.now()
                dtns = dtn.strftime("%d-%m-%Y")

                accuracy = int((int(asc)-int(ec))*100/int(asc))

                

                

                '''
                df1 = pd.DataFrame({"Auditor login": [al],"File Name":[fn], "Marketplace":[mp],"Audit Sample":[asc],"Error Count":[ec],"Classifier login":[cl],"Date":[dtns]})
                df2 = pd.read_excel(r"\\ant.amazon.com\dept-as\HYD11\GroupData\ABSC-HYD\ABSC-Ops-Team\Business Reviews\audit_details.xlsx", index_col=[0])
                
                print(df1)
                
                print(df2)
                
                
                df3 = df2.append(df1, ignore_index=True)
                df3.drop(df3.filter(regex="Unname"),axis=1, inplace=True)
                
                df3.to_excel((r"\\ant.amazon.com\dept-as\HYD11\GroupData\ABSC-HYD\ABSC-Ops-Team\Business Reviews\audit_details.xlsx"), index=False)
                
                #df.to_excel(writer,index=False,header=False,startrow=len(reader)+1)
                '''

               


                # use incase if .txt output is needed
                
                audit_fields=["Auditor login","File Name","Marketplace","Audit Sample","Error Count","Classifier login","Date"]
                audit_values=[self.user,self.txt_File_name.get(),self.cmb_Marketplace.get(),self.txt_Audit_sample.get(),self.txt_Error_count.get(),self.txt_Classifier_login.get(),dt.datetime.now()]
                s= '\n'+al+'\t'+fn+'\t'+mp+'\t'+asc+'\t'+ec+'\t'+cl+'\t'+dtns+'\t'+str(accuracy)
                f= open((r"\\ant.amazon.com\dept-as\HYD11\GroupData\ABSC-HYD\ABSC-Ops-Team\Business Reviews\audit_details.txt"),'a')
                f.write(s)
                f.close()

                # converting to excel

                
                tf_df_new = pd.read_csv(r"\\ant.amazon.com\dept-as\HYD11\GroupData\ABSC-HYD\ABSC-Ops-Team\Business Reviews\audit_details.txt", sep = '\t')
                tf_df_new.to_excel(r"\\ant.amazon.com\dept-as\HYD11\GroupData\ABSC-HYD\ABSC-Ops-Team\Business Reviews\audit_details.xlsx", index=False)

                # deleting unnamed cols

                file = r"\\ant.amazon.com\dept-as\HYD11\GroupData\ABSC-HYD\ABSC-Ops-Team\Business Reviews\audit_details.xlsx"
                excel_file = openpyxl.load_workbook(file)
                excel_sheet = excel_file['Sheet1']

                # delete column
                excel_sheet.delete_cols(idx=9 , amount=1)
                excel_file.save(file)
                
            
               

               # use incase if .csv output is needed
                '''
                with open(r"\\ant.amazon.com\dept-as\HYD11\GroupData\ABSC-HYD\ABSC-Ops-Team\Business Reviews\audit_details.xlsx", "a") as fs:
                    w = csv.writer(fs,dialect = 'excel-tab')
                    w.writerow([al,fn,mp,asc,ec,cl,dtns])
                    fs.close()
                '''

                

                if accuracy < 98:
                    messagebox.showinfo("Alert!",f"Reassign the file as Classification accuracy: {accuracy}%, is below the 98% target. \n\n Entry Success!", parent=self.root)
                else:
                    messagebox.showinfo("Success!",f"Classification accuracy: {accuracy}%\n\n Entry Success!", parent=self.root)
                
                
                
                
                
                
                self.clear()
            except Exception as es:
                messagebox.showerror("Error",f"Error due to:{str(es)}", parent = self.root)
        


root=Tk()
obj=dataEntry(root)
root.mainloop()