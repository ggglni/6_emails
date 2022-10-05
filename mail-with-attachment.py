import yagmail


sender = 'ggglnix@gmail.com'
receiver = 'giorgio.giulianifiacco@gmail.com'
subject = 'Mail with Attachement'
contents = ["""
Here is the content of the email!
Ciao!
""", 'filex.txt']

yag = yagmail.SMTP(user=sender, password='xxxx')

yag.send(to=receiver, subject=subject, contents=contents)

  



