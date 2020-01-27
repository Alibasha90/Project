from tkinter import *
from tkinter import messagebox
import sqlite3
import 	csv
import xlwt
from xlwt import Workbook


#==================================================================================================
					# FUNCTIONS
#===================================================================================================
         

def GO():
	new_list=['EMPLOYEE_NAME','PRIMARY_DOMAIN','SECONDARY_DOMAIN','MOBILE','EMAIL_ID','CURRENT_CTC','EXPECTED_CTC','NOTICE','DATE_OF_DISCUSSION','CURRENT_LOCATION','PREFERRED_LOCATION' ]
	my_mobile=l_srch.get()
	conn = sqlite3.connect('/home/mirafra/ali/new.db')
	cur=conn.cursor()
         Sql="SELECT * FROM NEW_TEXT WHERE PRIMARY_DOMAIN=my_mobile"

         cur.execute(sql)

#	cur.execute("SELECT * FROM NEW_TEXT WHERE mobile=='%s';" % my_mobile)
#	cur.execute("SELECT * FROM NEW_TEXT")
	data=cur.fetchall()
	cur.close()
	conn.close()	
	

#	with open('file.ex.ods','a') as csv_file:
#		csv_writer=csv.writer(csv_file,delimiter='-')
#		csv_writer.writerow(data)
	new=list(data[0])

# keys = ['EMPLOYEE_NAME','PRIMARY_DOMAIN','SECONDARY_DOMAIN','MOBILE','EMAIL_ID','CURRENT_CTC','EXPECTED_CTC','NOTICE','DATE_OF_DISCUSSION','CURRENT_LOCATION','PREFERRED_LOCATION' ]

 #values = [1, 2, 3]
#d = dict(zip(keys, values))
# print(dictionary)


	
#	wb = Workbook()
#	print(new)
#	j=0		 
#	for i in new:
#		print(new_list[j]+'--->'+str(i))
#		j+=1
	
#		with open('file.ex.ods','a') as csv_file:
#			csv_writer=csv.writer(csv_file,delimiter='-')
#			csv_writer.writerow(str(i))

# Workbook is created 
	wb = Workbook()

# add_sheet is used to create sheet. 
	sheet1 = wb.add_sheet('Sheet 1')

	sheet1.write(0,0,'EMPLOYEE_NAME')
	sheet1.write(0,1,'PRIMARY_DOMAIN')
	sheet1.write(0,2,'SECONDARY_DOMAIN')
	sheet1.write(0,3,'MOBILE')
	sheet1.write(0,4,'EMAIL_ID')
	sheet1.write(0,5,'CURRENT_CTC')
	sheet1.write(0,6,'ExPECTED_CTC')
	sheet1.write(0,7,'NOTICE')
	sheet1.write(0,8,'DATE_OF_DISCUSSION')
	sheet1.write(0,9,'CURRENT_LOCATION')
	sheet1.write(0,10,'PREFERRED_LOCATION')
		
	
	j=0		 
	for i in new:
		sheet1.write(1,j,i)
		j+=1
	wb.save('ali_data.xls')




def save():
	emp_name=l1_text.get()
	p_domain=l2_text.get()	
	s_domain=l3_text.get()	
	mobile=l4_text.get()	
	email_id=l5_text.get()	
	cctc=l6_text.get()	
	ectc=l7_text.get()	
	notice=l8_text.get()	
	d_of_d=l9_text.get()	
	cur_loc=l10_text.get()	
	pref_loc=l11_text.get()	


	if emp_name=='':
		l1_text.set(emp_name)
		messagebox.showwarning("Warning","Name  should be Mandatory!")
		return
	if mobile=='':
		l4_text.set(mobile)
		messagebox.showwarning("Warning","Mobile number should be Mandatory!")
		return
	

	if email_id=='':
		l5_text.set(email_id)
		messagebox.showwarning("Warning","Email should be Mandatory!")
		return

	l1_text.set('')
	l2_text.set('')
	l3_text.set('')
	l4_text.set('')
	l5_text.set('')
	l6_text.set('')
	l7_text.set('')
	l8_text.set('')
	l9_text.set('')
	l10_text.set('')
	l11_text.set('')
#================================================ SQLITE DATABASE STORING ==========================
		
#	conn = sqlite3.connect('/home/mirafra/ali/tk/mini_pcj/new.db')
	conn=sqlite3.connect('/home/mirafra/ali/new.db')
#	for t in [(emp_name,p_domain,s_domain,mobile,email_id,cctc,ectc,notice,d_of_d,cur_loc,pref_loc)]:



