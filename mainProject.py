import platform
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import sys

import mysql.connector
from prettytable import PrettyTable

mydb = mysql.connector.connect(host="localhost", user="root", passwd="123password", database="innovative_assignment")
mycursor = mydb.cursor()

try:
    import ttk

    py3 = False
except ImportError:
    import tkinter.ttk as ttk

    py3 = True

    # python backend starts


def display_table(choice):  # 1=student; 2=exam; 3=subject; 4=result; 5=attendance; 6=branch
    if choice == 1:
        mycursor.execute("select * from student")
        data = mycursor.fetchall()
        return data
    elif choice == 2:
        mycursor.execute("select * from exam")
        data = mycursor.fetchall()
        return data
    elif choice == 3:
        mycursor.execute("select * from subject")
        data = mycursor.fetchall()
        return data
    elif choice == 4:
        mycursor.execute("select * from result")
        data = mycursor.fetchall()
        return data
    elif choice == 5:
        mycursor.execute("select * from attendance")
        data = mycursor.fetchall()
        return data
    elif choice == 6:
        mycursor.execute("select * from branch")  # Error.setMessage(self, message_shown="Cannot fetch data!")

        data = mycursor.fetchall()
        return data
    else:
        #        Error(Toplevel(self.master))
        return "Cannot fetch data!"

    # python backend ends

    # Tkinter GUI code starts


class Student:
    def __init__(self, top=None):
        self.master = top
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.', background='#d9d9d9')
        self.style.configure('.', foreground="#000000")
        self.style.configure('.', font="TkDefaultFont")
        self.style.map('.', background=
        [('selected', "#d9d9d9"), ('active', "#ececec")])

        top.geometry("600x450+383+106")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(0, 0)
        top.title("Student")
        top.configure(background="#212529")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Canvas1 = tk.Canvas(top, background="white", insertbackground="black", highlightbackground="#d9d9d9",
                                 highlightcolor="black", relief="ridge", selectbackground="blue",
                                 selectforeground="white")
        self.Canvas1.place(relx=0.067, rely=0.111, relheight=0.74
                           , relwidth=0.872)

        self.Label1 = tk.Label(top, background="#212529", font="-family {Segoe UI} -size 13 -weight bold",
                               foreground="#ffffff", text='''Student Table''')
        self.Label1.place(relx=0.367, rely=0.022, height=31, width=174)

        self.style.configure('Treeview', font="TkDefaultFont", borderwidth=0)
        global tv
        tv = ScrolledTreeView(self.Canvas1)
        tv.place(relx=0.0, rely=0.0, relheight=0.712, relwidth=1.0)
        tv['columns'] = ("Col1", "Col2", "Col3", "Col4", "Col5")
        tv.column("#0", width=0, stretch="NO")
        tv.column("Col1", width=100)
        tv.column("Col2", width=100)
        tv.column("Col3", width=100, anchor="center")
        tv.column("Col4", width=100)
        tv.column("Col5", width=100)
        tv.heading("#0", text="", anchor="w")
        tv.heading("Col1", text="Student ID", anchor="w")
        tv.heading("Col2", text="Branch ID", anchor="w")
        tv.heading("Col3", text="Roll Number", anchor="center")
        tv.heading("Col4", text="Email", anchor="w")
        tv.heading("Col5", text="Password", anchor="w")
        #        count = 0
        #        for i in range(20):
        #            tv.insert(parent='', index="end", iid=count, text="Parent" + str(count),
        #                      values=("Col1" + str(count), "Col2" + str(count), "Col3" + str(count)))
        #            count += 1

        self.add_button = tk.Button(self.Canvas1, command=self.select_add, activebackground="#ececec",
                                    activeforeground="#000000", background="#3F454C",
                                    borderwidth="0", disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 9 "
                                                                                        "-weight bold",
                                    foreground="white", highlightbackground="#d9d9d9", highlightcolor="black",
                                    pady="0", text='''Add''')
        self.add_button.place(relx=0.402, rely=0.871, height=24, width=79)

        self.delete_button = tk.Button(self.Canvas1, command=self.select_delete, activebackground="#ececec",
                                       activeforeground="#000000", background="#3F454C",
                                       borderwidth="0", disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 9 "
                                                                                           "-weight bold",
                                       foreground="white", highlightbackground="#d9d9d9", highlightcolor="black",
                                       text="Delete")
        self.delete_button.place(relx=0.593, rely=0.871, height=24, width=79)

        self.modify_button = tk.Button(self.Canvas1, command=self.select_modify, activebackground="#ececec",
                                       activeforeground="#000000", background="#3F454C",
                                       borderwidth="0", disabledforeground="#a3a3a3",
                                       font="-family {Segoe UI} -size 9 -weight bold",
                                       foreground="white", highlightbackground="#d9d9d9", highlightcolor="black",
                                       text='''Modify''')
        self.modify_button.place(relx=0.784, rely=0.871, height=24, width=79)

        self.back_button = tk.Button(self.Canvas1, command=self.select_back, activebackground="#ececec",
                                     activeforeground="#000000", background="#343a40",
                                     borderwidth="0", disabledforeground="#a3a3a3",
                                     font="-family {Segoe UI} -size 9 -weight bold", foreground="#ffffff",
                                     highlightbackground="#d9d9d9", highlightcolor="black", pady="0", text='''Back''')
        self.back_button.place(relx=0.038, rely=0.871, height=24, width=79)

        # real data
        mycursor.execute("SELECT * from student;")
        output = mycursor.fetchall()

        for list_item in output:
            tv.insert(parent='', index="end", text="Parent", values=(
                str(list_item[0]), str(list_item[1]), str(list_item[2]), str(list_item[3]), str(list_item[4])))

    def select_back(self):
        self.master.withdraw()
        MainScreen(Toplevel(self.master))

    def select_delete(self):
        try:
            #            row_id = int(tv.focus().replace("I", ""))
            item = tv.item(tv.focus())
            tv.delete(tv.focus())
            sql_query = "DELETE FROM student WHERE student_id=" + str(item['values'][0]) + ";"
            try:
                mycursor.execute(sql_query)  # executing query
            except (mysql.connector.Error, mysql.connector.Warning) as e:  # fetching error
                messagebox.showerror("Error Message", "ERROR MESSAGE\n" + str(e))  # displaying error

        except:
            messagebox.showerror("Error Message", "Please select a row to be deleted")
        mydb.commit()

    def select_add(self):
        StudentAdd(Toplevel(self.master))

    def select_modify(self):
        if tv.focus() != "":
            StudentModify(Toplevel(self.master))
        else:
            messagebox.showerror("Error Message", "Please select a row to be modified")


class Exam:
    def __init__(self, top=None):
        self.master = top
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.', background='#d9d9d9')
        self.style.configure('.', foreground="#000000")
        self.style.configure('.', font="TkDefaultFont")
        self.style.map('.', background=
        [('selected', "#d9d9d9"), ('active', "#ececec")])

        top.geometry("600x450+383+106")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(0, 0)
        top.title("Exam")
        top.configure(background="#212529")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Canvas1 = tk.Canvas(top, background="white", insertbackground="black", highlightbackground="#d9d9d9",
                                 highlightcolor="black", relief="ridge", selectbackground="blue",
                                 selectforeground="white")
        self.Canvas1.place(relx=0.067, rely=0.111, relheight=0.74
                           , relwidth=0.872)

        self.Label1 = tk.Label(top, background="#212529", font="-family {Segoe UI} -size 13 -weight bold",
                               foreground="#ffffff", text='''Eaxm Table''')
        self.Label1.place(relx=0.367, rely=0.022, height=31, width=174)

        self.style.configure('Treeview', font="TkDefaultFont", borderwidth=0)

        global tv
        tv = ScrolledTreeView(self.Canvas1)
        tv.place(relx=0.0, rely=0.0, relheight=0.712, relwidth=1.0)
        tv['columns'] = ("Col1", "Col2", "Col3", "Col4", "Col5", "Col6", "Col7", "Col8")
        tv.column("#0", width=0, stretch="NO")
        tv.column("Col1", width=100)
        tv.column("Col2", width=100)
        tv.column("Col3", width=100)
        tv.column("Col4", width=100, anchor="center")
        tv.column("Col5", width=100)
        tv.column("Col6", width=100)
        tv.column("Col7", width=100)
        tv.column("Col8", width=100)
        tv.heading("#0", text="", anchor="w")
        tv.heading("Col1", text="Exam ID", anchor="w")
        tv.heading("Col2", text="Exam Name", anchor="w")
        tv.heading("Col3", text="Exam Duration", anchor="w")
        tv.heading("Col4", text="Exam Date", anchor="center")
        tv.heading("Col5", text="Total Question", anchor="w")
        tv.heading("Col6", text="Total Marks", anchor="w")
        tv.heading("Col7", text="Branch ID", anchor="w")
        tv.heading("Col8", text="Subject Code", anchor="w")

        self.add_button = tk.Button(self.Canvas1, activebackground="#ececec", activeforeground="#000000",
                                    background="#3F454C", borderwidth="0", disabledforeground="#a3a3a3",
                                    font="-family {Segoe UI} -size 9 " "-weight bold",
                                    foreground="white", highlightbackground="#d9d9d9", highlightcolor="black",
                                    pady="0", text='''Add''', command=self.select_add)

        self.add_button.place(relx=0.402, rely=0.871, height=24, width=79)

        self.delete_button = tk.Button(self.Canvas1, activebackground="#ececec", activeforeground="#000000",
                                       background="#3F454C",
                                       borderwidth="0", disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 9 "
                                                                                           "-weight bold",
                                       foreground="white", highlightbackground="#d9d9d9", highlightcolor="black",
                                       text="Delete", command=self.select_delete)
        self.delete_button.place(relx=0.593, rely=0.871, height=24, width=79)

        self.modify_button = tk.Button(self.Canvas1, activebackground="#ececec", activeforeground="#000000",
                                       background="#3F454C",
                                       borderwidth="0", disabledforeground="#a3a3a3",
                                       font="-family {Segoe UI} -size 9 -weight bold",
                                       foreground="white", highlightbackground="#d9d9d9", highlightcolor="black",
                                       text='''Modify''', command=self.select_modify)
        self.modify_button.place(relx=0.784, rely=0.871, height=24, width=79)

        self.back_button = tk.Button(self.Canvas1, activebackground="#ececec", activeforeground="#000000",
                                     background="#343a40",
                                     borderwidth="0", disabledforeground="#a3a3a3",
                                     font="-family {Segoe UI} -size 9 -weight bold", foreground="#ffffff",
                                     highlightbackground="#d9d9d9", highlightcolor="black", pady="0", text='''Back''',
                                     command=self.back)
        self.back_button.place(relx=0.038, rely=0.871, height=24, width=79)

        # real data
        mycursor.execute("SELECT * from exam;")
        output = mycursor.fetchall()

        for list_item in output:
            tv.insert(parent='', index="end", text="Parent", values=(
                str(list_item[0]), list_item[1], list_item[2], list_item[3], str(list_item[4]), str(list_item[5]),
                str(list_item[6]), list_item[7]))

    def back(self):
        self.master.withdraw()
        MainScreen(Toplevel(self.master))

    def select_modify(self):
        if tv.focus() != "":
            ExamModify(Toplevel(self.master))
        else:
            messagebox.showerror("Please select a row to be modified")

    def select_delete(self):
        try:
            #            row_id = int(tv.focus().replace("I", ""))
            item = tv.item(tv.focus())
            tv.delete(tv.focus())
            sql_query = "DELETE FROM exam WHERE exam_id=" + str(item['values'][0]) + ";"
            try:
                mycursor.execute(sql_query)  # executing query
            except (mysql.connector.Error, mysql.connector.Warning) as e:  # fetching error
                messagebox.showerror("Error Message", str(e))  # displaying error

        except:
            messagebox.showerror("Error Message", "Please select a row to be deleted")
        mydb.commit()

    def select_add(self):
        ExamAdd(Toplevel(self.master))


class Result:
    def __init__(self, top=None):
        self.master = top
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.', background='#d9d9d9')
        self.style.configure('.', foreground="#000000")
        self.style.configure('.', font="TkDefaultFont")
        self.style.map('.', background=
        [('selected', "#d9d9d9"), ('active', "#ececec")])

        top.geometry("600x450+383+106")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(0, 0)
        top.title("Result")
        top.configure(background="#212529")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Canvas1 = tk.Canvas(top, background="white", insertbackground="black", highlightbackground="#d9d9d9",
                                 highlightcolor="black", relief="ridge", selectbackground="blue",
                                 selectforeground="white")
        self.Canvas1.place(relx=0.067, rely=0.111, relheight=0.74
                           , relwidth=0.872)

        self.Label1 = tk.Label(top, background="#212529", font="-family {Segoe UI} -size 13 -weight bold",
                               foreground="#ffffff", text='''Result Table''')
        self.Label1.place(relx=0.367, rely=0.022, height=31, width=174)

        self.style.configure('Treeview', font="TkDefaultFont", borderwidth=0)
        global tv
        tv = ScrolledTreeView(self.Canvas1)
        tv.place(relx=0.0, rely=0.0, relheight=0.712, relwidth=1.0)
        tv['columns'] = ("Col1", "Col2", "Col3", "Col4", "Col5")
        tv.column("#0", width=0, stretch="NO")
        tv.column("Col1", width=100)
        tv.column("Col2", width=100)
        tv.column("Col3", width=100, anchor="center")
        tv.column("Col4", width=100)
        tv.column("Col5", width=100)
        tv.heading("#0", text="", anchor="w")
        tv.heading("Col1", text="Result ID", anchor="w")
        tv.heading("Col2", text="Student ID", anchor="w")
        tv.heading("Col3", text="Exam ID", anchor="center")
        tv.heading("Col4", text="Marks Obtained", anchor="w")
        tv.heading("Col5", text="Result", anchor="w")
        # count = 0
        # for i in range(20):
        #     self.tv.insert(parent='', index="end", iid=count, text="Parent" + str(count),
        #                    values=("Col1" + str(count), "Col2" + str(count), "Col3" + str(count)))
        #     count += 1

        self.add_button = tk.Button(self.Canvas1, activebackground="#ececec", activeforeground="#000000",
                                    background="#3F454C",
                                    borderwidth="0", disabledforeground="#a3a3a3",
                                    font="-family {Segoe UI} -size 9 "
                                         "-weight bold",
                                    foreground="white", highlightbackground="#d9d9d9", highlightcolor="black",
                                    pady="0", text='''Add''', command=self.select_add)
        self.add_button.place(relx=0.402, rely=0.871, height=24, width=79)

        self.delete_button = tk.Button(self.Canvas1, activebackground="#ececec", activeforeground="#000000",
                                       background="#3F454C",
                                       borderwidth="0", disabledforeground="#a3a3a3",
                                       font="-family {Segoe UI} -size 9 "
                                            "-weight bold",
                                       foreground="white", highlightbackground="#d9d9d9", highlightcolor="black",
                                       text="Delete", command=self.select_delete)
        self.delete_button.place(relx=0.593, rely=0.871, height=24, width=79)

        self.modify_button = tk.Button(self.Canvas1, activebackground="#ececec", activeforeground="#000000",
                                       background="#3F454C",
                                       borderwidth="0", disabledforeground="#a3a3a3",
                                       font="-family {Segoe UI} -size 9 -weight bold",
                                       foreground="white", highlightbackground="#d9d9d9", highlightcolor="black",
                                       text='''Modify''', command=self.select_modify)
        self.modify_button.place(relx=0.784, rely=0.871, height=24, width=79)

        self.back_button = tk.Button(self.Canvas1, activebackground="#ececec", activeforeground="#000000",
                                     background="#343a40",
                                     borderwidth="0", disabledforeground="#a3a3a3",
                                     font="-family {Segoe UI} -size 9 -weight bold", foreground="#ffffff",
                                     highlightbackground="#d9d9d9", highlightcolor="black", pady="0",
                                     text='''Back''',
                                     command=self.back)
        self.back_button.place(relx=0.038, rely=0.871, height=24, width=79)

        # real data
        mycursor.execute("SELECT * from result;")
        output = mycursor.fetchall()

        for list_item in output:
            tv.insert(parent='', index="end", text="Parent", values=(
                str(list_item[0]), str(list_item[1]), str(list_item[2]), str(list_item[3]), str(list_item[4])))

    def back(self):
        self.master.withdraw()
        MainScreen(Toplevel(self.master))

    def select_modify(self):
        if tv.focus() != "":
            ResultModify(Toplevel(self.master))
        else:
            messagebox.showerror("Error Message", "Please select a row to be modified")

    def select_delete(self):
        try:
            #            row_id = int(tv.focus().replace("I", ""))
            item = tv.item(tv.focus())
            tv.delete(tv.focus())
            sql_query = "DELETE FROM result WHERE result_id=" + str(item['values'][0]) + ";"
            try:
                mycursor.execute(sql_query)  # executing query
            except (mysql.connector.Error, mysql.connector.Warning) as e:  # fetching error
                messagebox.showerror("Error Message", "ERROR MESSAGE\n" + str(e))  # displaying error

        except:
            messagebox.showerror("Error Message", "Please select a row to be deleted")
        mydb.commit()

    def select_add(self):
        ResultAdd(Toplevel(self.master))


