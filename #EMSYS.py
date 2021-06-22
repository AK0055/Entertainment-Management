#ENTERTAINMENT MANAGEMENT SYSTEM
import mysql.connector
import tabulate
import re
import os
import datetime
from os import sys
from mysql.connector import(connection)
from tabulate import tabulate
#Connection
mydb=connection.MySQLConnection(host='localhost',user='root',passwd='Ajay@2001',database='a1')
mycursor=mydb.cursor()
def start():
     #login details and input
     userd=[('U001', '1@Abc'),('U002', '2@ABc'),('U003', '3@ABC'),('U004', '4@abC'),('U005', '5@aBc')]
     amtbal=[900,276,500,778,300]
     accnod=(10002,20003,30004,40005,50006)

     print("                                                      WELCOME TO akFLIX")
     print("                          Watch the latest hollywood movies and top-rated animation series online!")
     print("----------------------------------------------------------------------------------------------------------------")
     uname=input("                                                Enter username: ")
     iname=(uname,)
     upwd= input("                                                Enter password: ")
     print("----------------------------------------------------------------------------------------------------------------")

     ud=(uname,upwd)
     if ud in userd:
               for i in range(0,5):
                    if userd[i]==ud:
                         curr=i
               
               q1=("select name from client where userID=%s")
               mycursor.execute(q1,iname)
               rec=mycursor.fetchall()
               print("Welcome, ")
               print(tabulate(rec, tablefmt='psql'))
               print("Mind blowing stories, all in one place")
               q2=("select * from movie")
               mycursor.execute(q2)
               rq2=mycursor.fetchall()
               q3=("select * from anim")
               mycursor.execute(q3)
               rq3=mycursor.fetchall()
               print("            MOVIES")
               print(tabulate(rq2, tablefmt='psql'))
               print("            ANIMATION SERIES")
               print(tabulate(rq3, tablefmt='psql'))

               
               list_trans=[]
               list_watch=[]
               for i in range(0,5):
                    if i==curr:
                         chectran=("select pay_status from transact where userID=%s")
                         mycursor.execute(chectran,iname)
                         rechk=mycursor.fetchall()
                         rechk = str(rechk).replace("[('", "")
                         rechk = str(rechk).replace("',)]", "")
                         def Menu(iname,Wat):
                                        resp2=1
                                        while resp2==1:
                                             print("Choose one of the options to continue:")
                                             print("1...Watch TV shows and Movies")
                                             print("2...Add movies/anim to Watchlist:")
                                             print("3...Delete movies/anim from Watchlist:")
                                             print("4...Cancel your subscription")
                                             preff=int(input("Enter 1,2,3 or 4:"))
                                             if preff==2:

                                                       resp1=1
                                                       IDM=[]
                                                       IDA=[]
                                                       pos=0
                                                       while(resp1==1):
                                                       #Watchlisting
                                                            
                                                            
                                                            if((rect=='MOVIES')or(rect=='COMBO')):
                                                                 
                                                                 
                                                                 idi=str(input("Enter the title ID to add them to your watchlist!"))
                                                                 Wat.append(idi)


                                                                 IDM.append(idi)
                                                                 #print(IDM[-1])
                                                                 if(re.match("^M...$",IDM[-1])):
                                                                 
                                                                      q4M=("select M_NAME from movie where MID=%s")
                                                                      mycursor.execute(q4M,(IDM[-1],))
                                                                      rec=mycursor.fetchall()

                                                                      rec = str(rec).replace("[('", "")
                                                                      rec = str(rec).replace("',)]", "")
                                                                      print(rec)
                                                                      categ="MOVIES"
                                                                      tup_watch=(uname,IDM[-1],rec,categ)
                                                                      list_watch.append(tup_watch)
                                                                      qins1=("insert into watchlist values (%s,%s,%s,%s)")
                                                                      mycursor.execute(qins1,list_watch[-1])
                                                                      q4W=("select * from watchlist where userID=%s")
                                                                      mycursor.execute(q4W,iname)
                                                                      rq4M=mycursor.fetchall()
                                                                      print(tabulate(rq4M, tablefmt='psql'))
                                                                      saveM=input("Enter 's' to save your watchlist,else press any other key")
                                                                      if saveM=='s':
                                                                           q5M=("commit")
                                                                           mycursor.execute(q5M)
                                                                      resp1=int(input("Enter 1 to add more, 0 to exit"))
                                                                      if resp1==1:
                                                                           pos=pos+1
                                                            elif((rect=='ANIME')or(rect=='COMBO')):
                                                                 idi=str(input("Enter the title ID to add them to your watchlist!"))
                                                                 Wat.append(idi)

                                                                 IDA.append(idi)
                                                                 if(re.match("^A...$",IDA[-1])):
                                                                 
                                                                      q4A=("select A_NAME from ANIM where AID=%s")
                                                                      mycursor.execute(q4A,(IDA[-1],))
                                                                      rec=mycursor.fetchall()
                                                                      rec = str(rec).replace("[('", "")
                                                                      rec = str(rec).replace("',)]", "")
                                                                      print(rec)
                                                                      categ="ANIME"
                                                                      tup_watch=(uname,IDA[-1],rec,categ)
                                                                      list_watch.append(tup_watch)
                                                                      qins1=("insert into watchlist values (%s,%s,%s,%s)")
                                                                      mycursor.execute(qins1,list_watch[-1])
                                                                      q4A=("select * from watchlist where userID=%s")
                                                                      mycursor.execute(q4A,iname)
                                                                      rq4A=mycursor.fetchall()
                                                                      print(tabulate(rq4A, tablefmt='psql'))
                                                                      saveA=input("Enter 's' to save your watchlist,else press any other key")
                                                                      if saveA=='s':
                                                                           q5A=("commit")
                                                                           mycursor.execute(q5A)
                                                                      resp1=int(input("Enter 1 to add more, 0 to exit"))
                                                                      if resp1==1:
                                                                           pos=pos+1
                                                       
                                                                 
                                                            else:
                                                                 resp1=int(input("invalid entry,1 to try again, 0 to exit"))
                                                                 
                                                            
                                                       else:
                                                            
                                                            resp2=int(input("press 1 to return, 0 to exit"))
                                             
                                                  
                                        
                                             elif preff==3:
                                                       respd=1
                                                       while respd==1:
                                                            IDd=str(input("Enter the movie/animation ID to delete  them from your watchlist!"))
                                                            q4W=("select * from watchlist where userID=%s")
                                                            mycursor.execute(q4W,iname)
                                                            rq4M=mycursor.fetchall()
                                                            print(tabulate(rq4M, tablefmt='psql'))
                                                            if(re.match("^M...$",IDd)): 
                                                                 
                                                                      
                                                                 
                                                                 q4M=("delete from watchlist where WID=%s")
                                                                 mycursor.execute(q4M,(IDd,))
                                                                 
                                                                 saveM=input("Enter 's' to save your watchlist,else press any other key")
                                                                 if saveM=='s':
                                                                      q5M=("commit")
                                                                      mycursor.execute(q5M)
                                                                 q4W=("select * from watchlist where userID=%s")
                                                                 mycursor.execute(q4W,iname)
                                                                 rq4M=mycursor.fetchall()
                                                                 print(tabulate(rq4M, tablefmt='psql'))
                                                                 
                                                                 respd=int(input("Enter 1 to delete more, 0 to exit"))
                                                            elif(re.match("^A...$",IDd)):
                                                                 

                                                                 q4A=("delete from watchlist where WID=%s")
                                                                 mycursor.execute(q4A,(IDd,))

                                                                 
                                                                 saveA=input("Enter 's' to save your watchlist,else press any other key")
                                                                 if saveA=='s':
                                                                      q5A=("commit")
                                                                      mycursor.execute(q5A)
                                                                 q4A=("select * from watchlist where userID=%s")
                                                                 mycursor.execute(q4A,iname)
                                                                                  
                                                                 rq4A=mycursor.fetchall()
                                                                 print(tabulate(rq4A, tablefmt='psql'))
                                                                 respd=int(input("Enter 1 to delete more, 0 to exit"))
                                                            else:
                                                                 respd=int(input("invalid entry!,1 to try again,0 to exit"))
                                                                 
                                                       resp2=int(input("press 1 to return, 0 to exit"))
                                             elif preff==1:
                                                  if len(Wat)!=0:
                                                            flag=1
                                                            while(flag==1):
                                                                 IDtr=input("Enter the ID followed by 'x'of the title for which you like to view the trailer")
                                                                 IDx = str(IDtr).replace("x", "")
                                                                 if(IDx in Wat):
                                                                      flag=1
                                                                      FILE =  str(IDtr).replace("x", ".py")
                                                                      #print(FILE)
                                                                      os.startfile(FILE)
                                                                      flag=int(input("Press 1 to choose again, 0 to exit"))
                                                                 
                                                                 else:
                                                                      flag=int(input("Invalid entry,1 to retry, 0 to exit"))
                                                       
                                                            resp2=int(input("press 1 to return, 0 to exit"))
                                                  else:
                                                       print("The Watchlist is empty")
                                                       break;
                                                       resp2=int(input("press 1 to return, 0 to exit"))

                                             elif preff==4:    
                                                       tra=int(input("Enter 1 to keep your subscription, 0 to cancel"))
                                                       if tra==0:
                                                            q4d=("delete from transact where userID=%s")
                                                            mycursor.execute(q4d,iname)
                                                            q4dw=("delete from watchlist where userID=%s")
                                                            mycursor.execute(q4dw,iname)
                                                            save=int(input("Enter 1 to confirm"))
                                                            if save==1:
                                                                 q5t=("commit")
                                                                 mycursor.execute(q5t)
                                                                 print("Your Subscription is cancelled")
                                                                 inp=int(input("press 0 to log-out"))
                                                                 os.system("cls")
                                                                 start();
                                                                 
                                                       else:
                                                            print("Your subscription is not cancelled")
                                                       resp2=int(input("press 1 to return, 0 to exit"))

                         if rechk=="paid":
                                   qtr=("select pref from transact where userID=%s")
                                   mycursor.execute(qtr,iname)
                                   rect=mycursor.fetchall()
                                   rect = str(rect).replace("[('", "")
                                   rect = str(rect).replace("',)]", "")
                                   print(rect)

                                   #WATCH
                                   print("WATCHLIST")
                                   q4A=("select * from watchlist where userID=%s")
                                   mycursor.execute(q4A,iname)
                                   rq4A=mycursor.fetchall()
                                   print(tabulate(rq4A, tablefmt='psql'))
                                   q4W=("select WID from watchlist where userID=%s")
                                   mycursor.execute(q4W,iname)
                                   rq4W=mycursor.fetchall()
                                   Wat=[]
                                                       
                                   for x in rq4W:
                                        x = str(x).replace("('", "")
                                        x = str(x).replace("',)", "")
                                        #print(x)
                                        Wat.append(x)
                                   #print(Wat)
                                   Menu(iname,Wat);
               
                         else:
                              #display offers
                              print("Account number: ",accnod[i])
                              print("avl. balance: ",amtbal[i])
                              print("Here are some exciting offers!")
                              print("Choose your monthly package to continue")
                              print("1...MOVIES-----INR299 per month,    Quality:FHD")
                              print("2...ANIMATION--INR239 per month,    Quality:FHD")
                              print("3...COMBO------INR499 per month,    Quality:FHD")
                              pref=int(input("Now, select your mode of payment (Enter 1,2 or 3):"))
                              categ=('MOVIES','ANIME','COMBO')
                              price=(299,239,499)
                              inpacc=int(input("Enter your account number to proceed payment:"))
                              if (inpacc==accnod[i]) :
                                        if (amtbal[i]-price[pref-1])>0:
                                             #TRANSACTION
                                             amtbal[i]=amtbal[i]-price[pref-1]
                                             paystat="paid"
                                             print("available balance",amtbal[i])
                                             
                                             tup_trans=(uname,accnod[i],price[pref-1],paystat,amtbal[i],categ[pref-1])
                                             list_trans.append(tup_trans)
                                             #(userID,AC_num,pay_amt,pay_status,pay_bal)
                                             qins=("insert into transact values (%s,%s,%s,%s,%s,%s)")
                                             mycursor.execute(qins,tup_trans)
                                             save=input("Enter 's' to save your transaction,else press any other key")
                                             if save=='s':
                                                  qcom=("commit")
                                                  mycursor.execute(qcom)

                                             '''q4=("select * from transact")
                                             mycursor.execute(q4)
                                             rq4=mycursor.fetchall()
                                             print(tabulate(rq4, tablefmt='psql'))'''
                                             print("your transaction is complete")
                                             qtr=("select pref from transact where userID=%s")
                                             mycursor.execute(qtr,iname)
                                             rect=mycursor.fetchall()
                                             rect = str(rect).replace("[('", "")
                                             rect = str(rect).replace("',)]", "")
                                             print(rect)
                                             #WATCH
                                             print("WATCHLIST")
                                             q4A=("select * from watchlist where userID=%s")
                                             mycursor.execute(q4A,iname)
                                             rq4A=mycursor.fetchall()
                                             print(tabulate(rq4A, tablefmt='psql'))
                                             q4W=("select WID from watchlist where userID=%s")
                                             mycursor.execute(q4W,iname)
                                             rq4W=mycursor.fetchall()
                                             Wat=[]
                                                                 
                                             for x in rq4W:
                                                  x = str(x).replace("('", "")
                                                  x = str(x).replace("',)", "")
                                                  #print(x)
                                                  Wat.append(x)
                                             #print(Wat)
                                             Menu(iname,Wat);

     else:
          print("please visit us again!~TEAM akFLIX")
log=1
while(log==1):
     start();
     log=int(input("Press 1 to re-login, 0 to exit"))
     os.system("cls")

else:
     print("Please visit us again :)")

