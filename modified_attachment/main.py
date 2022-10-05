import yagmail
import pandas
import os

sender = 'ggglnix@gmail.com' 
subject = 'Bill from Giorgio'

yag = yagmail.SMTP(user=sender, password='nxexxenxdrfiznpc')

df = pandas.read_csv('monthly_customers.csv')

for index,row in df.iterrows():
    with open(f"""{row['month']}-{row['name']}.txt""",'w') as file: #open the file, named month-name.txt
        x = file.write(row['amount']) #write in the file
    contents = [f"""Hi {row['name']} this is the bill from Giorgio for {row['month']}!""",file.name] #create content of the email + attachment
    yag.send(to=row['email'], subject=subject, contents=contents) #send email