class Subject:
    def __init__(self, top=None):
        self.master = top
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.', background='#d9d9d9')
        self.style.configure('.', foreground="#000000")
        self.style.configure('.', font="TkDefaultFont")
        self.style.map('.', background=
        [('selected', "#d9d9d9"), ('active', "#ececec")])

        top.geometry("600x450+383+106")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(0, 0)
        top.title("Subject")
        top.configure(background="#212529")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Canvas1 = tk.Canvas(top, background="white", insertbackground="black", highlightbackground="#d9d9d9",
                                 highlightcolor="black", relief="ridge", selectbackground="blue",
                                 selectforeground="white")
        self.Canvas1.place(relx=0.067, rely=0.111, relheight=0.74
                           , relwidth=0.872)

        self.Label1 = tk.Label(top, background="#212529", font="-family {Segoe UI} -size 13 -weight bold",
                               foreground="#ffffff", text='''Subject Table''')
        self.Label1.place(relx=0.367, rely=0.022, height=31, width=174)

        self.style.configure('Treeview', font="TkDefaultFont", borderwidth=0)
        global tv
        tv = ScrolledTreeView(self.Canvas1)
        tv.place(relx=0.0, rely=0.0, relheight=0.712, relwidth=1.0)
        tv['columns'] = ("Col1", "Col2", "Col3", "Col4")
        tv.column("#0", width=0, stretch="NO")
        tv.column("Col1", width=100)
        tv.column("Col2", width=100, anchor="center")
        tv.column("Col3", width=100)
        tv.column("Col4", width=100)
        tv.heading("#0", text="", anchor="w")
        tv.heading("Col1", text="Subject Code", anchor="w")
        tv.heading("Col2", text="Branch ID", anchor="w")
        tv.heading("Col3", text="Subject Name", anchor="center")
        tv.heading("Col4", text="Subject Credit", anchor="w")
        # count = 0
        # for i in range(20):
        #     self.tv.insert(parent='', index="end", iid=count, text="Parent" + str(count),
        #                    values=("Col1" + str(count), "Col2" + str(count), "Col3" + str(count)))
        #     count += 1

        self.add_button = tk.Button(self.Canvas1, activebackground="#ececec", activeforeground="#000000",
                                    background="#3F454C",
                                    borderwidth="0", disabledforeground="#a3a3a3",
                                    font="-family {Segoe UI} -size 9 "
                                         "-weight bold",
                                    foreground="white", highlightbackground="#d9d9d9", highlightcolor="black",
                                    pady="0", text='''Add''', command=self.select_add)
        self.add_button.place(relx=0.402, rely=0.871, height=24, width=79)

        self.delete_button = tk.Button(self.Canvas1, activebackground="#ececec", activeforeground="#000000",
                                       background="#3F454C",
                                       borderwidth="0", disabledforeground="#a3a3a3",
                                       font="-family {Segoe UI} -size 9 "
                                            "-weight bold",
                                       foreground="white", highlightbackground="#d9d9d9",
                                       highlightcolor="black",
                                       text="Delete", command=self.select_delete)
        self.delete_button.place(relx=0.593, rely=0.871, height=24, width=79)

        self.modify_button = tk.Button(self.Canvas1, activebackground="#ececec", activeforeground="#000000",
                                       background="#3F454C",
                                       borderwidth="0", disabledforeground="#a3a3a3",
                                       font="-family {Segoe UI} -size 9 -weight bold",
                                       foreground="white", highlightbackground="#d9d9d9",
                                       highlightcolor="black",
                                       text='''Modify''', command=self.select_modify)
        self.modify_button.place(relx=0.784, rely=0.871, height=24, width=79)

        self.back_button = tk.Button(self.Canvas1, activebackground="#ececec", activeforeground="#000000",
                                     background="#343a40",
                                     borderwidth="0", disabledforeground="#a3a3a3",
                                     font="-family {Segoe UI} -size 9 -weight bold", foreground="#ffffff",
                                     highlightbackground="#d9d9d9", highlightcolor="black", pady="0",
                                     text='''Back''',
                                     command=self.back)
        self.back_button.place(relx=0.038, rely=0.871, height=24, width=79)

        # real data
        mycursor.execute("SELECT * from subject;")
        output = mycursor.fetchall()

        for list_item in output:
            tv.insert(parent='', index="end", text="Parent",
                      values=(str(list_item[0]), str(list_item[1]), str(list_item[2]), str(list_item[3])))

    def back(self):
        self.master.withdraw()
        MainScreen(Toplevel(self.master))

    def select_modify(self):
        if tv.focus() != "":
            SubjectModify(Toplevel(self.master))
        else:
            messagebox.showerror("Error Message", "Please select a row to be modified")

    def select_delete(self):
        try:
            #            row_id = int(tv.focus().replace("I", ""))
            item = tv.item(tv.focus())
            tv.delete(tv.focus())
            sql_query = "DELETE FROM subject WHERE subject_code='" + str(item['values'][0]) + "';"
            try:
                mycursor.execute(sql_query)  # executing query
            except (mysql.connector.Error, mysql.connector.Warning) as e:  # fetching error
                messagebox.showerror("Error Message", str(e))  # displaying error

        except:
            messagebox.showerror("Error Message", "Please select a row to be deleted")
        mydb.commit()

    def select_add(self):
        SubjectAdd(Toplevel(self.master))


class Attendance:
    def __init__(self, top=None):
        self.master = top
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.', background='#d9d9d9')
        self.style.configure('.', foreground="#000000")
        self.style.configure('.', font="TkDefaultFont")
        self.style.map('.', background=
        [('selected', "#d9d9d9"), ('active', "#ececec")])

        top.geometry("600x450+383+106")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(0, 0)
        top.title("Attendance")
        top.configure(background="#212529")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Canvas1 = tk.Canvas(top, background="white", insertbackground="black",
                                 highlightbackground="#d9d9d9", highlightcolor="black", relief="ridge",
                                 selectbackground="blue", selectforeground="white")
        self.Canvas1.place(relx=0.067, rely=0.111, relheight=0.74
                           , relwidth=0.872)

        self.Label1 = tk.Label(top, background="#212529", font="-family {Segoe UI} -size 13 -weight bold",
                               foreground="#ffffff", text='''Attendance Table''')
        self.Label1.place(relx=0.367, rely=0.022, height=31, width=174)

        self.style.configure('Treeview', font="TkDefaultFont", borderwidth=0)
        global tv
        tv = ScrolledTreeView(self.Canvas1)
        tv.place(relx=0.0, rely=0.0, relheight=0.712, relwidth=1.0)
        tv['columns'] = ("Col1", "Col2", "Col3", "Col4", "Col5")
        tv.column("#0", width=0, stretch="NO")
        tv.column("Col1", width=100)
        tv.column("Col2", width=100)
        tv.column("Col3", width=100, anchor="center")
        tv.column("Col4", width=100)
        tv.column("Col5", width=100)
        tv.heading("#0", text="", anchor="w")
        tv.heading("Col1", text="Attendance ID", anchor="w")
        tv.heading("Col2", text="Student ID", anchor="w")
        tv.heading("Col3", text="Exam ID", anchor="center")
        tv.heading("Col4", text="Login Time", anchor="w")
        tv.heading("Col5", text="Logout Time", anchor="w")
        # count = 0
        # for i in range(20):
        #     self.tv.insert(parent='', index="end", iid=count, text="Parent" + str(count),
        #                    values=("Col1" + str(count), "Col2" + str(count), "Col3" + str(count)))
        #     count += 1

        self.add_button = tk.Button(self.Canvas1, activebackground="#ececec", activeforeground="#000000",
                                    background="#3F454C",
                                    borderwidth="0", disabledforeground="#a3a3a3",
                                    font="-family {Segoe UI} -size 9 "
                                         "-weight bold",
                                    foreground="white", highlightbackground="#d9d9d9",
                                    highlightcolor="black",
                                    pady="0", text='''Add''', command=self.select_add)
        self.add_button.place(relx=0.402, rely=0.871, height=24, width=79)

        self.delete_button = tk.Button(self.Canvas1, activebackground="#ececec", activeforeground="#000000",
                                       background="#3F454C",
                                       borderwidth="0", disabledforeground="#a3a3a3",
                                       font="-family {Segoe UI} -size 9 "
                                            "-weight bold",
                                       foreground="white", highlightbackground="#d9d9d9",
                                       highlightcolor="black",
                                       text="Delete", command=self.select_delete)
        self.delete_button.place(relx=0.593, rely=0.871, height=24, width=79)

        self.modify_button = tk.Button(self.Canvas1, activebackground="#ececec", activeforeground="#000000",
                                       background="#3F454C",
                                       borderwidth="0", disabledforeground="#a3a3a3",
                                       font="-family {Segoe UI} -size 9 -weight bold",
                                       foreground="white", highlightbackground="#d9d9d9",
                                       highlightcolor="black",
                                       text='''Modify''', command=self.select_modify)
        self.modify_button.place(relx=0.784, rely=0.871, height=24, width=79)

        self.back_button = tk.Button(self.Canvas1, activebackground="#ececec", activeforeground="#000000",
                                     background="#343a40",
                                     borderwidth="0", disabledforeground="#a3a3a3",
                                     font="-family {Segoe UI} -size 9 -weight bold", foreground="#ffffff",
                                     highlightbackground="#d9d9d9", highlightcolor="black", pady="0",
                                     text='''Back''',
                                     command=self.back)
        self.back_button.place(relx=0.038, rely=0.871, height=24, width=79)

        # real data
        mycursor.execute("SELECT * from attendance;")
        output = mycursor.fetchall()

        for list_item in output:
            tv.insert(parent='', index="end", text="Parent", values=(
                str(list_item[0]), str(list_item[1]), str(list_item[2]), str(list_item[3]), str(list_item[4])))

    def back(self):
        self.master.withdraw()
        MainScreen(Toplevel(self.master))

    def select_modify(self):
        if tv.focus() != "":
            AttendanceModify(Toplevel(self.master))
        else:
            messagebox.showerror("Error Message", "Please select a row to be modified")

    def select_delete(self):
        try:
            #            row_id = int(tv.focus().replace("I", ""))
            item = tv.item(tv.focus())
            tv.delete(tv.focus())
            sql_query = "DELETE FROM attendance WHERE attendance_id=" + str(item['values'][0]) + ";"
            try:
                mycursor.execute(sql_query)  # executing query
            except (mysql.connector.Error, mysql.connector.Warning) as e:  # fetching error
                messagebox.showerror("Error Message", str(e))  # displaying error

        except:
            messagebox.showerror("Error Message", "Please select a row to be deleted")
        mydb.commit()

    def select_add(self):
        AttendanceAdd(Toplevel(self.master))


class Branch:
    def __init__(self, top=None):
        self.master = top
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.', background='#d9d9d9')
        self.style.configure('.', foreground="#000000")
        self.style.configure('.', font="TkDefaultFont")
        self.style.map('.', background=
        [('selected', "#d9d9d9"), ('active', "#ececec")])

        top.geometry("600x450+383+106")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(0, 0)
        top.title("Branch")
        top.configure(background="#212529")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Canvas1 = tk.Canvas(top, background="white", insertbackground="black",
                                 highlightbackground="#d9d9d9", highlightcolor="black", relief="ridge",
                                 selectbackground="blue", selectforeground="white")
        self.Canvas1.place(relx=0.067, rely=0.111, relheight=0.74
                           , relwidth=0.872)

        self.Label1 = tk.Label(top, background="#212529", font="-family {Segoe UI} -size 13 -weight bold",
                               foreground="#ffffff", text='''Branch Table''')
        self.Label1.place(relx=0.367, rely=0.022, height=31, width=174)

        self.style.configure('Treeview', font="TkDefaultFont", borderwidth=0)
        global tv
        tv = ScrolledTreeView(self.Canvas1)
        tv.place(relx=0.0, rely=0.0, relheight=0.712, relwidth=1.0)
        tv['columns'] = ("Col1", "Col2")
        tv.column("#0", width=0, stretch="NO")
        tv.column("Col1", width=100)
        tv.column("Col2", width=100, anchor="center")
        tv.heading("#0", text="", anchor="w")
        tv.heading("Col1", text="Branch ID", anchor="w")
        tv.heading("Col2", text="Branch Name", anchor="center")

        #        count = 0
        #        for i in range(20):
        #            self.tv.insert(parent='', index="end", iid=count, text="Parent" + str(count),
        #                values=("Col1 long long long long long long long long long long long text" + str(count), "Col2 such a long freaking text" + str(count)))
        #            count += 1

        self.add_button = tk.Button(self.Canvas1, command=self.select_add, activebackground="#ececec",
                                    activeforeground="#000000", background="#3F454C",
                                    borderwidth="0", disabledforeground="#a3a3a3",
                                    font="-family {Segoe UI} -size 9 "
                                         "-weight bold",
                                    foreground="white", highlightbackground="#d9d9d9",
                                    highlightcolor="black",
                                    pady="0", text='''Add''')
        self.add_button.place(relx=0.402, rely=0.871, height=24, width=79)

        self.delete_button = tk.Button(self.Canvas1, command=self.select_delete, activebackground="#ececec",
                                       activeforeground="#000000", background="#3F454C",
                                       borderwidth="0", disabledforeground="#a3a3a3",
                                       font="-family {Segoe UI} -size 9 "
                                            "-weight bold",
                                       foreground="white", highlightbackground="#d9d9d9",
                                       highlightcolor="black",
                                       text="Delete")
        self.delete_button.place(relx=0.593, rely=0.871, height=24, width=79)

        self.modify_button = tk.Button(self.Canvas1, command=self.select_modify, activebackground="#ececec",
                                       activeforeground="#000000", background="#3F454C",
                                       borderwidth="0", disabledforeground="#a3a3a3",
                                       font="-family {Segoe UI} -size 9 -weight bold",
                                       foreground="white", highlightbackground="#d9d9d9",
                                       highlightcolor="black",
                                       text='''Modify''')
        self.modify_button.place(relx=0.784, rely=0.871, height=24, width=79)

        self.back_button = tk.Button(self.Canvas1, activebackground="#ececec", activeforeground="#000000",
                                     background="#343a40",
                                     borderwidth="0", disabledforeground="#a3a3a3",
                                     font="-family {Segoe UI} -size 9 -weight bold", foreground="#ffffff",
                                     highlightbackground="#d9d9d9", highlightcolor="black", pady="0",
                                     text='''Back''',
                                     command=self.back)
        self.back_button.place(relx=0.038, rely=0.871, height=24, width=79)

        # real data
        mycursor.execute("SELECT * from branch;")
        output = mycursor.fetchall()

        for list_item in output:
            tv.insert(parent='', index="end", text="Parent",

                      values=(str(list_item[0]), str(list_item[1])))

    def back(self):
        self.master.withdraw()
        MainScreen(Toplevel(self.master))

    def select_modify(self):
        if tv.focus() != "":
            BranchModify(Toplevel(self.master))
        else:
            messagebox.showerror("Error Message", "Please select a row to be modified")

    def select_delete(self):
        try:
            #            row_id = int(tv.focus().replace("I", ""))
            item = tv.item(tv.focus())
            tv.delete(tv.focus())
            sql_query = "DELETE FROM branch WHERE branch_id=" + str(item['values'][0]) + ";"
            try:
                mycursor.execute(sql_query)  # executing query
            except (mysql.connector.Error, mysql.connector.Warning) as e:  # fetching error
                messagebox.showerror("Error Message", "ERROR MESSAGE\n" + str(e))  # displaying error

        except:
            messagebox.showerror("Error Message", "Please select a row to be deleted")
        mydb.commit()

    def select_add(self):
        BranchAdd(Toplevel(self.master))


