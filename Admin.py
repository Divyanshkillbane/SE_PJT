import csv
from tkinter import *
import pandas as pd
import dataframe_image as dfi
from PIL import ImageTk, Image
from datetime import date 


root = Tk()
root.geometry('800x600')
root.title("Management")

'''part 1 admission and enquiry'''
def profile():
          
   wr = Toplevel()
   wr.geometry('800x600')
   wr.title("Write")
# ''' 6 Labels and  enter bars '''
         
   lab1 = Label(wr,text = "Name").place(x = 10 , y =50 )
   lab2 = Label(wr, text = "Roll no.").place(x = 10 , y =90 )
   lab3 = Label(wr,text = "Sem").place(x = 10 , y = 130)
   lab4 = Label(wr , text = "Father Name").place(x = 10 , y = 170)
   lab5 = Label(wr, text = "Mother Name").place(x = 10 , y = 210)
   lab6 = Label(wr, text = "Mobile No.").place(x = 10 , y = 250)
        

   e1 = Entry(wr)
   e1.place(x = 150 , y = 50)
   e2 = Entry(wr)
   e2.place(x = 150, y = 90)
   e3 = Entry(wr)
   e3.place(x = 150 , y = 130)
   e4 = Entry(wr)
   e4.place(x = 150 , y = 170)
   e5 = Entry(wr)
   e5.place(x = 150 , y = 210)
   e6 = Entry(wr)
   e6.place(x = 150 , y = 250)
         

   def save():
       with open("data.csv",'a') as file_obj:
          lst = []
          lst.append(e1.get().capitalize())
          lst.append(e2.get().capitalize())
          lst.append(e3.get().capitalize())
          lst.append(e4.get().capitalize())
          lst.append(e5.get().capitalize())
          lst.append(e6.get().capitalize())

          write_obj = csv.writer(file_obj)

          write_obj.writerow(lst)

   def _search_():
# cnv = Canvas(sea, width = 720,height=400)
    # cnv.place(x=10,y=80)
        global img_label
        df = pd.read_csv("data.csv")
        name = e1.get()
        name = name.capitalize()
        print(name)
        

        temp_df = df[ df['Name'] == name]

        
        

        dfi.export(temp_df, 'df.png')
        img = ImageTk.PhotoImage(Image.open('df.png').resize((700,100)))
        # cnv.create_image(0,0,anchor =NW,image = img)
        img_label = Label(wr, image = img)
        img_label.place(x =10, y=310)

    
   def destroy():
       global img_label
       e1.delete(0,END)
       e2.delete(0,END)
       e3.delete(0,END)
       e4.delete(0,END)
       e5.delete(0,END)
       e6.delete(0,END)
       img_label.destroy()


   search_bt = Button(wr, text = "Search", command= _search_).place(x = 200 , y = 290)
   reset_bt = Button(wr, text = "Reset", command= destroy).place(x = 250 , y = 290)       

   save_but = Button(wr, text = "Save",command= save).place(x = 160 , y = 290)
   wr.mainloop()
        
write_bt = Button(root, text= 'Student Profile',command = profile).pack()


''' part 2  fees section'''

def fee():
    fs = Toplevel()
    fs.geometry('800x600')
    fs.title("Fees Report")
# ''' 6 Labels and  enter bars '''
    info_label = Label(fs, text = "INFORMATION").place(x = 5, y =20)     
    lab1 = Label(fs,text = "Recipt No.").place(x = 10 , y =50 )
    lab2 = Label(fs, text = "Enroll No.").place(x = 10 , y =90 )
    lab3 = Label(fs,text = "Branch").place(x = 10 , y = 130)
    lab4 = Label(fs , text = "Semester").place(x = 10 , y = 170)
    lab5 = Label(fs, text = "Total Amount").place(x = 10 , y = 210)
    lab6 = Label(fs, text = "Paid").place(x = 10 , y = 250)
    lab7 = Label(fs,text = "balance").place(x= 10,y=290)    

    e1 = Entry(fs)
    e1.place(x = 150 , y = 50)
    e2 = Entry(fs)
    e2.place(x = 150, y = 90)
    e3 = Entry(fs)
    e3.place(x = 150 , y = 130)
    e4 = Entry(fs)
    e4.place(x = 150 , y = 170)
    e5 = Entry(fs)
    e5.insert(0,"36500")
    e5.place(x = 150 , y = 210)
    e6 = Entry(fs)
    e6.place(x = 150 , y = 250)
    e7 = Entry(fs)
    e7.place(x=150,y=290)

    def receipt():
        to_be_paid = e5.get()
        paid = e6.get()
        bal = int(to_be_paid)-int(paid)
        e7.delete(0,END)
        e7.insert(0,bal)
        cnv = Canvas(fs,bg = 'white',highlightthickness=1,highlightbackground='black' ,width = 400,height=400)
        cnv.place(x=300,y=20)
        
        receipt_lab = Label(cnv,text="Fee Receipt",bg="white",font = 25).place(x=130 , y=20.5)
        date_lab = Label(cnv , text = "Date - "+ str(date.today()),bg="white").place(x=250,y=35)
        lab1 = Label(cnv,text = "Recipt No. : "+e1.get(),font = 22,bg="white").place(x = 90 , y =70 )
        lab2 = Label(cnv, text = "Enroll No. : "+ e2.get(),font = 22,bg="white").place(x = 90 , y =110 )
        lab3 = Label(cnv,text = "Branch : "+ e3.get(),font = 22,bg="white").place(x = 90 , y = 150)
        lab4 = Label(cnv , text = "Paid : "+ e6.get(),font = 22,bg="white").place(x = 90 , y = 190)
        lab5 = Label(cnv,text = "Remaining : "+ e7.get(),font = 22,bg="white").place(x = 90 , y=230)


    def destroy():
        global img_label1
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        #e5.delete(0,END)
        e6.delete(0,END)
        e7.delete(0,END)
        img_label1.destroy()
    
    def save():
        with open("fees.csv",'a') as file_obj:
          lst = []
          lst.append(e1.get().capitalize())
          lst.append(e2.get().capitalize())
          lst.append(e3.get().capitalize())
          lst.append(e4.get().capitalize())
          lst.append(e5.get().capitalize())
          lst.append(e6.get().capitalize())
          lst.append(e7.get().capitalize())
          
          write_obj = csv.writer(file_obj)

          write_obj.writerow(lst)

    receipt_bt = Button(fs, text = "Receipt", width = 15,command= receipt).place(x = 200 , y = 430)
    reset_bt = Button(fs, text = "Reset",width = 15, command= destroy).place(x = 300 , y = 430)       
    save_but = Button(fs, text = "Save",width = 15,command= save).place(x = 400 , y = 430)

