from flask import Flask,flash, render_template,url_for,request,redirect,send_file
from wtforms import form
from wtforms import StringField,SubmitField,RadioField
from wtforms.validators import DataRequired, Length, Email
from werkzeug.utils import secure_filename
from flask_mysqldb import MySQL
from forms import exhibitor_reg,deligate_reg,host_delg
import os

app=Flask(__name__)
app.config['SECRET_KEY']='5791628bb0b13ce0c676dfde280ba245'
# app.secret_key = os.urandom(24)
app.config['RECAPTCHA_PUBLIC_KEY']='6LfNNq8UAAAAAPHwriOj3KJpYfZQfq7-Zlot5ly7'
app.config['RECAPTCHA_PRIVATE_KEY']='6LfNNq8UAAAAAP-yKVnkUkwjdlV4R_TCE-5yxRcm'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'locked'
app.config['MYSQL_DB'] = 'ficcihes'

mysql = MySQL(app)

UPLOAD_FOLDER = 'C:/Users/Saurav Akolia/Desktop/u/MySqldatabase/Ficcihes/Documents/'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

ALLOWED_EXTENSIONS = set(['jpg', 'gif', 'png' ,'pdf'])
UPLOAD_FOLDER = 'C:/Users/Saurav Akolia/Desktop/u/MySqldatabase/Ficcihes/Documents/'

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def NewFolder(Email):
	# UPLOAD_FOLDER = "C:/Users/Saurav Akolia/Desktop/u/MySqldatabase/Ficci/Documents/"
	UPLOAD_FOLDER=UPLOAD_FOLDER+Email
	os.mkdir(UPLOAD_FOLDER)	


def upload_file(Email,file):
	if request.method =='POST':
		if 'file' not in request.files:
			flash('No file part')
			return redirect(request.url)

		if file.filename =='':
			flash('No selected file')
			return redirect(request.url)

		# UPLOAD_FOLDER = "C:/Users/Saurav Akolia/Desktop/u/MySqldatabase/Ficci/Documents/"
		UPLOAD_FOLDER=UPLOAD_FOLDER+Email
		

		if file and allowed_file(file.filename):
			filename=secure_filename(file.filename)
			file.save(os.path.join(UPLOAD_FOLDER, filename))
			

def file_addr(e):
	Folder=UPLOAD_FOLDER+e
	# file_list=os.listdir(Folder)
	file_list=[]
	path_list=[]
	p=Folder+'/PASSPORT/'
	file_list.append((os.listdir(p))[0])
	path_list.append(p+(os.listdir(p))[0])

	e=Folder+'/EMPLOYEE ID/'
	file_list.append((os.listdir(e))[0])
	path_list.append(e+(os.listdir(e))[0])

	b=Folder+'/BUSINESS CARD/'
	file_list.append((os.listdir(b))[0])
	path_list.append(b+(os.listdir(b))[0])

	return file_list,path_list






@app.route("/",methods=['GET','POST'])
def home():
	return render_template('home.html')


