import mysql.connector

mydb=mysql.connector.connect(
               host="localhost",
               user="root",
               passwd="locked",
               database="ficcihes"
               
	)

mycursor=mydb.cursor()

mycursor.execute("CREATE TABLE IF NOT EXISTS Delig_Accounts(id INT AUTO_INCREMENT PRIMARY KEY ,email VARCHAR(255),name VARCHAR(255))")
mycursor.execute("CREATE TABLE IF NOT EXISTS Exhibitor_Accounts(id  INT AUTO_INCREMENT PRIMARY KEY,email VARCHAR(255), password VARCHAR(255))")

# sql="CREATE TABLE IF NOT EXISTS Deligates_Reg(id INT AUTO_INCREMENT PRIMARY KEY ,email Text(),password"
# mycursor.execute(sql)

sql="CREATE TABLE IF NOT EXISTS Exhibitor_Reg(id INT AUTO_INCREMENT PRIMARY KEY ,comp_name Text Not NULL ,title TEXT NOT NULL,first_name TEXT NOT NULL,last_name TEXT NOT NULL,desig TEXT NOT NULL,cont_title TEXT  NOT NULL,cont_first_name TEXT NOT NULL,cont_last_name TEXT NOT NULL,cont_desig TEXT NOT NULL,add1 TEXT NOT NULL,add2 TEXT NOT NULL,city TEXT NOT NULL,pin TEXT NOT NULL,state TEXT NOT NULL,country TEXT NOT NULL,t_ccode TEXT NOT NULL,t_acode TEXT NOT NULL,p_no TEXT NOT NULL,f_ccode TEXT NOT NULL,f_acode TEXT NOT NULL, f_no TEXT NOT NULL,m_code TEXT NOT NULL,m_no TEXT NOT NULL,email TEXT NOT NULL,a_email TEXT NOT NULL,website TEXT NOT NULL,pan TEXT NOT NULL,tan TEXT NOT NULL,gst TEXT NOT NULL,schm TEXT NOT NULL,area TEXT NOT NULL)"
mycursor.execute(sql)

# sql="CREATE TABLE IF NOT EXISTS Deligate_Reg(id INT AUTO_INCREMENT PRIMARY KEY,name TEXT NOT NULL,desig TEXT NOT NULL,comp_name TEXT NOT NULL, m_addr TEXT NOT NULL,country TEXT NOT NULL,pin TEXT NOT NULL,state TEXT NOT NULL,city TEXT NOT NULL,gst TEXT NOT NULL,mobile_no TEXT NOT NULL,fax_no TEXT NOT NULL,email TEXT NOT NULL,i_delg TEXT NOT NULL,memb_no TEXT NOT NULL,overseas_delg TEXT NOT NULL,sponser TEXT NOT NULL,sponser_categ TEXT NOT NULL ,d1_name TEXT NOT NULL,d1_desig TEXT NOT NULL,d1_mobile TEXT NOT NULL,d1_email TEXT NOT NULL,d2_name TEXT NOT NULL,d2_desig TEXT NOT NULL,d2_mobile TEXT NOT NULL,d2_email TEXT NOT NULL,d3_name TEXT NOT NULL,d3_desig TEXT NOT NULL,d3_mobile TEXT NOT NULL,d3_email TEXT NOT NULL,d4_name TEXT NOT NULL,d4_desig TEXT NOT NULL,d4_mobile TEXT NOT NULL,d4_email TEXT NOT NULL,d5_name TEXT NOT NULL,d5_desig TEXT NOT NULL,d5_mobile TEXT NOT NULL,d5_email TEXT NOT NULL,d6_name TEXT NOT NULL,d6_desig TEXT NOT NULL,d6_mobile TEXT NOT NULL,d6_email TEXT NOT NULL,paym_mode TEXT NOT NULL,cheque_dd_no TEXT NOT NULL,bank TEXT NOT NULL,dated TEXT NOT NULL,amnt TEXT NOT NULL,amnt_gst TEXT NOT NULL)"

