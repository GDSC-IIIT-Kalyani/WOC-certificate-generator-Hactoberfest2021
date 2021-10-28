from flask import Flask,render_template,request

from PIL import Image as a1
from PIL import ImageDraw as a2
from PIL import ImageFont as a3


import imghdr


from auth import main
import os
import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import mimetypes
service = main()



app = Flask(__name__)
codes = ["A","B","C","D","E","F","G","H","I","J","K","L"]
winners =12
@app.route("/")
def Index():
    return render_template("index.html")

@app.route("/form" , methods=["POST"])
def form():


 email = request.form.get("email")
 name = request.form.get("name")
 code = request.form.get("code")
 font = a3.truetype('arial.ttf', 65)
 for i in range(0,winners):
   if(code == codes[i]):
    ay1 = a1.open('sample_cert.jpg')
    draw = a2.Draw(ay1)
    draw.text(xy=(401, 234), text='{}'.format(name), fill=(0, 0, 0), font=font)
    ay1.save('cert_save_folder/{}.jpg'.format(name))

    with open('cert_save_folder/{}.jpg'.format(name), 'rb') as f:
        image_data = f.read()
        image_type = imghdr.what(f.name)
        image_name = f.name
    
    file_attachements = [r'./cert_save_folder/',name,'.jpg']
    

    emailMsg = 'Three files attached'

    Message = MIMEMultipart()
    Message['to'] = email
    Message['subject'] = "Check out the new logo"
    Message.attach(MIMEText(emailMsg, 'plain'))

    for attachement in file_attachements:
        content_type, encoding = mimetypes.guess_type(attachement)
        main_type, sub_type = content_type.split('/', 1)
        file_name = os.path.basename(attachement)

        f = open(attachement, 'rb')

        myFile = MIMEBase(main_type, sub_type)
        myFile.set_payload(f.read())
        myFile.add_header('Content-Disposition' , 'attachement', filename = file_name)
        encoders.encode_base64(myFile)

        f.close()

        Message.attach(myFile)
    
    raw_string = base64.urlsafe_b64encode(Message.as_bytes()).decode()
    message = service.users().messages().send(userId='me', body={'raw': raw_string}).execute()
   
    return render_template("result.html")
 return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
