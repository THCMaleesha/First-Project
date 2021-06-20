from tkinter import *                                                                                                   #import tkinter module for create the GUIs
from tkinter import messagebox                                                                                          #import messagebox for display messageboxes in tne python application
from functools import partial                                                                                           #import partial for pass arguments to command in tkinter button
import pyodbc                                                                                                           #import pyodbc module to connect python application with ACCESS database

connection = pyodbc.connect(
    r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};'                                                               #Connect the Access Database with python program
    r'DBQ=C:\SCHOOL MANAGEMENT SYSTEM\System.accdb;'
)
cursor = connection.cursor()


def homepage():                                                                                                         #create the homepage window in a function
    home_page = Tk()                                                                                                    #calling the widget toolkit for homepage
    home_page.geometry("650x600")                                                                                       #set the size of the home page window
    home_page.title("DCC SCHOOL MANAGEMENT SYSTEM")                                                                     #set the titlte of the homepage
    image_name = PhotoImage(file="C:\\SCHOOL MANAGEMENT SYSTEM\\background.png")                                        #set a image as the backgrond of the homepage
    home_page_label = Label(home_page, image=image_name)
    home_page_label.place(x=0, y=0, relwidth=1, relheight=1)                                                            #set the place and size og the background image

    def student():
        student_page = Tk()                                                                                             #create a function for homepage student button and set its size title etc.
        student_page.geometry("700x600")
        student_page.title("DCC SCHOOL MANAGEMENT SYSTEM")
        student_page.configure(bg="light blue")

        student_index = StringVar()                                                                                     #convert into a string variable

        def view(student_index):                                                                                        # function for view the user searched student's details
            index_check = student_page.getvar(name=str(student_index))                                                  #get the student_index variable value into index_check variable
            with connection:
                x = cursor.execute("SELECT * FROM students WHERE ID ="+index_check).fetchone()                          #SELECT ALL DETAILS OF THE USER SEACHED STUDENT'S AND ASSIGN THEM INTO VARIABLE x
                y = x   # x is a tupple since x assign to y for separate its items
                my_list = []
                for items in y:
                    my_list.append(items)                                                                               # insert y's items into my_list
            Label(student_page, text=my_list[1],width = 25).place(x=210, y=270)                                         #print the list items by using their indexes
            Label(student_page, text=my_list[3],width = 25).place(x=210, y=310)
            Label(student_page, text=my_list[4],width = 25).place(x=210, y=350)
            Label(student_page, text=my_list[5],width = 25).place(x=210, y=390)
            Label(student_page, text=my_list[6],width = 25).place(x=210, y=430)
            Label(student_page, text=my_list[7],width = 25).place(x=210, y=470)

        def remove():
            student_page.destroy()
            student()                                                                                                   # refresh the  for a new search

        def all():
            all = Tk()                                                                                                  # create a window and set its configures for display all students in this school
            all.geometry('1300x500')
            all.title("DCC SCHOOL MANAGEMENT SYSTEM")
            all.configure(bg="light blue")

            Label(all, text="ALL STUDENTS DETAIL SHEET",width = 174).place(x=50, y=50)                                  #lable for heading
            Label(all, text="INDEX",width = 10).place(x=50, y=100)                                                      #lables for show the headings of the details
            Label(all, text="NAME",width = 25).place(x=150, y=100)
            Label(all, text="GRADE",width = 10).place(x=350, y=100)
            Label(all, text="BIRTH DAY",width = 20).place(x=450, y=100)
            Label(all, text="HOME TOWN",width = 20).place(x=620, y=100)
            Label(all, text="SEX",width = 10).place(x=790, y=100)
            Label(all, text="NAME OF THE GARDIAN",width = 25).place(x=890, y=100)
            Label(all, text="TELEPHONE NUMBER",width = 25).place(x=1095, y=100)

            with connection:
                cursor.execute("SELECT * FROM students")                                                                #select all students in the database,here we donot want to append datarows into a list because we use a full row for a one student details
                y = 150                                                                                                 #use a increasing y valuse for lable positions
                for row in cursor.fetchall():                                                                           #loop gets the row and prints its indexed items
                    Label(all, text=row[0],width = 10).place(x=50, y=y)
                    Label(all, text=row[1],width = 25).place(x=150, y=y)
                    Label(all, text=row[2],width = 10).place(x=350, y=y)
                    Label(all, text=row[3],width = 20).place(x=450, y=y)
                    Label(all, text=row[4],width = 20).place(x=620, y=y)
                    Label(all, text=row[5],width = 10).place(x=790, y=y)
                    Label(all, text=row[6],width = 25).place(x=890, y=y)
                    Label(all, text=row[7],width = 25).place(x=1095, y=y)
                    y += 40

        def grade1():
            grade1 = Tk()                                                                                               # create a window and set its configures for display grade 1 students in this school
            grade1.geometry('1300x500')
            grade1.title("DCC SCHOOL MANAGEMENT SYSTEM")
            grade1.configure(bg = "light blue")

            Label(grade1, text="GRADE 1 STUDENTS DETAIL SHEET", width=174).place(x=50, y=50)                            #lable for heading
            Label(grade1, text="INDEX", width=10).place(x=50, y=100)                                                    #lables for show the headings of the details
            Label(grade1, text="NAME", width=25).place(x=150, y=100)
            Label(grade1, text="GRADE", width=10).place(x=350, y=100)
            Label(grade1, text="BIRTH DAY", width=20).place(x=450, y=100)
            Label(grade1, text="HOME TOWN", width=20).place(x=620, y=100)
            Label(grade1, text="SEX", width=10).place(x=790, y=100)
            Label(grade1, text="NAME OF THE GARDIAN", width=25).place(x=890, y=100)
            Label(grade1, text="TELEPHONE NUMBER", width=25).place(x=1095, y=100)

            with connection:
                cursor.execute("SELECT * FROM students WHERE GRADE = '1' ")                                             #select grade 1 students in the database,here we donot want to append datarows into a list because we use a full row for a one student details
                y = 150                                                                                                 #use a increasing y valuse for lable positions
                for row in cursor.fetchall():                                                                           #loop gets the row and prints its indexed items
                    Label(grade1, text=row[0], width=10).place(x=50, y=y)
                    Label(grade1, text=row[1], width=25).place(x=150, y=y)
                    Label(grade1, text=row[2], width=10).place(x=350, y=y)
                    Label(grade1, text=row[3], width=20).place(x=450, y=y)
                    Label(grade1, text=row[4], width=20).place(x=620, y=y)
                    Label(grade1, text=row[5], width=10).place(x=790, y=y)
                    Label(grade1, text=row[6], width=25).place(x=890, y=y)
                    Label(grade1, text=row[7], width=25).place(x=1095, y=y)
                    y += 40

        def grade2():
            grade2 = Tk()                                                                                               # create a window and set its configures for display grade 2 students in this school
            grade2.geometry('1300x500')
            grade2.title("DCC SCHOOL MANAGEMENT SYSTEM")
            grade2.configure(bg="light blue")

            Label(grade2, text="GRADE 2 STUDENTS DETAIL SHEET", width=174).place(x=50, y=50)                            #lable for heading
            Label(grade2, text="INDEX", width=10).place(x=50, y=100)
            Label(grade2, text="NAME", width=25).place(x=150, y=100)
            Label(grade2, text="GRADE", width=10).place(x=350, y=100)
            Label(grade2, text="BIRTH DAY", width=20).place(x=450, y=100)
            Label(grade2, text="HOME TOWN", width=20).place(x=620, y=100)
            Label(grade2, text="SEX", width=10).place(x=790, y=100)
            Label(grade2, text="NAME OF THE GARDIAN", width=25).place(x=890, y=100)
            Label(grade2, text="TELEPHONE NUMBER", width=25).place(x=1095, y=100)

            with connection:
                cursor.execute("SELECT * FROM students WHERE GRADE = '2' ")                                             #select grade 2 students in the database,here we donot want to append datarows into a list because we use a full row for a one student details
                y = 150                                                                                                 #use a increasing y valuse for lable positions
                for row in cursor.fetchall():                                                                           #loop prints the details
                    Label(grade2, text=row[0], width=10).place(x=50, y=y)
                    Label(grade2, text=row[1], width=25).place(x=150, y=y)
                    Label(grade2, text=row[2], width=10).place(x=350, y=y)
                    Label(grade2, text=row[3], width=20).place(x=450, y=y)
                    Label(grade2, text=row[4], width=20).place(x=620, y=y)
                    Label(grade2, text=row[5], width=10).place(x=790, y=y)
                    Label(grade2, text=row[6], width=25).place(x=890, y=y)
                    Label(grade2, text=row[7], width=25).place(x=1095, y=y)
                    y += 40

        def grade3():
            grade3 = Tk()                                                                                               # create a window and set its configures for display grade 3 students in this school
            grade3.geometry('1300x500')
            grade3.title("DCC SCHOOL MANAGEMENT SYSTEM")
            grade3.configure(bg = "light blue")

            Label(grade3, text="GRADE 3 STUDENTS DETAIL SHEET", width=174).place(x=50, y=50)
            Label(grade3, text="INDEX", width=10).place(x=50, y=100)
            Label(grade3, text="NAME", width=25).place(x=150, y=100)
            Label(grade3, text="GRADE", width=10).place(x=350, y=100)
            Label(grade3, text="BIRTH DAY", width=20).place(x=450, y=100)
            Label(grade3, text="HOME TOWN", width=20).place(x=620, y=100)
            Label(grade3, text="SEX", width=10).place(x=790, y=100)
            Label(grade3, text="NAME OF THE GARDIAN", width=25).place(x=890, y=100)
            Label(grade3, text="TELEPHONE NUMBER", width=25).place(x=1095, y=100)

            with connection:
                cursor.execute("SELECT * FROM students WHERE GRADE = '3' ")
                y = 150
                for row in cursor.fetchall():   #loop print the data
                    Label(grade3, text=row[0], width=10).place(x=50, y=y)
                    Label(grade3, text=row[1], width=25).place(x=150, y=y)
                    Label(grade3, text=row[2], width=10).place(x=350, y=y)
                    Label(grade3, text=row[3], width=20).place(x=450, y=y)
                    Label(grade3, text=row[4], width=20).place(x=620, y=y)
                    Label(grade3, text=row[5], width=10).place(x=790, y=y)
                    Label(grade3, text=row[6], width=25).place(x=890, y=y)
                    Label(grade3, text=row[7], width=25).place(x=1095, y=y)
                    y += 40

        def grade4():
            grade4 = Tk()
            grade4.geometry('1300x500')
            grade4.title("DCC SCHOOL MANAGEMENT SYSTEM")
            grade4.configure(bg="light blue")

            Label(grade4, text="GRADE 4 STUDENTS DETAIL SHEET", width=174).place(x=50, y=50)
            Label(grade4, text="INDEX", width=10).place(x=50, y=100)
            Label(grade4, text="NAME", width=25).place(x=150, y=100)
            Label(grade4, text="GRADE", width=10).place(x=350, y=100)
            Label(grade4, text="BIRTH DAY", width=20).place(x=450, y=100)
            Label(grade4, text="HOME TOWN", width=20).place(x=620, y=100)
            Label(grade4, text="SEX", width=10).place(x=790, y=100)
            Label(grade4, text="NAME OF THE GARDIAN", width=25).place(x=890, y=100)
            Label(grade4, text="TELEPHONE NUMBER", width=25).place(x=1095, y=100)

            with connection:
                cursor.execute("SELECT * FROM students WHERE GRADE = '4' ")
                y = 150
                for row in cursor.fetchall():
                    Label(grade4, text=row[0], width=10).place(x=50, y=y)
                    Label(grade4, text=row[1], width=25).place(x=150, y=y)
                    Label(grade4, text=row[2], width=10).place(x=350, y=y)
                    Label(grade4, text=row[3], width=20).place(x=450, y=y)
                    Label(grade4, text=row[4], width=20).place(x=620, y=y)
                    Label(grade4, text=row[5], width=10).place(x=790, y=y)
                    Label(grade4, text=row[6], width=25).place(x=890, y=y)
                    Label(grade4, text=row[7], width=25).place(x=1095, y=y)
                    y += 40

        def grade5():
            grade5 = Tk()
            grade5.geometry('1100x1000')
            grade5.title("DCC SCHOOL MANAGEMENT SYSTEM")
            grade5.configure(bg="light blue")

            Label(grade5, text="GRADE 5 STUDENTS DETAIL SHEET", width=174).place(x=50, y=50)
            Label(grade5, text="INDEX", width=10).place(x=50, y=100)
            Label(grade5, text="NAME", width=25).place(x=150, y=100)
            Label(grade5, text="GRADE", width=10).place(x=350, y=100)
            Label(grade5, text="BIRTH DAY", width=20).place(x=450, y=100)
            Label(grade5, text="HOME TOWN", width=20).place(x=620, y=100)
            Label(grade5, text="SEX", width=10).place(x=790, y=100)
            Label(grade5, text="NAME OF THE GARDIAN", width=25).place(x=890, y=100)
            Label(grade5, text="TELEPHONE NUMBER", width=25).place(x=1095, y=100)

            with connection:
                cursor.execute("SELECT * FROM students WHERE GRADE = '5' ")
                y = 150
                for row in cursor.fetchall():
                    Label(grade5, text=row[0], width=10).place(x=50, y=y)
                    Label(grade5, text=row[1], width=25).place(x=150, y=y)
                    Label(grade5, text=row[2], width=10).place(x=350, y=y)
                    Label(grade5, text=row[3], width=20).place(x=450, y=y)
                    Label(grade5, text=row[4], width=20).place(x=620, y=y)
                    Label(grade5, text=row[5], width=10).place(x=790, y=y)
                    Label(grade5, text=row[6], width=25).place(x=890, y=y)
                    Label(grade5, text=row[7], width=25).place(x=1095, y=y)
                    y += 40

        Label(student_page, text="STUDENT MANAGEMENT UNIT", anchor=CENTER).place(x=250, y=20)                           #heading of the window

        Label(student_page, text="GRADE 1\t\t\t:", width=20).place(x=420, y=90)                                         #lable for view all grade one students
        Button(student_page, width=4, text="VIEW", activebackground="light blue", command=grade1).place(x=585, y=90)    #button for show all details of the grade 1 students

        Label(student_page, text="GRADE 2\t\t\t:", width=20).place(x=420, y=140)                                        #lable for view all grade 2 students
        Button(student_page, width=4, text="VIEW", activebackground="light blue", command=grade2).place(x=585, y=140)   #button for show all details of the grade 2 students

        Label(student_page, text="GRADE 3\t\t\t:", width=20).place(x=420, y=190)                                        #lable for view all grade 3 students
        Button(student_page, width=4, text="VIEW", activebackground="light blue", command=grade3).place(x=585, y=190)   #button for show all details of the grade 3 students

        Label(student_page, text="GRADE 4\t\t\t:", width=20).place(x=420, y=240)                                        #lable for view all grade 4 students
        Button(student_page, width=4, text="VIEW", activebackground="light blue", command=grade4).place(x=585, y=240)   #button for show all details of the grade 4 students

        Label(student_page, text="GRADE 5\t\t\t:", width=20).place(x=420, y=290)                                        #lable for view all grade 5 students
        Button(student_page, width=4, text="VIEW", activebackground="light blue", command=grade5).place(x=585, y=290)   #button for show all details of the grade 5 students

        Label(student_page, text="ALL\t\t\t:", width=20).place(x=420, y=340)                                            #lable for view all grade all students
        Button(student_page, width=4, text="VIEW", activebackground="light blue", command=all).place(x=585,y=340)       #button for show all details of the all students

        Label(student_page, text="SEARCH\t\t", width=20).place(x=90, y=90)                                              # label for search a student details

        Label(student_page, text="INDEX\t:").place(x=130, y=130)                                                        #label for enter student index
        Entry(student_page, width=20,textvariable=student_index).place(x=200, y=130)                                    #get the user input into student_index variable for search the deatails of entered indexed student

        Button(student_page, text="VIEW", activebackground="light blue", width=16, command=partial(view,student_index)).place(x=200,y=180)  #button for show details of that searched student

        Label(student_page, text="NAME\t\t:", width=15).place(x=90, y=270)                                              #labels for display name, birthday, home town,sex,gardian,telephone number
        Label(student_page, text="BIRTH DAY\t:", width=15).place(x=90, y=310)
        Label(student_page, text="HOME TOWN\t:", width=15).place(x=90, y=350)
        Label(student_page, text="SEX\t\t:", width=15).place(x=90, y=390)
        Label(student_page, text="GARDIAN\t:", width=15).place(x=90, y=430)
        Label(student_page, text="TP NO.\t\t:", width=15).place(x=90, y=470)

        Button(student_page, text="REFRESH", activebackground="light blue", width=16, command=remove).place(x=200, y=525)   #button for refresh the page for search new index

        Button(student_page, text="BACK", width=10, height=2, activebackground="light blue",command = student_page.destroy).place(x=450,y=525) # button for back to home page
        Button(student_page, text="EXIT", width=10, height=2, activebackground="light blue",command=home_page.destroy).place(x=560, y=525)  #button for exit from the system

        student_page.mainloop()


    def teachers():

        def principal():                                                                                                #function for show details about the principal
            with connection:                                                                                            #get the details of the principal for variable "x",
                x = cursor.execute("SELECT * FROM teachers WHERE ID = 1").fetchall()
                y = (x[0])                                                                                              #since x is a tupple it insert into a list for use by using a for loop,it gives the tupple's 0 index's items one by one into y=the list
                my_list = []
                for items in y:
                    my_list.append(items)
            Label(teacher_page, text=my_list[1],width = 35).place(x=420, y=90)                                          #lables for show principal's details
            Label(teacher_page, text=my_list[2],width = 35).place(x=420, y=130)
            Label(teacher_page, text=my_list[3],width = 35).place(x=420, y=170)
            Label(teacher_page, text=my_list[4],width = 35).place(x=420, y=210)

        def dep_principal():                                                                                            #function for show details about the deputy principal
            with connection:
                x = cursor.execute("SELECT * FROM teachers WHERE ID = 2").fetchall()                                    #get the details of the principal for variable "x",
                y = (x[0])
                my_list = []
                for items in y:                                                                                         #since x is a tupple it insert into a list for use by using a for loop,it gives the tupple's 0 index's items one by one into y=the list
                    my_list.append(items)
            Label(teacher_page, text=my_list[1],width = 35).place(x=420, y=90)
            Label(teacher_page, text=my_list[2],width = 35).place(x=420, y=130)
            Label(teacher_page, text=my_list[3],width = 35).place(x=420, y=170)
            Label(teacher_page, text=my_list[4],width = 35).place(x=420, y=210)

        def grade1_tea():
            with connection:
                x = cursor.execute("SELECT * FROM teachers WHERE ID = 3").fetchall()
                y = (x[0])
                my_list = []
                for items in y:
                    my_list.append(items)
            Label(teacher_page, text=my_list[1],width = 35).place(x=420, y=90)
            Label(teacher_page, text=my_list[2],width = 35).place(x=420, y=130)
            Label(teacher_page, text=my_list[3],width = 35).place(x=420, y=170)
            Label(teacher_page, text=my_list[4],width = 35).place(x=420, y=210)

        def grade2_tea():
            with connection:
                x = cursor.execute("SELECT * FROM teachers WHERE ID = 4").fetchall()
                y = (x[0])
                my_list = []
                for items in y:
                    my_list.append(items)
            Label(teacher_page, text=my_list[1],width = 35).place(x=420, y=90)
            Label(teacher_page, text=my_list[2],width = 35).place(x=420, y=130)
            Label(teacher_page, text=my_list[3],width = 35).place(x=420, y=170)
            Label(teacher_page, text=my_list[4],width = 35).place(x=420, y=210)

        def grade3_tea():
            with connection:
                x = cursor.execute("SELECT * FROM teachers WHERE ID = 5").fetchall()
                y = (x[0])
                my_list = []
                for items in y:
                    my_list.append(items)
            Label(teacher_page, text=my_list[1],width = 35).place(x=420, y=90)
            Label(teacher_page, text=my_list[2],width = 35).place(x=420, y=130)
            Label(teacher_page, text=my_list[3],width = 35).place(x=420, y=170)
            Label(teacher_page, text=my_list[4],width = 35).place(x=420, y=210)

        def grade4_tea():
            with connection:
                x = cursor.execute("SELECT * FROM teachers WHERE ID = 6").fetchall()
                y = (x[0])
                my_list = []
                for items in y:
                    my_list.append(items)
            Label(teacher_page, text=my_list[1],width = 35).place(x=420, y=90)
            Label(teacher_page, text=my_list[2],width = 35).place(x=420, y=130)
            Label(teacher_page, text=my_list[3],width = 35).place(x=420, y=170)
            Label(teacher_page, text=my_list[4],width = 35).place(x=420, y=210)

        def grade5_tea():
            with connection:
                x = cursor.execute("SELECT * FROM teachers WHERE ID = 7").fetchall()
                y = (x[0])
                my_list = []
                for items in y:
                    my_list.append(items)
            Label(teacher_page, text=my_list[1],width = 35).place(x=420, y=90)
            Label(teacher_page, text=my_list[2],width = 35).place(x=420, y=130)
            Label(teacher_page, text=my_list[3],width = 35).place(x=420, y=170)
            Label(teacher_page, text=my_list[4],width = 35).place(x=420, y=210)

        def allteachers():                                                                                              #create a function for show all teachers details
            all_tea = Tk()                                                                                              #create the window and set its configurations
            all_tea.geometry('850x900')
            all_tea.title("DCC SCHOOL MANAGEMENT SYSTEM")
            all_tea.configure(bg="light blue")

            Label(all_tea, text="ALL TEACHERS DETAIL SHEET").place(x=400, y=50)                                         #labels for show heading row of the details
            Label(all_tea, text="ID",width = 3).place(x=75, y=100)
            Label(all_tea, text="NAME",width = 20).place(x=120, y=100)
            Label(all_tea, text="WORK AS",width = 20).place(x=300, y=100)
            Label(all_tea, text="HOME TOWN",width = 20).place(x=475, y=100)
            Label(all_tea, text="TELEPHONE NUMBER",width = 20).place(x=650, y=100)

            with connection:
                cursor.execute("SELECT * FROM teachers")                                                                #get the details of the all teachers
                y = 150                                                                                                 #create a increasing valued vatiable called y for print te details
                for row in cursor.fetchall():                                                                           #print details by using there indexes
                    Label(all_tea, text=row[0],width = 3).place(x=75, y=y)
                    Label(all_tea, text=row[1],width = 20).place(x=120, y=y)
                    Label(all_tea, text=row[2],width = 20).place(x=300, y=y)
                    Label(all_tea, text=row[3],width = 20).place(x=475, y=y)
                    Label(all_tea, text=row[4],width = 20).place(x=650, y=y)
                    y += 40

            all_tea.mainloop()

        def remove():
                teacher_page.destroy()                                                                                  #function for refresh the window for a new viewing
                teachers()

        def enter(enter_name,enter_workas,enter_home,enter_tele,enter_email):                                                       #function for enter a new teacher details into the system

                te_name = teacher_page.getvar(name=str(enter_name))                                                     #get the values of the textvariables into new variables
                te_work = teacher_page.getvar(name=str(enter_workas))
                te_home = teacher_page.getvar(name=str(enter_home))
                te_tele = teacher_page.getvar(name=str(enter_tele))
                te_email = teacher_page.getvar(name=str(enter_email))

                sql_admission = "INSERT INTO teachers (NAME,`WORK AS`,`HOME TOWN`,`TELEPHONE NUMBER`,`email`) VALUES('" + te_name + "','" + te_work + "','" + te_home + "','" + te_tele + "','" + te_email + "')" #create a variable fro inserting details into data feilds

                with connection:
                    cursor.execute(sql_admission)                                                                       #by using above created variable insert the user entereds details into the database
                    cursor.commit()
                messagebox.showinfo("SUCCESSFUL", "THE TEACHER HAS ENTERED INTO DCC SCHOOL MANAGEMENT SYSTEM !!!")      #after entering show a message

        teacher_page = Tk()                                                                                             #cterate the teacher page window and set its configurations
        teacher_page.geometry("700x600")
        teacher_page.title("DCC SCHOOL MANAGEMENT SYSTEM")
        teacher_page.configure(bg="light blue")

        Label(teacher_page, text="TEACHERS MANAGEMENT UNIT", anchor=CENTER).place(x=250, y=20)                          #label for heading of the page

        Button(teacher_page, text="PRINCIPAL", width=20, activebackground="light blue",                                 #button for call details of the teachers,their commands matched with above created functions
                                  command=principal).place(x=90, y=90)
        Button(teacher_page, text="DEPUTY PRINCIPAL", width=20, activebackground="light blue",
                                         command=dep_principal).place(x=90, y=140)
        Button(teacher_page, text="GRADE 1 TEACHER", width=20, activebackground="light blue",
                                        command=grade1_tea).place(x=90, y=190)
        Button(teacher_page, text="GRADE 2 TEACHER", width=20, activebackground="light blue",
                                        command=grade2_tea).place(x=90, y=240)
        Button(teacher_page, text="GRADE 3 TEACHER", width=20, activebackground="light blue",
                                        command=grade3_tea).place(x=90, y=290)
        Button(teacher_page, text="GRADE 4 TEACHER", width=20, activebackground="light blue",
                                        command=grade4_tea).place(x=90, y=340)
        Button(teacher_page, text="GRADE 5 TEACHER", width=20, activebackground="light blue",
                                        command=grade5_tea).place(x=90, y=390)
        Button(teacher_page, text="ALL TEACHERS", width=20, activebackground="light blue",
                                    command=allteachers).place(x=90, y=440)


        Label(teacher_page, text="NAME\t\t:", width=15).place(x=300, y=90)                                              #labels for name the showing details
        Label(teacher_page, text="WORK AS\t:", width=15).place(x=300, y=130)
        Label(teacher_page, text="HOME TOWN\t:", width=15).place(x=300, y=170)
        Label(teacher_page, text="TP NO.\t\t:", width=15).place(x=300, y=210)

        Button(teacher_page, text="REFRESH", activebackground="light blue", width=20, height=1,                         #BUTTON FOR REFRESH THE WINDOW
                               command=remove).place(x=450, y=250)
        name = StringVar()                                                                                              #set the textvariable values as StrinVar values
        workas = StringVar()
        home = StringVar()
        tele = StringVar()
        email = StringVar()

        Label(teacher_page, text="NAME\t\t:", width=15).place(x=300, y=300)                                             #labels for name the entry widget and entry widget to enter the details
        Entry(teacher_page, width=35, textvariable=name).place(x=430, y=300)

        Label(teacher_page, text="WORK AS\t:", width=15).place(x=300, y=340)
        Entry(teacher_page, width=35, textvariable=workas).place(x=430, y=340)

        Label(teacher_page, text="HOME TOWN\t:", width=15).place(x=300, y=380)
        Entry(teacher_page, width=35, textvariable=home).place(x=430, y=380)

        Label(teacher_page, text="TP NO.\t\t:", width=15).place(x=300, y=420)
        Entry(teacher_page, width=35, textvariable=tele).place(x=430, y=420)

        Label(teacher_page, text = "email address\t:",width = 15).place(x=300,y=460)
        Entry(teacher_page, textvariable = email,width = 35).place(x=430,y=460)


        Button(teacher_page, text="ENTER", activebackground="light blue", width=20, height=1,command=partial(enter,name,workas,home,tele,email)).place(x=450, y=500)              #button for enter details into database

        Button(teacher_page, text="BACK", width=10, height=2, activebackground="light blue",command=teacher_page.destroy).place(x=500,                                      #button for back to home page
                                                                 y=525)
        Button(teacher_page, text="EXIT", width=10, height=2, activebackground="light blue",command=home_page.destroy).place(x=560, y=525)                                  #button for exit from the system

        teacher_page.mainloop()


    def academic():                                                                                                     #FUNCTION FOR ACADEMIC BUTTON

        def view(index):                                                                                                #function for view academic details of entered index
            index_check = accedemic_page.getvar(name=str(index))                                                        #get the entered index and grade of the student into variables
            grade_check = accedemic_page.getvar(name=str(grade))

            with connection:
                x = cursor.execute("SELECT * FROM summary WHERE ID =" + index_check).fetchone()                         #get the details of entered indexed student and append it into a list by using a for loop
                y = x
                my_list = []
                for items in y:
                    my_list.append(items)

                if grade_check == "1" or grade_check == "2":                                                            #check the entered grade and display the subject details,total and average
                    Label(accedemic_page, text=my_list[1],width = 25).place(x=250, y=180)
                    Label(accedemic_page, text=my_list[3],width = 25).place(x=250, y=210)
                    Label(accedemic_page, text="None",width = 25).place(x=250, y=240)
                    Label(accedemic_page, text=my_list[5],width = 25).place(x=250, y=270)
                    Label(accedemic_page, text="None",width = 25).place(x=250, y=300)
                    total = my_list[3] + my_list[5]                                                                     #calculate the total of the marks by using list items
                    Label(accedemic_page, text=total,width = 25).place(x=250, y=330)
                    average = total / 2                                                                                 #calculate the average by using total
                    Label(accedemic_page, text=average,width = 25).place(x=250, y=360)
                    if average > 50:                                                                                    #deside the status on the average of that student
                        status = "PASS"
                    else:
                        status = "FAIL"
                    Label(accedemic_page, text=status,width = 25).place(x=250, y=390)
                else:
                    Label(accedemic_page, text=my_list[1],width = 25).place(x=250, y=180)
                    Label(accedemic_page, text=my_list[3],width = 25).place(x=250, y=210)
                    Label(accedemic_page, text=my_list[4],width = 25).place(x=250, y=240)
                    Label(accedemic_page, text=my_list[5],width = 25).place(x=250, y=270)
                    Label(accedemic_page, text=my_list[6],width = 25).place(x=250, y=300)
                    total = my_list[3] + my_list[4] + my_list[5] + my_list[5]
                    Label(accedemic_page, text=total,width = 25).place(x=250, y=330)
                    average = total / 4
                    Label(accedemic_page, text=average,width = 25).place(x=250, y=360)
                    if average > 70:
                        status = "A"
                    elif average >= 50:
                        status = "B"
                    elif average >= 30:
                        status = "S"
                    else:
                        status = "FAIL"
                    Label(accedemic_page, text=status,width = 25).place(x=250, y=390)

        def remove():
            accedemic_page.destroy()        #refresh the window to search a new index academic details
            academic()

        def grade1():                                                                                                   #create a function for showing grade 1 students academic details
            grade1 = Tk()                                                                                               #create the window and its configurations
            grade1.geometry('850x1000')
            grade1.title("DCC SCHOOL MANAGEMENT SYSTEM")
            grade1.configure(bg="light blue")


            Label(grade1, text="GRADE 1 STUDENTS ACADEMIC DETAILS SHEET",width = 104).place(x=50, y=30)                 #lables for display main heading and other headings of the details
            Label(grade1, text="INDEX",width = 10).place(x=50, y=100)
            Label(grade1, text="NAME",width = 20).place(x=150, y=100)
            Label(grade1, text="SINHALA",width = 10).place(x=330, y=100)
            Label(grade1, text="BUDDHISM",width = 10).place(x=420, y=100)
            Label(grade1, text="TOTAL",width = 10).place(x=510, y=100)
            Label(grade1, text="AVERAGE",width = 10).place(x=610, y=100)
            Label(grade1, text="STATUS",width = 10).place(x=710, y=100)

            with connection:                                                                                            #select data from the summary query and dispay them by using a for loop and value increasing variable that called y for place them
                cursor.execute("SELECT * FROM summary WHERE GRADE = '1' ")
                y = 150
                for row in cursor.fetchall():
                    Label(grade1, text=row[0],width = 10).place(x=50, y=y)
                    Label(grade1, text=row[1],width = 20).place(x=150, y=y)
                    Label(grade1, text=row[3],width = 10).place(x=330, y=y)
                    Label(grade1, text=row[5],width = 10).place(x=420, y=y)
                    total = row[3] + row[5]                                                                             #generate the total of the marks and calculate the average and status of the students
                    Label(grade1, text=total,width = 10).place(x=510, y=y)
                    average = total / 2
                    Label(grade1, text=average,width = 10).place(x=610, y=y)
                    if average > 50:
                        status = "PASS"
                    else:
                        status = "FAIL"
                    Label(grade1, text=status,width = 10).place(x=710, y=y)
                    y += 40

        def grade2():
            grade2 = Tk()
            grade2.geometry('850x1000')
            grade2.title("DCC SCHOOL MANAGEMENT SYSTEM")
            grade2.configure(bg="light blue")

            Label(grade2, text="GRADE 2 STUDENTS ACADEMIC DETAILS SHEET", width=104).place(x=50, y=30)
            Label(grade2, text="INDEX", width=10).place(x=50, y=100)
            Label(grade2, text="NAME", width=20).place(x=150, y=100)
            Label(grade2, text="SINHALA", width=10).place(x=330, y=100)
            Label(grade2, text="BUDDHISM", width=10).place(x=420, y=100)
            Label(grade2, text="TOTAL", width=10).place(x=510, y=100)
            Label(grade2, text="AVERAGE", width=10).place(x=610, y=100)
            Label(grade2, text="STATUS", width=10).place(x=710, y=100)

            with connection:
                cursor.execute("SELECT * FROM summary WHERE GRADE = '2' ")
                y = 150
                for row in cursor.fetchall():
                    Label(grade2, text=row[0], width=10).place(x=50, y=y)
                    Label(grade2, text=row[1], width=20).place(x=150, y=y)
                    Label(grade2, text=row[3], width=10).place(x=330, y=y)
                    Label(grade2, text=row[5], width=10).place(x=420, y=y)
                    total = row[3] + row[5]
                    Label(grade2, text=total, width=10).place(x=510, y=y)
                    average = total / 2
                    Label(grade2, text=average, width=10).place(x=610, y=y)
                    if average > 50:
                        status = "PASS"
                    else:
                        status = "FAIL"
                    Label(grade2, text=status, width=10).place(x=710, y=y)
                    y += 40

        def grade3():
            grade3 = Tk()
            grade3.geometry('1050x1000')
            grade3.title("DCC SCHOOL MANAGEMENT SYSTEM")
            grade3.configure(bg="light blue")

            Label(grade3, text="GRADE 3 STUDENTS ACADEMIC DETAILS SHEET", width=135).place(x=50, y=30)
            Label(grade3, text="INDEX", width=10).place(x=50, y=100)
            Label(grade3, text="NAME", width=20).place(x=150, y=100)
            Label(grade3, text="SINHALA", width=10).place(x=330, y=100)
            Label(grade3, text="BUDDHISM", width=10).place(x=420, y=100)
            Label(grade3, text="MATHEMATICS", width=12).place(x=510, y=100)
            Label(grade3, text="ENGLISH", width=10).place(x=620, y=100)
            Label(grade3, text="TOTAL", width=10).place(x=720, y=100)
            Label(grade3, text="AVERAGE", width=10).place(x=820, y=100)
            Label(grade3, text="STATUS", width=10).place(x=920, y=100)

            with connection:
                cursor.execute("SELECT * FROM summary WHERE GRADE = '3' ")
                y = 150
                for row in cursor.fetchall():
                    Label(grade3, text=row[0], width=10).place(x=50, y=y)
                    Label(grade3, text=row[1], width=20).place(x=150, y=y)
                    Label(grade3, text=row[3], width=10).place(x=320, y=y)
                    Label(grade3, text=row[4], width=10).place(x=420, y=y)
                    Label(grade3, text=row[5], width=10).place(x=520, y=y)
                    Label(grade3, text=row[6], width=10).place(x=620, y=y)
                    total = row[3] + row[4] + row[5] + row[6]
                    Label(grade3, text=total, width=10).place(x=720, y=y)
                    average = total / 4
                    Label(grade3, text=average, width=10).place(x=820, y=y)
                    if average > 70:
                        status = "A"
                    elif average >= 50:
                        status = "B"
                    elif average >= 30:
                        status = "S"
                    else:
                        status = "FAIL"
                    Label(grade3, text=status, width=10).place(x=920, y=y)
                    y += 40

        def grade4():
            grade4 = Tk()
            grade4.geometry('1050x1000')
            grade4.title("DCC SCHOOL MANAGEMENT SYSTEM")
            grade4.configure(bg="light blue")

            Label(grade4, text="GRADE 4 STUDENTS ACADEMIC DETAILS SHEET", width=135).place(x=50, y=30)
            Label(grade4, text="INDEX", width=10).place(x=50, y=100)
            Label(grade4, text="NAME", width=20).place(x=150, y=100)
            Label(grade4, text="SINHALA", width=10).place(x=330, y=100)
            Label(grade4, text="BUDDHISM", width=10).place(x=420, y=100)
            Label(grade4, text="MATHEMATICS", width=12).place(x=510, y=100)
            Label(grade4, text="ENGLISH", width=10).place(x=620, y=100)
            Label(grade4, text="TOTAL", width=10).place(x=720, y=100)
            Label(grade4, text="AVERAGE", width=10).place(x=820, y=100)
            Label(grade4, text="STATUS", width=10).place(x=920, y=100)

            with connection:
                    cursor.execute("SELECT * FROM summary WHERE GRADE = '4' ")
                    y = 150
                    for row in cursor.fetchall():
                        Label(grade4, text=row[0], width=10).place(x=50, y=y)
                        Label(grade4, text=row[1], width=20).place(x=150, y=y)
                        Label(grade4, text=row[3], width=10).place(x=320, y=y)
                        Label(grade4, text=row[4], width=10).place(x=420, y=y)
                        Label(grade4, text=row[5], width=10).place(x=520, y=y)
                        Label(grade4, text=row[6], width=10).place(x=620, y=y)
                        total = row[3] + row[4] + row[5] + row[6]
                        Label(grade4, text=total, width=10).place(x=720, y=y)
                        average = total / 4
                        Label(grade4, text=average, width=10).place(x=820, y=y)
                        if average > 70:
                            status = "A"
                        elif average >= 50:
                            status = "B"
                        elif average >= 30:
                            status = "S"
                        else:
                            status = "FAIL"
                        Label(grade4, text=status, width=10).place(x=920, y=y)
                        y += 40

        def grade5():
            grade5 = Tk()
            grade5.geometry('1050x1000')
            grade5.title("DCC SCHOOL MANAGEMENT SYSTEM")
            grade5.configure(bg="light blue")

            Label(grade5, text="GRADE 5 STUDENTS ACADEMIC DETAILS SHEET", width=135).place(x=50, y=30)
            Label(grade5, text="INDEX", width=10).place(x=50, y=100)
            Label(grade5, text="NAME", width=20).place(x=150, y=100)
            Label(grade5, text="SINHALA", width=10).place(x=330, y=100)
            Label(grade5, text="BUDDHISM", width=10).place(x=420, y=100)
            Label(grade5, text="MATHEMATICS", width=12).place(x=510, y=100)
            Label(grade5, text="ENGLISH", width=10).place(x=620, y=100)
            Label(grade5, text="TOTAL", width=10).place(x=720, y=100)
            Label(grade5, text="AVERAGE", width=10).place(x=820, y=100)
            Label(grade5, text="STATUS", width=10).place(x=920, y=100)

            with connection:
                cursor.execute("SELECT * FROM summary WHERE GRADE = '5' ")
                y = 150
                for row in cursor.fetchall():
                    Label(grade5, text=row[0], width=10).place(x=50, y=y)
                    Label(grade5, text=row[1], width=20).place(x=150, y=y)
                    Label(grade5, text=row[3], width=10).place(x=320, y=y)
                    Label(grade5, text=row[4], width=10).place(x=420, y=y)
                    Label(grade5, text=row[5], width=10).place(x=520, y=y)
                    Label(grade5, text=row[6], width=10).place(x=620, y=y)
                    total = row[3] + row[4] + row[5] + row[6]
                    Label(grade5, text=total, width=10).place(x=720, y=y)
                    average = total / 4
                    Label(grade5, text=average, width=10).place(x=820, y=y)
                    if average > 70:
                        status = "A"
                    elif average >= 50:
                        status = "B"
                    elif average >= 30:
                        status = "S"
                    else:
                        status = "FAIL"
                    Label(grade5, text=status, width=10).place(x=920, y=y)
                    y += 40

        def enter():                                                                                                    #function for open a window to enter academic details into database

            marks_entery_page = Tk()                                                                                    #set the entry window and its configurations
            marks_entery_page.geometry("700x550")
            marks_entery_page.title("DCC SCHOOL MANAGEMENT SYSTEM")
            marks_entery_page.configure(bg="light blue")

            index = StringVar()                                                                                         #get the text variables as StringVar
            name = StringVar()
            grade = StringVar()
            sinhala = IntVar()
            buddhism = IntVar()
            maths = IntVar()
            english = IntVar()

            def enter(index,grade,sinhala,buddhism,maths,english):                                                      #function for enter details into database
                index_serch = marks_entery_page.getvar(name=str(index))                                                 #get the entered values into variables
                name_search = marks_entery_page.getvar(name=str(name))
                grade_serch = marks_entery_page.getvar(name=str(grade))
                sin = marks_entery_page.getvar(name=str(sinhala))
                buddhi = marks_entery_page.getvar(name=str(buddhism))
                math = marks_entery_page.getvar(name=str(maths))
                eng = marks_entery_page.getvar(name=str(english))


                with connection:                                                                                        #insert them into database
                    cursor.execute("INSERT INTO marks (NAME,SINHALA,BUDDHISM,MATHS,ENGLISH)WHERE ID = ('"+ index_serch +"') VALUES('" + name_search + "','" + sin + "','" + buddhi + "','" + math + "','" + eng + "')")
                    cursor.commit()
                messagebox.showinfo("SUCCESSFUL", "THE STUDENT MARKS HAS ENTERED IN DCC SCHOOL MANAGEMENT SYSTEM !!!")  #show a message about successful entering


            Label(marks_entery_page, text="ACCEDEMIC MANAGEMENT UNIT", anchor=CENTER).place(x=100, y=20)                #display the heading of the window

            Label(marks_entery_page, text="ENTER INDEX\t\t:", width=20).place(x=100, y=60)                              #DATA ENTRY HEADINGS AND ENTRY WIDGETS

            Entry(marks_entery_page,textvariable =index).place(x=270, y=60)

            Label(marks_entery_page, text="ENTER NAME\t\t:", width=20).place(x=100, y=100)

            Entry(marks_entery_page, textvariable=name).place(x=270, y=100)

            Label(marks_entery_page, text="GRADE\t\t\t:", width=20).place(x=100, y=140)

            Entry(marks_entery_page,textvariable = grade).place(x=270, y=140)

            Label(marks_entery_page, text="SINHALA\t\t:", width=20).place(x=100, y=210)
            Entry(marks_entery_page,textvariable = sinhala).place(x=270, y=210)

            Label(marks_entery_page, text="MATHEMATICS\t\t:", width=20).place(x=100, y=240)
            Entry(marks_entery_page,textvariable = maths).place(x=270, y=240)

            Label(marks_entery_page, text="BUDDHISM\t\t:", width=20).place(x=100, y=270)
            Entry(marks_entery_page,textvariable = buddhism).place(x=270, y=270)

            Label(marks_entery_page, text="ENGLISH\t\t\t:", width=20).place(x=100, y=300)
            Entry(marks_entery_page,textvariable = english).place(x=270, y=300)

            Button(marks_entery_page, text="ENTER MARKS", activebackground="light blue", width=17, height=2,command = partial(enter,index,grade,sinhala,buddhism,maths,english)).place(x=270, y=350)            #button foe open the marks entering page

            Button(marks_entery_page, text="EXIT", width=10, height=2, activebackground="light blue",command=marks_entery_page.destroy).place(x=560, y=485)                                                     #exit button for close the program

            marks_entery_page.mainloop()

        accedemic_page = Tk()                                                                                           #create the academic buton opened window and set its configurations
        accedemic_page.geometry("700x550")
        accedemic_page.title("DCC SCHOOL MANAGEMENT SYSTEM")
        accedemic_page.configure(bg="light blue")

        index = StringVar()                                                                                             #user inputs get as StringVar
        grade = StringVar()

        Label(accedemic_page, text="ACCEDEMIC MANAGEMENT UNIT", anchor=CENTER).place(x=250,y=20)                        #label for display the heading of the window

        Label(accedemic_page, text="ENTER INDEX\t\t:", width=20).place(x=100, y=100)                                    #lables and entry widgets for user inputs
        Entry(accedemic_page, textvariable=index).place(x=270, y=100)

        Label(accedemic_page, text="GRADE\t\t\t:", width=20).place(x=100, y=130)
        Entry(accedemic_page, textvariable=grade).place(x=270, y=130)

        Label(accedemic_page, text="NAME\t\t\t:", width=20).place(x=100, y=180)                                         #lables for displaying datas' headings
        Label(accedemic_page, text="SINHALA\t\t:", width=20).place(x=100, y=210)
        Label(accedemic_page, text="MATHEMATICS\t\t:", width=20).place(x=100, y=240)
        Label(accedemic_page, text="BUDDHISM\t\t:", width=20).place(x=100, y=270)
        Label(accedemic_page, text="ENGLISH\t\t\t:", width=20).place(x=100, y=300)
        Label(accedemic_page, text="TOTAL\t\t\t:", width=20).place(x=100, y=330)
        Label(accedemic_page, text="AVERAGE\t\t:", width=20).place(x=100, y=360)
        Label(accedemic_page, text="STATUS\t\t\t:", width=20).place(x=100, y=390)

        Button(accedemic_page, text="VIEW", activebackground="light blue", width=25, height=1, command=partial(view,index)).place(x=450, y=100)         #button for view data on inputted index
        Button(accedemic_page, text="REFRESH", activebackground="light blue", width=25, height=1,                                                       #button for refresh the window for new searching
                        command=remove).place(x=450, y=130)

        Button(accedemic_page, text="Grade 1 Full Report", activebackground="light blue", width=25, height=2,                                           #buttons for show data grade wise
                        command=grade1).place(x=450, y=180)
        Button(accedemic_page, text="Grade 2 Full Report", activebackground="light blue", width=25, height=2,
                        command=grade2).place(x=450, y=230)
        Button(accedemic_page, text="Grade 3 Full Report", activebackground="light blue", width=25, height=2,
                        command=grade3).place(x=450, y=280)
        Button(accedemic_page, text="Grade 4 Full Report", activebackground="light blue", width=25, height=2,
                        command=grade4).place(x=450, y=330)
        Button(accedemic_page, text="Grade 5 Full Report", activebackground="light blue", width=25, height=2,
                        command=grade5).place(x=450, y=380)

        Button(accedemic_page, text="ENTER MARKS", activebackground="light blue", width=25, height=2,                                                   #buttons for open data entering page
                       command=enter).place(x=100, y=485)

        Button(accedemic_page, text="BACK", width=10, height=2, activebackground="light blue",command = accedemic_page.destroy).place(x=450,            #button for back to home page
                                                                                                                   y=485)
        Button(accedemic_page, text="EXIT", width=10, height=2, activebackground="light blue",                                                          #button for exit from the system
                             command=home_page.destroy).place(x=560, y=485)

        accedemic_page.mainloop()


    def inquiry():                                                                                                      #create a frunction for open the inquiries window

        def attach_teachers():                                                                                          #functions for show various staff services providers details like as attaching teachers,payments,corespondance etc. you can see their details by pressing those buttons that engaged with these functions
            with connection:                                                                                            #get the details into variable called x and append them into a list by using a for loop
                x = cursor.execute("SELECT * FROM staff WHERE ID = 1").fetchall()
                y = x[0]
                my_list = []
                for items in y:
                    my_list.append(items)
                Label(inquiry_page, text=my_list[1],width = 25).place(x=460, y=140)                                     #print these details in list by using their indexes and appropriate lables
                Label(inquiry_page, text="8.00 a.m. - 12.00 p.m.",width = 25).place(x=460, y=180)
                Label(inquiry_page, text="SCHOOL OFFICE",width = 25).place(x=460, y=220)
                Label(inquiry_page, text=my_list[4],width = 25).place(x=460, y=260)

        def meet_administration():
            with connection:
                x = cursor.execute("SELECT * FROM staff WHERE ID = 2").fetchall()
                y = x[0]
                my_list = []
                for items in y:
                    my_list.append(items)
                Label(inquiry_page, text=my_list[1], width=25).place(x=460, y=140)
                Label(inquiry_page, text="8.00 a.m. - 12.00 p.m.", width=25).place(x=460, y=180)
                Label(inquiry_page, text="SCHOOL OFFICE", width=25).place(x=460, y=220)
                Label(inquiry_page, text=my_list[4], width=25).place(x=460, y=260)

        def corespondance():
            with connection:
                x = cursor.execute("SELECT * FROM staff WHERE ID = 5").fetchall()
                y = x[0]
                my_list = []
                for items in y:
                    my_list.append(items)
                Label(inquiry_page, text=my_list[1], width=25).place(x=460, y=140)
                Label(inquiry_page, text="8.00 a.m. - 12.00 p.m.", width=25).place(x=460, y=180)
                Label(inquiry_page, text="SCHOOL OFFICE", width=25).place(x=460, y=220)
                Label(inquiry_page, text=my_list[4], width=25).place(x=460, y=260)

        def welfare():
            with connection:
                x = cursor.execute("SELECT * FROM staff WHERE ID = 3").fetchall()
                y = x[0]
                my_list = []
                for items in y:
                    my_list.append(items)
                Label(inquiry_page, text=my_list[1], width=25).place(x=460, y=140)
                Label(inquiry_page, text="8.00 a.m. - 12.00 p.m.", width=25).place(x=460, y=180)
                Label(inquiry_page, text="SCHOOL OFFICE", width=25).place(x=460, y=220)
                Label(inquiry_page, text=my_list[4], width=25).place(x=460, y=260)

        def payments():
            with connection:
                x = cursor.execute("SELECT * FROM staff WHERE ID = 4").fetchall()
                y = x[0]
                my_list = []
                for items in y:
                    my_list.append(items)
                Label(inquiry_page, text=my_list[1], width=25).place(x=460, y=140)
                Label(inquiry_page, text="8.00 a.m. - 12.00 p.m.", width=25).place(x=460, y=180)
                Label(inquiry_page, text="SCHOOL OFFICE", width=25).place(x=460, y=220)
                Label(inquiry_page, text=my_list[4], width=25).place(x=460, y=260)

        def remove():                                                                                                   #function for refresh the page
            inquiry_page.destroy()
            inquiry()

        inquiry_page = Tk()                                                                                             #create the academic window and set its configurations
        inquiry_page.geometry("700x550")
        inquiry_page.title("DCC SCHOOL MANAGEMENT SYSTEM")
        inquiry_page.configure(bg="light blue")

        Label(inquiry_page, text="INQUIRIES UNIT", anchor=CENTER).place(x=250, y=20)                                                                #lable for display the heading of the page

        Label(inquiry_page,text="DESCRIPTION: Here you can choose the most suitable office worker for the service you want.").place(x=50, y=80)     #discription label

        Label(inquiry_page, text="Attaching teachers to classes\t", width=30).place(x=50, y=140)
        Button(inquiry_page, text="VIEW", width=5, activebackground="light blue",command=attach_teachers).place(x=290, y=140)                       #lables and buttons for display various staff details

        Label(inquiry_page, text="To make a time to meet administration", width=30).place(x=50, y=190)
        Button(inquiry_page, text="VIEW", width=5, activebackground="light blue",command=meet_administration).place(x=290, y=190)

        Label(inquiry_page, text="Corespondance\t\t\t", width=30).place(x=50, y=240)
        Button(inquiry_page, text="VIEW", width=5, activebackground="light blue",command=corespondance).place(x=290, y=240)

        Label(inquiry_page, text="Student Welfare\t\t\t", width=30).place(x=50, y=290)
        Button(inquiry_page, text="VIEW", width=5, activebackground="light blue", command=welfare).place(x=290, y=290)

        Label(inquiry_page, text="Payments\t\t\t", width=30).place(x=50, y=340)
        Button(inquiry_page, text="VIEW", width=5, activebackground="light blue", command=payments).place(x=290, y=340)

        Label(inquiry_page, text="NAME\t:", width=10).place(x=375, y=140)                                                                          #lables for display the headings of thtat showing details
        Label(inquiry_page, text="TIME\t:", width=10).place(x=375, y=180)
        Label(inquiry_page, text="VENUE\t:", width=10).place(x=375, y=220)
        Label(inquiry_page, text="TP NO.\t:", width=10).place(x=375, y=260)

        Button(inquiry_page, text="REFRESH", width=20, height=1, activebackground="light blue",command=remove).place(x=450, y=300)                 #BUTTON FOR REFRESH THE PAGE

        Button(inquiry_page, text="BACK", width=10, height=2, activebackground="light blue",command =  inquiry_page.destroy).place(x=450,y=485)     #BUTTONS FOR EXIT FROM THE SYSTEM AND BACK TO HOME PAGE
        Button(inquiry_page, text="EXIT", width=10, height=2, activebackground="light blue",command=home_page.destroy).place(x=560, y=485)

        inquiry_page.mainloop()


    def payments():                                                                                                     #create a page for payments and this function for open that page

        def refresh():                                                                                                  #refresh that page for create a new payment
            paytment_page.destroy()
            payments()

        def pay(paid_index,amount):                                                                                     #CREATE A FUNCTION TO ENTER PAYMENTS DETAILS INTO DATABASE

            amount_paid = paytment_page.getvar(name=str(amount))                                                        #assign user inputted data into variables
            grade_entered = paytment_page.getvar(name=str(entered_grade))
            paid_index_check = paytment_page.getvar(name=str(paid_index))

            with connection:                                                                                            #select IDs in the databse and append them into a list by using a for loop
                x = cursor.execute("SELECT ID FROM fees").fetchall()
                y = (x[0])
                my_list = []
                for items in y:
                    my_list.append(items)

            if paid_index_check not in my_list:                                                                         #check the user entered id in that list or not
                sql_admission = "INSERT INTO fees (ID,GRADE,AMOUNT) VALUES('" + paid_index_check + "','" + grade_entered + "','" + amount_paid + "')"
                with connection:                                                                                        #if not enter the details and show a successful message
                    cursor.execute(sql_admission)
                    cursor.commit()
                messagebox.showinfo("SUCCESSFUL", "THE PAYMENT HAS SUCCESSFUL !!!")
            else:
                messagebox.showinfo("ATTENTION", "THE PAYMENT HAS SUCCESSFUL YOU HAVE ALREADY PAID!!!")                 #else show a message for user about his previous payment


        paytment_page = Tk()                                                                                            #create the payment window and set its configurations
        paytment_page.geometry("700x350")
        paytment_page.title("DCC SCHOOL MANAGEMENT SYSTEM")
        paytment_page.configure(bg="light blue")

        paid_index = StringVar()                                                                                        #get the usetr inputs from textvariables as StringVar
        entered_grade = StringVar()
        amount = StringVar()

        Label(paytment_page, text="PAYMENT MANAGEMENT UNIT", anchor=CENTER).place(x=250, y=20)                          #heading of the page

        Label(paytment_page, text="INDEX\t\t\t:", width=20).place(x=180, y=80)                                          #Lables and entries for user inputs
        Entry(paytment_page, width=20,textvariable = paid_index).place(x=350, y=80)
        Label(paytment_page, text="GRADE\t\t\t:", width=20).place(x=180, y=110)
        Entry(paytment_page, width=20,textvariable = entered_grade).place(x=350, y=110)
        Label(paytment_page, text="AMOUNT\t\t:", width=20).place(x=180, y=140)
        Entry(paytment_page, width=20,textvariable = amount).place(x=350, y=140)

        Button(paytment_page, text="PAY", width=16, height=1, activebackground="light blue",command=partial(pay,paid_index,amount)).place(x=350, y=180)         #button for entering and checking the payment details

        Button(paytment_page, text="REFRESH", width=10, height=2, activebackground="light blue",command = refresh).place(x=340,y=270)                           #button for refresh the page for a new payment

        Button(paytment_page, text="BACK", width=10, height=2, activebackground="light blue",command = paytment_page.destroy).place(x=450,y=270)                #buttons for exit from the system and back to home page
        Button(paytment_page, text="EXIT", width=10, height=2, activebackground="light blue",command=home_page.destroy).place(x=560, y=270)

        paytment_page.mainloop()


    def admission():                                                                                                    #function to open the admission window

        def refresh():                                                                                                  #function for refresh the window for a new entry
            student_admission_page.destroy()
            admission()

        def submit(full_name,grade,birthday,home,male_female,gardian,telephone):                                        #function for enter user inputs into database

            name = student_admission_page.getvar(name=str(full_name))                                                   #get user inputs into variables
            gradee = student_admission_page.getvar(name=str(grade))
            birth = student_admission_page.getvar(name=str(birthday))
            hometown = student_admission_page.getvar(name=str(home))
            m_f = student_admission_page.getvar(name=str(male_female))
            gard = student_admission_page.getvar(name=str(gardian))
            tel = student_admission_page.getvar(name=str(telephone))

            if m_f == 1:                                                                                                #check the sex and create a variable to insert database the sex as a letter
                sex = "M"
            else:
                sex = "F"

            sql_admissionstu = "INSERT INTO students (NAME,GRADE,`BIRTH DAY`,`HOME TOWN`,SEX,`NAME OF THE GARDIAN`,`TELEPHONE NUMBER`) VALUES('"+name+"','"+gradee+"','"+birth+"','"+hometown+"','"+sex+"','"+gard+"','"+tel+"')"
            sql_admissionbooks = "INSERT INTO books (NAME) VALUES ('"+name+"')"

            with connection:                                                                                            #INSERT DATA INTO DATABASES
                cursor.execute(sql_admissionstu)
                cursor.commit()
                cursor.execute(sql_admissionbooks)
                cursor.commit()
            messagebox.showinfo("SUCCESSFUL", "THE STUDENT HAS REGISTERED IN DCC SCHOOL MANAGEMENT SYSTEM !!!")


        student_admission_page = Tk()                                                                                   #create the student addmission page window and set its configurations
        student_admission_page.geometry("600x550")
        student_admission_page.title("DCC SCHOOL MANAGEMENT SYSTEM")
        student_admission_page.configure(bg="light blue")


        full_name = StringVar()                                                                                         #get the user inputs as StringVar
        grade = StringVar()
        birthday = StringVar()
        home = StringVar()
        male_female = IntVar()
        gardian = StringVar()
        telephone = StringVar()

        Label(student_admission_page, text="ADMISSION FORM", justify=CENTER).place(x=250, y=30)                         #label to display heading of the page

        Label(student_admission_page, text="(1) FULL NAME\t\t\t\t:", ).place(x=55, y=100)                               #Lables for entry headings and entries for enter details
        Entry(student_admission_page, width=40,textvariable = full_name).place(x=310, y=100)

        Label(student_admission_page, text="(2) GRADE \t:").place(x=55, y=140)
        Entry(student_admission_page, width=40,textvariable = grade).place(x=310, y=140)

        Label(student_admission_page, text="(2) BIRTH DAY (in dd/mm/yyyy Format \t:").place(x=55,y=180)
        Entry(student_admission_page, width=40, textvariable=birthday).place(x=310, y=180)

        Label(student_admission_page, text="(3) HOME TOWN\t\t\t\t: ").place(x=55, y=220)
        Entry(student_admission_page, width=40,textvariable = home).place(x=310, y=220)

        Label(student_admission_page, text="(4) SEX \t\t\t\t\t:").place(x=55, y=260)
        Radiobutton(student_admission_page, width=5, text="MALE", activebackground="light blue",value=1,variable = male_female).place(x=310, y=260)
        Radiobutton(student_admission_page, width=5, text="FEMALE", activebackground="light blue",value=2,variable = male_female).place(x=400, y=260)

        Label(student_admission_page, text="(5) NAME OF THE GARDIAN\t\t:").place(x=55, y=300)
        Entry(student_admission_page, width=40,textvariable = gardian).place(x=310, y=300)

        Label(student_admission_page, text="(6) CONTACT NO\t\t\t\t:").place(x=55, y=340)
        Entry(student_admission_page, width=40,textvariable = telephone).place(x=310, y=340)

        Button(student_admission_page, text="SUBMIT", width=25, height=1,activebackground="light blue",command = partial(submit,full_name,grade,birthday,home,male_female,gardian,telephone)).place(x=340, y=370)


        Button(student_admission_page, text="REFRESH", width=10, height=2, activebackground="light blue",command = refresh).place(x=240,                                    #BUTTON FOR ENTER DATA INTO DATABASE
                                                                                                                  y=485)
        Button(student_admission_page, text="BACK", width=10, height=2, activebackground="light blue",command = student_admission_page.destroy).place(x=370, y=485)         #buttons to exit from the system and back to home page
        Button(student_admission_page, text="EXIT", width=10, height=2, activebackground="light blue",command=home_page.destroy).place(x=480, y=485)

        student_admission_page.mainloop()


    def staff():                                                                                                        #function to open the staff window
        staff_page = Tk()                                                                                               #create the staff window and set its configurations
        staff_page.geometry("900x900")
        staff_page.title("DCC SCHOOL MANAGEMENT SYSTEM")
        staff_page.configure(bg="light blue")

        with connection:                                                                                                #get the details and display them wise their id
            x = cursor.execute("SELECT * FROM staff WHERE ID = 1").fetchall()                                           #because of the data comes as the tupples insert them into a list and get list indexes for print
            y = (x[0])
            my_list = []
            for items in y:
                my_list.append(items)

        with connection:
            x = cursor.execute("SELECT * FROM staff WHERE ID = 2").fetchall()
            y = (x[0])
            my_list2 = []
            for items in y:
                my_list2.append(items)

        with connection:
            x = cursor.execute("SELECT * FROM staff WHERE ID = 3").fetchall()
            y = (x[0])
            my_list3 = []
            for items in y:
                my_list3.append(items)

        with connection:
            x = cursor.execute("SELECT * FROM staff WHERE ID = 4").fetchall()
            y = (x[0])
            my_list4 = []
            for items in y:
                my_list4.append(items)

        Label(staff_page, text="NAME\t:", width=10).place(x=50, y=140)                                                  #lables for details headings
        Label(staff_page, text="TIME\t:", width=10).place(x=50, y=170)
        Label(staff_page, text="VENUE\t:", width=10).place(x=50, y=200)
        Label(staff_page, text="TP NO.\t:", width=10).place(x=50, y=230)

        Label(staff_page, text=my_list[1],width = 23).place(x=150, y=140)                                               #lables for display the details
        Label(staff_page, text=my_list[2],width = 23).place(x=150, y=170)
        Label(staff_page, text=my_list[3],width = 23).place(x=150, y=200)
        Label(staff_page, text=my_list[4],width = 23).place(x=150, y=230)

        Label(staff_page, text=my_list2[1],width = 23).place(x=325, y=140)
        Label(staff_page, text=my_list2[2],width = 23).place(x=325, y=170)
        Label(staff_page, text=my_list2[3],width = 23).place(x=325, y=200)
        Label(staff_page, text=my_list2[4],width = 23).place(x=325, y=230)

        Label(staff_page, text=my_list3[1],width = 23).place(x=500, y=140)
        Label(staff_page, text=my_list3[2],width = 23).place(x=500, y=170)
        Label(staff_page, text=my_list3[3],width = 23).place(x=500, y=200)
        Label(staff_page, text=my_list3[4],width = 23).place(x=500, y=230)

        Label(staff_page, text=my_list4[1],width = 23).place(x=675, y=140)
        Label(staff_page, text=my_list4[2],width = 23).place(x=675, y=170)
        Label(staff_page, text=my_list4[3],width = 23).place(x=675, y=200)
        Label(staff_page, text=my_list4[4],width = 23).place(x=675, y=230)

        with connection:
            x = cursor.execute("SELECT * FROM staff WHERE ID = 5").fetchall()
            y = (x[0])
            my_list = []
            for items in y:
                my_list.append(items)

        Label(staff_page, text="NAME\t:", width=10).place(x=50, y=320)
        Label(staff_page, text="TIME\t:", width=10).place(x=50, y=350)
        Label(staff_page, text="VENUE\t:", width=10).place(x=50, y=380)
        Label(staff_page, text="TP NO.\t:", width=10).place(x=50, y=410)

        Label(staff_page, text=my_list[1],width = 23).place(x=150, y=320)
        Label(staff_page, text=my_list[2],width = 23).place(x=150, y=350)
        Label(staff_page, text=my_list[3],width = 23).place(x=150, y=380)
        Label(staff_page, text=my_list[4],width = 23).place(x=150, y=410)

        with connection:
            x = cursor.execute("SELECT * FROM staff WHERE ID = 6").fetchall()
            y = (x[0])
            my_list = []
            for items in y:
                my_list.append(items)
        Label(staff_page, text="NAME\t:", width=10).place(x=50, y=500)
        Label(staff_page, text="TIME\t:", width=10).place(x=50, y=530)
        Label(staff_page, text="VENUE\t:", width=10).place(x=50, y=560)
        Label(staff_page, text="TP NO.\t:", width=10).place(x=50, y=590)

        Label(staff_page, text=my_list[1],width = 23).place(x=150, y=500)
        Label(staff_page, text=my_list[2],width = 23).place(x=150, y=530)
        Label(staff_page, text=my_list[3],width = 23).place(x=150, y=560)
        Label(staff_page, text=my_list[4],width = 23).place(x=150, y=590)

        Label(staff_page, text="STAFF MANAGEMENT SYSTEM",width = 112).place(x=50, y=30)                                                             #lable for display the page heading

        Label(staff_page, text="OFFICE STAFF",width = 20).place(x=50, y=100)
        Label(staff_page, text="LIBRARIAN",width = 20).place(x=50, y=280)                                                                           #lables for display staff headings
        Label(staff_page, text="OTHERS",width = 20).place(x=50, y=460)
        Button(staff_page, text="BACK", width=10, height=2, activebackground="light blue",command = staff_page.destroy).place(x=600,y=600)          #buttons for return to home page and exit from the syatem
        Button(staff_page, text="EXIT", width=10, height=2, activebackground="light blue",command=home_page.destroy).place(x=700, y=600)

        staff_page.mainloop()


    def library():                                                                                                      #function to open library log in window
        libraray_log_in_page = Tk()                                                                                     #set its configurations
        libraray_log_in_page.geometry("700x350")
        libraray_log_in_page.title("DCC SCHOOL MANAGEMENT SYSTEM")
        libraray_log_in_page.configure(bg="light blue")

        input_username = StringVar()                                                                                    #get the user inputs as StringVar
        input_password = StringVar()



        def login():                                                                                                    #create a function to open the library page

            def librarypage():
                libraray_page = Tk()                                                                                    #creates the library page window and its configurations
                libraray_page.geometry("800x380")
                libraray_page.title("DCC SCHOOL MANAGEMENT SYSTEM")
                libraray_page.configure(bg="light blue")

                input_index = StringVar()                                                                               #get the user input as StringVar

                def refresh():
                    libraray_page.destroy()                                                                             #create a fnctions to refresh the page for a new searching
                    librarypage()

                def check(input_index):                                                                                 #check the index in the library database
                    index = libraray_page.getvar(name=str(input_index))                                                 #get the textvariable value into a new variable

                    if index == "":                                                                                     #give the messages after checking the index if it is a blank else show the library details
                        messagebox.showinfo("ATTENTION", "BLANK NOT ALLOWED.\nTRY AGAIN !!!")

                    else:
                        with connection:
                            x = cursor.execute("SELECT * FROM books WHERE ID =" +index).fetchone()                      #select the indexed library detasils from the databse
                            y = x
                            my_list = []
                            for items in y:
                                my_list.append(items)

                        Label(libraray_page, text=my_list[0],width = 23).place(x=370, y=140)                            #show details as lables
                        Label(libraray_page, text=my_list[1],width = 23).place(x=370, y=180)
                        Label(libraray_page, text=my_list[2],width = 23).place(x=370, y=220)

                Label(libraray_page, text="LIBRARY MANAGEMENT SYSTEM", anchor=CENTER,width = 70).place(x=150,y=20)      #heading of the library page
                Label(libraray_page, text="ENTER YOUR INDEX NUMBER \t:").place(x=150, y=60)                             #lable and entry for insert the index to check library details
                Entry(libraray_page, textvariable=input_index).place(x=370, y=60)

                Label(libraray_page, text="INDEX NUMBER\t\t\t:").place(x=150, y=140)                                    #headings for showing details
                Label(libraray_page, text="NAME\t\t\t\t:").place(x=150, y=180)
                Label(libraray_page, text="NAME OF THE BOOK ISSUED\t:").place(x=150, y=220)

                Button(libraray_page, text="CHECK", activebackground="light blue", width=16,                            #button to check the index in library database
                                      command=partial(check, input_index)).place(x=370, y=85)
                Button(libraray_page, text="EXIT", width=10, activebackground="light blue",                             #buttons for exit from the system and back to home page
                                     command=libraray_page.destroy).place(x=550, y=300)
                Button(libraray_page, text="REFRESH", width=10, activebackground="light blue",
                                     command=refresh).place(x=440, y=300)
                libraray_page.mainloop()

            usernmae_valid = "USER"                                                                                     #user name and the password of the library login system
            password_valid = "FHSS@1234"

            username = libraray_log_in_page.getvar(name=str(input_username))                                            #get the user inputs into variables
            password = libraray_log_in_page.getvar(name=str(input_password))

            if (username == "") and (password == ""):                                                                   #check it is a blank input or a invalid input or a valid input and give access to the library system
                messagebox.showinfo("ATTENTION", "BLANK NOT ALLOWED.\nTRY AGAIN !!!")

            elif (username == usernmae_valid) and (password == password_valid):
                messagebox.showinfo("WELCOME","LOGIN SUCCESSFUL.\n WELCOME TO DENIYAYA CENTRAL COLLEGE LIBRARY MANAGEMENT SYSTEM")
                log_in_page.quit()
                librarypage()
            else:
                messagebox.showinfo("ATTENTION", "INCORRECT USERNAME OR PASSWORD.\nTRY AGAIN !!!")

        Label(libraray_log_in_page, text="LIBRARY MANAGEMENT SYSTEM", anchor=CENTER).place(x=275,y = 50)                #heading of the log in page
        Label(libraray_log_in_page, text="Username   \t:").place(x=220, y=100)                                          #lables and entries for enter the user name and password
        Entry(libraray_log_in_page, textvariable=input_username).place(x=370, y=100)
        Label(libraray_log_in_page, text="Password   \t:").place(x=220, y=130)
        Entry(libraray_log_in_page, textvariable=input_password).place(x=370, y=130)
        Button(libraray_log_in_page, text="LOG IN", activebackground="light blue", width=6,command = login).place(x=370,y=170)                                      #buttons to exit from the system or back to home page
        Button(libraray_log_in_page, text="EXIT", activebackground="light blue", width=5,command=libraray_log_in_page.destroy).place(x=450, y=170)

        libraray_log_in_page.mainloop()


    def timetable():                                                                                                    #function to open the timetable

        time_table_page = Tk()                                                                                          #time table page window and create its configurations
        time_table_page.geometry("1000x450")
        time_table_page.title("DCC SCHOOL MANAGEMENT SYSTEM")
        time_table_page.configure(bg="light blue")

        Label(time_table_page,text = "TIME TABLE",anchor=CENTER,width = 113).place(x=100, y=30)                         #heading of the page

        Label(time_table_page,text = "TIME",width = 10).place(x = 100,y= 100)
        Label(time_table_page,text = "7.30 - 8.30",width = 10).place(x = 100,y= 140)
        Label(time_table_page,text = "8.30 - 9.30",width = 10).place(x = 100,y= 180)
        Label(time_table_page,text = "9.30 - 10.00",width = 10).place(x = 100,y= 220)
        Label(time_table_page,text = "10.00 - 11.00",width = 10).place(x = 100,y= 260)
        Label(time_table_page,text = "11.00 - 12.00",width = 10).place(x = 100,y= 300)
        Label(time_table_page,text = "12.00 - 1.00",width = 10).place(x = 100,y= 340)

        Label(time_table_page,text = "GRADE 1",width = 10).place(x = 225,y= 100)
        Label(time_table_page, text="SINHALA",width = 10).place(x=225, y=140)
        Label(time_table_page, text="READING",width = 10).place(x=225, y=180)
        Label(time_table_page, text="INTERVAL",width = 96).place(x=225, y=220)
        Label(time_table_page, text="BUDDHISM",width = 10).place(x=225, y=260)
        Label(time_table_page, text="ACTIVITIES",width = 10).place(x=225, y=300)

        Label(time_table_page,text = "GRADE 2",width = 10).place(x = 375,y= 100)
        Label(time_table_page, text="BUDDHISM",width = 10).place(x=375, y=140)
        Label(time_table_page, text="ACTIVITIES",width = 10).place(x=375, y=180)
        Label(time_table_page, text="SINHALA",width = 10).place(x=375, y=260)
        Label(time_table_page, text="READING",width = 10).place(x=375, y=300)

        Label(time_table_page,text = "GRADE 3",width = 10).place(x = 525,y= 100)
        Label(time_table_page, text="SINHALA",width = 10).place(x=525, y=140)
        Label(time_table_page, text="LIBRARY",width = 10).place(x=525, y=180)
        Label(time_table_page, text="BUDDHISM",width = 10).place(x=525, y=260)
        Label(time_table_page, text="ENGLISH",width = 10).place(x=525, y=300)
        Label(time_table_page,text = "MATHS",width = 10).place(x = 525,y= 340)

        Label(time_table_page,text = "GRADE 4",width = 10).place(x = 675,y= 100)
        Label(time_table_page, text="MATHS",width = 10).place(x=675, y=140)
        Label(time_table_page, text="BUSSHISM",width = 10).place(x=675, y=180)
        Label(time_table_page, text="SINHALA",width = 10).place(x=675, y=260)
        Label(time_table_page, text="LIBRARY",width = 10).place(x=675, y=300)
        Label(time_table_page, text="ENGLISH",width = 10).place(x=675, y=340)

        Label(time_table_page,text = "GRADE 5",width = 10).place(x = 825,y= 100)
        Label(time_table_page, text="ENGLISH",width = 10).place(x=825, y=140)
        Label(time_table_page, text="MATHS",width = 10).place(x=825, y=180)
        Label(time_table_page, text="SINHALA",width = 10).place(x=825, y=260)
        Label(time_table_page, text="BUDDHISM",width = 10).place(x=825, y=300)
        Label(time_table_page, text="LIBRARY",width = 10).place(x=825, y=340)

        Label(time_table_page,text = "THIS TIME TABLE IS VALID FOR EVERY WEEK DAYS AND FOR EVERY YEAR.").place(x=100,y=400 )

        time_table_page.mainloop()

    Label(home_page, text="SCHOOL MANAGEMENT SYSTEM OF DENIYAYA CENTRAL COLLEGE PRIMARY SECTION",anchor=CENTER,width = 70).place(x=50, y=20)            #heading of the homepage
    Button(home_page, text="TEACHER", activebackground="light blue", width=20, height=3,command=teachers).place(x=50, y=150)                            #buttons for call above functions named as teachers, students, payments,library, admission etc.
    Button(home_page, text="STUDENT", activebackground="light blue", width=20, height=3,command=student).place(x=210, y=150)
    Button(home_page, text="ACADEMIC", activebackground="light blue", width=20, height=3,command=academic).place(x=50, y=210)
    Button(home_page, text="INQUIRIES", activebackground="light blue", width=20, height=3,command=inquiry).place(x=210, y=210)
    Button(home_page, text="PAYMENTS", activebackground="light blue", width=20, height=3,command=payments).place(x=50, y=270)
    Button(home_page, text="ADMISSION", activebackground="light blue", width=20, height=3,command=admission).place(x=210, y=270)

    Button(home_page, text="LIBRARY", activebackground="light blue", width=20, height=1,command = library).place(x=450, y=150)
    Button(home_page, text="STAFF", activebackground="light blue", width=20, height=1, command=staff).place(x=450, y=190)
    Button(home_page, text="TIME TABLE", activebackground="light blue", width=20, height=1,command = timetable).place(x=450,y=230)

    Button(home_page, text="EXIT", width=20, activebackground="light blue", command=home_page.destroy).place(x=450, y=300)                              #button to exit from the system

    home_page.mainloop()



