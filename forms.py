from wtforms import Form

from wtforms import StringField, PasswordField, SubmitField,SelectField,IntegerField, BooleanField,RadioField,DateField,FormField,TextAreaField
from wtforms.validators import DataRequired, Length, Email,AnyOf
from wtforms import validators


class deligate_reg(Form):
    name = StringField('Name',
                           [validators.DataRequired(), Length(min=2, max=20)])
    desig = StringField('Designation',
                           [validators.DataRequired(), Length(min=2, max=20)])
    company=StringField('Name of the Company'
                  ,[validators.DataRequired(),Length(min=2,max=20)])
    address = StringField('  Mailing Address',validators=[DataRequired(), Length(min=2, max=20)])

    country = StringField('Country',
                           validators=[DataRequired()])
    state = StringField('State ')
    # gst=RadioField('Do you have a registered GSTN',choices=[('Yes','Yes'),('No','No')])
    City=StringField("City",[validators.DataRequired()])
    Mobile=StringField('Mobile',
                           validators=[DataRequired(), Length(min=12,max=20)])  
    Fax=StringField('Fax No')
    Email = StringField('Email',
                        validators=[DataRequired(), Email()])
    
    d1_name=StringField('name')
    d1_desig=StringField('desig')
    d1_org=StringField('org')
    d1_mobile=StringField('mobile')
    d1_email=StringField('email',[validators.Email()])

    d2_name=StringField('name')
    d2_desig=StringField('desig')
    d2_org=StringField('org')
    d2_mobile=StringField('mobile')
    d2_email=StringField('email')


    d3_name=StringField('name')
    d3_desig=StringField('desig')
    d3_org=StringField('org')
    d3_mobile=StringField('mobile')
    d3_email=StringField('email',)

    d4_name=StringField('name')
    d4_desig=StringField('desig')
    d4_org=StringField('org')
    d4_mobile=StringField('mobile')
    d4_email=StringField('email')

    d5_name=StringField('name')
    d5_desig=StringField('desig')
    d5_org=StringField('org')
    d5_mobile=StringField('mobile')
    d5_email=StringField('email')

    d6_name=StringField('name')
    d6_desig=StringField('desig')
    d6_org=StringField('org')
    d6_mobile=StringField('mobile')
    d6_email=StringField('email')

    # paym_mode=RadioField('Payment Mode:',choices=[(' Demand Draft/Cheque',' Demand Draft/Cheque'),('NEFT','NEFT'),('SWIFT','SWIFT'),('Online','Online')])
    date=DateField('date',format='%Y/%m/%d')
    submit = SubmitField('Submit')
    # recaptcha=RecaptchaField()


class exhibitor_reg(Form):
    email = StringField('Email Address', [validators.Length(min=6, max=35),validators.Email()])



    password = PasswordField('Password', [
        validators.DataRequired(),validators.Length(min=6,max=20)])

    company=StringField('Company Name',
                        [validators.DataRequired(),validators.Length(min=2, max=20) ])     
         
    first_name=StringField('First Name',
                        [validators.DataRequired(),validators.Length(min=2,max=24) ])      
    last_name=StringField('Last Name',
                        [validators.DataRequired(),validators.Length(min=2,max=24) ])      
    desig=StringField('Designation',
                        [validators.DataRequired(),validators.Length(min=2,max=24) ])      
    
    cont_first_name=StringField('Contact First Name',
                        [validators.DataRequired(),validators.Length(min=2,max=24) ])      
    cont_last_name=StringField('Contact Last Name',
                        [validators.DataRequired(),validators.Length(min=2,max=24) ])      
    cont_desig=StringField('Contact Designation',
                        [validators.DataRequired(),validators.Length(min=2,max=24) ])      
    add1=StringField('Address Line 1',
                        [validators.DataRequired(),validators.Length(min=2,max=24) ])      
    add2=StringField('Address Line 2',
                        [validators.DataRequired(),validators.Length(min=2,max=24) ])      
    city=StringField('City',
                        [validators.DataRequired(),validators.Length(min=2,max=24) ])      

    pin=IntegerField('Pin/Zip Code',
                        [validators.DataRequired() ])      
    state=StringField('State',
                        [validators.DataRequired(),validators.Length(min=2,max=24) ])      

    country=StringField('country')
    tel=StringField('Telephone')
    fax=StringField('Fax')
    mobile=StringField('Mobile',
                        [validators.DataRequired(),validators.Length(min=2,max=24) ])      
    email=StringField('Email',
                        [validators.DataRequired(), Email()])
    a_email=StringField('Alternate Email',
                        [validators.DataRequired(), validators.Email()])
    website=StringField('Website')
    pan=StringField('PAN Number',
                        [validators.DataRequired(),validators.Length(min=2,max=24) ])      
    tan=StringField('TAN Number')
                            
    gst=StringField('GST Number',
                        [validators.DataRequired(),validators.Length(min=2,max=24) ])
    
    scheme=SelectField("Scheme",choices=[('selected','schemes'),('Shell','Shell'),('Bare','Bare'),('Pavillion','Pavillion')],validators=[validators.DataRequired()])

    area=StringField('Area',
                        [validators.DataRequired(),validators.Length(min=2,max=24) ])      
    acpt_tos= BooleanField('acpt_tos')

    submit = SubmitField('Submit')

    title=SelectField("title",choices=[('Mr','Mr'),('Mrs','Mrs'),('Ms','Ms'),('Dr','Dr'),('Engg','Engg'),('Prof','Prof'),('Col','Col')],validators=[validators.DataRequired()])

    cont_title=SelectField("title",choices=[('Mr','Mr'),('Mrs','Mrs'),('Ms','Ms'),('Dr','Dr'),('Engg','Engg'),('Prof','Prof'),('Col','Col')],validators=[validators.DataRequired()])

