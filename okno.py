__author__ = 'Laszewski'
import _tkinter
from Tkinter import *
import MySQLdb
#definicje

root = Tk()



#rozmier okna
RTitle=root.title("MySQL connector") #Nazwa okna
root.minsize(600,450)   #rozmiar okna
root.maxsize(600,450)


# Wprowaqdzanie danych
fields = ("user","password","host","database")

# USER

user = Label(root, text="user name")
user.pack( side = TOP, anchor = W)
E1 = Entry(root, bd =5)
E1.pack(side = TOP, anchor = W)

# PASSWORD

password = Label(root, text="password")
password.pack( side = TOP, anchor = W)
E2 = Entry(root, bd =5)
E2.pack(side = TOP, anchor = W)

# HOST

host = Label(root, text="host")
host.pack( side = TOP, anchor = W)
E3 = Entry(root, bd =5)
E3.pack(side = TOP, anchor = W)
 # BASE

base = Label(root, text="base")
base.pack( side = TOP, anchor = W)
E4 = Entry(root, bd =5)
E4.pack(side = TOP, anchor = W)


root.mainloop()




db = MySQLdb.connect(user = user, password = password, host = host, db = base)

  #  cursor = conn.cursor ()
  #  cursor.execute ("SELECT VERSION()")
  #  row = cursor.fetchone ()
  #  print "server version:", row[0]
  #  cursor.close ()