@app.route("/exhibitor",methods=['GET','POST'])
def exhibitor():
	forms=exhibitor_reg(request.form)

	flash(forms.errors)
	if request.method =="POST" and forms.validate():
		email=forms.email.data
		password=forms.password.data
		company=forms.company.data
		title=forms.title.data
		first_name=forms.first_name.data
		last_name=forms.last_name.data
		desig=forms.desig.data
		cont_title=forms.cont_title.data
		cont_first_name=forms.cont_first_name.data
		cont_last_name=forms.cont_last_name.data
		cont_desig=forms.cont_desig.data
		add1=forms.add1.data
		add2=forms.add2.data
		city=forms.city.data
		pin=forms.pin.data
		state=forms.state.data
		mobile=forms.mobile.data
		email=forms.email.data
		a_email=forms.email.data
		pan=forms.pan.data
		gst=forms.gst.data
		scheme=forms.scheme.data
		area=forms.area.data
		# acpt_tos=forms.acpt_tos.data

		p_no=forms.tel.data
		f_no=forms.fax.data
		website=forms.website.data
		tan=forms.tan.data

		details=request.form
		country=details['country']
		t_ccode=details['tel1']
		t_acode=details['tel2']
		
		f_ccode=details['fax1']
		f_acode=details['fax2']
		m_code=details['mob1']
		
	
	

		cur=mysql.connection.cursor()

		#for Checking if data already exists
		x = cur.execute("SELECT * FROM Exhibitor_Accounts WHERE email = (%s)",(email,))
		if int(x)>0:
			return 'username already exists'
		else:
			field_names = [i[0] for i in cur.description]

			sql="INSERT INTO Exhibitor_Reg(comp_name,title,first_name,last_name,desig,cont_title,cont_first_name,cont_last_name,cont_desig,add1,add2,city,pin,state,country,t_ccode,t_acode,p_no,f_ccode,f_acode,f_no,m_code,m_no,email,a_email,website,pan,tan,gst,schm,area)VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
			
			val=(company,title,first_name,last_name,desig,cont_title,cont_first_name,cont_last_name,cont_desig,add1,add2,city,pin,state,country,t_ccode,t_acode,p_no,f_ccode,f_acode,f_no,m_code,mobile,email,a_email,website,pan,tan,gst,scheme,area)
			cur.execute(sql, val)
			mysql.connection.commit()

			sql1="INSERT INTO exhibitor_accounts(email,password) VALUES (%s,%s) " 
			value=email,password
			cur.execute(sql1, value)
			mysql.connection.commit()
			cur.close()
			

			return 'sucess'	

	return render_template('exhibit.html',form=forms)

@app.route("/exhibitdata",methods=['GET','POST'])
def exhibitdata():

	##for getting data from database
	mycursor=mysql.connection.cursor()
	mycursor=mysql.connection.cursor()
	mycursor.execute("SELECT id,first_name,comp_name,email,m_no FROM exhibitor_reg")
	x=mycursor.fetchall()

	#for posting the specfic data	
	selected_data = request.args.get('type')
	if (selected_data) :
		mycursor.execute("SELECT * FROM exhibitor_reg WHERE id='"+selected_data+"'")
		mydata=mycursor.fetchall()
		field_names = [i[0] for i in mycursor.description]
		return 	render_template('ExhibitData.html',posts=mydata[0],field_names = field_names)	
	
	return render_template('ExhibitSummary.html',posts=x)

@app.route("/exhibituserdata",methods=['GET','POST'])
def exhibituserdata():

	##for getting data from database
	mycursor=mysql.connection.cursor()
	mycursor=mysql.connection.cursor()
	mycursor.execute("SELECT * FROM exhibitor_accounts")
	x=mycursor.fetchall()	
	field_names = [i[0] for i in mycursor.description]

	return render_template('ExhibitUserData.html',posts=x,field_names = field_names)

