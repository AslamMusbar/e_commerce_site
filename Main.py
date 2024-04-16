from flask import Flask, render_template, flash, request, session,send_file
from flask import render_template, redirect, url_for, request
#from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from werkzeug.utils import secure_filename
import datetime
import mysql.connector


import sys
app = Flask(__name__)
app.config['DEBUG']
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

@app.route("/")
def homepage():
    return render_template('index.html')

@app.route("/AdminLogin")
def AdminLogin():
    return render_template('AdminLogin.html')
@app.route("/viewcart")
def viewcart():
    uname = session['uname']
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='shopme')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT * FROM addcart where uname='" + uname + "' and status='1' ")
    data = cur.fetchall()


    return render_template('viewcart.html',data=data)
@app.route("/OwnerLogin")
def OwnerLogin():
    return render_template('OwnerLogin.html')
@app.route("/ownerregister")
def ownerregister():
    return render_template('ownerregister.html')
@app.route("/UserLogin")
def UserLogin():
    return render_template('UserLogin.html')
@app.route("/AddRaider")
def AddRaider():
    return render_template('AddRaider.html')

@app.route("/Newproduct")
def Newproduct():
    return render_template('NewProduct.html')
@app.route("/OwnerHome")
def OwnerHome():
    uname=session['uname']
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='shopme')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT * FROM ownertb where UserName='"+uname+"' ")
    data = cur.fetchall()
    #return render_template('AdminHome.html', data=data)
    return render_template('OwnerHome.html',data=data)



@app.route("/ViewOwner")
def ViewOwner():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='shopme')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT * FROM ownertb ")
    data = cur.fetchall()
    #return render_template('AdminHome.html', data=data)

    return render_template('ViewOwner.html',data=data)
@app.route("/ViewRaider")
def ViewRaider():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='shopme')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT * FROM raider ")
    data = cur.fetchall()
    #return render_template('AdminHome.html', data=data)

    return render_template('ViewRaider.html',data=data)

@app.route("/AProductInfo")
def AProductInfo():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='shopme')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT * FROM protb ")
    data = cur.fetchall()
    #return render_template('AdminHome.html', data=data)

    return render_template('AProductInfo.html',data=data)
@app.route("/NewUser")
def NewUser():
    return render_template('NewUser.html')
@app.route("/AdminHome")
def AdminHome():

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='shopme')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT * FROM regtb ")
    data = cur.fetchall()
    return render_template('AdminHome.html', data=data)

@app.route("/UserHome")
def UserHome():
    uname=session['uname']

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='shopme')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT * FROM regtb where UserName='"+uname+"' ")
    data = cur.fetchall()
    return render_template('UserHome.html', data=data)




@app.route("/adminlogin", methods=['GET', 'POST'])
def adminlogin():
    error = None
    if request.method == 'POST':
       if request.form['uname'] == 'admin' and request.form['password'] == 'admin':

           conn = mysql.connector.connect(user='root', password='', host='localhost', database='shopme')
           # cursor = conn.cursor()
           cur = conn.cursor() 
           cur.execute("SELECT * FROM regtb ")
           data = cur.fetchall()
           return render_template('AdminHome.html', data=data)

       else:

           alert = 'Username or Password is wrong'
           return render_template('goback.html', data=alert)

@app.route("/newuser", methods=['GET', 'POST'])
def newuser():
    if request.method == 'POST':

        name1 = request.form['name']
        gender1 = request.form['gender']
        Age = request.form['age']
        email = request.form['email']
        pnumber = request.form['phone']
        address = request.form['address']

        uname = request.form['uname']
        password = request.form['psw']
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='shopme')
        cursor = conn.cursor()
        cursor.execute("SELECT * from regtb where username='" + uname + "' and Password='" + password + "'")
        data = cursor.fetchone()
        if data is None:
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='shopme')
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO regtb VALUES ('" + name1 + "','" + gender1 + "','" + Age + "','" + email + "','" + pnumber + "','" + address + "','" + uname + "','" + password + "')")
            conn.commit()
            conn.close()
            # return 'file register successfully'

            return render_template('UserLogin.html')
        else:
            return "username And Password Is Already Given"


