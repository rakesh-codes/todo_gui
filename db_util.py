import mysql.connector

class Todo:
    db_connection = None 

    def getConnection(self):
        usr_name = "root"
        usr_password = "password"
        db_host = "127.0.0.1"
        db_name = "to_do"
        self.db_connection = mysql.connector.connect(user=usr_name,password=usr_password,host=db_host,database=db_name)
        if self.db_connection.is_connected():
            #print("Connection successful")
            return self.db_connection
        else:
            print("Connection failed")
            return None

    def closeConnection(self): 
        if self.db_connection.is_connected():
            self.db_connection.close()
            #print("Disconnection is successful")
        else:
            print("Database connection not open")
