from dbconnection import MySQLDBConnection


class UserOperations:
    connection = MySQLDBConnection

    def __init__(self, username, password, email):
        self.username = username
        self.password = password
        self.email = email
        self.connection = MySQLDBConnection(host="localhost", port="3306", username="python", password="python")
        self.connection.connect()

    def disconnect(self):
        self.connection.disconnect()

    def insert(self):

        try:
            with self.connection.get_cursor() as cursor:
                sql = "INSERT INTO `users` (`email`,`password`,`name`) VALUES (%s,%s,%s)"
                cursor.execute(sql, (self.email, self.password, self.username))
            self.connection.commit()

        except:
            self.connection.connection.rollback()

    def fetch_all(self):

        with self.connection.get_cursor() as cursor:
            sql = "SELECT * FROM `users`"
            cursor.execute(sql)
            result = cursor.fetchall()
            print result

    def delete(self, email):
        try:

            with self.connection.get_cursor() as cursor:
                sql = "DELETE FROM `users` WHERE email = %s"
                cursor.execute(sql, email)
            self.connection.commit()

        except:
            self.connection.connection.rollback()


userOperation = UserOperations("prince", "secret", "sam@test.com")
userOperation.insert()
userOperation.fetch_all()
userOperation.delete("sam@test.com")
userOperation.fetch_all()
userOperation.disconnect()
