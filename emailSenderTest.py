#! Python3
# This program should do 4 things: connect to user's selected SMTP server; get login info from user;
# Send a simple email that user composes; close the connection.

import smtplib, logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug('Start of program')

# Establish email server connection
print('Welcome to Brett\'s email program! Let\'s send a message.')
print('First, I need your email provider. Please enter one of these: Gmail, Yahoo, Outlook')
emailServer = input()

# TODO: Troubleshoot the if and elif statements. Only Gmail works right now.
#if emailServer == 'Gmail':
#    emailProvider = 'smtp.gmail.com'
if emailServer == 'Yahoo!':
    emailProvider = 'smtp.mail.yahoo.com'
if emailServer == 'Yahoo':
    emailProvider = 'smtp.mail.yahoo.com'
if emailServer == 'Outlook':
    emailProvider = 'smtp.office365.com' # Found this server name on serversmtp.com
# TODO: Test other email providers (iCloud, AT&T, Comcast, Verizon)
else:
    print('I don\'t know that email provider. Please try again.')

#emailServer = 'smtp.gmail.com'
conn = smtplib.SMTP(emailProvider, '587')
conn.ehlo()
conn.starttls()

# User enters their email and password:
print('Please enter your email address:')
userName = input()
print()
print('Thanks. Now enter your email password:')
password = input()
print()

# User composes their email
print('Who would you like to send your message to?')
emailTo = input()
print()
print('Alright, let\'s compose this email. What\'s the subject?')
subject = input()
print()
print('Got it. What do you want to say to ' + emailTo + '?')
body = input()
print()
print('And what signature would you like to close the email with?')
signature = input()
print()

# Displays email for user to approve before sending
print('Okay, perfect. Here\'s what I have so far:')
print()
print('To: ' + emailTo + '\nSubject: ' + subject + '\nBody: ' + body + '\nSignature: ' + signature)

# Program logs in to Gmail with user-defined name and password
conn.login(userName, password)

logging.debug('Attempting to send the email')
try:
    conn.sendmail(userName, emailTo, 'Subject: ' + subject + '\n\n' + body +'\n\n' + signature)
    #conn.sendmail('brettandrews3@gmail.com', 'brettandrews@aq2tech.com', 'Subject: Test Program\n\nIs this working?\n\n- Fingers crossed!')
except:
    print('That email didn\'t send. Try again.')
else:
    print('88 MILES PER HOUR!!!')

# Close the connection and end the program
conn.close()
logging.debug('End of program')