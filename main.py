from flask import Flask, render_template
import os
main = Flask(__name__)

images = os.path.join('static', 'Images')

main.config['Images'] = images


@main.route('/')
def Main():
    Image_name1 = os.path.join(main.config['Images'], 'logo.jpg')
    Image_name2 = os.path.join(main.config['Images'], 'business-woman.jpg')
    Image_name3 = os.path.join(main.config['Images'], 'business-man.jpg')
    return render_template('mainpage.html', I1 = Image_name1, I2 = Image_name2, I3 = Image_name3)