@app.route("/userlogin", methods=['GET', 'POST'])
def userlogin():
    error = None
    if request.method == 'POST':
        username = request.form['uname']
        password = request.form['password']
        session['uname'] = request.form['uname']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='shopme')
        cursor = conn.cursor()
        cursor.execute("SELECT * from regtb where username='" + username + "' and Password='" + password + "'")
        data = cursor.fetchone()
        if data is None:
            alert = 'Username or Password is wrong'
            return render_template('goback.html', data=alert)
        else:

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='shopme')
            # cursor = conn.cursor()
            cur = conn.cursor()
            cur.execute("SELECT * FROM regtb where username='" + username + "' and Password='" + password + "'")
            data = cur.fetchall()

            return render_template('UserHome.html', data=data )


@app.route("/ologin", methods=['GET', 'POST'])
def ologin():
    error = None
    if request.method == 'POST':
        username = request.form['uname']
        password = request.form['password']
        session['uname'] = request.form['uname']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='shopme')
        cursor = conn.cursor()
        cursor.execute("SELECT * from ownertb where username='" + username + "' and Password='" + password + "'")
        data = cursor.fetchone()
        if data is None:
            alert = 'Username or Password is wrong'
            return render_template('goback.html', data=alert)
        else:

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='shopme')
            # cursor = conn.cursor()
            cur = conn.cursor()
            cur.execute("SELECT * FROM ownertb where username='" + username + "' and Password='" + password + "'")
            data = cur.fetchall()

            return render_template('OwnerHome.html', data=data )
@app.route("/newowner", methods=['GET', 'POST'])
def newowner():
    if request.method == 'POST':
        sname = request.form['sname']
        sgst = request.form['sgst']
        name1 = request.form['name']
        gender1 = request.form['gender']
        Age = request.form['age']
        email = request.form['email']
        pnumber = request.form['phone']
        address = request.form['address']

        uname = request.form['uname']
        password = request.form['psw']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='shopme')
        cursor = conn.cursor()
        cursor.execute("SELECT * from ownertb where username='" + uname + "' and Password='" + password + "'")
        data = cursor.fetchone()
        if data is None:
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='shopme')
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO ownertb VALUES ('" + sname + "','" + sgst + "','" + name1 + "','" + gender1 + "','" + Age + "','" + email + "','" + pnumber + "','" + address + "','" + uname + "','" + password + "')")
            conn.commit()
            conn.close()
            # return 'file register successfully'

            return render_template('OwnerLogin.html')
        else:
            return "UserName And Password Already Given"


@app.route("/newproduct", methods=['GET', 'POST'])
def newproduct():
    if request.method == 'POST':
        if request.form["submit"] == "Submit":
            Cname = request.form['Cname']
            Ptype = request.form['Ptype']
            Pname = request.form['Pname']
            color = request.form['color']
            price = request.form['price']
            Uvideo = request.form['Uvideo']
            spec = request.form['spec']

            file = request.files['file']
            file.save("static/upload/" + file.filename)

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='shopme')
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO protb VALUES ('','" + Cname + "','" + Ptype + "','" + Pname + "','" + color + "','" + price + "','" + Uvideo + "','" + spec + "','" + file.filename + "')")
            conn.commit()
            conn.close()
            alert = 'Product register successfully'
            return render_template('goback.html', data=alert)

        elif request.form["submit"] == "Update":

            Pid = request.form['Pid']
            Cname = request.form['Cname']
            Ptype = request.form['Ptype']
            Pname = request.form['Pname']
            color = request.form['color']
            price = request.form['price']
            Uvideo = request.form['Uvideo']
            spec = request.form['spec']



            conn = mysql.connector.connect(user='root', password='', host='localhost', database='shopme')
            cursor = conn.cursor()
            cursor.execute(
                "update  protb set CompanyName ='" + Cname + "',ProductType='" + Ptype + "',ProductName='" + Pname + "',Color='" + color + "',Price='" + price + "',VideoUrl='" + Uvideo + "',Specifications='" + spec + "' where id='"+Pid+"' ")
            conn.commit()
            conn.close()
            alert = 'Record Updated!'
            return render_template('goback.html', data=alert)

        elif request.form["submit"] == "Search":
            Pid = request.form['Pid']

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='shopme')
            # cursor = conn.cursor()
            cur = conn.cursor()
            cur.execute("SELECT * FROM protb where id='"+ Pid +"' ")
            data = cur.fetchone()

            if data:
                pid=data[0]
                Cname = data[1]
                Ptype = data[2]
                Pname = data[3]
                color = data[4]
                price = data[5]
                Uvideo = data[6]
                spec = data[7]

                conn = mysql.connector.connect(user='root', password='', host='localhost', database='shopme')
                # cursor = conn.cursor()
                cur = conn.cursor()
                cur.execute("SELECT * FROM protb ")
                data = cur.fetchall()

                return render_template('Newproduct.html', Pid=pid,Cname=Cname,Ptype=Ptype,Pname=Pname,color=color,price=price,Uvideo=Uvideo,spec=spec)

            else:
                return 'Incorrect username / password !'
        elif request.form["submit"] == "Delete":

            Pid = request.form['Pid']
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='shopme')
            cursor = conn.cursor()
            cursor.execute(
                "delete from   protb   where id='" + Pid + "' ")
            conn.commit()
            conn.close()
            alert = 'Record Deleted!'
            return render_template('goback.html', data=alert)





    return render_template('goback.html')


