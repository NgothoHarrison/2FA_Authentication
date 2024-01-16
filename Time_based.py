import time
import pyotp
import qrcode

key = "keythatisveryrandomandsecure"

totp = pyotp.TOTP(key)

print(totp.now()) 

input_code = input("Enter 2FA code : ")



if totp.verify(input_code):
    print("Welcome")
else:
    print("Access Denied")

# time.sleep(10)