class CustomQuery:
    def __init__(self, top=None):
        self.master = top
        '''This class configures and populates the toplevel window.
                        top is the toplevel containing window.'''
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.', background="#d9d9d9")
        self.style.configure('.', foreground="#000000")
        self.style.map('.', background=[('selected', "#d9d9d9"), ('active', "#ececec")])

        top.geometry("705x450+373+129")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(0, 0)
        top.title("Custom Query")
        top.configure(background="#212529")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Label1 = tk.Label(top, activebackground="#f9f9f9", activeforeground="black", background="#212529",
                               disabledforeground="#a3a3a3", foreground="#ffffff", highlightbackground="#d9d9d9",
                               highlightcolor="black", text='''Query :''')
        self.Label1.place(relx=0.014, rely=0.067, height=19, width=53)

        self.Entry1 = tk.Entry(top, background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                               foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                               insertbackground="black", selectbackground="blue", selectforeground="white")
        self.Entry1.place(relx=0.085, rely=0.067, height=20, relwidth=0.743)

        self.execute_button = tk.Button(top, command=self.select_execute, activebackground="#ececec",
                                        activeforeground="#000000", background="#CED4DA", disabledforeground="#a3a3a3",
                                        foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                        pady="0", text='''Execute''')
        self.execute_button.place(relx=0.851, rely=0.067, height=24, width=87)

        self.clear_button = tk.Button(top, command=self.select_clear, activebackground="#ececec",
                                      activeforeground="#000000", background="#CED4DA", disabledforeground="#a3a3a3",
                                      foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                      pady="0", text='''Clear''')
        self.clear_button.place(relx=0.539, rely=0.889, height=24, width=87)

        global Scrolledtext1
        Scrolledtext1 = ScrolledText(top, state="disable", background="white", font="TkTextFont", foreground="black",
                                     highlightbackground="#d9d9d9", highlightcolor="black", insertbackground="black",
                                     insertborderwidth="3", selectbackground="blue", selectforeground="white",
                                     wrap="none")
        Scrolledtext1.place(relx=0.028, rely=0.2, relheight=0.633
                            , relwidth=0.945)

        self.back_button = tk.Button(top, command=self.back, activebackground="#ececec", activeforeground="#000000",
                                     background="#CED4DA", disabledforeground="#a3a3a3", foreground="#000000",
                                     highlightbackground="#d9d9d9", highlightcolor="black", pady="0", text='''Back''')
        self.back_button.place(relx=0.355, rely=0.889, height=24, width=87)
        self.column_names = []
        self.err_for_column_names = ""

    def get_columns(self, table_name):
        sql_q = "SELECT `COLUMN_NAME` FROM `INFORMATION_SCHEMA`.`COLUMNS` WHERE `TABLE_SCHEMA`='innovative_assignment' AND `TABLE_NAME`='" + table_name.replace(
            ";", "") + "';"
        try:
            mycursor.execute(sql_q)  # executing query
            self.column_names1 = mycursor.fetchall()
            self.column_names = list(map(lambda x: x[0], self.column_names1))
            print(column for column in self.column_names)
            for i in range(len(self.column_names)):
                print(type(self.column_names[i]))
                self.column_names[i] = self.column_names[i].replace(",", "")

            print(self.column_names)

        except (mysql.connector.Error, mysql.connector.Warning) as e:  # fetching error
            self.err_for_column_names = str(e)
            print(self.err_for_column_names)

    def get_table_name(self, query_string):
        words = query_string.lower().split()
        print(words, words[words.index("from") + 1])
        return words[words.index("from") + 1]

    def select_execute(self):
        self.column_names = []
        self.err_for_column_names = ""
        sql_query = self.Entry1.get()  # getting text from entry
        print(sql_query)

        if "unlock" == sql_query:
            Scrolledtext1.config(state="normal")
            return
        elif "lock" == sql_query:
            Scrolledtext1.config(state="disable")
            return
        elif "credits" == sql_query:
            Scrolledtext1.config(state="normal")
            Scrolledtext1.delete("1.0", "end")
            Scrolledtext1.insert(1.0,
                                 "This project is created by : \n\t19BCE237 Sakshi Sanghavi\n\t19BCE238 Harshil Sanghvi\n\t19BCE245 Aayush Shah")
            Scrolledtext1.config(state="disable")
            return

        if ("from" in sql_query) and ("select *" in sql_query) and (sql_query.count("join") == 0):
            print("hello")
            self.get_columns(self.get_table_name(sql_query))
        else:
            print("NOT HELLO")

        try:
            mycursor.execute(sql_query)  # executing query
            self.display_output(mycursor.fetchall(), 1)  # displaying output
        except (mysql.connector.Error, mysql.connector.Warning) as e:  # fetching error
            self.display_output("ERROR MESSAGE : \n" + self.err_for_column_names + "\n" + str(e), 2)  # displaying error
        mydb.commit()

    def select_clear(self):
        Scrolledtext1.config(state="normal")
        self.Entry1.delete(0, 'end')
        Scrolledtext1.delete("1.0", "end")
        Scrolledtext1.config(state="disable")

    def display_output(self, output_message, choice):

        Scrolledtext1.config(state="normal")  # changing text box's state so that we can edit it
        Scrolledtext1.delete("1.0", "end")  # deletes previous contents

        if choice == 1:  # select statement
            myTable = PrettyTable(self.column_names)
            for list_item in output_message:
                myTable.add_row(list_item)
            print(myTable)
            Scrolledtext1.insert(1.0, myTable)  # showing output message

        else:  # not select  statement
            print(output_message)
            Scrolledtext1.insert(1.0, output_message)  # showing output message
        Scrolledtext1.config(state="disable")  # disabling text box's state so that user cannot change it's content

    def back(self):
        self.master.withdraw()
        MainScreen(Toplevel(self.master))


class AutoScroll(object):
    """Configure the scrollbars for a widget."""

    def __init__(self, master):
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))
        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')
        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)
        # Copy geometry methods of master  (taken from ScrolledText.py)
        if py3:
            methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() | tk.Place.__dict__.keys()
        else:
            methods = tk.Pack.__dict__.keys() + tk.Grid.__dict__.keys() + tk.Place.__dict__.keys()
        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        """Hide and show scrollbar as needed."""

        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)

        return wrapped

    def __str__(self):
        return str(self.master)


def _create_container(func):
    """Creates a ttk Frame with a given master, and use this new frame to
                place the scrollbars and the widget."""

    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)

    return wrapped


class ScrolledText(AutoScroll, tk.Text):
    """A standard Tkinter Text widget with scrollbars that will
    automatically show/hide as needed."""

    @_create_container
    def __init__(self, master, **kw):
        tk.Text.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)


class ScrolledTreeView(AutoScroll, ttk.Treeview):
    """A standard ttk Treeview widget with scrollbars that will
                automatically show/hide as needed."""

    @_create_container
    def __init__(self, master, **kw):
        ttk.Treeview.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)


def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))


def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')


def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1 * int(event.delta / 120), 'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1 * int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')