sql="CREATE TABLE IF NOT EXISTS Delig_Reg(id INT AUTO_INCREMENT PRIMARY KEY,name TEXT NOT NULL,desig TEXT NOT NULL,comp_name TEXT NOT NULL, m_addr TEXT NOT NULL,country TEXT NOT NULL,pin TEXT NOT NULL,state TEXT NOT NULL,city TEXT NOT NULL,gst TEXT NOT NULL,mobile_no TEXT NOT NULL,fax_no TEXT NOT NULL,email TEXT NOT NULL,delegate TEXT NOT NULL,ind_prtcpnt TEXT NOT NULL,memb_no TEXT NOT NULL, sponser_categ TEXT NOT NULL ,d1_name TEXT NOT NULL,d1_desig TEXT NOT NULL,d1_org TEXT NOT NULL,d1_mobile TEXT NOT NULL,d1_email TEXT NOT NULL,d2_name TEXT NOT NULL,d2_desig TEXT NOT NULL,d2_org TEXT NOT NULL,d2_mobile TEXT NOT NULL,d2_email TEXT NOT NULL,d3_name TEXT NOT NULL,d3_desig TEXT NOT NULL,d3_org TEXT NOT NULL,d3_mobile TEXT NOT NULL,d3_email TEXT NOT NULL,d4_name TEXT NOT NULL,d4_desig TEXT NOT NULL,d4_org TEXT NOT NULL,d4_mobile TEXT NOT NULL,d4_email TEXT NOT NULL,d5_name TEXT NOT NULL,d5_desig TEXT NOT NULL,d5_org TEXT NOT NULL,d5_mobile TEXT NOT NULL,d5_email TEXT NOT NULL,d6_name TEXT NOT NULL,d6_desig TEXT NOT NULL,d6_org TEXT NOT NULL,d6_mobile TEXT NOT NULL,d6_email TEXT NOT NULL,paym_mode TEXT NOT NULL,cheque_dd_no TEXT NOT NULL,bank TEXT NOT NULL,dated TEXT NOT NULL)"
# sql = "DROP TABLE Delig_Reg"
mycursor.execute(sql)

sql="CREATE TABLE IF NOT EXISTS Hot_Delig(id INT AUTO_INCREMENT PRIMARY KEY,recomnd TEXT NOT NULL,reg TEXT NOT NULL,attend TEXT NOT NULL,gender TEXT NOT NULL,title TEXT NOT NULL,last_name TEXT NOT NULL,first_name TEXT NOT NULL,recomnd_2019 TEXT NOT NULL,occupation TEXT NOT NULL,desig TEXT NOT NULL,org TEXT NOT NULL,add1 TEXT NOT NULL, add2 TEXT NOT NULL, city TEXT NOT NULL,pin TEXT NOT NULL,state TEXT NOT NULL,country TEXT NOT NULL,tel_ccode TEXT NOT NULL,tel_acode TEXT NOT NULL,tel TEXT NOT NULL,f_ccode TEXT NOT NULL,f_acode TEXT NOT NULL,fax TEXT NOT NULL, mobile_ccode TEXT NOT NULL,mobile TEXT NOT NULL,personal_email TEXT NOT NULL,off_email TEXT NOT NULL,comm_email TEXT NOT NULL,website TEXT NOT NULL,profile TEXT NOT NULL,detailed_profile TEXT NOT NULL,operated_countries TEXT NOT NULL,stud_sent_2017 TEXT NOT NULL,stud_sent_2018 TEXT NOT NULL ,stud_2017_other TEXT NOT NULL,stud_2018_other TEXT NOT NULL,full_name TEXT NOT NULL,dob TEXT NOT NULL,nationality TEXT NOT NULL,passport_no TEXT NOT NULL,passport_country TEXT NOT NULL, passport_issue TEXT NOT NULL,passport_exp TEXT NOT NULL,delhi_arriv TEXT NOT NULL,delhi_dep TEXT NOT NULL )"
mycursor.execute(sql)

# mycursor.execute("TRUNCATE TABLE Hot_Delig")