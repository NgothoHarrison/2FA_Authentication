import time
import pyotp
import qrcode

key = "keythatisveryrandomandsecure"

totp = pyotp.TOTP(key)

print(totp.now())

input_code = input("Enter 2FA code : ")

uri = pyotp.totp.TOTP(key).provisioning_uri(name="Hank ",
                                            issuer_name="2FA APP by @CodeWithHank")

print(uri)

qrcode.make(uri).save("code.png")

# if totp.verify(input_code):
#     print("Welcome")
# else:
#     print("Access Denied")

# time.sleep(10)
