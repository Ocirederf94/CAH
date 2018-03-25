import sqlite3


def createTableUsers():
    db = connectToDb()
    cursor = db.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, userName TEXT UNIQUE  NOT NULL, password TEXT NOT NULL)''')
    db.commit()
    db.close()


def getDatabaseUserName(userNameToSearch):
    db = connectToDb()
    cursor = db.cursor()
    cursor.execute('''SELECT userName FROM users WHERE userName=?''', ([userNameToSearch]))
    userName = cursor.fetchone()
    db.close()
    
    return userName

def getIdFromUserNameAndPass(userNameToSearch, passwordToSearch):
    db = connectToDb()
    cursor = db.cursor()
    cursor.execute('''SELECT id FROM users WHERE userName=? and password=?''', (userNameToSearch, passwordToSearch))
    userName = cursor.fetchone()
    db.close()
    
    return userName
    
def insertUserNameInDb(userNameToAdd, passwordToAdd):
    db = connectToDb()
    cursor = db.cursor()
    cursor.execute('''INSERT INTO users(userName, password) VALUES(?, ?) ''', (userNameToAdd, passwordToAdd))
    db.commit()
    db.close()
    
def connectToDb():
    #return sqlite3.connect('db.sqlite3')
    return sqlite3.connect('D:\Projects\Git\CAH\CAH\db.sqlite3')

