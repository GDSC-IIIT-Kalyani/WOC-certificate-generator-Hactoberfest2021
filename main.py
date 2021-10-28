from flask import Flask,render_template,request

from PIL import Image as a1
from PIL import ImageDraw as a2
from PIL import ImageFont as a3


import imghdr
import smtplib
from email.message import EmailMessage

app = Flask(__name__)
codes = ["A","B","C","D","E","F","G","H","I","J","K","L"]
winners =12
@app.route("/")
def Index():
    return render_template("index.html")

@app.route("/form" , methods=["POST"])
def form():

    # Enter your email and password  from which you want to sent the image
 Your_email = "dummy e-mail"
 Your_Password = "dummy password"

 email = request.form.get("email")
 name = request.form.get("name")
 code = request.form.get("code")
 font = a3.truetype('arial.ttf', 65)
 for i in range(0,winners):
   if(code == codes[i]):
    codes[i] = ran.randint(8485,904356)
    ay1 = a1.open('sample_cert.jpg')
    draw = a2.Draw(ay1)
    draw.text(xy=(401, 234), text='{}'.format(name), fill=(0, 0, 0), font=font)
    ay1.save('cert_save_folder/{}.jpg'.format(name))



    newMessage = EmailMessage()                         
    newMessage['Subject'] = "Check out the new logo" 
    newMessage['From'] = Your_email                
    newMessage['To'] = email              
    newMessage.set_content('Let me know what you think. Image attached!') 
    with open('cert_save_folder/{}.jpg'.format(name), 'rb') as f:
        image_data = f.read()
        image_type = imghdr.what(f.name)
        image_name = f.name
    
    newMessage.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)


    server = smtplib.SMTP("smtp.gmail.com" , 587)
    server.starttls()
    server.login(Your_email , Your_Password)
    server.send_message(newMessage)
   
    return render_template("result.html")
 return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
