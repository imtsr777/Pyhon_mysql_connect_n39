import mysql.connector

dbConnection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "sarik45",
    database = "foundation_n39"
)

class Application:

    def __init__(self):
        self.__dbConnection = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "sarik45",
            database = "foundation_n39"
        )

    def getConnection(self):
        return self.__dbConnection
    