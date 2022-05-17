# Functions


def computepay(h, r):
 if(h>40):
   reg = h * r
   otp = (h-40) * (r * 0.5)
   pay = reg + otp
 else:
   pay = h * r
 return pay
    
hrs = input("Enter Hours:")
fh = float(hrs)
rate = input("Enter Rate:")
fr = float(rate)

P = computepay(fh,fr)

print("Pay",P)
