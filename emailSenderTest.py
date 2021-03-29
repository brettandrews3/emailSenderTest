#! Python3

# This program should do 4 things: connect to Gmail's SMTP server; login as me;
# Send a simple email to my work email; close the connection.

import smtplib

conn = smtplib.SMTP('smtp.gmail.com', '587')
conn.ehlo()
conn.starttls()

conn.login('brettandrews3@gmail.com', 'Allmine11!')

try:
    conn.sendmail('brettandrews3@gmail.com', 'brettandrews@aq2tech.com')
    #conn.sendmail('brettandrews3@gmail.com', 'brettandrews@aq2tech.com', 'Subject: Test Program\n\nIs this working?\n\n- Fingers crossed!')
except:
    print('That email didn\'t send. Try again.')
else:
    print('88 MILES PER HOUR!!!')


conn.close()