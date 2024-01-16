import time
import pyotp

key = "thekeyshouldbeprivatetotheserveronly"

counter = 0

hotp = pyotp.HOTP(key)

print(hotp.at(0))
print(hotp.at(1))
print(hotp.at(2))
print(hotp.at(3))

for j in range(4):
    print(hotp.verify(input("Enter OTP : "), counter))
    counter += 1
