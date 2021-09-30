from PIL import Image as a1
from PIL import ImageDraw as a2
from PIL import ImageFont as a3
import pandas as pan

ayush = pan.read_csv('name_of_cert_owners.csv')
font = a3.truetype('arial.ttf', 65)
for index, i in ayush.iterrows():
    ay1 = a1.open('sample_cert.jpg')
    draw = a2.Draw(ay1)
    draw.text(xy=(401, 234), text='{}'.format(i['name']), fill=(0, 0, 0), font=font)
    ay1.save('cert_save_folder/{}.jpg'.format(i['name']))
