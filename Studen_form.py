class StudentForm:
    formtype = "StudentForm"

    def printdata(self):
        print(f"name is {self.name}")
        print(f"University is {self.University}")
        print(f"Branch is {self.branch}")
        print(f"Passout Year is {self.year}")


Al_QayyumApplication = StudentForm()
Al_QayyumApplication.name = "Sabeel Al Qayyum"
Al_QayyumApplication.University = "Telangana University"
Al_QayyumApplication.branch = "B.com (Computers)"
Al_QayyumApplication.year = "2022 Jan"

Al_QayyumApplication.printdata()