@app.route("/deligate",methods=['GET','POST'])  
def deligate():
	form=deligate_reg(request.form)
	if request.method=='POST' and form.validate():
		name=form.name.data
		desig=form.desig.data
		company=form.company.data
		address=form.address.data
		
		City=form.City.data
		Mobile=form.Mobile.data
		Fax=form.Fax.data
		Email=form.Email.data

		# delg_type=form.delg_type.data
		d1_name=form.d1_name.data
		d1_desig=form.d1_desig.data
		d1_org=form.d1_org.data
		d1_mobile=form.d1_mobile.data
		d1_email=form.d1_email.data

		d2_name=form.d2_name.data
		d2_desig=form.d2_desig.data
		d2_org=form.d2_org.data
		d2_mobile=form.d2_mobile.data
		d2_email=form.d2_email.data

		d3_name=form.d3_name.data
		d3_desig=form.d3_desig.data
		d3_org=form.d3_org.data
		d3_mobile=form.d3_mobile.data
		d3_email=form.d3_email.data

		d4_name=form.d4_name.data
		d4_desig=form.d4_desig.data
		d4_org=form.d4_org.data
		d4_mobile=form.d4_mobile.data
		d4_email=form.d4_email.data

		d5_name=form.d5_name.data
		d5_desig=form.d5_desig.data
		d5_org=form.d5_org.data
		d5_mobile=form.d5_mobile.data
		d5_email=form.d5_email.data

		d6_name=form.d6_name.data
		d6_desig=form.d6_desig.data
		d6_org=form.d6_org.data
		d6_mobile=form.d6_mobile.data
		d6_email=form.d6_email.data

		date=form.date.data

		details=request.form
		country=details['country']
		pin=details['pincode']
		state=details['state']
		gst=details['gstyesno']
		delegate=details['delegate']
		participant=details['participant']
		membershipNumber=details['membershipNumber']
		sponsorcat=details['sponsorcat']
		paymode=details['paymode']
		chequeDD=details['chequeDD']
		bankdetail=details['bankdetail']

		cur=mysql.connection.cursor()

		#for Checking if data already exists
		x = cur.execute("SELECT * FROM delig_accounts WHERE email = (%s)",(Email,))
		if int(x)>0:
			return 'username already exists'
		else:
			# field_names = [i[0] for i in cur.description]delegate

			# sql="INSERT INTO Exhibitor_Reg(comp_name,title,first_name,last_name,desig,cont_title,cont_first_name,cont_last_name,cont_desig,add1,add2,city,pin,state,country,t_ccode,t_acode,p_no,f_ccode,f_acode,f_no,m_code,m_no,email,a_email,website,pan,tan,gst,schm,area)VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
			sql="INSERT INTO delig_reg(name,desig,comp_name,m_addr,country,pin,state,city,gst,mobile_no,fax_no,email,delegate,ind_prtcpnt,memb_no,sponser_categ,d1_name,d1_desig,d1_org,d1_mobile,d1_email, d2_name,d2_desig,d2_org,d2_mobile,d2_email, d3_name,d3_desig,d3_org,d3_mobile,d3_email, d4_name,d4_desig,d4_org,d4_mobile,d4_email, d5_name,d5_desig,d5_org,d5_mobile,d5_email, d6_name,d6_desig,d6_org,d6_mobile,d6_email,paym_mode,cheque_dd_no,bank,dated) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
			# val=(company,title,first_name,last_name,desig,cont_title,cont_first_name,cont_last_name,cont_desig,add1,add2,city,pin,state,country,t_ccode,t_acode,p_no,f_ccode,f_acode,f_no,m_code,mobile,email,a_email,website,pan,tan,gst,scheme,area)
			val=(name,desig,company,address,country,pin,state,City,gst,Mobile,Fax,Email,delegate,participant,membershipNumber,sponsorcat,d1_name,d1_desig,d1_org,d1_mobile,d1_email, d2_name,d2_desig,d2_org,d2_mobile,d2_email, d3_name,d3_desig,d3_org,d3_mobile,d3_email, d4_name,d4_desig,d4_org,d4_mobile,d4_email, d5_name,d5_desig,d5_org,d5_mobile,d5_email, d6_name,d6_desig,d6_org,d6_mobile,d6_email,paymode,chequeDD,bankdetail,date)
			cur.execute(sql, val)
			mysql.connection.commit()
  
			sql1="INSERT INTO delig_accounts(email,name) VALUES (%s,%s) " 
			value=Email,name
			cur.execute(sql1, value)
			mysql.connection.commit()
			cur.close()


			return 'sucess'	

	
	return render_template('delig.html',form=form)	


@app.route("/deligdata",methods=['GET','POST'])
def deligdata():

	##for getting data from database
	mycursor=mysql.connection.cursor()
	mycursor=mysql.connection.cursor()
	mycursor.execute("SELECT id,name,comp_name,email,mobile_no FROM delig_reg")
	x=mycursor.fetchall()

	#for posting the specfic data	
	selected_data = request.args.get('type')
	if (selected_data) :
		mycursor.execute("SELECT * FROM delig_reg WHERE id='"+selected_data+"'")
		mydata=mycursor.fetchall()
		field_names = [i[0] for i in mycursor.description]
		return 	render_template('DeligData.html',posts=mydata[0],field_names = field_names)	
	
	return render_template('DeligSummary.html',posts=x)

