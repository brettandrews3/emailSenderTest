#! Python3
# This program should do 4 things: connect to user's selected SMTP server; get login info from user;
# Send a simple email that user composes; close the connection.

import smtplib, logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.basicConfig(filename='myProgramLog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logging.debug('Start of program')

# Establish email server connection
print('Welcome to Brett\'s email program! Let\'s send a message.')
emailServer = input('First, I need your email provider: Gmail, Yahoo, or Outlook?\n')

# TODO: Troubleshoot the if and elif statements. Only Gmail works right now.
if emailServer == 'Gmail':
    emailProvider = 'smtp.gmail.com'
elif emailServer == 'Yahoo!':
    emailProvider = 'smtp.mail.yahoo.com'
elif emailServer == 'Yahoo':
    emailProvider = 'smtp.mail.yahoo.com'
elif emailServer == 'Outlook':
    emailProvider = 'smtp.office365.com' # Found this server name on serversmtp.com
# TODO: Test other email providers (iCloud, AT&T, Comcast, Verizon)
else:
    print('I don\'t know that email provider. Please try again.')

#emailServer = 'smtp.gmail.com'
conn = smtplib.SMTP(emailProvider, '587')
conn.ehlo()
conn.starttls()

# User enters their email and password:
userName = input('Please enter your email address:\n')
print()
password = input('Thanks. Now enter your email password:\n')
print()

# User composes their email
emailTo = input('Who would you like to send your message to?\n')
print()
subject = input('Alright, let\'s compose this email. What\'s the subject?\n')
print()
body = input('Got it. What do you want to say to ' + emailTo + '?\n')
print()
signature = input('And what signature would you like to close the email with?\n')
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