#	conn.execute(''' INSERT INTO NEW_TEXT (emp_name,p_domain ,s_domain,mobile ,email_id,cctc ,ectc ,notice ,d_of_d , cur_loc ,pref_loc )VALUES(?,?,?,?,?,?,?,?,?,?,?)''',(emp_name,p_domain ,s_domain,mobile ,email_id,cctc ,ectc ,notice ,d_of_d , cur_loc ,pref_loc )  )	

	conn.execute(''' INSERT INTO NEW_TEXT (EMPLOYEE_NAME,PRIMARY_DOMAIN,SECONDARY_DOMAIN,MOBILE,EMAIL_ID, CURRENT_CTC,EXPECTED_CTC,NOTICE,DATE_OF_DISCUSSION,CURRENT_LOCATION,PREFERRED_LOCATION)
VALUES(?,?,?,?,?,?,?,?,?,?,?)''',( emp_name,p_domain ,s_domain,mobile ,email_id,cctc ,ectc ,notice ,d_of_d , cur_loc ,pref_loc  )  )



#	conn.execute('INSERT NEW_TEXT values(?,?,?,?,?,?,?,?,?,?,?)',t)
	conn.commit()	
	conn.close()
#====================================================================================================






#==============================================  MAIN CREATION ======================================
window = Tk()#--------window creation

window.title("Employees Database application")

window.geometry('900x850')

#----------------------------------------------------- Labels creation -------------------

l1_text=StringVar()
l1 = Label(window, text="Employee Name:",font=('bold',12),pady=20)
l1.grid(row=0,column=0,sticky=W)
l1_entry=Entry(window,width=50,textvariable=l1_text)
l1_entry.grid(row=0,column=1) 

 
l2_text=StringVar()
l2 = Label(window, text="Primary Domain:",font=('bold',12),pady=20)
l2.grid(row=1,column=0,sticky=W)
l2_entry=Entry(window,width=50,textvariable=l2_text)
l2_entry.grid(row=1,column=1) 


l3_text=StringVar()
l3 = Label(window, text="Secondary Domain:",font=('bold',12),pady=20)
l3.grid(row=2,column=0,sticky=W)
l3_entry=Entry(window,width=50,textvariable=l3_text)
l3_entry.grid(row=2,column=1) 

l4_text=StringVar()
l4 = Label(window, text="Mobile Number:",font=('bold',12),pady=20)
l4.grid(row=3,column=0,sticky=W)
l4_entry=Entry(window,width=50,textvariable=l4_text)
l4_entry.grid(row=3,column=1) 


l5_text=StringVar()
l5 = Label(window, text="Email ID:",font=('bold',12),pady=20)
l5.grid(row=4,column=0,sticky=W)
l5_entry=Entry(window,width=50,textvariable=l5_text)
l5_entry.grid(row=4,column=1) 

l6_text=StringVar()
l6 = Label(window, text="Current CTC:",font=('bold',12),pady=20)
l6.grid(row=5,column=0,sticky=W)
l6_entry=Entry(window,width=50,textvariable=l6_text)
l6_entry.grid(row=5,column=1) 


l7_text=StringVar()
l7 = Label(window, text="Expected CTC:",font=('bold',12),pady=20)
l7.grid(row=6,column=0,sticky=W)
l7_entry=Entry(window,width=50,textvariable=l7_text)
l7_entry.grid(row=6,column=1) 


l8_text=StringVar()
l8 = Label(window, text="Notice Period:",font=('bold',12),pady=20)
l8.grid(row=7,column=0,sticky=W)
l8_entry=Entry(window,width=50,textvariable=l8_text)
l8_entry.grid(row=7,column=1) 


l9_text=StringVar()
l9 = Label(window, text="Date Of Discussion:",font=('bold',12),pady=20)
l9.grid(row=8,column=0,sticky=W)
l9_entry=Entry(window,width=50,textvariable=l9_text)
l9_entry.grid(row=8,column=1) 


l10_text=StringVar()
l10 = Label(window, text="Present Location:",font=('bold',12),pady=20)
l10.grid(row=9,column=0,sticky=W)
l10_entry=Entry(window,width=50,textvariable=l10_text)
l10_entry.grid(row=9,column=1) 



l11_text=StringVar()
l11 = Label(window, text="Preffered Location:",font=('bold',12),pady=20)
l11.grid(row=10,column=0,sticky=W)
l11_entry=Entry(window,width=50,textvariable=l11_text)
l11_entry.grid(row=10,column=1) 





#sagebox==================================================== buttons ====================================
btn=Button(window,text='SAVE',width=15,command=save,bg='green',fg='white')
btn.grid(row=11,column=0,pady=20)

btn=Button(window,text='CLOSE',width=15,command=window.destroy,bg='red',fg='white')
btn.grid(row=11,column=1,pady=20)

#=====================================================search ======================================
l_srch=StringVar()
srch=Label(window,text='SEARCH:-')
srch.grid(row=11,column=2,sticky=W)

srch_entry=Entry(window,width=25,textvariable=l_srch)
srch_entry.grid(row=11,column=3)
btn=Button(window,text='GO',command=GO,width=3,bg='blue',fg='white')
btn.grid(row=11,column=5,columnspan=5)
#=====================================================================================================
window.mainloop()       # main loop calling here
#=====================================================================================================
