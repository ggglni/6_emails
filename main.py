import yagmail
import time
from datetime import datetime as dt

sender = 'ggglnix@gmail.com'
receiver = 'bianco.cinzia@yahoo.it'
subject = 'automated email'
contents = """
Here is the content of the email!
Ciao!
"""
i = 0

while True: #an email every 30 seconds
    now = dt.now()
    print(now)
    if (now.hour == 10 and now.minute == 53):
        yag = yagmail.SMTP(user=sender, password='xxxxxxxxxx')
        subject = subject + str(i)
        yag.send(to=receiver, subject=subject, contents=contents)
        print('email sent '+str(i))
        ++i
        time.sleep(60)
  



