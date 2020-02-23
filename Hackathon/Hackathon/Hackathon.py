


def main():
    print("Welcome to the Stem Study Buddy Program!")
    choice = main_menu()
    course_number = checkcourse(choice)
    print("Would you like to run the program again?\n")
    check = input("Enter 1 for yes, any other key for no.\n")
    if (check == "1" or check == 1):
        main()
    

def main_menu():
        
    """This is the main funciton, it should identify the students class """ 
        
    print("Please enter in the major for the class you need to study for: ")
    print("1. for Electrical Engineering")
    print("2. for Bioengineering")
    print("3. for Chemcial Engineering")
    print("4. for Mechanical Engineering")
    print("5. for Civil Engineering")
    print("6. for Biology")
    print("7. for Data Analytics")
    print("8. for Chemistry")
    choice = input()
    return choice
        
#This tests the course major and asks for the course number 
def checkcourse(choice):
    global course_number
        

        
    if (choice == "1"):
        
        check = input("What is the EE course number?\n")
        course_number = "EE" + str(check)
        #declaring options

        study_materials = "study materials"
        exam_1 = "Exam 1"
        exam_2 = "Exam 2"
        study_guideEE = "study guides"
        # #declaring files
        EE214_eqs = open('EE_gen_EQs.txt','r')
        EE214_exam1 = open('Exam1EE.txt','r')
        EE214_exam2 = open('Exam2EE.txt', 'r')
        EE214studyguide = open('EEstudyguide.txt','r')
        EE261_eqs = open('EE261_geneqs.txt','r')
        EE261_exam1 = open('EE261_Exam1.txt','r')
        EE261_exam2 = open('EE261_Exam2.txt', 'r')
        EE261studyguide = open('EE261_studyguide.txt','r')
        EE331_eqs = open('EE331_geneqs.txt','r')
        EE331_exam1 = open('EE331_Exam1.txt','r')
        EE331_exam2 = open('EE331_Exam2.txt', 'r')
        EE331studyguide = open('EE331_studyguide.txt','r')
        #ELECTRICAL ENGINEERING
        if (course_number == "EE214"): #Electrical Engineering 214
            print("Digital Logic Circuits")
            study_question = input("Would you like 1). study materials or 2). general equations? ")
            if (study_question == study_materials or study_question == "1"):
                material_question = input("Choose one of the following: Exam 1, Exam2, or study guides: ")
                if (material_question == exam_1 or material_question == "1" or material_question == "exam1"):
                            print(EE214_exam1.read())
                elif (material_question == exam_2 or material_question == "2" or material_question == "exam2"):
                            print(EE214_exam2.read())
                else: print(EE214studyguide.read())
            else: print(EE214_eqs.read())
        elif (course_number == "EE261"): #Electrical Engineering 261
            print("Electrical Circuits")
            study_question = input("Would you like 1). study materials or 2). general equations? ")
            if (study_question == study_materials or study_question == "1"):
                material_question = input("Choose one of the following: Exam 1, Exam2, or study guides: ")
                if (material_question == exam_1 or material_question == "1" or material_question == "exam1"):
                    print(EE261_exam1.read())
                elif (material_question == exam_2 or material_question == "2" or material_question == "exam2"):
                    print(EE261_exam2.read())
                else: print(EE261studyguide.read())
            else: print(EE261_eqs.read())
        elif (course_number == "EE 331"): #Electrical Engineering 261
            print("Electromagnetic Fields and Waves")
            study_question = input("Would you like study 1). materials or 2). general equations? ")
            if (study_question == study_materials or study_question == "1"):
                material_question = input("Choose one of the following: Exam 1, Exam2, or study guides: ")
                if (material_question == exam_1 or material_question == "1" or material_question == "exam1"):
                    print(EE331_exam1.read())
                elif (material_question == exam_2 or material_question == "2" or material_question == "exam2"):
                    print(EE331_exam2.read())
                else: print(EE331studyguide.read())
            else: print(EE331_eqs.read())
        else:
            print("Course not recognized, please try again!\n")
            checkcourse(choice)

            #Bioengineering
    elif (choice == "2" or choice == "BE" or choice == "Bioengineering"):
        check = input("What is the BE course number?\n")
        course_number = "BE" + str(check) 
        if (course_number == "BE330"): #initially checks the course number
            print("This is Bioinstrumentation\n")
            material =  input("Would you like 1). Study Materials or 2). General Equations?\n")
            if (material == "study materials" or material == "1"):
                exams = input("Would you like Exam 1, or Exam 2?\n")
                if (exams == "exam 1" or exams == "exam1" or exams == "1"):
                    exam1 = open("BE330_Exam1.txt", "r")
                    print(exam1.read())
                        
                elif(exams == "exam 2" or exams == "exam2" or exams == "2"):
                    exam2 = open("BE330_EXAM2.txt", "r")
                    print(exam2.read())
                        
                else:
                    print("Wrong input recognized, please try again")
                    checkcourse(choice)

            elif(material == "general equations" or material == "2"):
                geneq = open("BE330_GEN.txt","r")
                print(geneq.read())
                    
            else:
                print("Sorry, input entered is not recognized ")
                checkcourse(choice)
            
        elif(course_number == "BE340"): 
            print("This is Unified Systems I\n")
            material =  input("Would you like 1). Study Materials or 2). General Equations?\n") 
            if (material == "study materials" or material == "1"): #Checks against the above inputs 
                exams = input("Would you like Exam 1, or Exam 2?\n")
                if (exams == "exam 1" or exams == "exam1" or exams == "1"):
                    exam1 = open("BE340_EXAM1.txt", "r")
                    print(exam1.read())
                        
                elif(exams == "exam 2" or exams == "exam2" or exams == "2"):
                    exam2 = open("BE340_EXAM2.txt", "r")
                    print(exam2.read())
                        
                else:
                    print("Wrong input recognized, please try again")
                    checkcourse(choice)

            elif(material == "general equations" or material == "2"):
                geneq = open("BE340_GEN.txt","r")
                print(geneq.read())

        elif(course_number == "BE435"): 
            print("This is Bioelectric Phenomena and Devices\n")
            material =  input("Would you like 1). Study Materials or 2). General Equations?\n") 
            if (material == "study materials" or material == "1"): #Checks against the above inputs 
                exams = input("Would you like Exam 1, or Exam 2?\n")
                if (exams == "exam 1" or exams == "exam1" or exams == "1"):
                    exam1 = open("BE425_EXAM1.txt", "r")
                    print(exam1.read())
                        
                elif(exams == "exam 2" or exams == "exam2" or exams == "2"):
                    exam2 = open("BE425_EXAM2.txt", "r")
                    print(exam2.read())
                        
                else:
                    print("Wrong input recognized, please try again")
                    checkcourse(choice)

            elif(material == "general equations" or material == "2"):
                geneq = open("BE425_GEN.txt","r")
                print(geneq.read())
        else:
            print("Sorry, this course is not recognized, please try again!\n")
            checkcourse(choice)
        return course_number 
    #Chemical Engineering

    elif (choice == "3" or choice == "CHE" or choice == "Chemical Engineering"):
        check = input("What is the CHE course number?\n")
        course_number = "CHE" + str(check)
        study_materials = "study materials"
        exam_1 = "Exam 1"
        exam_2 = "Exam 2"
        study_guideEE = "study guides"
        #declaring files
        CHE201_eqs = open('CHE201_geneqs.txt','r')
        CHE201_exam1 = open('CHE201_Exam1.txt','r')
        CHE201_exam2 = open('CHE201_Exam2.txt', 'r')
        CHE201studyguide = open('CHE201_studyguides.txt','r')
        CHE310_eqs = open('CHE310_geneqs.txt','r')
        CHE310_exam1 = open('CHE310_Exam1.txt','r')
        CHE310_exam2 = open('CHE310_Exam2.txt', 'r')
        CHE310studyguide = open('CHE310_studyguides.txt','r')
        CHE301_eqs = open('CHE301_geneqs.txt','r')
        CHE301_exam1 = open('CHE301_Exam1.txt','r')
        CHE301_exam2 = open('CHE301_Exam2.txt', 'r')
        CHE301studyguide = open('CHE301_studyguideS.txt','r')
        #CHEMICAL ENGINEERING
        if (course_number == "CHE201"): #Chemical Engineering 201
            print("Chemical Process Principles and Calculations ")
            study_question = input("Would you like 1). study materials or 2). general equations? ")
            if (study_question == study_materials or study_question == "1"):
                material_question = input("Choose one of the following: Exam 1, Exam2, or study guides: ")
                if (material_question == exam_1 or material_question == "exam1" or material_question == "1"):
                    print(CHE201_exam1.read())
                elif (material_question == exam_2 or material_question == "exam2" or material_question == "2"):
                    print(CHE201_exam2.read())
                else: print(CHE201studyguide.read())
            else: print(CHE201_eqs.read())
        elif (course_number == "CHE310"): #Chemical Engineering 215
            print("Introduction to Transport Processes")
            study_question = input("Would you like 1). study materials or 2). general equations? ")
            if (study_question == study_materials or study_question == "1"):
                material_question = input("Choose one of the following: Exam 1, Exam2, or study guides: ")
                if (material_question == exam_1 or material_question == "exam1" or material_question == "1"):
                    print(CHE310_exam1.read())
                elif (material_question == exam_2 or material_question == "exam2" or material_question == "2"):
                    print(CHE310_exam2.read())
                else: print(CHE310studyguide.read())
            else: print(CHE310_eqs.read())
        elif (course_number == "CHE301"): #Chemical Engineering 301
            print("Chemical Engineering Thermodynamics")
            study_question = input("Would you like 1). study materials or 2). general equations? ")
            if (study_question == study_materials or study_question == "1"):
                material_question = input("Choose one of the following: Exam 1, Exam2, or study guides: ")
                if (material_question == exam_1 or material_question == "exam1" or material_question == "1"):
                    print(CHE301_exam1.read())
                elif (material_question == exam_2 or material_question == "exam2" or material_question == "2"):
                    print(CHE301_exam2.read())
                else: print(CHE301studyguide.read())
            else: print(CHE301_eqs.read())
        else:
            print("This ChemE class is NOT AVAILABLE!! Please try again!\n")
            checkcourse(choice)
    #Mechanical Engineering
    elif (choice == "4" or choice == "ME" or choice == "Mechanical Engineering"):
        check = input("What is the ME course number?\n")
        course_number = "ME" + str(check) 
            
            

        if (course_number ==  "ME214"):

            material_choice = input("Would you like 1). Study Materials or 2). General Equations?\n")
            if (material_choice == "General Equations" or material_choice == "2" or material_choice == "general equations"):

                outFile = open("ME214_Gen.txt", "r")

                print(outFile.read())

                outFile.close()

            elif (material_choice == "Study Materials" or material_choice == "1" or material_choice == "study materials" ):

                material_choice = input("Would you like to Exam 1 or Exam 2? ")

                if (material_choice == "1"):

                    outFile = open("ME214_Exam1.txt", "r")

                    print(outFile.read())

                elif (material_choice == "2"):

                    outFile = open("ME214_Exam2.txt", "r")

                    print(outFile.read())

                else:

                    print("Incorrect input!  Please try again!")
                    checkcourse(choice)

            else:

                print("Incorrect input!  Please try again!")
                checkcourse(choice)


        elif(course_number == "ME301"):
            material_choice = input("Would you like 1). Study Materials or 2). General Equations?\n")
            if (material_choice == "General Equations" or material_choice == "2" or material_choice == "general equations"):

                outFile = open("ME301_Gen.txt", "r")

                print(outFile.read())

                outFile.close()

            elif (material_choice == "Study Materials" or material_choice == "1" or material_choice == "study materials"):

                material_choice = input("Would you like to Exam 1 or Exam 2? ")

                if (material_choice == "1"):

                    outFile = open("ME301_Exam1.txt", "r")

                    print(outFile.read())

                elif (material_choice == "2"):

                    outFile = open("ME301_Exam2.txt", "r")

                    print(outFile.read())

                else:

                    print("Incorrect input!  Please try again!")
                    checkcourse(choice)

            else:

                print("Incorrect input!  Please try again!")
                checkcourse(choice)
        else:
            print("Sorry, the entered course is not available, please try again!\n")
            checkcourse(choice)
    #Civil Engineering
    elif (choice == "5" or choice == "CE" or choice == "Civil Engineering"):
        check = input("What is the CE course number?\n")
        course_number = "CE" + str(check) 
            
        study_materials = "study materials"
        exam_1 = "Exam 1"
        exam_2 = "Exam 2"
        study_guideEE = "study guides"
        #declaring files
        CE211_eqs = open('CE211_geneqs.txt','r')
        CE211_exam1 = open('CE211_Exam1.txt','r')
        CE211_exam2 = open('CE211_Exam2.txt', 'r')
        CE211studyguide = open('CE211_studyguides.txt','r')
        CE215_eqs = open('CE215_geneqs.txt','r')
        CE215_exam1 = open('CE215_Exam1.txt','r')
        CE215_exam2 = open('CE215_Exam2.txt', 'r')
        CE215studyguide = open('CE215_studyguides.txt','r')
        CE430_eqs = open('CE430_geneqs.txt','r')
        CE430_exam1 = open('CE430_Exam1.txt','r')
        CE430_exam2 = open('CE430_Exam2.txt', 'r')
        CE430studyguide = open('CE430_studyguideS.txt','r')
        #CIVIL ENGINEERING
        if (course_number == "CE211"): #Civil Engineering 214
            print("Statics")
            study_question = input("Would you like 1). study materials or 2). general equations? ")
            if (study_question == study_materials or study_question == "1"):
                material_question = input("Choose one of the following: Exam 1, Exam2, or study guides: ")
                if (material_question == exam_1 or material_question == "exam1" or material_question == "1"):
                    print(CE211_exam1.read())
                elif (material_question == exam_2  or material_question == "2" or material_question == "exam2"):
                    print(CE211_exam2.read())
                else: print(CE211studyguide.read())
            else: print(CE211_eqs.read())
        elif (course_number == "CE215"): #Civil Engineering 215
            print("Mechanics of Materials")
            study_question = input("Would you like 1). study materials or 2). general equations? ")
            if (study_question == study_materials or study_question == "1"):
                material_question = input("Choose one of the following: Exam 1, Exam2, or study guides: ")
                if (material_question == exam_1 or material_question == "1" or material_question == "exam1"):
                    print(CE215_exam1.read())
                elif (material_question == exam_2 or material_question == "exam2" or material_question == "2"):
                    print(CE215_exam2.read())
                else: print(CE215studyguide.read())
            else: print(CE215_eqs.read())
        elif (course_number == "CE430"): #Civil Engineering 430
            print("Analysis of Indeterminate Structures")
            study_question = input("Would you like 1). study materials or 2). general equations? ")
            if (study_question == study_materials):
                material_question = input("Choose one of the following: Exam 1, Exam2, or study guides: ")
                if (material_question == exam_1 or material_question == "exam1" or material_question == "1"):
                    print(CE430_exam1.read())
                elif (material_question == exam_2 or material_question == "exam2" or material_question == "2"):
                    print(CE430_exam2.read())
                else: print(CE440studyguide.read())
            else: print(CE430_eqs.read())
        else:
            print("This CE class is NOT AVAILABLE!! Please try again!\n")
            checkcourse(choice)

        return course_number 
    #Biology
    elif (choice == "6" or choice == "BIO" or choice == "Biology"):
        check = input("What is the BIO course number?\n")
        course_number = "BIO" + str(check) 
        if (course_number == "BIO301"): #initially checks the course number
            print("This is General Genetics\n")
            material =  input("Would you like 1). Study Materials or 2). General Anatomy?\n")
            if (material == "study materials" or material == "1"):
                exams = input("Would you like notes on Exam 1, Exam 2, or a study guide?\n")
                if (exams == "exam 1" or exams == "exam1" or exams == "1"):
                    exam1 = open("BIO301_Exam1.txt", "r")
                    print(exam1.read())
                        
                elif(exams == "exam 2" or exams == "exam2" or exams == "2"):
                    exam2 = open("BIO301_EXAM2.txt", "r")
                    print(exam2.read())
                        
                else:
                    print("Wrong input recognized, please try again")
                    checkcourse(choice)

            elif(material == "general equations" or material == "2"):
                geneq = open("BIO301_GEN.txt","r")
                print(geneq.read())
                    
            elif(material == "study guide" or material == "3"):
                study = open("BIO301_STUDY.txt","r")
                print(study.read())

            else:
                print("Sorry, input entered is not recognized ")
                checkcourse(choice)
            
        elif(course_number == "BIO315"): 
            print("Gross and Microanatomy\n")
            material =  input("Would you like 1). Study Materials or 2). General Anatomy\n") 
            if (material == "study materials" or material == "1"): #Checks against the above inputs 
                exams = input("Would you like Exam 1, Exam 2, or a study guide?\n")
                if (exams == "exam 1" or exams == "exam1" or exams == "1"):
                    exam1 = open("BE315_EXAM1.txt", "r")
                    print(exam1.read())
                        
                elif(exams == "exam 2" or exams == "exam2" or exams == "2"):
                    exam2 = open("BE315_EXAM2.txt", "r")
                    print(exam2.read())

                elif(material == "study guide" or material == "3"):
                    study = open("BIO315_STUDY.txt","r")
                    print(study.read())

                else:
                    print("Wrong input recognized, please try again")
                    checkcourse(choice)

            elif(material == "general equations" or material == "2"):
                geneq = open("BE315_GEN.txt","r")
                print(geneq.read())

        elif(course_number == "BIO353"): 
            print("Advanced Human Physiology\n")
            material =  input("Would you like 1). Study Materials or 2). General Anatomy?\n") 
            if (material == "study materials" or material == "1"): #Checks against the above inputs 
                exams = input("Would you like Exam 1, Exam 2, or a study guide?\n")
                if (exams == "exam 1" or exams == "exam1" or exams == "1"):
                    exam1 = open("BIO353_EXAM1.txt", "r")
                    print(exam1.read())
                        
                elif(exams == "exam 2" or exams == "exam2" or exams == "2"):
                    exam2 = open("BIO353_EXAM2.txt", "r")
                    print(exam2.read())
                        
                elif(exams == "study guide" or exams == "3"):
                    study = open("BIO353_STUDY.txt","r")
                    print(study.read())
                else:
                    print("Wrong input recognized, please try again")
                    checkcourse(choice)

            elif(material == "general equations" or material == "2"):
                geneq = open("BIO353_GEN.txt","r")
                print(geneq.read())
        else:
            print("Sorry, this course is not recognized. Please try again!")
            checkcourse(choice)
            #Data Analytics Courses
        return course_number
    elif (choice == "7" or choice == "DATA" or choice == "Data Analytics"):
        check = input("What is the DATA course number?\n")
        course_number = "DA" + str(check) 
        if (course_number ==  "DA115"):
            material_choice = input("Would you like 1). Study Materials or 2). General Equations?\n")
            if (material_choice == "General Equations" or material_choice == "2" or material_choice == "general equations"):

                outFile = open("DA115_Gen.txt", "r")

                print(outFile.read())

                outFile.close()

            elif (material_choice == "Study Materials" or material_choice == "1" or material_choice == "study materials"):

                material_choice = input("Would you like to Exam 1 or Exam 2? ")

                if (material_choice == "1"):

                    outFile = open("DA115_Exam1.txt", "r")

                    print(outFile.read())

                elif (material_choice == "2"):

                    outFile = open("DA115_Exam2.txt", "r")

                    print(outFile.read())

                else:

                    print("Incorrect input!  Please try again!")
                    checkcourse(choice)

            else:

                print("Incorrect input!  Please try again!")
                checkcourse(choice)

        elif(course_number == "DA215"):
            material_choice = input("Would you like 1). Study Materials or 2). General Equations?\n")

            if (material_choice == "General Equations" or material_choice == "2" or material_choice == "general equations"):

                outFile = open("DA215_Gen.txt", "r")

                print(outFile.read())

                outFile.close()

            elif (material_choice == "Study Materials" or material_choice == "1" or material_choice == "study materials"):

                material_choice = input("Would you like to Exam 1 or Exam 2? ")

                if (material_choice == "1"):

                    outFile = open("DA215_Exam1.txt", "r")

                    print(outFile.read())

                elif (material_choice == "2"):

                    outFile = open("DA215_Exam2.txt", "r")

                    print(outFile.read())

                else:

                    print("Incorrect input!  Please try again!")
                    checkcourse(choice)

            else:

                print("Incorrect input!  Please try again!")
                checkcourse(choice)
        else:
            print("Sorry this course is not recognized, please try again!")
            checkcourse(choice)
        #Chemistry Courses
        return course_number
    elif(choice == "8" or choice == "CHEM" or choice == "Chemistry"):
        check = input("What is the CHEM course number?\n")
        course_number = "CHEM" + str(check)
        if (course_number == "CHEM331"): #initially checks the course number
            print("This is Physical Chemistry\n")
            material =  input("Would you like 1). Study Materials or 2). General Equations?\n")
            if (material == "study materials" or material == "1"):
                exams = input("Would you like Exam 1, or Exam 2?\n")
                if (exams == "exam 1" or exams == "exam1" or exams == "1"):
                    exam1 = open("CHEM201_Exam1.txt", "r")
                    print(exam1.read())
                        
                elif(exams == "exam 2" or exams == "exam2" or exams == "2"):
                    exam2 = open("CHEM201_EXAM2.txt", "r")
                    print(exam2.read())
                        
                else:
                    print("Wrong input recognized, please try again")
                    checkcourse(choice)

            elif(material == "general equations" or material == "2"):
                geneq = open("CHEM201_GEN.txt","r")
                print(geneq.read())
                    
            else:
                print("Sorry, input entered is not recognized ")
                checkcourse(choice)
            
        elif(course_number == "CHEM345"): 
            print("This is Organic Chemistry\n")
            material =  input("Would you like 1). Study Materials or 2). General Equations?\n") 
            if (material == "study materials" or material == "1"): #Checks against the above inputs 
                exams = input("Would you like Exam 1, or Exam 2?\n")
                if (exams == "exam 1" or exams == "exam1" or exams == "1"):
                    exam1 = open("CHEM345_ EXAM1.txt", "r")
                    print(exam1.read())
                        
                elif(exams == "exam 2" or exams == "exam2" or exams == "2"):
                    exam2 = open("CHEM345_EXAM2.txt", "r")
                    print(exam2.read())
                        
                else:
                    print("Wrong input recognized, please try again")
                    checkcourse(choice)

            elif(material == "general equations" or material == "2"):
                geneq = open("CHEM345_GEN.txt","r")
                print(geneq.read())
            else:
                print("Wrong input recognized, please try egain")
                checkcourse(choice)
        else:
            print("Sorry, this course is not recognized, please try again!")
            checkcourse(choice)
    else:
        print("Sorry, this major is not recognized, please try again!")
        main()
    return course_number

main()
    


#def material_check(course_number):








