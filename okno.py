__author__ = 'Laszewski'
import _tkinter
from Tkinter import *
import MySQLdb  # TO BEDZIE TRZEBA USUNAC
import mysql.connector
from mysql.connector import errorcode
#definicje

root = Tk()



#rozmier okna
RTitle=root.title("MySQL connector") #Nazwa okna
root.minsize(600,450)   #rozmiar okna
root.maxsize(600,450)



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

#################### Dfinicja dla przycisku RUN

def run(self):
    try:
        cnx = mysql.connector.connect(user="E1",password="E2",host="E3", database="E4")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Cos poszlo nie tak, sprawdz wprowadzone dane, albo zjedz banana")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Podana baza nie istnieje")
        else:
            print(err)
    else:
        cnx.close()







#db = MySQLdb.connect(user = E1, password = E2, host = E3, db = E4)

  #  cursor = conn.cursor ()
  #  cursor.execute ("SELECT VERSION()")
  #  row = cursor.fetchone ()
  #  print "server version:", row[0]
  #  cursor.close ()






