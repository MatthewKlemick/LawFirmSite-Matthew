from flask import Flask, render_template
import os
main = Flask(__name__)

images = os.path.join('static', 'Images')

main.config['Images'] = images


@main.route('/')
def Main():
    i1 = os.path.join(main.config['Images'], 'logo.jpg')
    i2 = os.path.join(main.config['Images'], 'business-woman.jpg')
    i3 = os.path.join(main.config['Images'], 'business-man.jpg')
    i4 = os.path.join(main.config['Images'], 'space.jpg')
    return render_template('mainpage.html', I1 = i1, I2 = i2, I3 = i3, I4 = i4 )