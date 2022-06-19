while(True):
    print("Press q to exit")
    name = input("Enter the name\n")
    if name == 'q':
        break
    fathern = input(f"Enter father's name of {name}\n")
    clas = int(input("Enter the class\n"))
    school = input("Enter the name of the school: ")
    year = input('Enter the current year of this session: ')
# *Report Card for class 11th and 12th
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    for i in range(11, 13):
        if (clas == i):
            stream = input("Enter the stream of student: ")

            _a = input(f"Enter {name}'s first subject\n")
            _b = input(f"Enter {name}'s second subject\n")
            _c = input(f"Enter {name}'s third subject\n")
            _d = input(f"Enter {name}'s fourth subject\n")
            _e = input(f"Enter {name}'s fifth subject\n")

            _sub1 = int(input(f"Enter student's marks in {_a}\n"))
            _sub2 = int(input(f"Enter student's marks in {_b}\n"))
            _sub3 = int(input(f"Enter student's marks in {_c}\n"))
            _sub4 = int(input(f"Enter student's marks in {_d}\n"))
            _sub5 = int(input(f"Enter student's marks in {_e}\n"))

            mm = int(input("Enter the maximum marks of all subjects: "))
            m_m = (mm+mm+mm+mm+mm)

            def repo():
                '''This function return percentage of student'''
                return b

            def total():
                '''This function return total marks of students'''
                return a
            a = (_sub1+_sub2+_sub3+_sub4+_sub5)
            b = (a/m_m*100)

            n = total()
            y = repo()

            def report():
                '''This function return compartment of student'''
                if _sub1*3 < mm:
                    return(f"You got compartment in {_a}")

                elif _sub2*3 < mm:
                    return(f"You got compartment in {_b}")

                elif _sub3*3 < mm:
                    return(f"You got compartment in {_c}")

                elif _sub4*3 < mm:
                    return(f"You got compartment in {_d}")

                elif _sub5*3 < mm:
                    return(f"You got compartment in {_e}")

                if b <= 33:
                    return("You are failed")
                else:
                    return("Congratulations! You are passed")
            d = report()

            def percent():
                '''This function return grades'''
                if b >= 90:
                    return('''You got  grade 'A'
OUTSTANDING ''')
                elif b >= 80:
                    return('''You got  grade 'B'
EXCELLENT ''')
                elif b >= 70:
                    return('''You got  grade 'C' 
GOOD''')
                elif b >= 60:
                    return('''You got  grade 'D'
AVERAGE ''')
                elif b >= 50:
                    return('''You got  grade 'E'
NEED TO WORK HARD ''')
                else:
                    return("You got 'F' ")
            e = percent()

            with open(f"{name}.txt", "w") as f:
                f.write(f'''Name of the student-{name}
Class of the student-{clas}
Stream of the student-{stream}
Father's name of {name}-{fathern}

                                {school} \t
---------------  Academic result of class {clas}th ({year})\t  ----------
***********************************************************************************
** \nSubject                                                       Marks         **
1. {_a                                }                            {_sub1}       **
2. {_b                                }                            {_sub2}       **
3. {_c                                }                            {_sub3}       **
4. {_d                                }                            {_sub4}       **
5. {_e                                }                            {_sub5}       **
**                                                                               **
***********************************************************************************
Maximum marks - {m_m}
Total marks obtained - {n}
You got {y} percent
{d}
{e}''')
            print("******Report card is prepared**********")