fees_bt = Button(root, text= 'Fees Report',command = fee).pack()

'''part 3 marksheet '''

def marksheet():
    mk = Toplevel()
    mk.geometry('700x500')
    mk.title("Marksheet")
    
    

    roll_lab = Label(mk,font = 20 ,text = "Enter roll number").place(x= 20 , y=50)
    rn = Entry(mk)
    rn.place(x= 160, y = 50 )
    
    def result():
        global img_label
        df = pd.read_csv("result.csv")
        roll_NO = rn.get()
        roll_NO = roll_NO
        print(roll_NO)
        
        # if df['Roll no.'] == roll_NO:
        #     success = Label(mk,text = 'sucass').place(x = 550, y = 400)
        # else:
        #    not_found = Label(mk,text='Not Found').place(x =550,y=400)   

        temp_df = df[ df['RollNo.'] == int(roll_NO)]

        dfi.export(temp_df, 'result.png')
        pic = ImageTk.PhotoImage(Image.open('result.png').resize((500,50)))
        img_label = Label(mk, image = pic)
        img_label.place(x =10, y=120)

    def new_result():
        info_label = Label(mk, text = "---MARKS----------------------------------------------------------------------",font =20).place(x = 5, y =180)     
        lab1 = Label(mk,text = "Mathematics",font =20).place(x = 30 , y =220 )
        lab2 = Label(mk, text = "MEFA",font =20).place(x = 30 , y =260 )
        lab3 = Label(mk,text = "DSA",font =20).place(x = 30 , y = 300)
        lab4 = Label(mk , text = "OOPS",font =20).place(x = 30 , y = 340)
        lab5 = Label(mk, text = "SE",font =20).place(x = 30 , y = 370)
        lab6 = Label(mk, text = "Grand Total",font =20).place(x = 210 , y = 220)
        lab7 = Label(mk,text = "Percentage",font =20).place(x= 210,y=250)
        lab8 = Label(mk,text= 'State',font = 20).place(x=210 , y = 280 ) 
        
        e1 = Entry(mk,width = 5)
        e1.place(x = 140 , y = 220)
        e2 = Entry(mk,width = 5)
        e2.place(x = 140, y = 260)
        e3 = Entry(mk,width = 5)
        e3.place(x = 140 , y = 300)
        e4 = Entry(mk,width = 5)
        e4.place(x = 140 , y = 340)
        e5 = Entry(mk,width = 5)
        e5.place(x = 140 , y = 370)
        e6 = Entry(mk,width = 5)
        e6.place(x = 320 , y = 220)
        e7 = Entry(mk,width = 5)
        e7.place(x=320,y=250)
        e8 = Entry(mk,width = 5)
        e8.place(x=320,y= 280)
        
        def upload():
            with open("result.csv",'a') as file_obj:
                lst = []
                lst.append(rn.get())
                lst.append(e1.get())
                lst.append(e2.get())
                lst.append(e3.get())
                lst.append(e4.get())
                lst.append(e5.get())
                lst.append(e6.get())
                lst.append(e7.get())
                lst.append(e8.get())
          
                write_obj = csv.writer(file_obj)

                write_obj.writerow(lst)

        def evaluate():
            a=float(e1.get())
            b=float(e2.get())
            c=float(e3.get())
            d=float(e4.get())
            e=float(e5.get())
            if a > 33.0 and b>33.0 and c>33.0 and d>33.0 and e>33.0:
                sum =  a+ b +c  +d +e 
                e6.insert(0,sum)
                percentage = (sum/500)*100
                e7.insert(0,str(percentage) + '%' )
                e8.insert(0,'PASS')       

            
            else:
                e8.insert(0,"FAIL")
                
        evaluate_bt = Button(mk, font = 5,text ='Evaluate', command= evaluate).place(x=340,y=420)
        save_bt = Button(mk, font = 5,text ='Upload',command = upload).place(x=420,y=420)

    find_bt = Button(mk, font = 7, text= 'Find',command = result).place(x = 70, y = 80)
    create_one = Button(mk, font=7 ,text= 'Create One',command = new_result).place(x=150,y=80)

marksheet_bt = Button(root, text = "Marksheet",command = marksheet).pack()


root.mainloop()