@app.route("/AProductInfo1")
def AProductInfo1():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='shopme')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT * FROM protb ")
    data = cur.fetchall()
    #return render_template('AdminHome.html', data=data)

    return render_template('AProductInfo1.html',data=data)

@app.route("/AbookInfo")
def AbookInfo():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='shopme')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT * FROM protb ")
    data = cur.fetchall()
    #return render_template('AdminHome.html', data=data)

    return render_template('AbookInfo.html',data=data)
@app.route("/Search")
def Search():



    conn = mysql.connector.connect(user='root', password='', host='localhost', database='shopme')
    cur = conn.cursor()
    cur.execute("SELECT * FROM protb ")
    data = cur.fetchall()
    return render_template('Search.html',data=data)
@app.route("/typesearch", methods=['GET', 'POST'])
def typesearch():

    cname = request.form['Cname']
    ptype = request.form['Ptype']


    conn = mysql.connector.connect(user='root', password='', host='localhost', database='shopme')
    cursor = conn.cursor()
    cursor.execute("SELECT * from protb where CompanyName='" + cname + "' and ProductType='" + ptype + "'")
    data = cursor.fetchone()
    if data is None:
        alert = 'Product Not Found!'
        return render_template('goback.html', data=alert)
    else:



        conn = mysql.connector.connect(user='root', password='', host='localhost', database='shopme')
        cur = conn.cursor()
        cur.execute("SELECT * FROM protb where CompanyName='" + cname + "' and ProductType='" + ptype + "' ")
        data = cur.fetchall()

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='shopme')
        cur = conn.cursor()
        cur.execute("SELECT ProductId,Image,ProductName,Price FROM temptb where CompanyName='" + cname + "' and ProductType='" + ptype + "' ")
        data1 = cur.fetchall()

        return render_template('Search.html', data=data, data1=data1)







@app.route("/addraider", methods=['GET', 'POST'])
def addraider():
    if request.method == 'POST':

        name1 = request.form['name']
        gender1 = request.form['gender']
        Age = request.form['age']
        email = request.form['email']
        pnumber = request.form['phone']
        address = request.form['address']




        conn = mysql.connector.connect(user='root', password='', host='localhost', database='shopme')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO raider VALUES ('" + name1 + "','" + gender1 + "','" + Age + "','" + email + "','" + pnumber + "','" + address + "')")
        conn.commit()
        conn.close()
        # return 'file register successfully'


    return render_template('ViewRaider.html')

