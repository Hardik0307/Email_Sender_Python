import smtplib  #SMTP -Simple Mail Transfer Protocol
msg = """
<Mail from Sender>

Hello, keep focusing on Python.It's cool and provide mailing
service. Toodels!!
                                -User
"""
con = smtplib.SMTP('smtp.gmail.com',587) #for Gmail
# Yahoo - smtp.yahoo.com,587
# Outlook/Hotmail - smpt-mail.outlook.com,587

con.ehlo() 
con.starttls()
con.login(user_mail,password) # in signal quote
con.sendmail(from_addr,to_addrs,msg)
con.quit()
