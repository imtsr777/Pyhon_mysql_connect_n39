from Application import Application

class StudentInterface:

    id: int = None

    firstName: str = None

    lastName: str = None

    age: int = None

    course: int = None



class Students:

    def __init__(self):
        self.app = Application()
        self.dbConnection = self.app.getConnection()
        self.cursor = self.dbConnection.cursor()


    def getStudentsList(self, page = 1, size = 5) -> list[StudentInterface]:
        data = []
        try:
            query = "SELECT * FROM students ORDER BY id LIMIT %s OFFSET %s"
            self.cursor.execute(query, (size, (page - 1) * size))
            students = self.cursor.fetchall()
            

            for student in students:
                obj = StudentInterface()

                obj.id = student[0]
                obj.firstName = student[1]
                obj.lastName = student[2]
                obj.age = student[3]
                obj.course = student[4]
                data.append(obj)

        except:
            print("Hatolik")
        
        return data
        


    def getById(self, id: int) -> StudentInterface:
        obj = StudentInterface()
        try:
            query = "SELECT * FROM students WHERE id = %s"
            self.cursor.execute(query, ( id, ))
            student = self.cursor.fetchone()

            if( student ):
                obj.id = student[0]
                obj.firstName = student[1]
                obj.lastName = student[2]
                obj.age = student[3]
                obj.course = student[4]

        except:
            print("Error")

        return obj
    
    def deleteById(self, id: int) -> bool:
        try:
            query = "DELETE FROM students WHERE id=%s"
            self.cursor.execute(query, (id, ))
            self.dbConnection.commit()
            return True
        except:
            print("Hatolik")
            return False



# obj = Students()
# a = obj.getStudentsList()

# for item in a:
#     print(item.age, end=" ")
#     print(item.firstName, end=" ")
#     print(item.lastName, end=" ")
#     print(item.course)
