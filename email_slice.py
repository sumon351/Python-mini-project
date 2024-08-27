# email slice in python
# here is my email nhaque3510@gmail.com
#here nhaque3510 is a username
# and gmail.com is a domain name
email=input("Enter your email : ")
index=email.index("@")
username=email[:index]
domain=email[index+1:]
print(f"your user name is : {username} and domain name is : {domain}")
