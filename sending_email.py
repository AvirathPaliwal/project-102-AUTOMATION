import smtplib 
    
def main():
     email = smtplib.SMTP('BMW.gmail.com', 587) 
     email.starttls() 
     #type e-mail which you are seeing for example
     email.login("BMW@gmail.com", "BMW@2008") 
     message = "we are giveing you over new BMW car :)"
     email.sendmail("BMW", "avirathplaiwal2008@gmail.com",message) 
     email.quit()


main()