import pickle
import os
def add_record() :
    try :
        if os.path.isfile("record") :
            f=open("record","ab")
        else :
            f=open("record","wb")
        while True :
            print("ENTER 'Y' OR 'y' TO CONTINUE....AND 'N' OR 'n' TO BREAK...")
            while True :
                rol=input("enter roll number =    ")
                if rol.isdigit() and len(rol)==4 :
                    break
                else :
                    print("ENTER VALID ROLL NUMBER")
                    continue
            while True :
                name = input("enter name of student =    ")
                if name.isdigit() and name==" " :
                    print("ENTER VALID NAME ")
                    continue
                else :
                    name = name.upper()
                    break

            while True :
                pm=input("ENTER MATHS MARKS =    ")
                if pm.isdigit() and (int(pm)>=0 and int(pm)<=100) :
                    break
                else :
                    print("ENTER VALID MARKS OF MATHS")
                    continue
            while True :
                cm=input("ENTER ENGLISH MARKS =    ")
                if cm.isdigit() and (int(cm)>=0 and int(cm)<=100) :
                    break
                else :
                    print("ENTER VALID MARKS OF ENGLISH")
                    continue
            while True :
                mm=input("ENTER SCIENCE MARKS =    ")
                if mm.isdigit() and (int(mm)>=0 and int(mm)<=100) :
                    break
                else :
                    print("ENTER VALID MARKS OF SCIENCE")
                    continue
            smark=[pm,cm,mm]
            total=0
            for i in smark :
                total = total + int(i)
            percentage=(total)//3
            percentage=str(percentage) + "%"
            record=[rol,name,smark,percentage]
            pickle.dump(record,f)
            while True :
                ch=input("enter your choice (Y/N) to continue with add record =    ")
                if (ch=="y" or ch=="Y") or (ch=="n" or ch=="N") :
                    break
                else :
                    print("ENTER VALID CHOICE TO CONTINUE OR BREAK.......")
                    continue
            if ch=="y" or ch=="Y" :
                continue
            else :
                break
    except EOFError :
        f.close()
        print("RECORD ADDED")
def display_record() :
    try :
        f=open("record","rb")
        print(" " * 46, "*" * 25)
        print(" " * 50, "STUDENT RECORDS")
        print(" " * 46, "*" * 25)
        print("*" * 108)
        print("*", "%-5s" % "S no."," ", "*", "%-6s" % "ROLL No.", "*","%-10s"%"NAME", "*","%-8s"%"ENGLISH","*","%-7s"%"MATHS","*","%-10s"%"SCIENCE","*","%-12s"%"PERCENTAGE","*")
        print( "*" * 108)
        i=0
        while True :
            r=pickle.load(f)
            i=i+1
            print("*", "%-5s" % i," ", "*", "%-10s" % r[0], "*", "%-12s" % r[1], "*", "%-8s" % r[2][0], "*","%-7s" % r[2][1], "*", "%-12s" % r[2][2], "*", "%-12s" % r[3], "*")
            print("-" * 94)
    except EOFError :
        print(" " * 38, "#" * 25)
        f.close()
    except IOError :
        print("unable to open file")
def search_record() :
    try :
        f=open("record","rb")
        print("ENTER 'nd' OR 'ND' TO SEARCH BY NAME ....")
        print("ENTER 'rl' OR 'RL' TO SEARCH BY ROLL NUMBER ....")
        while True :
            cs=input("ENTER WAY YOU WANT TO SEARCH=    ")
            cs=cs.lower()
            if cs=="nd" or cs=="rl" :
                break
            else :
                print("ENTER CHOICE ADS GIVEN ABOVE....")
                continue
        if cs=="nd" :
            z=0
            while True :
                name=input("enter name you want to search=     ")
                name=name.upper()
                if name.isdigit() and name==" " :
                    print("ENTER VALID NAME.....")
                    continue
                else :
                    break
            print(" " * 40, "*" * 25)
            print(" " * 44, "STUDENT RECORD")
            print(" " * 40, "*" * 25)
            print("*" * 83)
            while True :
                r=pickle.load(f)
                p=""
                i=0
                for i in range(0,len(name)) :
                    p=p+r[1][i]
                if name==p :
                    z=1
                    print("*", "%-6s" % "ROLL NUMBER", "*", "%-10s" % "NAME", "*", "%-8s" % "ENGLISH", "*","%-7s" % "MATHS", "*", "%-10s" % "HINDI", "*", "%-12s" % "PERCENTAGE", "*")
                    print("*", "%-15s" % r[0], "*", "%-10s" %r[1], "*","%-11s" %r[2][0], "*", "%-10s" %r[2][1], "*", "%-12s" %r[2][2], "*", "%-15s" %r[3],"*")
                    print("*" *83)
        else :
            z=0
            while True :
                rol=input("ENTER ROLL  NUMBER YOU WANT TO DELETE =     ")
                if rol.isdigit() and len(rol)<=4 :
                    break
                else :
                    print("ENTER VALID ROLL NUMBER")
                    continue
            print(" " * 40, "*" * 25)
            print(" " * 44, "STUDENT RECORD")
            print(" " * 40, "*" * 25)
            print("*" * 83)
            while True :
                r=pickle.load(f)
                p=""
                for i in range(0,len(rol)) :
                    p=p+r[0][i]
                if rol==p :
                    z=1
                print("*", "%-6s" % "ROLL NUMBER", "*", "%-10s" % "NAME", "*", "%-8s" % "ENGLISH", "*", "%-7s" % "MATHS", "*", "%-10s" % "HINDI", "*", "%-12s" % "PERCENTAGE", "*")
                print("*", "%-15s" % r[0], "*", "%-10s" % r[1], "*", "%-11s" % r[2][0], "*", "%-10s" % r[2][1], "*","%-12s" % r[2][2], "*", "%-15s" % r[3], "*")
                print("*" * 83)
    except EOFError :
        f.close()
        if z==0 :
            print("RECORD NOT FOUND")
    except IOError :
        print("UNABLE TO OPEN FILE")