@app.route("/fullInfo")
def fullInfo():
    pid = request.args.get('pid')
    session['pid'] = pid

    rat1 = ''
    rat2 = ''
    rat3 = ''
    rat4 = ''
    rat5 = ''










    conn = mysql.connector.connect(user='root', password='', host='localhost', database='shopme')
    cursor = conn.cursor()
    cursor.execute(
        "SELECT  ROUND(AVG(Rate), 1) as numRating FROM reviewtb WHERE ProductId  ='" + pid + "' ")
    data2 = cursor.fetchone()
    print(data2[0])
    if data2 is None:
        avgrat = 0


    else:

        if data2[0] == 'None':
            avgrat = 0
            if (int(avgrat) == 1):
                rat1 = 'checked'
            if (int(avgrat) == 2):
                rat2 = 'checked'
            if (int(avgrat) == 3):
                rat3 = 'checked'
            if (int(avgrat) == 4):
                rat4 = 'checked'
            if (int(avgrat) == 5):
                rat5 = 'checked'
        else:
            avgrat = data2[0]

            if (avgrat == 1):
                rat1 = 'checked'
            if (avgrat == 2):
                rat2 = 'checked'
            if (avgrat == 3):
                rat3 = 'checked'
            if (avgrat == 4):
                rat4 = 'checked'
            if (avgrat == 5):
                rat5 = 'checked'



    conn = mysql.connector.connect(user='root', password='', host='localhost', database='shopme')
    cursor = conn.cursor()
    cursor.execute(
        "SELECT  count(Rate)  as numRating FROM reviewtb WHERE ProductId  ='" + pid + "' ")
    data3 = cursor.fetchone()
    if data3:
        avgrat = data3[0]



    else:
        return 'Incorrect username / password !'






    conn = mysql.connector.connect(user='root', password='', host='localhost', database='shopme')
    cursor = conn.cursor()
    cursor.execute("SELECT  sum(Smile1) as count1,sum(Smile2) as count2, sum(Smile3) as count3, sum(Smile4) as count4, sum(Smile5) as count5, sum(Smile6) as count6 FROM  reviewtb where ProductId='"+ pid +"' ")
    data = cursor.fetchone()
    if data:
        smile1 = data[0]
        smile2 = data[1]
        smile3 =  data[2]
        smile4 =  data[3]
        smile5 =  data[4]
        smile6 =  data[5]
    else:
        return 'Incorrect username / password !'

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='shopme')
    cur = conn.cursor()
    cur.execute("SELECT UserName,Review FROM reviewtb where ProductId='" + pid + "' ")
    reviewdata = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='shopme')
    cur = conn.cursor()
    cur.execute("SELECT * FROM protb where id='" + pid + "' ")
    data1 = cur.fetchall()



    return render_template('ProductFullInfo1.html',data=data1 ,avgrat=avgrat, rat1=rat1, rat2=rat2, rat3=rat3, rat4=rat4, rat5=rat5,smile1=smile1,smile2=smile2,smile3=smile3, smile4=smile4, smile5=smile5 ,smile6=smile6, reviewdata=reviewdata )


@app.route("/Book", methods=['GET', 'POST'])
def Book():
    if request.method == 'POST':
        from uuid import getnode as get_mac
        #mac = get_mac()

        uname = session['uname']
        pid = request.form['id']


        qty = request.form['qty']
        ctype = request.form['ctype']
        cardno = request.form['cardno']
        cvno = request.form['cvno']

        Bookingid = ''
        ProductName =''
        UserName= uname
        Mobile=''
        Email=''
        Qty = qty
        Amount=''
        Mac=get_mac()

        CardType= ctype
        CardNo=cardno
        CvNo=cvno
        date = datetime.datetime.now().strftime('%d-%b-%Y')

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='shopme')
        cursor = conn.cursor()
        cursor.execute("SELECT  *  FROM protb where  id='" + pid + "'")
        data = cursor.fetchone()

        if data:
            ProductName = data[3]
            price = data[5]

            Amount= float(price) *  float(Qty)

            print(Amount)


        else:
            return 'Incorrect username / password !'



        conn = mysql.connector.connect(user='root', password='', host='localhost', database='shopme')
        cursor = conn.cursor()
        cursor.execute("SELECT  *  FROM  regtb where  UserName='" + uname + "'")
        data = cursor.fetchone()

        if data:
            Mobile = data[4]
            Email= data[3]


        else:
            return 'Incorrect username / password !'

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='shopme')
        cursor = conn.cursor()
        cursor.execute("SELECT  count(*) as count  FROM  booktb  ")
        data = cursor.fetchone()

        if data:
            count = data[0]

            if count == 0:
                count =1;
            else:
                count+=1




        else:
            return 'Incorrect username / password !'
        print(count)

        Bookingid="BOOKID00" + str(count)



        conn = mysql.connector.connect(user='root', password='', host='localhost', database='shopme')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO booktb VALUES ('','" + Bookingid + "','"+ pid +"','" + ProductName + "','" + uname + "','" + Mobile + "','" + Email + "','" + Qty + "','" + str(Amount) + "','" + str(Mac) + "','"+ CardType +"','"+ CardNo +"','"+ CvNo +"','"+ date +"','Book','1','','')")
        conn.commit()
        conn.close()
        # return 'file register successfully'

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='shopme')
        cur = conn.cursor()
        cur.execute("SELECT * FROM booktb where  UserName= '"+ uname +"' ")
        data = cur.fetchall()

        conn1 = mysql.connector.connect(user='root', password='', host='localhost', database='shopme')
        cursor1 = conn1.cursor()
        cursor1.execute("update addcart set status='2' where id='"+pid+"' and uname='"+uname+"'")
        conn1.commit()
        conn1.close()




    return render_template('UbookInfo.html' , data =data )

@app.route("/UBookInfo")
def UBookInfo():
    uname = session['uname']

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='shopme')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT * FROM booktb  where UserName='" + uname +"'  ")
    data = cur.fetchall()
    return render_template('UBookInfo.html', data=data)

