__author__ = 'Laszewski'
import _tkinter
from Tkinter import *
import MySQLdb  # TO BEDZIE TRZEBA USUNAC
import mysql.connector
from mysql.connector import errorcode
import urllib
import urllib2
import htmllib
# definicje


root = Tk()


#rozmier okna
RTitle = root.title("MySQL connector")  #Nazwa okna
root.minsize(600, 450)  #rozmiar okna
root.maxsize(600, 450)



def usr(self): pass

user = Label(root, text="user name")
user.pack(side=TOP, anchor=W)
uEntry = Entry(root, bd=5).pack(side=TOP, anchor=W)
#u = Entry(root, bd =5)
#u.pack(side = TOP, anchor = W,)


# PASSWORD
def paswd(self): pass


password = Label(root, text="password")
password.pack(side=TOP, anchor=W)
pEntry = Entry(root, bd=5).pack(side=TOP, anchor=W)
#   p = Entry(root, bd =5)
#p.pack(side = TOP, anchor = W)

# HOST
def hst(self): pass


host = Label(root, text="host")
host.pack(side=TOP, anchor=W)
hEntry = Entry(root, bd=5).pack(side=TOP, anchor=W)
#h = Entry(root, bd =5)
#h.pack(side = TOP, anchor = W)
# BASE
def bsd(self): pass


base = Label(root, text="base")
base.pack(side=TOP, anchor=W)
bEntry = Entry(root, bd=5).pack(side=TOP, anchor=W)
#b = Entry(root, bd =5)
#b.pack(side = TOP, anchor = W)  #################### Dfinicja dla przycisku RUN

def run():
    try:
        cnx = mysql.connector.connect(user= usr, password= paswd, host= hst, database= bsd)
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Cos poszlo nie tak, sprawdz wprowadzone dane, albo zjedz banana")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Podana baza nie istnieje")
        else:
            print(err)
    else:
        cnx.close()


##### Przycisk RUN

b = Button(root, text="RUN", command=run)
b.pack()

root.mainloop()




#db = MySQLdb.connect(user = E1, password = E2, host = E3, db = E4)

#  cursor = conn.cursor ()
#  cursor.execute ("SELECT VERSION()")
#  row = cursor.fetchone ()
#  print "server version:", row[0]
#  cursor.close ()






