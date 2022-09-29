import yagmail
import time

sender = 'ggglnix@gmail.com'
receiver = 'nakigi4629@canyona.com'
subject = 'automated email'
contents = """
Here is the content of the email!
Ciao!
"""
i = 0

while True:
  time.sleep(30)
  yag = yagmail.SMTP(user=sender, password='ybhztkldfrckmklu')
  subject = subject + str(i)
  yag.send(to=receiver, subject=subject, contents=contents)
  ++i
  



