# flask_blog
#health_check

Last update 2/6/18
Rewriting DB to hold new Entries for BP, Sugar, Pulse, Weight, 

Must rewrite html ids and labels properly
---


Necessary if git is not already installed ----


apt-get install git

Initial Server Setup on Digital Ocean 14.x with Python 2.x ------


sudo apt-get update -y && sudo apt-get upgrade -y && sudo apt-get install apache2 mysql-client mysql-server -y && sudo apt-get install libapache2-mod-wsgi && sudo a2enmod wsgi && cd /var/www && mkdir FlaskApp && cd FlaskApp && mkdir FlaskApp && cd FlaskApp && mkdir static templates && nano __init__.py && sudo apt-get update -y && sudo apt-get upgrade -y && apt-get install python-pip -y && pip install Flask && nano /etc/apache2/sites-available/FlaskApp.conf && sudo a2ensite FlaskApp && service apache2 reload && cd /var/www/FlaskApp && nano flaskapp.wsgi && service apache2 restart

Part 1    ——— Copy and Paste

from flask import Flask

app = Flask(__name__)

@app.route('/')
def homepage():
    return "Hi there, how ya doin this is the test page to check Flask?"


if __name__ == "__main__":
    app.run(debug=True)

Part 2 ---————— Copy and Paste

<VirtualHost *:80>
                ServerName Put Ip Address Here
                ServerAdmin youemail@email.com
                WSGIScriptAlias / /var/www/FlaskApp/flaskapp.wsgi
                <Directory /var/www/FlaskApp/FlaskApp/>
                        Order allow,deny
                        Allow from all
                </Directory>
                Alias /static /var/www/FlaskApp/FlaskApp/static
                <Directory /var/www/FlaskApp/FlaskApp/static/>
                        Order allow,deny
                        Allow from all
                </Directory>
                ErrorLog ${APACHE_LOG_DIR}/error.log
                LogLevel warn
                CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>

Part 3   ————— Copy and Paste


#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/FlaskApp/")

from FlaskApp import app as application
application.secret_key = 'your secret key. If you share your website, do NOT share it with this key.'




How to Check for errors ---
tail -f /var/log/apache2/error.log


Adding SSh Keygen for Github ---


ssh-keygen -t rsa -b 4096 -C 'viseth89@gmail.com' && eval "$(ssh-agent -s)" && nano ~/.ssh/config && ssh-add -K ~/.ssh/id_rsa && cat ~/.ssh/id_rsa.pub && git config --global user.name 'viseth89' &&  git config --global user.email viseth89@gmail.com


Command to put for github ---- Follow up with adding key on github.com

Host *
 AddKeysToAgent yes
 UseKeychain yes
 IdentityFile ~/.ssh/id_rsa