def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1 * int(event.delta / 120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1 * int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')


class BranchAdd:
    def __init__(self, top=None):
        self.master = top
        top.geometry("342x139+527+141")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(0, 0)
        top.title("Add")
        top.configure(background="#CED4DA")

        self.id_label = tk.Label(top, background="#CED4DA", disabledforeground="#a3a3a3", foreground="#000000",
                                 text='''Branch id :''')
        self.id_label.place(relx=0.234, rely=0.144, height=17, width=74)

        self.name_label = tk.Label(top, background="#CED4DA", disabledforeground="#a3a3a3", foreground="#000000",
                                   text='''Branch name :''')
        self.name_label.place(relx=0.187, rely=0.36, height=17, width=84)

        self.id_entry = tk.Entry(top, background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                 foreground="#000000", insertbackground="black")
        self.id_entry.place(relx=0.468, rely=0.144, height=20, relwidth=0.304)

        self.name_entry = tk.Entry(top, background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                   foreground="#000000", insertbackground="black")
        self.name_entry.place(relx=0.468, rely=0.36, height=20, relwidth=0.304)

        self.back_button = tk.Button(top, command=self.select_back, activebackground="#ececec",
                                     activeforeground="#000000", background="#E9ECEF", disabledforeground="#a3a3a3",
                                     foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                     pady="0", text='''Back''')
        self.back_button.place(relx=0.146, rely=0.647, height=24, width=87)

        self.add_button = tk.Button(top, command=lambda: self.select_add(self.id_entry.get(),
                                                                         self.name_entry.get()),
                                    activebackground="#ececec", activeforeground="#000000", background="#E9ECEF",
                                    disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                                    highlightcolor="black", pady="0", text='''Add''')
        self.add_button.place(relx=0.556, rely=0.647, height=24, width=87)

    def select_back(self):
        self.master.withdraw()

    def select_add(self, branch_id, branch_name):
        if branch_id.isnumeric() and len(branch_id) != 0:
            if branch_name.replace(" ", "").isalpha() and len(branch_name) != 0:

                sql_query = "INSERT INTO branch VALUES(" + branch_id + ", '" + branch_name + "');"
                try:
                    mycursor.execute(sql_query)  # executing query
                    tv.insert(parent='', index='end', text="Parent", values=(str(branch_id), branch_name))
                    print("inside try : ", mycursor.fetchall())
                except (mysql.connector.Error, mysql.connector.Warning) as e:  # fetching error
                    messagebox.showerror("Error Message", "ERROR MESSAGE :\n" + str(e))
                    print("inside except : ", mycursor.fetchall())  # displaying error

            else:
                messagebox.showerror("Error Message", "ERROR MESSAGE\n" + "Enter proper branch name")
        else:
            messagebox.showerror("Error Message", "ERROR MESSAGE\n" + "Enter proper branch id")
        print(branch_id, branch_name)
        self.master.withdraw()
        mydb.commit()


class AttendanceAdd:
    def __init__(self, top=None):
        self.master = top
        top.geometry("342x224+434+151")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(0, 0)
        top.title("Add")
        top.configure(background="#CED4DA")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.att_id_label = tk.Label(top, activebackground="#f9f9f9", activeforeground="black", background="#CED4DA",
                                     disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                                     highlightcolor="black", text='''Attendance id :''')
        self.att_id_label.place(relx=0.152, rely=0.089, height=15, width=94)

        self.login_label = tk.Label(top, activebackground="#f9f9f9", activeforeground="black", background="#CED4DA",
                                    disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                                    highlightcolor="black", text='''Login time :''')
        self.login_label.place(relx=0.205, rely=0.223, height=19, width=74)

        self.att_id_entry = tk.Entry(top, background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                     foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                     insertbackground="black", selectbackground="blue", selectforeground="white")
        self.att_id_entry.place(relx=0.468, rely=0.089, height=20
                                , relwidth=0.304)

        time_format1 = StringVar(top, value='HH:MM:SS')
        time_format2 = StringVar(top, value='HH:MM:SS')
        self.login_entry = tk.Entry(top, background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                    foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                    insertbackground="black", selectbackground="blue", selectforeground="white",
                                    textvariable=time_format1)
        self.login_entry.place(relx=0.468, rely=0.223, height=20, relwidth=0.304)

        self.logout_label = tk.Label(top, activebackground="#f9f9f9", activeforeground="black", background="#CED4DA",
                                     disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                                     highlightcolor="black", text='''Logout time :''')
        self.logout_label.place(relx=0.175, rely=0.357, height=19, width=84)

        self.student_id_label = tk.Label(top, activebackground="#f9f9f9", activeforeground="black",
                                         background="#CED4DA", disabledforeground="#a3a3a3", foreground="#000000",
                                         highlightbackground="#d9d9d9", highlightcolor="black", text='''Student id :''')
        self.student_id_label.place(relx=0.205, rely=0.491, height=19, width=74)

        self.exam_id_label = tk.Label(top, activebackground="#f9f9f9", activeforeground="black", background="#CED4DA",
                                      disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                                      highlightcolor="black", text='''Exam id :''')
        self.exam_id_label.place(relx=0.219, rely=0.625, height=21, width=74)

        self.logout_entry = tk.Entry(top, background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                     foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                     insertbackground="black", selectbackground="blue", selectforeground="white",
                                     textvariable=time_format2)
        self.logout_entry.place(relx=0.468, rely=0.357, height=20
                                , relwidth=0.304)

        self.student_id_entry = tk.Entry(top, background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                         foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                         insertbackground="black", selectbackground="blue", selectforeground="white")
        self.student_id_entry.place(relx=0.468, rely=0.491, height=20
                                    , relwidth=0.304)

        self.exam_id_entry = tk.Entry(top, background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                      foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                      insertbackground="black", selectbackground="blue", selectforeground="white")
        self.exam_id_entry.place(relx=0.468, rely=0.625, height=20
                                 , relwidth=0.304)

        self.add_button = tk.Button(top, activebackground="#ececec", activeforeground="#000000", background="#E9ECEF",
                                    disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                                    highlightcolor="black", pady="0", text='''Add''',
                                    command=lambda: self.select_add(self.att_id_entry.get(),
                                                                    self.student_id_entry.get(),
                                                                    self.exam_id_entry.get(), self.login_entry.get(),
                                                                    self.logout_entry.get()))
        self.add_button.place(relx=0.585, rely=0.804, height=24, width=87)

        self.back_button = tk.Button(top, activebackground="#ececec", activeforeground="#000000", background="#E9ECEF",
                                     disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                                     highlightcolor="black", pady="0", text='''Back''', command=self.select_back)
        self.back_button.place(relx=0.175, rely=0.804, height=24, width=87)

    def select_back(self):
        self.master.withdraw()

    def select_add(self, attendance_id, student_id, exam_id, login_time, logout_time):
        if len(attendance_id) != 0 and len(student_id) != 0 and len(exam_id) != 0 and len(login_time) != 0 and len(
                logout_time) != 0:

            if login_time != logout_time:
                sql_query = "INSERT INTO attendance VALUES(" + str(attendance_id) + ", " + str(student_id) + ", " + str(
                    exam_id) + ", TIME('" + login_time + "'), TIME('" + logout_time + "'));"
                try:
                    mycursor.execute(sql_query)  # executing query
                    tv.insert(parent='', index='end', text="Parent",
                              values=(str(attendance_id), str(student_id), str(exam_id), login_time, logout_time))
                    print("inside try : ", mycursor.fetchall())
                except (mysql.connector.Error, mysql.connector.Warning) as e:  # fetching error
                    messagebox.showerror("Error Message", "ERROR MESSAGE :\n" + str(e))
                    print("inside except : ", mycursor.fetchall())  # displaying error
            else:
                messagebox.showerror("Error Message", "Login time cannot be equal to logout time!")

        else:
            messagebox.showerror("Error Message", "No field should be empty")
        print(attendance_id, student_id, exam_id, login_time, logout_time)
        self.master.withdraw()
        mydb.commit()


class ExamAdd:
    def __init__(self, top=None):
        self.master = top
        top.geometry("342x316+624+174")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(0, 0)
        top.title("Add")
        top.configure(background="#CED4DA")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.exam_id_label = tk.Label(top, activebackground="#f9f9f9", activeforeground="black", background="#CED4DA",
                                      disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                                      highlightcolor="black", text='''Exam id :''')
        self.exam_id_label.place(relx=0.234, rely=0.063, height=21, width=64)

        self.exam_duration_label = tk.Label(top, activebackground="#f9f9f9", activeforeground="black",
                                            background="#CED4DA", disabledforeground="#a3a3a3", foreground="#000000",
                                            highlightbackground="#d9d9d9", highlightcolor="black",
                                            text='''Exam duration :''')
        self.exam_duration_label.place(relx=0.14, rely=0.253, height=18
                                       , width=94)

        self.exam_id_entry = tk.Entry(top, background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                      foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                      insertbackground="black", selectbackground="blue", selectforeground="white")
        self.exam_id_entry.place(relx=0.468, rely=0.063, height=20
                                 , relwidth=0.304)

        self.name_entry = tk.Entry(top, background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                   foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                   insertbackground="black", selectbackground="blue", selectforeground="white")
        self.name_entry.place(relx=0.468, rely=0.158, height=20, relwidth=0.304)

        self.tot_ques_label = tk.Label(top, activebackground="#f9f9f9", activeforeground="black", background="#CED4DA",
                                       disabledforeground="#a3a3a3", foreground="#000000",
                                       highlightbackground="#d9d9d9", highlightcolor="black",
                                       text='''Total questions :''')
        self.tot_ques_label.place(relx=0.117, rely=0.443, height=18, width=104)

        self.branch_id_label = tk.Label(top, activebackground="#f9f9f9", activeforeground="black", background="#CED4DA",
                                        disabledforeground="#a3a3a3", foreground="#000000",
                                        highlightbackground="#d9d9d9", highlightcolor="black", text='''Branch id :''')
        self.branch_id_label.place(relx=0.205, rely=0.633, height=18, width=74)

        time_format = StringVar(top, value='HH:MM:SS')
        self.duration_entry = tk.Entry(top, background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                       foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                       insertbackground="black", selectbackground="blue", selectforeground="white",
                                       textvariable=time_format)
        self.duration_entry.place(relx=0.468, rely=0.253, height=20
                                  , relwidth=0.304)

        date_format = StringVar(top, value='YYYY-MM-DD')
        self.date_entry = tk.Entry(top, background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                   foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                   insertbackground="black", selectbackground="blue", selectforeground="white",
                                   textvariable=date_format)
        self.date_entry.place(relx=0.468, rely=0.348, height=20, relwidth=0.304)

        self.tot_ques_entry = tk.Entry(top, background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                       foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                       insertbackground="black", selectbackground="blue", selectforeground="white")
        self.tot_ques_entry.place(relx=0.468, rely=0.443, height=20
                                  , relwidth=0.304)

        self.tot_marks_entry = tk.Entry(top, background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                        foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                        insertbackground="black", selectbackground="blue", selectforeground="white")
        self.tot_marks_entry.place(relx=0.468, rely=0.538, height=20
                                   , relwidth=0.304)

        self.branch_id_entry = tk.Entry(top, background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                        foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                        insertbackground="black", selectbackground="blue", selectforeground="white")
        self.branch_id_entry.place(relx=0.468, rely=0.633, height=20
                                   , relwidth=0.304)

        self.sub_code_entry = tk.Entry(top, background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                       foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                       insertbackground="black", selectbackground="blue", selectforeground="white")
        self.sub_code_entry.place(relx=0.468, rely=0.728, height=20
                                  , relwidth=0.304)

        self.exam_name_label = tk.Label(top, activebackground="#f9f9f9", activeforeground="black", background="#CED4DA",
                                        disabledforeground="#a3a3a3", foreground="#000000",
                                        highlightbackground="#d9d9d9", highlightcolor="black", text='''Exam name :''')
        self.exam_name_label.place(relx=0.175, rely=0.158, height=21, width=84)

        self.exam_date_label = tk.Label(top, activebackground="#f9f9f9", activeforeground="black", background="#CED4DA",
                                        disabledforeground="#a3a3a3", foreground="#000000",
                                        highlightbackground="#d9d9d9", highlightcolor="black", text='''Exam date :''')
        self.exam_date_label.place(relx=0.199, rely=0.348, height=21, width=74)

        self.tot_marks_label = tk.Label(top, activebackground="#f9f9f9", activeforeground="black", background="#CED4DA",
                                        disabledforeground="#a3a3a3", foreground="#000000",
                                        highlightbackground="#d9d9d9", highlightcolor="black", text='''Total marks :''')
        self.tot_marks_label.place(relx=0.175, rely=0.538, height=21, width=84)

        self.sub_code_label = tk.Label(top, activebackground="#f9f9f9", activeforeground="black", background="#CED4DA",
                                       disabledforeground="#a3a3a3", foreground="#000000",
                                       highlightbackground="#d9d9d9", highlightcolor="black", text='''Subject code :''')
        self.sub_code_label.place(relx=0.164, rely=0.728, height=21, width=84)

        self.back_button = tk.Button(top, activebackground="#ececec", activeforeground="#000000", background="#E9ECEF",
                                     disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                                     highlightcolor="black", pady="0", text='''Back''', command=self.select_back)
        self.back_button.place(relx=0.175, rely=0.854, height=24, width=87)

        self.add_button = tk.Button(top, activebackground="#ececec", activeforeground="#000000", background="#E9ECEF",
                                    disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                                    highlightcolor="black", pady="0", text='''Add''',
                                    command=lambda: self.select_add(self.exam_id_entry.get(), self.name_entry.get(),
                                                                    self.duration_entry.get(), self.date_entry.get(),
                                                                    self.tot_ques_entry.get(),
                                                                    self.tot_marks_entry.get(),
                                                                    self.branch_id_entry.get(),
                                                                    self.sub_code_entry.get()))
        self.add_button.place(relx=0.585, rely=0.854, height=24, width=87)

    def select_back(self):
        self.master.withdraw()

    def select_add(self, exam_id, exam_name, exam_duration, exam_date, exam_question, total_marks, branch_id,
                   subject_code):
        if len(exam_id) != 0 and len(exam_name) != 0 and len(exam_duration) != 0 and len(exam_date) != 0 and len(
                exam_question) != 0 and len(total_marks) != 0 and len(branch_id) != 0 and len(subject_code) != 0:

            print("begin")
            sql_query = "INSERT INTO exam VALUES(" + exam_id + ", '" + exam_name + "', TIME('" + exam_duration + "'), STR_TO_DATE('" + exam_date + "', '%Y-%m-%d'), " + str(
                exam_question) + ", " + str(total_marks) + ", " + str(branch_id) + ", '" + subject_code + "');"
            print("End")
            try:
                mycursor.execute(sql_query)  # executing query
                tv.insert(parent='', index='end', text="Parent", values=(
                    exam_id, exam_name, exam_duration, exam_date, exam_question, total_marks, branch_id, subject_code))
                print("inside try : ", mycursor.fetchall())
            except (mysql.connector.Error, mysql.connector.Warning) as e:  # fetching error
                messagebox.showerror("Error Message", "ERROR MESSAGE :\n" + str(e))
                print("inside except : ", mycursor.fetchall())  # displaying error

        else:
            messagebox.showerror("Error Message", "No field should be empty")
        print(exam_id, exam_name, exam_duration, exam_date, exam_question, total_marks, branch_id, subject_code)
        self.master.withdraw()
        mydb.commit()


class ResultAdd:
    def __init__(self, top=None):
        self.master = top
        top.geometry("342x224+501+160")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(0, 0)
        top.title("Add")
        top.configure(background="#CED4DA")
        top.configure(highlightcolor="black")

        self.res_id_label = tk.Label(top, activebackground="#f9f9f9", activeforeground="black", background="#CED4DA",
                                     disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                                     highlightcolor="black", text='''Result id :''')
        self.res_id_label.place(relx=0.234, rely=0.089, height=15, width=64)

        self.marks_label = tk.Label(top, activebackground="#f9f9f9", activeforeground="black", background="#CED4DA",
                                    disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                                    highlightcolor="black", text='''Marks obtained :''')
        self.marks_label.place(relx=0.117, rely=0.223, height=19, width=104)

        self.res_id_entry = tk.Entry(top, background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                     foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                     insertbackground="black", selectbackground="blue", selectforeground="white")
        self.res_id_entry.place(relx=0.468, rely=0.089, height=20
                                , relwidth=0.304)

        self.marks_entry = tk.Entry(top, background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                    foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                    insertbackground="black", selectbackground="blue", selectforeground="white")
        self.marks_entry.place(relx=0.468, rely=0.223, height=20, relwidth=0.304)

        self.res_label = tk.Label(top, activebackground="#f9f9f9", activeforeground="black", background="#CED4DA",
                                  disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                                  highlightcolor="black", text='''Result :''')
        self.res_label.place(relx=0.263, rely=0.357, height=19, width=54)

        self.student_id_label = tk.Label(top, activebackground="#f9f9f9", activeforeground="black",
                                         background="#CED4DA", disabledforeground="#a3a3a3", foreground="#000000",
                                         highlightbackground="#d9d9d9", highlightcolor="black", text='''Student id :''')
        self.student_id_label.place(relx=0.205, rely=0.491, height=19, width=74)

        self.exam_id_label = tk.Label(top, activebackground="#f9f9f9", activeforeground="black", background="#CED4DA",
                                      disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                                      highlightcolor="black", text='''Exam id :''')
        self.exam_id_label.place(relx=0.219, rely=0.625, height=21, width=74)

        self.res_entry = tk.Entry(top, background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                  foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                  insertbackground="black", selectbackground="blue", selectforeground="white")
        self.res_entry.place(relx=0.468, rely=0.357, height=20, relwidth=0.304)

        self.student_id_entry = tk.Entry(top, background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                         foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                         insertbackground="black", selectbackground="blue", selectforeground="white")
        self.student_id_entry.place(relx=0.468, rely=0.491, height=20
                                    , relwidth=0.304)

        self.exam_id_entry = tk.Entry(top, background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                      foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                      insertbackground="black", selectbackground="blue", selectforeground="white")
        self.exam_id_entry.place(relx=0.468, rely=0.625, height=20
                                 , relwidth=0.304)

        self.back_button = tk.Button(top, activebackground="#ececec", activeforeground="#000000", background="#E9ECEF",
                                     disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                                     highlightcolor="black", pady="0", text='''Back''', command=self.select_back)
        self.back_button.place(relx=0.175, rely=0.804, height=24, width=87)

        self.add_button = tk.Button(top, activebackground="#ececec", activeforeground="#000000", background="#E9ECEF",
                                    disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                                    highlightcolor="black", pady="0", text='''Add''',
                                    command=lambda: self.select_add(self.res_id_entry.get(),
                                                                    self.student_id_entry.get(),
                                                                    self.exam_id_entry.get(), self.marks_entry.get(),
                                                                    self.res_entry.get()))
        self.add_button.place(relx=0.585, rely=0.804, height=24, width=87)

    def select_back(self):
        self.master.withdraw()

    def select_add(self, result_id, student_id, exam_id, marks_obtained, result):
        if len(result_id) != 0 and len(student_id) != 0 and len(exam_id) != 0 and len(marks_obtained) != 0 and len(
                result) != 0:

            sql_query = "INSERT INTO result VALUES(" + result_id + ", " + student_id + ", " + exam_id + ", " + marks_obtained + ", '" + result + "');"
            try:
                print("s0")
                mycursor.execute(sql_query)  # executing query
                print("s1")
                tv.insert(parent='', index='end', text="Parent",
                          values=(str(result_id), str(student_id), str(exam_id), str(marks_obtained), result))
                print("s2")
                print("inside try : ", mycursor.fetchall())
            except (mysql.connector.Error, mysql.connector.Warning) as e:  # fetching error
                messagebox.showerror("Error Message", "ERROR MESSAGE :\n" + str(e))
                print("inside except : ", mycursor.fetchall(), str(e))  # displaying error

        else:
            messagebox.showerror("Error Message", "No field should be empty")
        print(result_id, student_id, exam_id, marks_obtained, result)
        self.master.withdraw()
        mydb.commit()


class StudentAdd:
    def __init__(self, top=None):
        self.master = top
        top.geometry("342x224+510+158")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(0, 0)
        top.title("Add")
        top.configure(background="#CED4DA")

        self.student_id_label = tk.Label(top, activebackground="#f9f9f9", activeforeground="black",
                                         background="#CED4DA", disabledforeground="#a3a3a3", foreground="#000000",
                                         highlightbackground="#d9d9d9", highlightcolor="black",
                                         text='''Student id :''')
        self.student_id_label.place(relx=0.211, rely=0.089, height=15,
                                    width=74)

        self.roll_no_label = tk.Label(top, background="#CED4DA", disabledforeground="#a3a3a3", foreground="#000000",
                                      text='''Roll no. :''')
        self.roll_no_label.place(relx=0.257, rely=0.223, height=19,
                                 width=54)

        self.student_id_entry = tk.Entry(top, background="white", foreground="#000000",
                                         highlightbackground="#d9d9d9", highlightcolor="black",
                                         insertbackground="black", selectbackground="blue",
                                         selectforeground="white")
        self.student_id_entry.place(relx=0.468, rely=0.089, height=20
                                    , relwidth=0.304)

        self.roll_no_entry = tk.Entry(top, background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                      foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                      insertbackground="black", selectbackground="blue", selectforeground="white")
        self.roll_no_entry.place(relx=0.468, rely=0.223, height=20
                                 , relwidth=0.304)

        self.back_button = tk.Button(top, activebackground="#ececec", activeforeground="#000000",
                                     background="#E9ECEF", disabledforeground="#a3a3a3", foreground="#000000",
                                     highlightbackground="#d9d9d9", highlightcolor="black", pady="0",
                                     text='''Back''', command=self.select_back)
        self.back_button.place(relx=0.175, rely=0.804, height=24, width=87)

        self.add_button = tk.Button(top, activebackground="#ececec", activeforeground="#000000",
                                    background="#E9ECEF", disabledforeground="#a3a3a3", foreground="#000000",
                                    highlightbackground="#d9d9d9", highlightcolor="black", pady="0", text='''Add''',
                                    command=lambda: self.select_add(self.student_id_entry.get(),
                                                                    self.branch_id_entry.get(),
                                                                    self.roll_no_entry.get(), self.email_entry.get(),
                                                                    self.password_entry.get()))
        self.add_button.place(relx=0.585, rely=0.804, height=24, width=87)

        self.email_label = tk.Label(top, activebackground="#f9f9f9", activeforeground="black", background="#CED4DA",
                                    disabledforeground="#a3a3a3", foreground="#000000",
                                    highlightbackground="#d9d9d9", highlightcolor="black", text='''E-mail :''')
        self.email_label.place(relx=0.254, rely=0.357, height=19, width=64)

        self.password_label = tk.Label(top, activebackground="#f9f9f9", activeforeground="black",
                                       background="#CED4DA", disabledforeground="#a3a3a3",
                                       foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                       text='''Password :''')
        self.password_label.place(relx=0.234, rely=0.491, height=19,
                                  width=64)

        self.branch_id_label = tk.Label(top, activebackground="#f9f9f9", activeforeground="black",
                                        background="#CED4DA", disabledforeground="#a3a3a3", foreground="#000000",
                                        highlightbackground="#d9d9d9", highlightcolor="black",
                                        text='''Branch id :''')
        self.branch_id_label.place(relx=0.219, rely=0.625, height=21,
                                   width=74)

        self.email_entry = tk.Entry(top, background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                    foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                    insertbackground="black", selectbackground="blue", selectforeground="white")
        self.email_entry.place(relx=0.468, rely=0.357, height=20,
                               relwidth=0.304)

        self.password_entry = tk.Entry(top, background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                       foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                       insertbackground="black", selectbackground="blue", selectforeground="white")
        self.password_entry.place(relx=0.468, rely=0.491, height=20
                                  , relwidth=0.304)

        self.branch_id_entry = tk.Entry(top, background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                        foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                        insertbackground="black", selectbackground="blue", selectforeground="white")
        self.branch_id_entry.place(relx=0.468, rely=0.625, height=20
                                   , relwidth=0.304)

    def select_back(self):
        self.master.withdraw()

    def select_add(self, student_id, branch_id, roll_no, email, password):
        if len(student_id) != 0 and len(roll_no) != 0 and len(password) != 0 and len(branch_id):
            if not email.isnumeric():
                sql_query = "INSERT INTO student VALUES('" + student_id + "', '" + branch_id + "', '" + roll_no + "', '" + email + "', '" + password + "');"
                try:
                    mycursor.execute(sql_query)  # executing query
                    tv.insert(parent='', index='end', text="Parent",
                              values=(str(student_id), str(branch_id), str(roll_no), str(email), str(password)))
                    print("inside try : ", mycursor.fetchall())
                except (mysql.connector.Error, mysql.connector.Warning) as e:  # fetching error
                    messagebox.showerror("Error Message", "ERROR MESSAGE :\n" + str(e))
                    print("inside except : ", mycursor.fetchall())  # displaying error
            else:
                messagebox.showerror("Error Message", "Email can't be only numeric!")
        else:
            messagebox.showerror("Error Message", "No field should be empty")
        print(student_id, roll_no, email, password, branch_id)
        self.master.withdraw()
        mydb.commit()


class SubjectAdd:
    def __init__(self, top=None):
        self.master = top
        top.geometry("342x200+501+160")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(0, 0)
        top.title("Add")
        top.configure(background="#CED4DA")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.sub_code_label = tk.Label(top, activebackground="#f9f9f9", activeforeground="black", background="#CED4DA",
                                       disabledforeground="#a3a3a3", foreground="#000000",
                                       highlightbackground="#d9d9d9", highlightcolor="black", text='''Subject code :''')
        self.sub_code_label.place(relx=0.175, rely=0.12, height=13, width=84)

        self.sub_name_label = tk.Label(top, activebackground="#f9f9f9", activeforeground="black", background="#CED4DA",
                                       disabledforeground="#a3a3a3", foreground="#000000",
                                       highlightbackground="#d9d9d9", highlightcolor="black", text='''Subject name :''')
        self.sub_name_label.place(relx=0.158, rely=0.25, height=17, width=94)

        self.sub_code_entry = tk.Entry(top, background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                       foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                       insertbackground="black", selectbackground="blue", selectforeground="white")
        self.sub_code_entry.place(relx=0.468, rely=0.1, height=20, relwidth=0.304)

        self.sub_name_entry = tk.Entry(top, background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                       foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                       insertbackground="black", selectbackground="blue", selectforeground="white")
        self.sub_name_entry.place(relx=0.468, rely=0.25, height=20, relwidth=0.304)

        self.sub_credit_label = tk.Label(top, activebackground="#f9f9f9", activeforeground="black",
                                         background="#CED4DA", disabledforeground="#a3a3a3", foreground="#000000",
                                         highlightbackground="#d9d9d9", highlightcolor="black",
                                         text='''Subject credit :''')
        self.sub_credit_label.place(relx=0.173, rely=0.4, height=17, width=84)

        self.branch_id_label = tk.Label(top, activebackground="#f9f9f9", activeforeground="black", background="#CED4DA",
                                        disabledforeground="#a3a3a3", foreground="#000000",
                                        highlightbackground="#d9d9d9", highlightcolor="black", text='''Branch id :''')
        self.branch_id_label.place(relx=0.219, rely=0.55, height=17, width=74)

        self.sub_credit_entry = tk.Entry(top, background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                         foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                         insertbackground="black", selectbackground="blue", selectforeground="white")
        self.sub_credit_entry.place(relx=0.468, rely=0.4, height=20, relwidth=0.304)

        self.branch_id_entry = tk.Entry(top, background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                        foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                        insertbackground="black", selectbackground="blue", selectforeground="white")
        self.branch_id_entry.place(relx=0.468, rely=0.55, height=20, relwidth=0.304)

        self.add_button = tk.Button(top, activebackground="#ececec", activeforeground="#000000", background="#E9ECEF",
                                    disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                                    highlightcolor="black", pady="0", text='''Add''',
                                    command=lambda: self.select_add(self.sub_code_entry.get(),
                                                                    self.branch_id_entry.get(),
                                                                    self.sub_name_entry.get(),
                                                                    self.sub_credit_entry.get()))
        self.add_button.place(relx=0.585, rely=0.75, height=24, width=87)

        self.back_button = tk.Button(top, activebackground="#ececec", activeforeground="#000000", background="#E9ECEF",
                                     disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                                     highlightcolor="black", pady="0", text='''Back''', command=self.select_back)
        self.back_button.place(relx=0.175, rely=0.75, height=24, width=87)

    def select_back(self):
        self.master.withdraw()

    def select_add(self, subject_code, branch_id, subject_name, subject_credit):
        if len(subject_code) != 0 and len(branch_id) != 0 and len(subject_name) != 0 and len(subject_credit) != 0:
            if not subject_name.isnumeric():
                sql_query = "INSERT INTO subject VALUES('" + subject_code + "', " + branch_id + ", '" + subject_name + "', " + subject_credit + ");"
                try:
                    mycursor.execute(sql_query)  # executing query
                    tv.insert(parent='', index='end', text="Parent",
                              values=(subject_code, branch_id, subject_name, str(subject_credit)))
                    print("inside try : ", mycursor.fetchall())
                except (mysql.connector.Error, mysql.connector.Warning) as e:  # fetching error
                    messagebox.showerror("Error Message", "ERROR MESSAGE :\n" + str(e))
                    print("inside except : ", mycursor.fetchall())  # displaying error
            else:
                messagebox.showerror("Error Message", "Subject name cannot be numeric!")
        else:
            messagebox.showerror("Error Message", "No field should be empty")
        print(subject_code, branch_id, subject_name, subject_credit)
        self.master.withdraw()
        mydb.commit()


class AttendanceModify:
    def __init__(self, top=None):
        self.master = top
        top.geometry("327x430+455+152")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(0, 0)
        top.title("Modify")
        top.configure(background="#CED4DA")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Label1 = tk.Label(top, activebackground="#CED4DA", activeforeground="black", background="#CED4DA",
                               disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 13 -weight bold",
                               foreground="#212529", highlightbackground="#d9d9d9", highlightcolor="black",
                               text='''PRESENT DATA''')
        self.Label1.place(relx=0.245, rely=0.023, height=14, width=154)

        self.Label1_1 = tk.Label(top, activebackground="#f9f9f9", activeforeground="black", background="#CED4DA",
                                 disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 13 -weight bold",
                                 foreground="#212529", highlightbackground="#d9d9d9", highlightcolor="black",
                                 text='''NEW DATA''')
        self.Label1_1.place(relx=0.306, rely=0.465, height=14, width=114)

        self.login_label1 = tk.Label(top, activebackground="#f9f9f9", activeforeground="black", background="#CED4DA",
                                     disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                                     highlightcolor="black", text='''Login time :''')
        self.login_label1.place(relx=0.183, rely=0.163, height=22, width=75)

        self.logout_label1 = tk.Label(top, activebackground="#f9f9f9", activeforeground="black", background="#CED4DA",
                                      disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                                      highlightcolor="black", text='''Logout time :''')
        self.logout_label1.place(relx=0.153, rely=0.233, height=23, width=86)

        self.attendance_id_label1 = tk.Label(top, activebackground="#f9f9f9", activeforeground="black",
                                             background="#CED4DA", disabledforeground="#a3a3a3", foreground="#000000",
                                             highlightbackground="#d9d9d9", highlightcolor="black",
                                             text='''Attendance id :''')
        self.attendance_id_label1.place(relx=0.144, rely=0.098, height=14, width=85)

        self.exam_id_label = tk.Label(top, activebackground="#f9f9f9", activeforeground="black", background="#CED4DA",
                                      disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                                      highlightcolor="black", text='''Exam id :''')
        self.exam_id_label.place(relx=0.242, rely=0.381, height=13, width=50)

        self.student_id_label1 = tk.Label(top, activebackground="#f9f9f9", activeforeground="black",
                                          background="#CED4DA", disabledforeground="#a3a3a3", foreground="#000000",
                                          highlightbackground="#d9d9d9", highlightcolor="black",
                                          text='''Student id :''')
        self.student_id_label1.place(relx=0.19, rely=0.312, height=13, width=74)

        self.attendance_id_entry1 = tk.Entry(top, background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                             foreground="#000000", highlightbackground="#d9d9d9",
                                             highlightcolor="black", insertbackground="black", selectbackground="blue",
                                             selectforeground="white")
        self.attendance_id_entry1.place(relx=0.459, rely=0.093, height=20, relwidth=0.318)

        self.login_entry1 = tk.Entry(top, background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                     foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                     insertbackground="black", selectbackground="blue", selectforeground="white")
        self.login_entry1.place(relx=0.459, rely=0.163, height=20, relwidth=0.318)

        self.logout_entry1 = tk.Entry(top, background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                      foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                      insertbackground="black", selectbackground="blue", selectforeground="white")
        self.logout_entry1.place(relx=0.459, rely=0.233, height=20, relwidth=0.318)

        self.student_id_entry1 = tk.Entry(top, background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                          foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                          insertbackground="black", selectbackground="blue", selectforeground="white")
        self.student_id_entry1.place(relx=0.459, rely=0.302, height=20, relwidth=0.318)

        self.exam_id_entry1 = tk.Entry(top, background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                       foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                       insertbackground="black", selectbackground="blue", selectforeground="white")
        self.exam_id_entry1.place(relx=0.459, rely=0.372, height=20, relwidth=0.318)

        self.attendance_id_entry2 = tk.Entry(top, background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                             foreground="#000000", highlightbackground="#d9d9d9",
                                             highlightcolor="black", insertbackground="black", selectbackground="blue",
                                             selectforeground="white")
        self.attendance_id_entry2.place(relx=0.459, rely=0.535, height=20, relwidth=0.318)

        time_format1 = StringVar(top, value='HH:MM:SS')
        time_format2 = StringVar(top, value='HH:MM:SS')

        self.login_entry2 = tk.Entry(top, background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                     foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                     insertbackground="black", selectbackground="blue", selectforeground="white",
                                     textvariable=time_format1)
        self.login_entry2.place(relx=0.459, rely=0.605, height=20, relwidth=0.318)

        self.logout_entry2 = tk.Entry(top, background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                      foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                      insertbackground="black", selectbackground="blue", selectforeground="white",
                                      textvariable=time_format2)
        self.logout_entry2.place(relx=0.459, rely=0.674, height=20, relwidth=0.318)

        self.student_id_entry2 = tk.Entry(top, background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                          foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                          insertbackground="black", selectbackground="blue", selectforeground="white")
        self.student_id_entry2.place(relx=0.459, rely=0.744, height=20, relwidth=0.318)

        self.exam_id_entry2 = tk.Entry(top, background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                       foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                       insertbackground="black", selectbackground="blue", selectforeground="white")
        self.exam_id_entry2.place(relx=0.459, rely=0.814, height=20, relwidth=0.318)

        self.attendance_id_label2 = tk.Label(top, activebackground="#f9f9f9", activeforeground="black",
                                             background="#CED4DA", disabledforeground="#a3a3a3", foreground="#000000",
                                             highlightbackground="#d9d9d9", highlightcolor="black",
                                             text='''Attendance id :''')
        self.attendance_id_label2.place(relx=0.153, rely=0.54, height=14, width=85)

        self.login_label2 = tk.Label(top, activebackground="#f9f9f9", activeforeground="black", background="#CED4DA",
                                     disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                                     highlightcolor="black", text='''Login time :''')
        self.login_label2.place(relx=0.183, rely=0.6, height=23, width=76)

        self.logout_label2 = tk.Label(top, activebackground="#f9f9f9", activeforeground="black", background="#CED4DA",
                                      disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                                      highlightcolor="black", text='''Logout time :''')
        self.logout_label2.place(relx=0.147, rely=0.674, height=22, width=95)

        self.student_id_label2 = tk.Label(top, activebackground="#f9f9f9", activeforeground="black",
                                          background="#CED4DA", disabledforeground="#a3a3a3", foreground="#000000",
                                          highlightbackground="#d9d9d9", highlightcolor="black",
                                          text='''Student id :''')
        self.student_id_label2.place(relx=0.214, rely=0.753, height=13, width=64)

        self.exam_id_label2 = tk.Label(top, activebackground="#f9f9f9", activeforeground="black", background="#CED4DA",
                                       disabledforeground="#a3a3a3", foreground="#000000",
                                       highlightbackground="#d9d9d9", highlightcolor="black", text='''Exam id :''')
        self.exam_id_label2.place(relx=0.214, rely=0.819, height=13, width=70)

        self.modify_button = tk.Button(top, activebackground="#ececec", activeforeground="#000000",
                                       background="#E9ECEF", disabledforeground="#a3a3a3", foreground="#000000",
                                       highlightbackground="#d9d9d9", highlightcolor="black", pady="0",
                                       text='''Modify''',
                                       command=lambda: self.select_modify(self.attendance_id_entry2.get(),
                                                                          self.student_id_entry2.get(),
                                                                          self.exam_id_entry2.get(),
                                                                          self.login_entry2.get(),
                                                                          self.logout_entry2.get()))
        self.modify_button.place(relx=0.642, rely=0.907, height=24, width=77)

        self.cancel_button = tk.Button(top, activebackground="#ececec", activeforeground="#000000",
                                       background="#E9ECEF", disabledforeground="#a3a3a3", foreground="#000000",
                                       highlightbackground="#d9d9d9", highlightcolor="black", pady="0",
                                       text='''Cancel''', command=self.select_back)
        self.cancel_button.place(relx=0.153, rely=0.907, height=24, width=77)

        global item_modifyAttendance
        item_modifyAttendance = tv.item(tv.focus())['values']
        print("PREVIOUSLY : ")
        print(item_modifyAttendance[0])
        print(item_modifyAttendance[1])
        print(item_modifyAttendance[2])
        print(item_modifyAttendance[3])
        print(item_modifyAttendance[4])
        self.attendance_id_entry1.insert(0, item_modifyAttendance[0])
        self.attendance_id_entry1.config(state="disable")
        self.student_id_entry1.insert(0, item_modifyAttendance[1])
        self.student_id_entry1.config(state="disable")
        self.exam_id_entry1.insert(0, item_modifyAttendance[2])
        self.exam_id_entry1.config(state="disable")
        self.login_entry1.insert(0, item_modifyAttendance[3])
        self.login_entry1.config(state="disable")
        self.logout_entry1.insert(0, item_modifyAttendance[4])
        self.logout_entry1.config(state="disable")

    def select_back(self):
        self.master.withdraw()

    def select_modify(self, attendance_id, student_id, exam_id, login_time, logout_time):
        if login_time != logout_time:
            try:
                sql_query = "UPDATE attendance SET attendance_id=" + str(attendance_id) + ", student_id=" + str(
                    student_id) + ", exam_id=" + str(
                    exam_id) + ", login_time=TIME('" + login_time + "'), logout_time=TIME('" + logout_time + "') WHERE attendance_id=" + str(
                    item_modifyAttendance[0]) + ";"
                try:
                    print(sql_query)
                    mycursor.execute(sql_query)  # executing query
                    print("s1")
                    tv.item(tv.focus(), text="",
                            values=(str(attendance_id), str(student_id), str(exam_id), login_time, logout_time))
                    print("s2")
                except (mysql.connector.Error, mysql.connector.Warning) as e:  # fetching error
                    messagebox.showerror("Error Message", "ERROR MESSAGE\n" + str(e))  # displaying error

            except:
                messagebox.showerror("Error Message", "Modification failed")
        else:
            messagebox.showerror("Error Message", "Login time cannot be equal to logout time!")
        # print("NEW : ", attendance_id, student_id, exam_id, login_time, logout_time)
        mydb.commit()
        self.master.withdraw()


class BranchModify:
    def __init__(self, top=None):
        self.master = top
        top.geometry("327x253+556+102")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(0, 0)
        top.title("Modify")
        top.configure(background="#CED4DA")

        self.menubar = tk.Menu(top, font="TkMenuFont", bg="#d9d9d9", fg="#000000")

        self.Label1 = tk.Label(top, background="#CED4DA", disabledforeground="#a3a3a3",
                               font="-family {Segoe UI} -size 13 -weight bold", foreground="#212529",
                               text='''PRESENT DATA''')
        self.Label1.place(relx=0.275, rely=0.036, height=24, width=149)

        self.Label2 = tk.Label(top, background="#CED4DA", disabledforeground="#a3a3a3", foreground="#000000",
                               text='''Branch id :''')
        self.Label2.place(relx=0.214, rely=0.158, height=16, width=74)

        self.Entry1 = tk.Entry(top, background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                               foreground="#000000", insertbackground="black")
        self.Entry1.place(relx=0.459, rely=0.158, height=20, relwidth=0.318)

        self.Label3 = tk.Label(top, background="#CED4DA", disabledforeground="#a3a3a3", foreground="#000000",
                               text='''Branch name :''')
        self.Label3.place(relx=0.183, rely=0.277, height=16, width=74)

        self.Entry2 = tk.Entry(top, background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                               foreground="#000000", insertbackground="black")
        self.Entry2.place(relx=0.459, rely=0.277, height=20, relwidth=0.318)

        self.Label4 = tk.Label(top, background="#CED4DA", disabledforeground="#a3a3a3",
                               font="-family {Segoe UI} -size 13 -weight bold", foreground="#212529",
                               text='''NEW DATA''')
        self.Label4.place(relx=0.336, rely=0.407, height=27, width=105)

        self.Label5 = tk.Label(top, background="#CED4DA", disabledforeground="#a3a3a3", foreground="#000000",
                               text='''Branch name :''')
        self.Label5.place(relx=0.141, rely=0.672, height=17, width=94)

        self.Label6 = tk.Label(top, background="#CED4DA", disabledforeground="#a3a3a3", foreground="#000000",
                               text='''Branch id :''')
        self.Label6.place(relx=0.22, rely=0.553, height=17, width=62)

        self.back_button = tk.Button(top, command=self.select_back, activebackground="#ececec",
                                     activeforeground="#000000", background="#E9ECEF", disabledforeground="#a3a3a3",
                                     foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                     pady="0", text='''Back''')
        self.back_button.place(relx=0.153, rely=0.83, height=24, width=77)

        self.modify_button = tk.Button(top,
                                       command=lambda: self.select_modify(self.Entry1_1.get(), self.Entry1_2.get()),
                                       activebackground="#ececec", activeforeground="#000000", background="#E9ECEF",
                                       disabledforeground="#a3a3a3", foreground="#000000",
                                       highlightbackground="#d9d9d9", highlightcolor="black", pady="0",
                                       text='''Modify''')
        self.modify_button.place(relx=0.612, rely=0.83, height=24, width=77)

        self.Entry1_1 = tk.Entry(top, background="white", disabledforeground="#a3a3a3",
                                 font="TkFixedFont", foreground="#000000", highlightbackground="#d9d9d9",
                                 highlightcolor="black", insertbackground="black", selectbackground="blue",
                                 selectforeground="white")
        self.Entry1_1.place(relx=0.459, rely=0.553, height=20, relwidth=0.318)

        self.Entry1_2 = tk.Entry(top, background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                 foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                 insertbackground="black", selectbackground="blue", selectforeground="white")
        self.Entry1_2.place(relx=0.459, rely=0.672, height=20, relwidth=0.318)

        global item_modifyBranch
        item_modifyBranch = tv.item(tv.focus())[
            'values']
        print("PREVIOUSLY : ")
        print(item_modifyBranch[0])
        print(item_modifyBranch[1])
        self.Entry1.insert(0, item_modifyBranch[0])
        self.Entry1.config(state="disable")
        self.Entry2.insert(0, item_modifyBranch[1])
        self.Entry2.config(state="disable")

    def select_back(self):
        self.master.withdraw()

    def select_modify(self, branch_id, branch_name):
        if not branch_name.isnumeric():
            try:
                sql_query = "UPDATE branch SET branch_id=" + str(self.Entry1_1.get()) + ", branch_name='" + str(
                    self.Entry1_2.get()) + "' WHERE branch_id=" + str(item_modifyBranch[0]) + ";"
                try:
                    mycursor.execute(sql_query)  # executing query
                    tv.item(tv.focus(), text="", values=(str(self.Entry1_1.get()), self.Entry1_2.get()))
                except (mysql.connector.Error, mysql.connector.Warning) as e:  # fetching error
                    messagebox.showerror("Error Message", "ERROR MESSAGE\n" + str(e))  # displaying error
            except:
                messagebox.showerror("Error Message", "Modification failed")
        else:
            messagebox.showerror("Error Message", "Branch Name cannot be numeric!")
        mydb.commit()
        self.master.withdraw()


class ExamModify:
    def __init__(self, top=None):
        self.master = top
        top.geometry("327x602+562+80")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(0, 0)
        top.title("Modify")
        top.configure(background="#CED4DA")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")
        date_format = StringVar(top, value='YYYY-MM-DD')
        time_format = StringVar(top, value='HH:MM:SS')

        self.present_label = tk.Label(top, activebackground="#CED4DA", activeforeground="black", background="#CED4DA",
                                      disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 13 -weight bold",
                                      foreground="#212529", highlightbackground="#d9d9d9", highlightcolor="black",
                                      text='''PRESENT DATA''')
        self.present_label.place(relx=0.245, rely=0.017, height=19, width=154)

        self.new_label = tk.Label(top, activebackground="#f9f9f9", activeforeground="black", background="#CED4DA",
                                  disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 13 -weight bold",
                                  foreground="#212529", highlightbackground="#d9d9d9", highlightcolor="black",
                                  text='''NEW DATA''')
        self.new_label.place(relx=0.306, rely=0.473, height=19, width=114)

        self.exam_label1 = tk.Label(top, activebackground="#f9f9f9", activeforeground="black", background="#CED4DA",
                                    disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                                    highlightcolor="black", text='''Exam id :''')
        self.exam_label1.place(relx=0.245, rely=0.066, height=19, width=55)

        self.exam_entry1 = tk.Entry(top, background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                    foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                    insertbackground="black", selectbackground="blue", selectforeground="white")
        self.exam_entry1.place(relx=0.459, rely=0.066, height=20, relwidth=0.318)

        self.name_label1 = tk.Label(top, activebackground="#f9f9f9", activeforeground="black", background="#CED4DA",
                                    disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                                    highlightcolor="black", text='''Name :''')
        self.name_label1.place(relx=0.275, rely=0.116, height=18, width=46)

        self.name_entry1 = tk.Entry(top, background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                    foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                    insertbackground="black", selectbackground="blue", selectforeground="white")
        self.name_entry1.place(relx=0.459, rely=0.116, height=20, relwidth=0.318)

        self.duration_label1 = tk.Label(top, activebackground="#f9f9f9", activeforeground="black", background="#CED4DA",
                                        disabledforeground="#a3a3a3", foreground="#000000",
                                        highlightbackground="#d9d9d9", highlightcolor="black", text='''Duration :''')
        self.duration_label1.place(relx=0.239, rely=0.166, height=18, width=55)

        self.duration_entry1 = tk.Entry(top, background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                        foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                        insertbackground="black", selectbackground="blue", selectforeground="white")
        self.duration_entry1.place(relx=0.459, rely=0.166, height=20, relwidth=0.318)

        self.date_label1 = tk.Label(top, activebackground="#f9f9f9", activeforeground="black", background="#CED4DA",
                                    disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                                    highlightcolor="black", text='''Date :''')
        self.date_label1.place(relx=0.275, rely=0.216, height=18, width=55)

        self.date_entry1 = tk.Entry(top, background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                    foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                    insertbackground="black", selectbackground="blue", selectforeground="white")
        self.date_entry1.place(relx=0.459, rely=0.216, height=20, relwidth=0.318)

        self.ques_label1 = tk.Label(top, activebackground="#f9f9f9", activeforeground="black", background="#CED4DA",
                                    disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                                    highlightcolor="black", text='''Total questions :''')
        self.ques_label1.place(relx=0.135, rely=0.266, height=18, width=89)

        self.ques_entry1 = tk.Entry(top, background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                    foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                    insertbackground="black", selectbackground="blue", selectforeground="white")
        self.ques_entry1.place(relx=0.459, rely=0.266, height=20, relwidth=0.318)

        self.marks_label1 = tk.Label(top, activebackground="#f9f9f9", activeforeground="black", background="#CED4DA",
                                     disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                                     highlightcolor="black", text='''Total marks :''')
        self.marks_label1.place(relx=0.19, rely=0.316, height=17, width=75)

        self.marks_entry1 = tk.Entry(top, background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                     foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                     insertbackground="black", selectbackground="blue", selectforeground="white")
        self.marks_entry1.place(relx=0.459, rely=0.316, height=20, relwidth=0.318)

        self.branch_label1 = tk.Label(top, activebackground="#f9f9f9", activeforeground="black", background="#CED4DA",
                                      disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                                      highlightcolor="black", text='''Branch id :''')
        self.branch_label1.place(relx=0.22, rely=0.365, height=18, width=64)

        self.branch_entry1 = tk.Entry(top, background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                      foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                      insertbackground="black", selectbackground="blue", selectforeground="white")
        self.branch_entry1.place(relx=0.459, rely=0.365, height=20, relwidth=0.318)

        self.subject_label1 = tk.Label(top, activebackground="#f9f9f9", activeforeground="black", background="#CED4DA",
                                       disabledforeground="#a3a3a3", foreground="#000000",
                                       highlightbackground="#d9d9d9", highlightcolor="black", text='''Subject code :''')
        self.subject_label1.place(relx=0.162, rely=0.415, height=18, width=80)

        self.subject_entry1 = tk.Entry(top, background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                       foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                       insertbackground="black", selectbackground="blue", selectforeground="white")
        self.subject_entry1.place(relx=0.459, rely=0.415, height=20, relwidth=0.318)

        self.exam_label2 = tk.Label(top, activebackground="#f9f9f9", activeforeground="black", background="#CED4DA",
                                    disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                                    highlightcolor="black", text='''Exam id :''')
        self.exam_label2.place(relx=0.245, rely=0.523, height=20, width=55)

        self.exam_entry2 = tk.Entry(top, background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                    foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                    insertbackground="black", selectbackground="blue", selectforeground="white")
        self.exam_entry2.place(relx=0.459, rely=0.523, height=20, relwidth=0.318)

        self.name_label2 = tk.Label(top, activebackground="#f9f9f9", activeforeground="black", background="#CED4DA",
                                    disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                                    highlightcolor="black", text='''Name :''')
        self.name_label2.place(relx=0.275, rely=0.573, height=18, width=46)

        self.name_entry2 = tk.Entry(top, background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                    foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                    insertbackground="black", selectbackground="blue", selectforeground="white")
        self.name_entry2.place(relx=0.459, rely=0.573, height=20, relwidth=0.318)

        self.duration_label2 = tk.Label(top, activebackground="#f9f9f9", activeforeground="black", background="#CED4DA",
                                        disabledforeground="#a3a3a3", foreground="#000000",
                                        highlightbackground="#d9d9d9", highlightcolor="black", text='''Duration :''')
        self.duration_label2.place(relx=0.239, rely=0.623, height=18, width=55)

        self.duration_entry2 = tk.Entry(top, background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                        foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                        insertbackground="black", selectbackground="blue", selectforeground="white",
                                        textvariable=time_format)
        self.duration_entry2.place(relx=0.459, rely=0.623, height=20, relwidth=0.318)

        self.date_label2 = tk.Label(top, activebackground="#f9f9f9", activeforeground="black", background="#CED4DA",
                                    disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                                    highlightcolor="black", text='''Date :''')
        self.date_label2.place(relx=0.275, rely=0.673, height=18, width=55)

        self.date_entry2 = tk.Entry(top, background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                    foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                    insertbackground="black", selectbackground="blue", selectforeground="white",
                                    textvariable=date_format)
        self.date_entry2.place(relx=0.459, rely=0.673, height=20, relwidth=0.318)

        self.ques_label2 = tk.Label(top, activebackground="#f9f9f9", activeforeground="black", background="#CED4DA",
                                    disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                                    highlightcolor="black", text='''Total questions :''')
        self.ques_label2.place(relx=0.135, rely=0.723, height=18, width=89)

        self.ques_entry2 = tk.Entry(top, background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                    foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                    insertbackground="black", selectbackground="blue", selectforeground="white")
        self.ques_entry2.place(relx=0.459, rely=0.723, height=20, relwidth=0.318)

        self.marks_label2 = tk.Label(top, activebackground="#f9f9f9", activeforeground="black", background="#CED4DA",
                                     disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                                     highlightcolor="black", text='''Total marks :''')
        self.marks_label2.place(relx=0.19, rely=0.772, height=17, width=75)

        self.marks_entry2 = tk.Entry(top, background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                     foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                     insertbackground="black", selectbackground="blue", selectforeground="white")
        self.marks_entry2.place(relx=0.459, rely=0.772, height=20, relwidth=0.318)

        self.branch_label2 = tk.Label(top, activebackground="#f9f9f9", activeforeground="black", background="#CED4DA",
                                      disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                                      highlightcolor="black", text='''Branch id :''')
        self.branch_label2.place(relx=0.22, rely=0.822, height=18, width=64)

        self.branch_entry2 = tk.Entry(top, background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                      foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                      insertbackground="black", selectbackground="blue", selectforeground="white")
        self.branch_entry2.place(relx=0.459, rely=0.822, height=20, relwidth=0.318)

        self.subject_label2 = tk.Label(top, activebackground="#f9f9f9", activeforeground="black", background="#CED4DA",
                                       disabledforeground="#a3a3a3", foreground="#000000",
                                       highlightbackground="#d9d9d9", highlightcolor="black", text='''Subject code :''')
        self.subject_label2.place(relx=0.168, rely=0.872, height=18, width=80)

        self.subject_entry2 = tk.Entry(top, background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                       foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                       insertbackground="black", selectbackground="blue", selectforeground="white")
        self.subject_entry2.place(relx=0.459, rely=0.872, height=20, relwidth=0.318)

        self.modify_button = tk.Button(top, activebackground="#ececec", activeforeground="#000000",
                                       background="#E9ECEF", disabledforeground="#a3a3a3", foreground="#000000",
                                       highlightbackground="#d9d9d9", highlightcolor="black", pady="0",
                                       text='''Modify''', command=lambda: self.select_modify(self.exam_entry2.get(),
                                                                                             self.name_entry2.get(),
                                                                                             self.duration_entry2.get(),
                                                                                             self.date_entry2.get(),
                                                                                             self.ques_entry2.get(),
                                                                                             self.marks_entry2.get(),
                                                                                             self.branch_entry2.get(),
                                                                                             self.subject_entry2.get()))
        self.modify_button.place(relx=0.642, rely=0.93, height=24, width=77)

        self.back_button = tk.Button(top, activebackground="#ececec", activeforeground="#000000", background="#E9ECEF",
                                     disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                                     highlightcolor="black", pady="0", text='''Back''', command=self.select_back)
        self.back_button.place(relx=0.135, rely=0.93, height=24, width=77)

        global item_modifyExam
        item_modifyExam = tv.item(tv.focus())['values']
        print("PREVIOUSLY : ")
        print(item_modifyExam[0])
        print(item_modifyExam[1])
        print(item_modifyExam[2])
        print(item_modifyExam[3])
        print(item_modifyExam[4])
        print(item_modifyExam[5])
        print(item_modifyExam[6])
        print(item_modifyExam[7])
        self.exam_entry1.insert(0, item_modifyExam[0])
        self.exam_entry1.config(state="disable")
        self.name_entry1.insert(0, item_modifyExam[1])
        self.name_entry1.config(state="disable")
        self.duration_entry1.insert(0, item_modifyExam[2])
        self.duration_entry1.config(state="disable")
        self.date_entry1.insert(0, item_modifyExam[3])
        self.date_entry1.config(state="disable")
        self.ques_entry1.insert(0, item_modifyExam[4])
        self.ques_entry1.config(state="disable")
        self.marks_entry1.insert(0, item_modifyExam[5])
        self.marks_entry1.config(state="disable")
        self.branch_entry1.insert(0, item_modifyExam[6])
        self.branch_entry1.config(state="disable")
        self.subject_entry1.insert(0, item_modifyExam[7])
        self.subject_entry1.config(state="disable")

    def select_back(self):
        self.master.withdraw()

    def select_modify(self, exam_id, exam_name, exam_duration, exam_date, total_questions, total_marks, branch_id,
                      subject_code):
        try:
            sql_query = "UPDATE exam SET exam_id=" + str(
                exam_id) + ", exam_name='" + exam_name + "' , exam_duration=TIME('" + exam_duration + "'), exam_date=STR_TO_DATE('" + exam_date + "', '%Y-%m-%d'), total_questions=" + str(
                total_questions) + ", total_marks=" + str(total_marks) + ", branch_id=" + str(
                branch_id) + ", subject_code='" + subject_code + "' WHERE exam_id=" + str(item_modifyExam[0]) + ";"
            try:
                mycursor.execute(sql_query)  # executing query
                tv.item(tv.focus(), text="", values=(
                    str(exam_id), exam_name, exam_duration, exam_date, str(total_questions), str(total_marks),
                    str(branch_id), subject_code))
            except (mysql.connector.Error, mysql.connector.Warning) as e:  # fetching error
                messagebox.showerror("Error Message", "ERROR MESSAGE\n" + str(e))  # displaying error

        except:
            messagebox.showerror("Error Message", "Modification failed")

        print("NEW : ", exam_id, exam_name, exam_duration, exam_date, total_questions, total_marks, branch_id,
              subject_code)
        mydb.commit()
        self.master.withdraw()


class ResultModify:
    def __init__(self, top=None):
        self.master = top
        top.geometry("327x430+589+46")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(0, 0)
        top.title("Modify")
        top.configure(background="#CED4DA")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Label1 = tk.Label(top, activebackground="#CED4DA", activeforeground="black", background="#CED4DA",
                               disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 13 -weight bold",
                               foreground="#212529", highlightbackground="#d9d9d9", highlightcolor="black",
                               text='''PRESENT DATA''')
        self.Label1.place(relx=0.245, rely=0.023, height=14, width=154)

        self.Label1_1 = tk.Label(top, activebackground="#f9f9f9", activeforeground="black", background="#CED4DA",
                                 disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 13 -weight bold",
                                 foreground="#212529", highlightbackground="#d9d9d9", highlightcolor="black",
                                 text='''NEW DATA''')
        self.Label1_1.place(relx=0.306, rely=0.465, height=14, width=114)

        self.marks_label1 = tk.Label(top, activebackground="#f9f9f9", activeforeground="black", background="#CED4DA",
                                     disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                                     highlightcolor="black", text='''Marks obtained :''')
        self.marks_label1.place(relx=0.125, rely=0.167, height=12, width=95)

        self.res_label1 = tk.Label(top, activebackground="#f9f9f9", activeforeground="black", background="#CED4DA",
                                   disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                                   highlightcolor="black", text='''Result :''')
        self.res_label1.place(relx=0.275, rely=0.24, height=13, width=46)

        self.res_id_label1 = tk.Label(top, activebackground="#f9f9f9", activeforeground="black", background="#CED4DA",
                                      disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                                      highlightcolor="black", text='''Result id :''')
        self.res_id_label1.place(relx=0.245, rely=0.098, height=14, width=55)

        self.exam_id_label = tk.Label(top, activebackground="#f9f9f9", activeforeground="black", background="#CED4DA",
                                      disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                                      highlightcolor="black", text='''Exam id :''')
        self.exam_id_label.place(relx=0.239, rely=0.381, height=13, width=60)

        self.student_id_label1 = tk.Label(top, activebackground="#f9f9f9", activeforeground="black",
                                          background="#CED4DA", disabledforeground="#a3a3a3", foreground="#000000",
                                          highlightbackground="#d9d9d9", highlightcolor="black",
                                          text='''Student id :''')
        self.student_id_label1.place(relx=0.214, rely=0.312, height=13, width=64)

        self.res_id_entry1 = tk.Entry(top, background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                      foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                      insertbackground="black", selectbackground="blue", selectforeground="white")
        self.res_id_entry1.place(relx=0.459, rely=0.093, height=20, relwidth=0.318)

        self.marks_entry1 = tk.Entry(top, background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                     foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                     insertbackground="black", selectbackground="blue", selectforeground="white")
        self.marks_entry1.place(relx=0.459, rely=0.163, height=20, relwidth=0.318)

        self.res_entry1 = tk.Entry(top, background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                   foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                   insertbackground="black", selectbackground="blue", selectforeground="white")
        self.res_entry1.place(relx=0.459, rely=0.233, height=20, relwidth=0.318)

        self.student_id_entry1 = tk.Entry(top, background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                          foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                          insertbackground="black", selectbackground="blue", selectforeground="white")
        self.student_id_entry1.place(relx=0.459, rely=0.302, height=20, relwidth=0.318)

        self.exam_id_entry1 = tk.Entry(top, background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                       foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                       insertbackground="black", selectbackground="blue", selectforeground="white")
        self.exam_id_entry1.place(relx=0.459, rely=0.372, height=20, relwidth=0.318)

        self.res_id_entry2 = tk.Entry(top, background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                      foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                      insertbackground="black", selectbackground="blue", selectforeground="white")
        self.res_id_entry2.place(relx=0.459, rely=0.535, height=20, relwidth=0.318)

        self.marks_entry2 = tk.Entry(top, background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                     foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                     insertbackground="black", selectbackground="blue", selectforeground="white")
        self.marks_entry2.place(relx=0.459, rely=0.605, height=20, relwidth=0.318)

        self.res_entry2 = tk.Entry(top, background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                   foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                   insertbackground="black", selectbackground="blue", selectforeground="white")
        self.res_entry2.place(relx=0.459, rely=0.674, height=20, relwidth=0.318)

        self.student_id_entry2 = tk.Entry(top, background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                          foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                          insertbackground="black", selectbackground="blue", selectforeground="white")
        self.student_id_entry2.place(relx=0.459, rely=0.744, height=20, relwidth=0.318)

        self.exam_id_entry2 = tk.Entry(top, background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                       foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                       insertbackground="black", selectbackground="blue", selectforeground="white")
        self.exam_id_entry2.place(relx=0.459, rely=0.814, height=20, relwidth=0.318)

        self.Entry1_7 = tk.Entry(top, background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                 foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                 insertbackground="black", selectbackground="blue", selectforeground="white")
        self.Entry1_7.place(relx=2.875, rely=1.828, height=20, relwidth=0.318)

        self.res_id_label2 = tk.Label(top, activebackground="#f9f9f9", activeforeground="black", background="#CED4DA",
                                      disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                                      highlightcolor="black", text='''Result id :''')
        self.res_id_label2.place(relx=0.245, rely=0.54, height=14, width=55)

        self.marks_label2 = tk.Label(top, activebackground="#f9f9f9", activeforeground="black", background="#CED4DA",
                                     disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                                     highlightcolor="black", text='''Marks obtained :''')
        self.marks_label2.place(relx=0.128, rely=0.609, height=13, width=96)

        self.res_label2 = tk.Label(top, activebackground="#f9f9f9", activeforeground="black", background="#CED4DA",
                                   disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                                   highlightcolor="black", text='''Result :''')
        self.res_label2.place(relx=0.269, rely=0.681, height=12, width=55)

        self.student_id_label2 = tk.Label(top, activebackground="#f9f9f9", activeforeground="black",
                                          background="#CED4DA", disabledforeground="#a3a3a3", foreground="#000000",
                                          highlightbackground="#d9d9d9", highlightcolor="black",
                                          text='''Student id :''')
        self.student_id_label2.place(relx=0.22, rely=0.753, height=13, width=64)

        self.exam_id_label2 = tk.Label(top, activebackground="#f9f9f9", activeforeground="black", background="#CED4DA",
                                       disabledforeground="#a3a3a3", foreground="#000000",
                                       highlightbackground="#d9d9d9", highlightcolor="black", text='''Exam id :''')
        self.exam_id_label2.place(relx=0.226, rely=0.823, height=13, width=70)

        self.modify_button = tk.Button(top, activebackground="#ececec", activeforeground="#000000",
                                       background="#E9ECEF", disabledforeground="#a3a3a3", foreground="#000000",
                                       highlightbackground="#d9d9d9", highlightcolor="black", pady="0",
                                       text='''Modify''', command=lambda: self.select_modify(self.res_id_entry2.get(),
                                                                                             self.student_id_entry2.get(),
                                                                                             self.exam_id_entry2.get(),
                                                                                             self.marks_entry2.get(),
                                                                                             self.res_entry2.get()))
        self.modify_button.place(relx=0.642, rely=0.907, height=24, width=77)

        self.cancel_button = tk.Button(top, activebackground="#ececec", activeforeground="#000000",
                                       background="#E9ECEF", disabledforeground="#a3a3a3", foreground="#000000",
                                       highlightbackground="#d9d9d9", highlightcolor="black", pady="0",
                                       text='''Cancel''', command=self.select_back)
        self.cancel_button.place(relx=0.153, rely=0.907, height=24, width=77)

        global item_modifyResult
        item_modifyResult = tv.item(tv.focus())['values']
        print("PREVIOUSLY : ")
        print(item_modifyResult[0])
        print(item_modifyResult[1])
        print(item_modifyResult[2])
        print(item_modifyResult[3])
        print(item_modifyResult[4])
        self.res_id_entry1.insert(0, item_modifyResult[0])
        self.res_id_entry1.config(state="disable")
        self.student_id_entry1.insert(0, item_modifyResult[1])
        self.student_id_entry1.config(state="disable")
        self.exam_id_entry1.insert(0, item_modifyResult[2])
        self.exam_id_entry1.config(state="disable")
        self.marks_entry1.insert(0, item_modifyResult[3])
        self.marks_entry1.config(state="disable")
        self.res_entry1.insert(0, item_modifyResult[4])
        self.res_entry1.config(state="disable")

    def select_back(self):
        self.master.withdraw()

    def select_modify(self, result_id, student_id, exam_id, marks_obtained, result):
        try:
            sql_query = "UPDATE result SET result_id=" + str(result_id) + ", student_id=" + str(
                student_id) + ", exam_id=" + str(exam_id) + ", marks_obtained=" + str(
                marks_obtained) + ", result='" + str(result) + "' WHERE result_id=" + str(item_modifyResult[0]) + ";"
            try:
                mycursor.execute(sql_query)  # executing query
                tv.item(tv.focus(), text="",
                        values=(str(result_id), str(student_id), str(exam_id), str(marks_obtained), result))
            except (mysql.connector.Error, mysql.connector.Warning) as e:  # fetching error
                messagebox.showerror("Error Message", "ERROR MESSAGE\n" + str(e))  # displaying error

        except:
            messagebox.showerror("Error Message", "Modification failed")
        mydb.commit()
        self.master.withdraw()


class StudentModify:
    def __init__(self, top=None):
        self.master = top
        top.geometry("327x430+589+46")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(0, 0)
        top.title("Modify")
        top.configure(background="#CED4DA")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Label1 = tk.Label(top, activebackground="#CED4DA", activeforeground="black", background="#CED4DA",
                               disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 13 -weight bold",
                               foreground="#212529", highlightbackground="#d9d9d9", highlightcolor="black",
                               text='''PRESENT DATA''')
        self.Label1.place(relx=0.245, rely=0.023, height=14, width=154)

        self.Label1_1 = tk.Label(top, activebackground="#f9f9f9", activeforeground="black", background="#CED4DA",
                                 disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 13 -weight bold",
                                 foreground="#212529", highlightbackground="#d9d9d9", highlightcolor="black",
                                 text='''NEW DATA''')
        self.Label1_1.place(relx=0.306, rely=0.465, height=14, width=114)

        self.roll_no_label1 = tk.Label(top, activebackground="#f9f9f9", activeforeground="black", background="#CED4DA",
                                       disabledforeground="#a3a3a3", foreground="#000000",
                                       highlightbackground="#d9d9d9", highlightcolor="black", text='''Roll no. :''')
        self.roll_no_label1.place(relx=0.248, rely=0.167, height=12, width=55)

        self.email_label1 = tk.Label(top, activebackground="#f9f9f9", activeforeground="black", background="#CED4DA",
                                     disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                                     highlightcolor="black", text='''Email :''')
        self.email_label1.place(relx=0.275, rely=0.24, height=13, width=46)

        self.student_id_label1 = tk.Label(top, activebackground="#f9f9f9", activeforeground="black",
                                          background="#CED4DA", disabledforeground="#a3a3a3", foreground="#000000",
                                          highlightbackground="#d9d9d9", highlightcolor="black",
                                          text='''Student id :''')
        self.student_id_label1.place(relx=0.214, rely=0.098, height=14, width=65)

        self.branch_id_label = tk.Label(top, activebackground="#f9f9f9", activeforeground="black", background="#CED4DA",
                                        disabledforeground="#a3a3a3", foreground="#000000",
                                        highlightbackground="#d9d9d9", highlightcolor="black", text='''Branch id :''')
        self.branch_id_label.place(relx=0.217, rely=0.381, height=13, width=60)

        self.password_label1 = tk.Label(top, activebackground="#f9f9f9", activeforeground="black", background="#CED4DA",
                                        disabledforeground="#a3a3a3", foreground="#000000",
                                        highlightbackground="#d9d9d9", highlightcolor="black", text='''Password :''')
        self.password_label1.place(relx=0.214, rely=0.312, height=13, width=64)

        self.student_id_entry1 = tk.Entry(top, background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                          foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                          insertbackground="black", selectbackground="blue", selectforeground="white")
        self.student_id_entry1.place(relx=0.459, rely=0.093, height=20, relwidth=0.318)

        self.roll_no_entry1 = tk.Entry(top, background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                       foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                       insertbackground="black", selectbackground="blue", selectforeground="white")
        self.roll_no_entry1.place(relx=0.459, rely=0.163, height=20, relwidth=0.318)

        self.email_entry1 = tk.Entry(top, background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                     foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                     insertbackground="black", selectbackground="blue", selectforeground="white")
        self.email_entry1.place(relx=0.459, rely=0.233, height=20, relwidth=0.318)

        self.password_entry1 = tk.Entry(top, background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                        foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                        insertbackground="black", selectbackground="blue", selectforeground="white")
        self.password_entry1.place(relx=0.459, rely=0.302, height=20, relwidth=0.318)

        self.branch_id_entry1 = tk.Entry(top, background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                         foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                         insertbackground="black", selectbackground="blue", selectforeground="white")
        self.branch_id_entry1.place(relx=0.459, rely=0.372, height=20, relwidth=0.318)

        self.student_id_entry2 = tk.Entry(top, background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                          foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                          insertbackground="black", selectbackground="blue", selectforeground="white")
        self.student_id_entry2.place(relx=0.459, rely=0.535, height=20, relwidth=0.318)

        self.roll_no_entry2 = tk.Entry(top, background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                       foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                       insertbackground="black", selectbackground="blue", selectforeground="white")
        self.roll_no_entry2.place(relx=0.459, rely=0.605, height=20, relwidth=0.318)

        self.email_entry2 = tk.Entry(top, background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                     foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                     insertbackground="black", selectbackground="blue", selectforeground="white")
        self.email_entry2.place(relx=0.459, rely=0.674, height=20, relwidth=0.318)

        self.password_entry2 = tk.Entry(top, background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                        foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                        insertbackground="black", selectbackground="blue", selectforeground="white")
        self.password_entry2.place(relx=0.459, rely=0.744, height=20, relwidth=0.318)

        self.branch_id_entry2 = tk.Entry(top, background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                         foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                         insertbackground="black", selectbackground="blue", selectforeground="white")
        self.branch_id_entry2.place(relx=0.459, rely=0.814, height=20, relwidth=0.318)

        self.student_id_label2 = tk.Label(top, activebackground="#f9f9f9", activeforeground="black",
                                          background="#CED4DA", disabledforeground="#a3a3a3", foreground="#000000",
                                          highlightbackground="#d9d9d9", highlightcolor="black",
                                          text='''Student id :''')
        self.student_id_label2.place(relx=0.214, rely=0.54, height=14, width=65)

        self.roll_no_label2 = tk.Label(top, activebackground="#f9f9f9", activeforeground="black", background="#CED4DA",
                                       disabledforeground="#a3a3a3", foreground="#000000",
                                       highlightbackground="#d9d9d9", highlightcolor="black", text='''Roll no. :''')
        self.roll_no_label2.place(relx=0.251, rely=0.609, height=13, width=56)

        self.email_label2 = tk.Label(top, activebackground="#f9f9f9", activeforeground="black", background="#CED4DA",
                                     disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                                     highlightcolor="black", text='''Email :''')
        self.email_label2.place(relx=0.269, rely=0.681, height=12, width=55)

        self.password_label2 = tk.Label(top, activebackground="#f9f9f9", activeforeground="black", background="#CED4DA",
                                        disabledforeground="#a3a3a3", foreground="#000000",
                                        highlightbackground="#d9d9d9", highlightcolor="black", text='''Password :''')
        self.password_label2.place(relx=0.22, rely=0.753, height=13, width=64)

        self.branch_id_label2 = tk.Label(top, activebackground="#f9f9f9", activeforeground="black",
                                         background="#CED4DA", disabledforeground="#a3a3a3", foreground="#000000",
                                         highlightbackground="#d9d9d9", highlightcolor="black", text='''Branch id :''')
        self.branch_id_label2.place(relx=0.211, rely=0.823, height=13, width=70)

        self.modify_button = tk.Button(top, activebackground="#ececec", activeforeground="#000000",
                                       background="#E9ECEF", disabledforeground="#a3a3a3", foreground="#000000",
                                       highlightbackground="#d9d9d9", highlightcolor="black", pady="0",
                                       text='''Modify''',
                                       command=lambda: self.select_modify(self.student_id_entry2.get(),
                                                                          self.roll_no_entry2.get(),
                                                                          self.email_entry2.get(),
                                                                          self.password_entry2.get(),
                                                                          self.branch_id_entry2.get()))
        self.modify_button.place(relx=0.642, rely=0.907, height=24, width=77)

        self.cancel_button = tk.Button(top, activebackground="#ececec", activeforeground="#000000",
                                       background="#E9ECEF", disabledforeground="#a3a3a3", foreground="#000000",
                                       highlightbackground="#d9d9d9", highlightcolor="black", pady="0",
                                       text='''Cancel''')
        self.cancel_button.place(relx=0.153, rely=0.907, height=24, width=77)

        global item_modifyStudent
        item_modifyStudent = tv.item(tv.focus())['values']
        print("PREVIOUSLY : ")
        print(item_modifyStudent[0])
        print(item_modifyStudent[1])
        print(item_modifyStudent[2])
        print(item_modifyStudent[3])
        print(item_modifyStudent[4])
        print("BEGIN")
        self.student_id_entry1.insert(0, item_modifyStudent[0])
        self.student_id_entry1.config(state="disable")
        self.branch_id_entry1.insert(0, item_modifyStudent[1])
        self.branch_id_entry1.config(state="disable")
        self.roll_no_entry1.insert(0, item_modifyStudent[2])
        self.roll_no_entry1.config(state="disable")
        self.email_entry1.insert(0, item_modifyStudent[3])
        self.email_entry1.config(state="disable")
        self.password_entry1.insert(0, item_modifyStudent[4])
        self.password_entry1.config(state="disable")
        print("END")

    def select_back(self):
        self.master.withdraw()

    def select_modify(self, student_id, roll_no, email, password, branch_id):
        try:
            if not email.isnumeric():
                print("begin")
                sql_query = "UPDATE student SET student_id=" + str(student_id) + ", branch_id=" + str(
                    branch_id) + ", roll_no='" + roll_no + "', email='" + email + "', password='" + password + "' WHERE student_id=" + str(
                    item_modifyStudent[0]) + ";"
                print("end")
                try:
                    mycursor.execute(sql_query)  # executing query
                    tv.item(tv.focus(), text="", values=(str(student_id), str(branch_id), roll_no, email, password))
                except (mysql.connector.Error, mysql.connector.Warning) as e:  # fetching error
                    messagebox.showerror("Error Message", "ERROR MESSAGE\n" + str(e))  # displaying error
            else:
                messagebox.showerror("Error Message", "Email cannot be numeric!")

        except:
            messagebox.showerror("Error Message", "Modification failed")
        mydb.commit()
        self.master.withdraw()


class SubjectModify:
    def __init__(self, top=None):
        self.master = top
        top.geometry("327x370+455+152")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(0, 0)
        top.title("Modify")
        top.configure(background="#CED4DA", highlightbackground="#d9d9d9", highlightcolor="black")

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.245, rely=0.027, height=22, width=154)
        self.Label1.configure(activebackground="#f9f9f9", activeforeground="black", background="#CED4DA",
                              disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 13 -weight bold",
                              foreground="#212529", highlightbackground="#d9d9d9", highlightcolor="black",
                              text='''PRESENT DATA''')

        self.Label1_1 = tk.Label(top)
        self.Label1_1.place(relx=0.306, rely=0.432, height=22, width=114)
        self.Label1_1.configure(activebackground="#f9f9f9", activeforeground="black", background="#CED4DA",
                                disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 13 -weight bold",
                                foreground="#212529", highlightbackground="#d9d9d9", highlightcolor="black",
                                text='''NEW DATA''')

        self.name_label1 = tk.Label(top)
        self.name_label1.place(relx=0.122, rely=0.189, height=19, width=95)
        self.name_label1.configure(activebackground="#f9f9f9", activeforeground="black", background="#CED4DA",
                                   disabledforeground="#a3a3a3", foreground="#000000",
                                   highlightbackground="#d9d9d9",
                                   highlightcolor="black", text='''Subject name :''')

        self.credit_label1 = tk.Label(top)
        self.credit_label1.place(relx=0.135, rely=0.27, height=20, width=86)
        self.credit_label1.configure(activebackground="#f9f9f9", activeforeground="black", background="#CED4DA",
                                     disabledforeground="#a3a3a3", foreground="#000000",
                                     highlightbackground="#d9d9d9",
                                     highlightcolor="black", text='''Subject credit :''')

        self.code_label1 = tk.Label(top)
        self.code_label1.place(relx=0.128, rely=0.103, height=22, width=95)
        self.code_label1.configure(activebackground="#f9f9f9", activeforeground="black", background="#CED4DA",
                                   disabledforeground="#a3a3a3", foreground="#000000",
                                   highlightbackground="#d9d9d9",
                                   highlightcolor="black", text='''Subject code :''')

        self.branch_id_label1 = tk.Label(top)
        self.branch_id_label1.place(relx=0.183, rely=0.362, height=11, width=74)
        self.branch_id_label1.configure(activebackground="#f9f9f9", activeforeground="black", background="#CED4DA",
                                        disabledforeground="#a3a3a3", foreground="#000000",
                                        highlightbackground="#d9d9d9",
                                        highlightcolor="black", text='''Branch id :''')

        self.code_entry1 = tk.Entry(top)
        self.code_entry1.place(relx=0.459, rely=0.108, height=20, relwidth=0.318)
        self.code_entry1.configure(background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                   foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                   insertbackground="black", selectbackground="blue", selectforeground="white")

        self.name_entry1 = tk.Entry(top)
        self.name_entry1.place(relx=0.459, rely=0.189, height=20, relwidth=0.318)
        self.name_entry1.configure(background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                   foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                   insertbackground="black", selectbackground="blue", selectforeground="white")

        self.credit_entry1 = tk.Entry(top)
        self.credit_entry1.place(relx=0.459, rely=0.27, height=20
                                 , relwidth=0.318)
        self.credit_entry1.configure(background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                     foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                     insertbackground="black", selectbackground="blue", selectforeground="white")

        self.branch_id_entry1 = tk.Entry(top)
        self.branch_id_entry1.place(relx=0.459, rely=0.351, height=20
                                    , relwidth=0.318)
        self.branch_id_entry1.configure(background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                        foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                        insertbackground="black", selectbackground="blue", selectforeground="white")

        self.code_entry2 = tk.Entry(top)
        self.code_entry2.place(relx=0.459, rely=0.514, height=20, relwidth=0.318)

        self.code_entry2.configure(background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                   foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                   insertbackground="black", selectbackground="blue", selectforeground="white")

        self.name_entry2 = tk.Entry(top)
        self.name_entry2.place(relx=0.459, rely=0.595, height=20, relwidth=0.318)
        self.name_entry2.configure(background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                   foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                   insertbackground="black", selectbackground="blue", selectforeground="white")

        self.credit_entry2 = tk.Entry(top)
        self.credit_entry2.place(relx=0.459, rely=0.676, height=20
                                 , relwidth=0.318)
        self.credit_entry2.configure(background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                     foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                     insertbackground="black", selectbackground="blue", selectforeground="white")

        self.branch_id_entry2 = tk.Entry(top)
        self.branch_id_entry2.place(relx=0.459, rely=0.757, height=20
                                    , relwidth=0.318)
        self.branch_id_entry2.configure(background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                        foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                        insertbackground="black", selectbackground="blue", selectforeground="white")

        self.code_label2 = tk.Label(top)
        self.code_label2.place(relx=0.153, rely=0.514, height=22, width=85)
        self.code_label2.configure(activebackground="#f9f9f9", activeforeground="black", background="#CED4DA",
                                   disabledforeground="#a3a3a3", foreground="#000000",
                                   highlightbackground="#d9d9d9",
                                   highlightcolor="black", text='''Subject code :''')

        self.name_label2 = tk.Label(top)
        self.name_label2.place(relx=0.147, rely=0.595, height=20, width=86)
        self.name_label2.configure(activebackground="#f9f9f9", activeforeground="black", background="#CED4DA",
                                   disabledforeground="#a3a3a3", foreground="#000000",
                                   highlightbackground="#d9d9d9",
                                   highlightcolor="black", text='''Subject name :''')

        self.credit_label2 = tk.Label(top)
        self.credit_label2.place(relx=0.15, rely=0.673, height=19, width=85)
        self.credit_label2.configure(activebackground="#f9f9f9", activeforeground="black", background="#CED4DA",
                                     disabledforeground="#a3a3a3", foreground="#000000",
                                     highlightbackground="#d9d9d9",
                                     highlightcolor="black", text='''Subject credit :''')

        self.branch_id_label2 = tk.Label(top)
        self.branch_id_label2.place(relx=0.214, rely=0.768, height=11, width=64)
        self.branch_id_label2.configure(activebackground="#f9f9f9", activeforeground="black", background="#CED4DA",
                                        disabledforeground="#a3a3a3", foreground="#000000",
                                        highlightbackground="#d9d9d9",
                                        highlightcolor="black", text='''Branch id :''')

        self.modify_button = tk.Button(top)
        self.modify_button.place(relx=0.612, rely=0.865, height=24, width=77)
        self.modify_button.configure(activebackground="#ececec", activeforeground="#000000", background="#E9ECEF",
                                     disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                                     highlightcolor="black", pady="0", text='''Modify''',
                                     command=lambda: self.select_modify(self.code_entry2.get(),
                                                                        self.branch_id_entry2.get(),
                                                                        self.name_entry2.get(),
                                                                        self.credit_entry2.get()))

        self.cancel_button = tk.Button(top)
        self.cancel_button.place(relx=0.183, rely=0.865, height=24, width=77)
        self.cancel_button.configure(activebackground="#ececec", activeforeground="#000000", background="#E9ECEF",
                                     disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                                     highlightcolor="black", pady="0", text='''Cancel''', command=self.select_back)

        global item_modifySubject
        item_modifySubject = tv.item(tv.focus())['values']
        print("PREVIOUSLY : ")
        print(item_modifySubject[0])
        print(item_modifySubject[1])
        print(item_modifySubject[2])
        print(item_modifySubject[3])
        self.code_entry1.insert(0, item_modifySubject[0])
        self.code_entry1.config(state="disable")
        self.name_entry1.insert(0, item_modifySubject[2])
        self.name_entry1.config(state="disable")
        self.credit_entry1.insert(0, item_modifySubject[3])
        self.credit_entry1.config(state="disable")
        self.branch_id_entry1.insert(0, item_modifySubject[1])
        self.branch_id_entry1.config(state="disable")

    def select_back(self):
        self.master.withdraw()

    def select_modify(self, subject_code, branch_id, subject_name, subject_credit):
        if not subject_name.isnumeric():
            try:
                sql_query = "UPDATE subject SET subject_code='" + subject_code + "' , branch_id=" + str(
                    branch_id) + ", subject_name='" + subject_name + "', subject_credit=" + subject_credit + " WHERE subject_code='" + str(
                    item_modifySubject[0]) + "';"
                #            print(sql_query)
                try:
                    mycursor.execute(sql_query)  # executing query
                    tv.item(tv.focus(), text="",
                            values=(subject_code, str(branch_id), subject_name, str(subject_credit)))
                except (mysql.connector.Error, mysql.connector.Warning) as e:  # fetching error
                    print("hello error : ", str(e))
                    messagebox.showerror("Error Message", "ERROR MESSAGE\n" + str(e))  # displaying error
                    print("failure")

            except:
                messagebox.showerror("Error Message", "Modification failed")
        else:
            messagebox.showerror("Error Message", "Subject Name cannot be just numeric!")
        mydb.commit()
        self.master.withdraw()