# * Report Card for class 1st to 10th
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    for n in range(6, 11):
        if (clas == n):
            sub1 = int(input("Enter student's marks in Hindi\n"))
            sub2 = int(input("Enter student's marks in English\n"))
            sub3 = int(input("Enter student's marks in Social Science\n"))
            sub4 = int(input("Enter student's marks in Science\n"))
            sub5 = int(input("Enter student's marks in I.T.\n"))
            sub6 = int(input("Enter student's marks in Sanskrit\n"))
            sub7 = int(input("Enter student's marks in Maths\n"))

            _mm = int(input("Enter the maximum marks of all subjects: "))
            m_m_ = (_mm+_mm+_mm+_mm+_mm+_mm+_mm)

            def repo():
                '''This function returns percentage of student,'''
                return b

            def total():
                '''This function returns sum of marks of all subjects'''
                return a
            a = (sub1+sub2+sub3+sub4+sub5+sub6+sub7)
            b = (a/m_m_*100)

            n = total()
            y = repo()

            def report():
                '''This fuction shows compartment of students.'''
                if sub1*3 < _mm:
                    return(f"You got compartment in Hindi")
                elif sub2*3 < _mm:
                    return(f"You got compartment in English")
                elif sub3*3 < _mm:
                    return(f"You got compartment in Social Science")
                elif sub4*3 < _mm:
                    return(f"You got compartment in Science")
                elif sub5*3 < _mm:
                    return(f"You got compartment in I.T.")
                elif sub6*3 < _mm:
                    return(f"You got compartment in Drawing")
                elif sub7*3 < _mm:
                    return(f"You got compartment in Maths")

                if b <= 33:
                    return("You are failed")
                else:
                    return(f"Congratulations! You are passed")
            d = report()

            def percent():
                '''This function return grades'''
                if b >= 90:
                    return('''You got  grade 'A'
OUTSTANDING ''')
                elif b >= 80:
                    return('''You got  grade 'B'
EXCELLENT ''')
                elif b >= 70:
                    return('''You got  grade 'C' 
GOOD''')
                elif b >= 60:
                    return('''You got  grade 'D'
AVERAGE ''')
                elif b >= 50:
                    return('''You got  grade 'E'
NEED TO WORK HARD ''')
                else:
                    return("You got 'F' ")
            e = percent()

            porc = (f'''Name of the student-{name}
Class of the student - {clas}
Father's name of {name} - {fathern}

                            {school}\t 
---------------  Academic result of class {clas}th ({year})\t  ----------
*********************************************************************
**        Subject             Marks                                 
1.        Hindi              {sub1}                                   
2.        English            {sub2}                                   
3.        Social Science     {sub3}                                   
4.        Science            {sub4}                                   
5.        I.T.               {sub5}                                   
6.        Drawing            {sub6}                                   
7.        Maths              {sub7}                                   
*********************************************************************

Maximum marks - {m_m_}
Total marks obtained - {n}
You got {y} Percent
{d}
{e}''')
            with open(f"{name}.txt", "w") as f:
                f.write(porc)
                print("******Report card is prepared**********")
# *Report card for class 1st to 6th
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    for j in range(1, 6):
        if (clas == j):
            sub1 = int(input("Enter student's marks in Hindi\n"))
            sub2 = int(input("Enter student's marks in English\n"))
            sub3 = int(
                input("Enter student's marks in Environmental Studies\n"))
            sub4 = int(input("Enter student's marks in General Knowledge\n"))
            sub5 = int(input("Enter student's marks in Computer\n"))
            sub6 = int(input("Enter student's marks in Maths\n"))
            sub7 = input("Enter grade in Drawing: ")

            _mm = int(input("Enter the maximum marks of all subjects: "))
            m_m_ = (_mm+_mm+_mm+_mm+_mm+_mm)

            def repo():
                '''This function returns percentage of student,'''
                return b

            def total():
                '''This function returns sum of marks of all subjects'''
                return a
            a = (sub1+sub2+sub3+sub4+sub5+sub6)
            b = (a/m_m_*100)

            n = total()
            y = repo()

            def report():
                '''This fuction shows compartment of students.'''
                if sub1*3 < _mm:
                    return(f"You got compartment in Hindi")
                elif sub2*3 < _mm:
                    return(f"You got compartment in English")
                elif sub3*3 < _mm:
                    return(f"You got compartment in Environmental Studies")
                elif sub4*3 < _mm:
                    return(f"You got compartment in General Knowledge")
                elif sub5*3 < _mm:
                    return(f"You got compartment in Computer")
                elif sub6*3 < _mm:
                    return(f"You got compartment in Maths")

                if b <= 33:
                    return("You are failed")
                else:
                    return(f"Congratulations! You are passed")
            d = report()

            def percent():
                '''This function return grades'''
                if b >= 90:
                    return('''You got  grade 'A'
OUTSTANDING ''')
                elif b >= 80:
                    return('''You got  grade 'B'
EXCELLENT ''')
                elif b >= 70:
                    return('''You got  grade 'C' 
GOOD''')
                elif b >= 60:
                    return('''You got  grade 'D'
AVERAGE ''')
                elif b >= 50:
                    return('''You got  grade 'E'
NEED TO WORK HARD ''')
                else:
                    return("You got 'F' ")
            e = percent()

            def normal():
                if clas == 1:
                    return "st"
                elif clas == 2:
                    return "nd"
                elif clas == 3:
                    return "rd"
                elif clas == 4 or 5:
                    return "th"
                else:
                    return ""
            oop = normal()

            porc = (f'''Name of the student-{name}
Class of the student - {clas}
Father's name of {name} - {fathern}

                            {school}\t 
---------------  Academic result of class {clas}{oop} ({year})\t  ----------
*********************************************************************
**        Subject                   Marks           Grade                       
1.        Hindi                     {sub1}                                   
2.        English                   {sub2}                                   
3.        Environmental Studies     {sub3}                                   
4.        General Knowledge         {sub4}                                   
5.        Computer                  {sub5}                                   
6.        Maths                     {sub6}
7.        Drawing                                   {sub7}                                                 
*********************************************************************

Maximum marks - {m_m_}
Total marks obtained - {n}
You got {y} Percent
{d}
{e}''')
            with open(f"{name}.txt", "w") as f:
                f.write(porc)
                print("******Report card is prepared**********")