@app.route("/Hdeligate",methods=['GET','POST']) 
def Host_delg():

	form=host_delg(request.form)

	if request.method=='POST' and form.validate():
		details=request.form
		recomnd=form.recom.data
		reg=form.reg.data
		attend=form.attend.data
		gender=form.gender.data
		title=form.title.data
		last_name=form.last_name.data
		first_name=form.first_name.data
		recomnd_2019=details['recommendedby']

		other_recommendedby=details['other_recommendedby']

		occupation=details['occupation']
		desig=form.desig.data
		org=form.org.data
		add1=form.add1.data
		add2=form.add2.data
		city=form.city.data
		pin=form.pin.data
		state=form.state.data
		country=details['country']
		tel_ccode=form.tel.country_code.data
		tel_acode=form.tel.area_code.data
		tel=form.tel.number.data
		f_ccode=form.fax.country_code.data
		f_acode=form.fax.area_code.data
		fax=form.fax.number.data
		mobile_ccode=form.mobile_ccode.data
		mobile=form.mobile.data



		personal_email=form.p_email.data
		off_email=form.o_email.data
		comm_email=form.c_email.data
		website=form.website.data
		profile=form.profile.data
		detailed_profile=form.d_profile.data
		operated_countries=form.op_country.data
		stud_sent_2017=form.sent_ind_17.data
		stud_sent_2018=form.sent_ind_18.data
		stud_2017_other=form.sent_cont_17.data
		stud_2018_other=form.sent_cont_18.data
		full_name=form.p_name.data
		dob=form.dob.data
		nationality=form.nationality.data
		passport_no=details['passportno']
		passport_country=details['pass_country']
		passport_issue=form.pasport_issue.data
		passport_exp=form.passport_exp.data
		delhi_arriv=form.delhi_arrival.data
		delhi_dep=form.delhi_dept.data


		cur=mysql.connection.cursor()

		#for Checking if data already exists
		x = cur.execute("SELECT * FROM hot_delig WHERE comm_email = (%s)",(comm_email,))
		if int(x)>0:
			return 'username already exists'
		else:
			# field_names = [i[0] for i in cur.description]delegate

			# sql="INSERT INTO delig_reg(name,desig,comp_name,m_addr,country,pin,state,city,gst,mobile_no,fax_no,email,delegate,ind_prtcpnt,memb_no,sponser_categ,d1_name,d1_desig,d1_org,d1_mobile,d1_email, d2_name,d2_desig,d2_org,d2_mobile,d2_email, d3_name,d3_desig,d3_org,d3_mobile,d3_email, d4_name,d4_desig,d4_org,d4_mobile,d4_email, d5_name,d5_desig,d5_org,d5_mobile,d5_email, d6_name,d6_desig,d6_org,d6_mobile,d6_email,paym_mode,cheque_dd_no,bank,dated) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
			sql="INSERT INTO hot_delig(recomnd,reg,attend,gender,title,last_name,first_name,recomnd_2019,occupation,desig,org,add1,add2,city,pin,state,country,tel_ccode,tel_acode,tel,f_ccode,f_acode,fax,mobile_ccode,mobile,personal_email,off_email,comm_email,website,profile,detailed_profile,operated_countries,stud_sent_2017,stud_sent_2018,stud_2017_other,stud_2018_other,full_name,dob,nationality,passport_no,passport_country,passport_issue,passport_exp,delhi_arriv,delhi_dep) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
			#val=(name,desig,company,address,country,pin,state,City,gst,Mobile,Fax,Email,delegate,participant,membershipNumber,sponsorcat,d1_name,d1_desig,d1_org,d1_mobile,d1_email, d2_name,d2_desig,d2_org,d2_mobile,d2_email, d3_name,d3_desig,d3_org,d3_mobile,d3_email, d4_name,d4_desig,d4_org,d4_mobile,d4_email, d5_name,d5_desig,d5_org,d5_mobile,d5_email, d6_name,d6_desig,d6_org,d6_mobile,d6_email,paymode,chequeDD,bankdetail,date)
			val=(recomnd,reg,attend,gender,title,last_name,first_name,recomnd_2019,occupation,desig,org,add1,add2,city,pin,state,country,tel_ccode,tel_acode,tel,f_ccode,f_acode,fax,mobile_ccode,mobile,personal_email,off_email,comm_email,website,profile,detailed_profile,operated_countries,stud_sent_2017,stud_sent_2018,stud_2017_other,stud_2018_other,full_name,dob,nationality,passport_no,passport_country,passport_issue,passport_exp,delhi_arriv,delhi_dep)
			cur.execute(sql, val)
			mysql.connection.commit()

			#for uploading the user document to the local disk
			
			ALLOWED_EXTENSIONS = set(['jpg', 'gif', 'png' ,'pdf'])
			UPLOAD_FOLDER = 'C:/Users/Saurav Akolia/Desktop/u/MySqldatabase/Ficcihes/Documents/'
			# if 'file' not in request.files :
			# 	flash('No file part')
			# 	return redirect(request.url)
			
					
			
			UPLOAD_FOLDER=UPLOAD_FOLDER+comm_email
			os.mkdir(UPLOAD_FOLDER)

			file=request.files.get("delegate_passport")
			if file.filename =='':
				flash('No selected file')
				return redirect(request.url)
			if file and allowed_file(file.filename):
				PASSPORT=UPLOAD_FOLDER+'/'+'PASSPORT'
				os.mkdir(PASSPORT)
				filename=secure_filename(file.filename)
				file.save(os.path.join(PASSPORT , filename))

			# if 'file' not in request.files :
			# 	flash('No file part')
			# 	return redirect(request.url)
			file=request.files.get("delegate_idcard")
			if file.filename =='':
				flash('No selected file')
				return redirect(request.url)
			if file and allowed_file(file.filename):
				EMPLOYEE_ID=UPLOAD_FOLDER+'/'+'EMPLOYEE ID'
				os.mkdir(EMPLOYEE_ID)
				filename=secure_filename(file.filename)
				file.save(os.path.join(EMPLOYEE_ID , filename))

			# if 'file' not in request.files :
			# 	flash('No file part')
			# 	return redirect(request.url)
			file=request.files.get("delegate_businesscard")
			if file.filename =='':
				flash('No selected file')
				return redirect(request.url)
			if file and allowed_file(file.filename):
				BUSINESS_CARD=UPLOAD_FOLDER+'/'+'BUSINESS CARD'
				os.mkdir(BUSINESS_CARD)
				filename=secure_filename(file.filename)
				file.save(os.path.join(BUSINESS_CARD , filename))	
			


			return 'sucess'	

	return render_template('HostDelig.html',form=form) 

