#! Python3
# This program should do 4 things: connect to Gmail's SMTP server; login as me;
# Send a simple email to my work email; close the connection.

import smtplib, logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug('Start of program')

conn = smtplib.SMTP('smtp.gmail.com', '587')
conn.ehlo()
conn.starttls()

# User enters their email and password:
print('Please enter your Gmail address:')
userName = input()
print()

print('Thanks. Now enter your Gmail password:')
password = input()
print()

print('Who would you like to send your message to?')
emailTo = input()
print()

# Program logs in to Gmail with user-defined name and password
conn.login(userName, password)

logging.debug('Attempting to send the email')
try:
    conn.sendmail(userName, emailTo, 'Subject: Variable Test\n\nTesting out using variables for conn.login()')
    #conn.sendmail('brettandrews3@gmail.com', 'brettandrews@aq2tech.com', 'Subject: Test Program\n\nIs this working?\n\n- Fingers crossed!')
except:
    print('That email didn\'t send. Try again.')
else:
    print('88 MILES PER HOUR!!!')


conn.close()

logging.debug('End of program')