def delete_record() :
    try :
        f=open("record","rb")
        tf=open("tempfile4","wb")
        print("ENTER 'rd' OR 'RD' TO DELETE BY ROLL NUMBER....")
        print("ENTER 'nd' OR 'ND' TO DELETE BY NAME......")
        while True :
            cs=input("ENTER WAY OF DELETING =    ")
            cs=cs.lower()
            if cs=="nd" or cs=="rd" :
                break
            else :
                print("ENTER CHOICE AS GIVEN ABOVE")
                continue
        if cs=="nd" :
            z=0
            while True :
                name=input("ENTER NAME TO DELETE =   ")
                name=name.upper()
                if name.isdigit() or name==" " :
                    print("ENTER VALID NAME TO SEARCH.....")
                    continue
                else :
                    break
        else :
            z = 0
            while True:
                rol = input("ENTER ROLL NUMBER TO DELETE =   ")
                if rol.isdigit() and len(rol) == 4:
                    break
                else:
                    print("ENTER VALID ROLL NUMBER TO SEARCH.....")
                    continue
            while True :
                r=pickle.load(f)
                if r[0]==rol :
                    z=1
                    print("RECORD DELETEED")
                else :
                    pickle.dump(r,tf)
    except EOFError :
        f.close()
        tf.close()
        if z==0 :
            print("record not found")
        else :
            os.remove("record")
            os.rename("tempfile4","record")
    except IOError :
        print("UNABLE TO OPEN FILE")
def modify_record() :
    try :
        f=open("record","rb")
        tf=open("tempfile4","wb")
        rno=input("ENTER ROLL NUMBER FOR MODIFICATION =    ")
        z=0
        while True :
            r=pickle.load(f)
            if r[0]==rno :
                z=1
                print("ENTER 'rl' TO MODIFY ROLL NUMBER")
                print("ENTER 'n' TO MODIFY NAME")
                while True :
                    ch=input("ENTER YOUR CHOICE =    ")
                    if ch=="rl" or ch=="n":
                        break
                    else :
                        print("enter valid roll number")
                        continue
                while True :

                    rml=input("ENTER NEW ROLL NUMBER =    ")
                    if rml.isdigit() and len(rml)==4 :

                        break
                    else :
                        print("ENTER VALLID ROLL NUMBER FOR MODIFICATION")
                        continue
                r=[rml,r[1],r[2]]
                print(f"ROLL NUMBER =   '{r[0]}'  ,  NAME =   '{r[1]}'  , ENGLISH MARKS = '{r[2][0]}',MATHS MARKS =   '{r[2][1]}',HINDI MARKS = '{r[2][2]}',PERCENTAGE=   '{r[2]}'")
                pickle.dump(r,tf)

            elif ch=="n":
                z=1
                while True :
                        nm=input("ENTER NAME FOR MODIFICATION =   ")
                        if nm.isdigit() or nm==" " :
                            print("NAME SHOULD BE IN ALPHABETIC FORM")
                            continue
                        else :
                            break
                nm=nm.upper()
                r=[r[0],nm,r[2]]
                print(f"ROLL NUMBER =   '{r[0]}'  ,  NAME =   '{r[1]}'  , ENGLISH MARKS = '{r[2][0]}',MATHS MARKS =   '{r[2][1]}',HINDI MARKS = '{r[2][2]}',PERCENTAGE=   '{r[2]}' ")
                pickle.dump(r,tf)
            else :
                pickle.dump(r,tf)
    except EOFError :
        f.close()
        tf.close()
        if z==0 :
            print("record not found")
        else :
            os.remove("record")
            os.rename("tempfile4","record")
    except IOError :
        print("UNABLE TO OPEN FILE")
def main_menu() :
    print(" "*46, "*" * 25)
    print(" "*54, "MAIN MENU")
    print(" "*54, "1. ADD RECORD")
    print(" "*54,"2.DISPLAY RECORD")
    print(" "*54, "3.SEARCH RECORD")
    print(" "*54, "4.DELETE RECORD")
    print(" " * 54, "5.MODIFY RECORD")
    print(" "*54,"0.EXIT")
    while True :
        while True :
            ch=input("ENTER CHOICE =   ")
            if ch.isdigit():
                break
            else :
                print("ENTER VALID MENU CHOICE")
                continue
        if ch=="1" :
            add_record()
            input("PRESS ENTER TO CONTINUE......")
        elif ch=="2" :
            display_record()
            input("PRESS ENTER TO CONTINUE.....")
        elif ch=="3" :
            search_record()
            input("PRESS ENTER TO CONTINUE.....")
        elif ch=="4" :
            delete_record()
            input("PRESS ENTER TO CONTINUE.....")
        elif ch=="5" :
            modify_record()
            input("PRESS ENTER TO CONTINUE.....")
        elif ch=="0" :
            print("EXIT")
            break
        else :
            print("ENTER VALID MENU CHOICE......")
            continue
    print(" " * 46, "*" * 25)
if __name__=="__main__" :
    main_menu()


