from tkinter import *
import random
import time

root = Tk()
root.geometry("1600x800+0+0")
root.title("Restaurant Management System")

tops=Frame(root, width = 1600, height = 50, bg ="powder blue", relief=SUNKEN)
tops.pack(side=TOP)

f1=Frame(root, width = 800, height = 700, bg ="powder blue", relief=SUNKEN)
f1.pack(side=LEFT)

f2=Frame(root, width = 400, height = 500, bg ="powder blue", relief=SUNKEN)
f2.pack(side=RIGHT)
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++Time+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
localtime=time.asctime(time.localtime(time.time()))
lblinfo=Label(tops, font= ('arial', 50, 'bold'), text="Restaurant Management System", fg= 'Steel blue', bd=10, anchor='w')
lblinfo.grid(row=0, column=0)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
lblinfo=Label(tops, font= ('arial', 20, 'bold'), text=localtime, fg= 'Steel blue', bd=10, anchor='w')
lblinfo.grid(row=1, column=0)



root.mainloop()


