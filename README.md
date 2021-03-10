# LawFirmSite-Matthew
​​​​​​​
Law Firm Site

This program is made to host a flask web app on the users computer, more specifially the web page of 'Lucksore Legal' which is defined in the mainpage.html template.
The web page is made to have a Logo at the top centre of the header just above the centred text 'Lucksore Legal'.
Below this, there is a 'Services' division containing 4 services provided by Lucksore Legal - they each have a title and a description.

Below the 'Services' division there is an 'About' division with information about the Lucksore team, containing a photo, the names and titles of the 2 Lucksore team members.
After this there is a footer element which contains contact information including telephone number, email address and physical address of the Lucksore Legal company.
The web page has a simple colour palette with shades of black, white and blue. All fonts used on the web page are the standard html fonts.  

this program has :

    >Python script (main.py) to start a local server 
    >Main html page (mainpage.html) which contains 
        - Logo
        - Header
        - Services section contaning 4 services, each serivce has a
            > Title
            > Description
        - About section contaning 2 team members, each member has a
            > Photo
            > Name
            > Title
        - Footer with the contact details below
            > Telephone number
            > Email address
            > Physical address 

In order to get the web page running, a virtual environment must be created and the following commands need to be run

1- cd Documents\GitHub\LawFirmSite-Matthew\VE\Scripts
2- activate
3- cd ..
4- cd ..
5- set FLASK_APP=main.py
6- flask run

After executing these commands, the following url needs to be entered into your browser http://127.0.0.1:5000/

Matthew Klemick