@app.route("/ABookInfo")
def ABookInfo():


    conn = mysql.connector.connect(user='root', password='', host='localhost', database='shopme')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT * FROM booktb")
    data = cur.fetchall()
    return render_template('ABookInfo.html', data=data)

@app.route("/UReviewInfo")
def UReviewInfo():
    uname = session['uname']

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='shopme')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT Bookid,ProductId,ProductName,UserName,MacAddress,Rate,Review FROM reviewtb  where UserName='" + uname +"'  ")
    data = cur.fetchall()
    return render_template('UReviewInfo.html', data=data)


@app.route("/AReviewInfo")
def AReviewInfo():


    conn = mysql.connector.connect(user='root', password='', host='localhost', database='shopme')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT Bookid,ProductId,ProductName,UserName,MacAddress,Rate,Review FROM reviewtb   ")
    data = cur.fetchall()
    return render_template('AReviewInfo.html', data=data)

@app.route("/addcart", methods=['GET', 'POST'])
def addcart():
    if request.method == 'POST':

        id = request.form['id']
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='shopme')
        cur = conn.cursor()
        cur.execute("SELECT * FROM protb where id='"+id+"' ")
        data = cur.fetchone()
        pid=data[0]
        cname=data[1]
        ptype=data[2]
        pname=data[3]
        color=data[4]
        price=data[5]
        uname = session['uname']





        conn = mysql.connector.connect(user='root', password='', host='localhost', database='shopme')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO addcart VALUES ('"+str(pid)+"','"+cname+"','" + ptype + "','" + pname + "','" + color + "','" + price + "','" + uname + "','1')")
        conn.commit()
        conn.close()
        # return 'file register successfully'

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='shopme')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT * FROM addcart  where uname='" + uname + "' and status='1'")
    data = cur.fetchall()
    return render_template('viewcart.html', data=data)

    #return render_template('viewcart.html')
@app.route("/addbook", methods=['GET', 'POST'])
def addbook():
    if request.method == 'POST':

        id = request.form['id']
        amount = request.form['amount']
        qty = request.form['qty']
        Amount = float(amount) * float(qty)
        print(Amount)


    return render_template('ProductFullInfo.html',data=id,data1=qty,data2=Amount)


@app.route("/action")
def action():
    from datetime import datetime
    time_now = datetime.now().strftime("%H:%M:%S")
    id = request.args.get('id')
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='shopme')
    cursor = conn.cursor()
    cursor.execute("update booktb set status='packing',time='"+time_now+"' where id='"+id+"'")
    conn.commit()
    conn.close()
    return render_template('ABookInfo.html')

@app.route("/action1")
def action1():
    from datetime import datetime
    time_now = datetime.now().strftime("%H:%M:%S")
    id = request.args.get('id')
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='shopme')
    cursor = conn.cursor()
    cursor.execute("update booktb set status='shipment',time='"+time_now+"' where id='"+id+"'")
    conn.commit()
    conn.close()
    return render_template('ABookInfo.html')
@app.route("/action2")
def action2():
    from datetime import datetime
    time_now = datetime.now().strftime("%H:%M:%S")
    id = request.args.get('id')
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='shopme')
    cursor = conn.cursor()
    cursor.execute("update booktb set status='delivered',time='"+time_now+"' where id='"+id+"'")
    conn.commit()
    conn.close()
    return render_template('ABookInfo.html')
@app.route("/p1")
def p1():
    from datetime import datetime
    time_now = datetime.now().strftime("%H:%M:%S")
    id = request.args.get('id')
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='shopme')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT * FROM booktb  where id='" + id +"'")
    data = cur.fetchone()
    pid=data[2]
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='shopme')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT * FROM protb  where id='" + pid + "'")
    data1 = cur.fetchone()

    return render_template('bill.html',data=data,data1=data1)
@app.route("/assgin")
def assgin():


    id = request.args.get('id')
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='shopme')
    # cursor = conn.cursor()
    cur = conn.cursor()
    cur.execute("SELECT * FROM raider")
    data1 = cur.fetchall()

    return render_template('assign.html',data=id,data1=data1)

@app.route("/assignraider", methods=['GET', 'POST'])
def assignraider():
    if request.method == 'POST':

        id = request.form['id']
        name = request.form['name']
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='shopme')
        cursor = conn.cursor()
        cursor.execute("update booktb set dname='"+name+"' where id='" + id + "'")

        conn.commit()
        conn.close()
        return render_template('ABookInfo.html')








if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)