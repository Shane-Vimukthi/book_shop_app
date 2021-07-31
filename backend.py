import sqlite3

class Database:

    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title TEXT, author TEXT, year TEXT, isbn INTEGER)")
        self.conn.commit()


    def insert(self,title, author, year, isbn):
        self.cur.execute("INSERT INTO book VALUES(NULL, ?, ?, ?, ?)", (title, author, year, isbn))
        self.conn.commit() # if u do changes to the db use commit or else dont


    def view(self):

        self.cur.execute("SELECT * FROM book")
        rows = self.cur.fetchall()

        return rows


    def search(self, title="", author="", year="",isbn=""): #if user pass only one this function will generate an error so the defaul is set to the empty

        self.cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", (title, author, year,isbn))
        rows = self.cur.fetchall()
        return rows


    def delete(self, id):

        self.cur.execute("DELETE FROM book WHERE id=?", (id,))
        self.conn.commit() # if u do changes to the db use commit or else dont



    def update(self, id, title, author, year, isbn):

        self.cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", (title, author, year, isbn, id))
        self.conn.commit() # if u do changes to the db use commit or else dont

    def __del__(self):
        self.conn.close()


# insert("the jupiter ", " martin smith", 1919, 8883)
# delete(3)
# update(2, "The moon", "joos pola", 1948, 4523)
# print(view())


# print(search(author='john tablet'))