import pandas
import yagmail

sender = 'ggglnix@gmail.com'

subject = 'Mail with Attachement'
contents = ["""
Here is the content of the email!
Ciao!
""", 'filex.txt']

yag = yagmail.SMTP(user=sender, password='xxxc')

df = pandas.read_csv('contacts.csv')

for index,row in df.iterrows():
    print(row['email'], row['name'])
    contents = [f"""Hi {row['name']} here is the content of the email!""", f"""{row['attachment']}"""]
    yag.send(to=row['email'], subject=subject, contents=contents)
    print('email sent to '+row['name'])