@app.route("/hostdata",methods=['GET','POST'])
def hostdata():

	##for getting data from database
	mycursor=mysql.connection.cursor()
	mycursor=mysql.connection.cursor()
	mycursor.execute("SELECT id,full_name,org,comm_email,mobile FROM hot_delig")
	x=mycursor.fetchall()

	# For fetching document address 
	mycursor.execute("SELECT comm_email FROM hot_delig")
	y=mycursor.fetchall()
	# doc_add=[]
	doc_info=[]
	doc_dict={}
	for i in y:
		file_list,path_list= file_addr(str(i[0]))
		doc_info.append(file_list)
		#doc_add.append( path_list)
		
		#for storing the file and its address in dictionary
		for j,k in zip(file_list,path_list): 
			doc_dict[j]=k

	#for posting the specfic data		
	selected_data = request.args.get('type')
	if (selected_data) :
		mycursor.execute("SELECT * FROM hot_delig WHERE id='"+selected_data+"'")
		mydata=mycursor.fetchall()
		field_names = [i[0] for i in mycursor.description]

		return 	render_template('HostData.html',posts=mydata[0],field_names = field_names)


	return render_template('HostSummary.html',posts=zip(x,doc_info),doc_dict=doc_dict)

@app.route("/layout",methods=['GET','POST'])
def layout():
	return render_template('layout.html')

@app.route("/l",methods=['GET','POST'])
def l():
	return render_template('l.html')



# for showing documents 
@app.route("/send",methods=['GET','POST'])
def send():
	file_url=request.args.get('doc')
	return send_file(file_url)




if __name__ == '__main__':
    app.run(debug=True)

	