def login():                                                                                                            #function to log into the system and open the homepage and all others
    usernmae_valid = "USER"                                                                                             #valid username and password
    password_valid = "FHSS@1234"

    if (input_username.get() == "") and (input_password.get() == ""):                                                   #check the inputted username password is a blank or a invalid input or a valid one and if it is a validone give access to enter the home page
        messagebox.showinfo("ATTENTION","BLANK NOT ALLOWED.\nTRY AGAIN !!!")

    elif (input_username.get() == usernmae_valid) and (input_password.get() == password_valid):
        messagebox.showinfo("WELCOME","LOGIN SUCCESSFUL.\n WELCOME TO DENIYAYA CENTRAL COLLEGE SCHOOL MANAGEMENT SYSTEM")
        log_in_page.destroy()
        homepage()
    else:
        messagebox.showinfo("ATTENTION","INCORRECT USERNAME OR PASSWORD.\nTRY AGAIN !!!")


log_in_page = Tk()                                                                                                      #create the login page and its configurations
log_in_page.title("DCC SCHOOL MANAGEMENT SYSTEM")
image_name = PhotoImage(file = "C:\\SCHOOL MANAGEMENT SYSTEM\\background.png")
background_label = Label(log_in_page,image=image_name)
background_label.place(x=0,y=0,relwidth=1,relheight=1)
log_in_page.geometry("700x390")

input_username = StringVar()                                                                                            #get the user inputs as StringVar
input_password = StringVar()

log_in_page_label = Label(log_in_page,text = "SCHOOL MANAGEMENT SYSTEM OF DENIYAYA CENTRAL COLLEGE PRIMARY SECTION",anchor = CENTER).place(x = 110,y = 20)          #heading of the login page

username_label = Label(log_in_page,text = "Username   \t\t:").place(x = 200,y = 100)                                                                                #entries and lables to user's useage to enter username and password
username = Entry(log_in_page,width = 20,textvariable = input_username).place(x = 370,y = 100)

password_label = Label(log_in_page,text = "Password   \t\t:").place(x = 200,y = 130)
password = Entry(log_in_page,width = 20,textvariable = input_password).place(x = 370,y = 130)


login_button = Button(log_in_page,text = "LOG IN",activebackground = "light blue",width = 6,command = login).place(x = 370,y = 170)                                   #log in button to access to the homepage
exit_button = Button(log_in_page,text = "EXIT",activebackground = "light blue",width = 5,command = log_in_page.destroy).place(x = 450,y = 170)                         #exit button to exit

log_in_page.mainloop()
