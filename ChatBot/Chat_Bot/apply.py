from .application import international_application, transfer_application, freshman_application
from .application import application_Controller
from .application import words_list

class apply():
    message = "What is your type of student? (transfer, international, freshman)"
    controller = None
    student = None

    def createStudent(self, studentType):
        if (studentType == "transfer"):
            self.student = transfer_application.transfer()
        elif (studentType == "international"):
            self.student = international_application.international()
        else:
            self.student = freshman_application.freshman()
        self.controller = application_Controller.application_Controller(self.student)

    # we need a method to recognize from user input -> our expected input
    #def executeCommand(self, command):
    #    return self.student.show(command)

    def executeCommand(self, command):
        temp = None
        keywords = []
        if(command == words_list.words_list.process):
            temp = self.student.showApplicationProcess()
        elif(command == words_list.words_list.requiredDocs):
            temp = self.student.showRequiredDocuments()
        elif(command == words_list.words_list.contact):
            temp = self.student.showContact()
        elif(command == words_list.words_list.criteria):
            temp = self.student.showAdmissionCriteria()
        elif(command == words_list.words_list.deadlines):
            temp = self.student.showDeadlines()
        if(temp != None):
            keywords.append(temp)
        else:
            keywords = command
        for keyword in keywords:
            self.controller.search(keyword)