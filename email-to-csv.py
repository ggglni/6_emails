import yagmail
import pandas


sender = 'ggglnix@gmail.com'
 
subject = 'automated email'
contents = """
Here is the content of the email!
Ciao!
"""

yag = yagmail.SMTP(user=sender, password='nxexxenxdrfiznpc')

df = pandas.read_csv('contacts.csv')

for index,row in df.iterrows():
    print(row['email'], row['name'])
    contents = f"""Hi {row['name']} here is the content of the email!"""
    yag.send(to=row['email'], subject=subject, contents=contents)
    print('email sent to '+row['name'])

  



