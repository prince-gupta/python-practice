import pymysql.cursors

from pymysql.connections import Connection


class MySQLDBConnection:

    connection = Connection

    def __init__(self, host, port, username, password):
        self.host = host
        self.port = port
        self.username = username
        self.password = password

    def connect(self):
        MySQLDBConnection.connection = pymysql.connect(host=self.host,
                                          user=self.username,
                                          password=self.password,
                                          db='python_test',
                                          charset='utf8mb4',
                                          cursorclass=pymysql.cursors.DictCursor
                                          )
        print "Connection with DB : python_test at host : %s with user : %s has been established." % (self.host,self.username)
        return MySQLDBConnection.connection

    def disconnect(self):
        print "Connection with DB : python_test at host : %s with user : %s has been stopped." % (
        self.host, self.username)
        MySQLDBConnection.connection.close()

    def get_cursor(self):
        return MySQLDBConnection.connection.cursor()

    def commit(self):
        MySQLDBConnection.connection.commit()
        return


# connection = MySQLDBConnection(host="localhost", port="3306", username="python", password="python")
# connection.connect()
# connection.disconnect()