class MainScreen:
    def __init__(self, top=None):
        self.master = top
        top.geometry("600x450+383+106")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(0, 0)
        top.title("Examination Management System")
        top.configure(background="#212529")

        self.Canvas = tk.Canvas(top, background="#f8f9fa", insertbackground="black", relief="ridge",
                                selectbackground="blue", selectforeground="white")
        self.Canvas.place(relx=0.117, rely=0.178, relheight=0.607, relwidth=0.772)

        self.student_button = tk.Button(self.Canvas, command=self.select_student, activebackground="#ececec",
                                        activeforeground="#000000", background="#3F454C", borderwidth="0",
                                        disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 9 -weight bold",
                                        foreground="#ffffff", highlightbackground="#d9d9d9", highlightcolor="black",
                                        pady="0", text='''Student''')
        self.student_button.place(relx=0.13, rely=0.33, height=24, width=90)

        self.exam_button = tk.Button(self.Canvas, command=self.select_exam, activebackground="#ececec",
                                     activeforeground="#000000", background="#3F454C", borderwidth="0",
                                     disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 9 -weight bold",
                                     foreground="white", highlightbackground="#d9d9d9", highlightcolor="black",
                                     pady="0", text='''Exam''')
        self.exam_button.place(relx=0.67, rely=0.33, height=24, width=90)

        self.subject_button = tk.Button(self.Canvas, command=self.select_subject, activebackground="#ececec",
                                        activeforeground="#000000", background="#3F454C", borderwidth="0",
                                        disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 9 -weight bold",
                                        foreground="#ffffff", highlightbackground="#d9d9d9", highlightcolor="black",
                                        pady="0", text='''Subject''')
        self.subject_button.place(relx=0.13, rely=0.513, height=24, width=90)

        self.result_button = tk.Button(self.Canvas, command=self.select_result, activebackground="#ececec",
                                       activeforeground="#000000", background="#3F454C", borderwidth="0",
                                       disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 9 -weight bold",
                                       foreground="white", highlightbackground="#d9d9d9", highlightcolor="black",
                                       pady="0", text='''Result''')
        self.result_button.place(relx=0.67, rely=0.513, height=24, width=90)

        self.attendance_button = tk.Button(self.Canvas, command=self.select_attendance, activebackground="#ececec",
                                           activeforeground="#000000", background="#3F454C", borderwidth="0",
                                           disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 9 -weight bold",
                                           foreground="white", highlightbackground="#d9d9d9", highlightcolor="black",
                                           pady="0", text="Attendance")
        self.attendance_button.place(relx=0.13, rely=0.696, height=24, width=90)

        self.branch_button = tk.Button(self.Canvas, command=self.select_branch, activebackground="#ececec",
                                       activeforeground="#000000", background="#3F454C", borderwidth="0",
                                       disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 9 -weight bold",
                                       foreground="white", highlightbackground="#d9d9d9", highlightcolor="black",
                                       overrelief="flat", text="Branch")
        self.branch_button.place(relx=0.67, rely=0.696, height=24, width=90)

        self.custom_query_button = tk.Button(self.Canvas, command=self.select_custom_query, activebackground="#ececec",
                                             activeforeground="#000000", background="#3F454C",
                                             font="-family {Segoe UI} -size 9 -weight bold", borderwidth="0",
                                             disabledforeground="#a3a3a3", foreground="#ffffff",
                                             highlightbackground="#d9d9d9", highlightcolor="black", overrelief="flat",
                                             text="Custom Query")
        self.custom_query_button.place(relx=0.382, rely=0.844, height=24, width=110)

        self.Label1 = tk.Label(self.Canvas, background="#f8f9fa", disabledforeground="#a3a3a3",
                               font="-family {Segoe UI} -size 14 -weight bold", foreground="#212529",
                               text="Select a table")
        self.Label1.place(relx=0.216, rely=0.11, height=31, width=264)

    def select_student(self):
        self.master.withdraw()
        Student(Toplevel(self.master))

    def select_exam(self):
        self.master.withdraw()
        Exam(Toplevel(self.master))

    def select_subject(self):
        self.master.withdraw()
        Subject(Toplevel(self.master))

    def select_result(self):
        self.master.withdraw()
        Result(Toplevel(self.master))

    def select_attendance(self):
        self.master.withdraw()
        Attendance(Toplevel(self.master))

    def select_branch(self):
        self.master.withdraw()
        Branch(Toplevel(self.master))

    def select_custom_query(self):
        self.master.withdraw()
        CustomQuery(Toplevel(self.master))


root = tk.Tk()
top = MainScreen(
    root)
root.mainloop()

# Tkinter GUI code ends