class ContactForm(Form):
    country_code=IntegerField('Country Code')
    area_code=IntegerField('Area Code')
    number=StringField('Number')


class host_delg(Form):
        recom=SelectField('WERE YOU RECOMMENDED TO US ALSO FOR HES 2016 / 2017 / 2018',choices=[(0,'- Select -'),('Yes','Yes'),('No','No')],validators=[validators.DataRequired()])
        
        reg=SelectField('DID YOU ALSO REGISTER FOR HES 2016 / 2017 /2018',choices=[('Yes','Yes'),('No','No')])
        
        attend=SelectField('DID YOU ATTEND HES 2016 / 2017 / 2018',choices=[('2015','ATTENDED 2015'),('2016','ATTENDED 2016'),('2017','ATTENDED 2017'),('Not','NOT ATTENDED')])
        
        title=SelectField("TITLE",choices=[('Mr','Mr'),('Mrs','Mrs'),('Ms','Ms'),('Dr','Dr'),('Engg','Engg'),('Prof','Prof'),('Col','Col')],validators=[validators.DataRequired()])
       
        gender=SelectField('GENDER',choices=[('m','MALE'),('f','FEMALE')])

        first_name=StringField('FIRST NAME',
                        [validators.DataRequired(),validators.Length(min=2,max=24) ])      
        last_name=StringField('LAST NAME',
                        [validators.DataRequired(),validators.Length(min=2,max=24) ])      
        desig=StringField('DESIGNATION',
                        [validators.DataRequired(),validators.Length(min=2,max=24) ]) 
        org=StringField('ORGANISATION NAME(FULL NAME)',
                        [validators.DataRequired(),validators.Length(min=2, max=20) ])
        add1=StringField('ADDRESS LINE 1',
                        [validators.DataRequired(),validators.Length(min=2,max=24) ])      
        add2=StringField('ADDRESS LINE 2',
                        [validators.DataRequired(),validators.Length(min=2,max=24) ])      
        city=StringField('CITY',
                        [validators.DataRequired(),validators.Length(min=2,max=24) ])      

        pin=IntegerField('PIN/ZIP CODE',
                        [validators.DataRequired() ])      
        state=StringField('STATE',
                        [validators.DataRequired(),validators.Length(min=2,max=24) ])      

        country=StringField('COUNTRY')

        # t_ccode=StringField('Country Code')
        # t_acode=StringField('Area Code')
        # tel=StringField('Phone Numbe')
        # fax=StringField('Fax')
        tel=FormField(ContactForm)
        fax=FormField(ContactForm)
        mobile_ccode=StringField('Country Code')
        mobile=StringField('Mobile Number',
                        [validators.DataRequired(),validators.Length(min=2,max=24) ]) 
        mobilei_ccode=StringField('Country Code')
        mobilei=StringField('India Mobile Number',
                        [validators.DataRequired(),validators.Length(min=2,max=24) ])                     
        p_email=StringField('PERSONAL E-MAIL ID',
                        [validators.DataRequired(), Email()])
        o_email=StringField('OFFICIAL E-MAIL ID',
                        [validators.DataRequired(), validators.Email()])
        c_email=StringField('E-MAIL ID FOR COMMUNICATION',
                        [validators.DataRequired(), Email()])
        website=StringField('WEBSITE') 
        profile=TextAreaField('YOUR PROFILE ',[validators.DataRequired()])
        d_profile=TextAreaField('YOUR DETAILED PROFILE',[validators.DataRequired()])
        op_country=StringField('NAME OF THE COUNTRIES YOU OPERATE IN (KINDLY USE COMMAS IF MORE THAN ONE)',[validators.DataRequired()])
        sent_ind_17=StringField('NO. OF STUDENTS SENT TO INDIA IN 2017 (PLEASE MENTION THE NAME OF THE INSTITUTIONS ALSO)')
        sent_ind_18=StringField('NO. OF STUDENTS SENT TO INDIA IN 2018 (PLEASE MENTION THE NAME OF THE INSTITUTIONS ALSO)')
        sent_cont_17=StringField('NO. OF STUDENTS SENT TO ANY OTHER COUNTRY IN 2017 (PLEASE MENTION THE NAME OF COUNTRIES ALSO)')
        sent_cont_18=StringField('NO. OF STUDENTS SENT TO ANY OTHER COUNTRY IN 2018 (PLEASE MENTION THE NAME OF COUNTRIES ALSO)')
        p_name=StringField('FULL NAME (AS IN PASSPORT)',[validators.DataRequired()])
        dob=DateField('DATE OF BIRTH',format='%Y/%m/%d')
        nationality=StringField('NATIONALITY',[validators.DataRequired()])
        pasport_issue=DateField('PASSPORT ISSUE DATE',format='%Y/%m/%d')
        passport_exp=DateField('PASSPORT EXPIRY DATE',format='%Y/%m/%d')
        delhi_arrival=DateField('ARRIVAL DATE IN DELHI',format='%Y/%m/%d')
        delhi_dept=DateField('DEPARTURE DATE FROM DELHI',format='%Y/%m/%d')

        submit = SubmitField('Submit')