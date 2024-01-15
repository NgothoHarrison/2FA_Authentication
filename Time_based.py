import time
import pyotp
import qrcode

key = "keythatisveryrandomandsecure"

uri = pyotp.totp.TOTP(key).provisioning_uri(name="Hank" 
                                            issuer_name="@CodeWithHank")

print(uri)

qrcode.make(uri).save("scan.png")

# totp = pyotp.TOTP(key)

# print(totp.now()) 

# input_code = input("Enter 2FA code : ")



# if totp.verify(input_code):
#     print("Welcome")
# else:
#     print("Access Denied")

# time.sleep(10)
