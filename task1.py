
amount = int(input("enter a purchase amount: "))
coupon = input("coupon Applied: ")
member= input("premium member: ")
if amount >10000 and coupon == "yes" and member == "yes":
  print("maximum discount")
elif amount >5000 and coupon == "yes" :
  print("medium discount")
else :
  print("no discount")

  # 1.Employee Promotion Eligibility

age = int(input("Enter age: "))
experience = int(input("Enter experience: "))
salary = int(input("Enter salary: "))
if age > 25 and experience > 5 and salary > 50000:
    print("Eligible for Promotion")
else:
    print("Not Eligible")


# 2.  Student Distinction Category

maths = int(input("Enter maths marks: "))
science = int(input("Enter science marks: "))
english = int(input("Enter english marks: "))
if maths >= 75 and science >= 75 and english >= 75:
    print("Distinction")
elif maths >= 35 and science >= 35 and english >= 35:
    print("Pass")
else:
    print("Fail")

    # 3. Website Login System

username = input("Enter username: ")
password = input("Enter password: ")
otp = input("Enter OTP: ")
if username == "admin" and password == "1234" and otp == "5678":
    print("Login Successful")
else:
    print("Invalid Credentials")
  

  # 4. Check Internet Package Category

speed = int(input("Enter internet speed: "))
data = int(input("Enter data usage: "))
days = int(input("Enter remaining days: "))
if speed > 100 and data > 500 and days > 20:
    print("Premium Plan")
elif speed > 50 and data > 200 and days > 10:
    print("Standard Plan")
else:
    print("Basic Plan")


# 5. Check Job Eligibility

degree = input("Do you have degree? (yes/no): ")
experience = int(input("Enter experience: "))
age = int(input("Enter age: "))
if degree == "yes" and experience >= 2 and age > 21:
    print("Eligible for Interview")
else:
    print("Not Eligible")

    # 6. Check Flight Boarding Eligibility

ticket = input("Ticket available? (yes/no): ")
passport = input("Passport available? (yes/no): ")
luggage = int(input("Enter luggage weight: "))
if ticket == "yes" and passport == "yes" and luggage < 30:
    print("Boarding Allowed")
else:
    print("Boarding Denied")

    # 7. Check Scholarship Eligibility

marks = int(input("Enter marks: "))
attendance = int(input("Enter attendance percentage: "))
income = int(input("Enter family income: "))
if marks >= 85 and attendance >= 90 and income < 300000:
    print("Scholarship Approved")
else:
    print("Scholarship Rejected")

    # 8. Check Mobile Unlock System

pin = input("Enter PIN: ")
face = input("Face detected? (yes/no): ")
fingerprint = input("Fingerprint matched? (yes/no): ")
if pin == "1234" and face == "yes" and fingerprint == "yes":
    print("Mobile Unlocked")
else:
    print("Access Denied")

# 9. Check Hotel Booking Eligibility

rooms = int(input("Enter number of rooms: "))
days = int(input("Enter number of days: "))
budget = int(input("Enter budget: "))
if rooms >= 2 and days >= 3 and budget > 50000:
    print("Luxury Booking")
elif rooms >= 1 and days >= 2 and budget > 20000:
    print("Standard Booking")
else:
    print("Budget Booking")

    # 10. Check Exam Topper Category

sub1 = int(input("Enter subject 1 marks: "))
sub2 = int(input("Enter subject 2 marks: "))
sub3 = int(input("Enter subject 3 marks: "))
total = sub1 + sub2 + sub3
if total >= 270:
    print("Topper")
elif total >= 180:
    print("Average")
else:
    print("Needs Improvement")

    # 11. Gym Membership Category
age = int(input("Enter age: "))
weight = int(input("Enter weight: "))
height = float(input("Enter height: "))
if age > 18 and weight > 50 and height > 5.5:
    print("Fitness Category A")
elif age > 18 and weight > 45:
    print("Fitness Category B")
else:
    print("Basic Category")

    # 12. Check Traffic Penalty System
helmet = input("Helmet available: ")
license = input("License available: ")
speed = int(input("Enter speed: "))
if helmet == "yes" and license == "yes" and speed < 80:
    print("No Fine")
elif speed >= 80:
    print("Heavy Fine")
else:
    print("Normal Fine")

    # 13. Movie Ticket Pricing
age = int(input("Enter age: "))
day = input("Enter day: ")
member = input("Membership available: ")
if age < 18 and member == "yes" and day == "Sunday":
    print("50% Discount")
elif member == "yes":
    print("25% Discount")
else:
    print("No Discount")

    # 14.  Weather Alert System
temperature = int(input("Enter temperature: "))
wind = int(input("Enter wind speed: "))
rain = input("Is it raining: ")
if temperature > 40 and wind > 50 and rain == "no":
    print("Heat Alert")
elif wind > 50 and rain == "yes":
    print("Storm Alert")
else:
    print("Normal Weather")

# 15. Check Online Shopping Offer
amount = int(input("Enter purchase amount: "))
coupon = input("Coupon available? (yes/no): ")
member = input("Premium membership? (yes/no): ")
if amount > 10000 and coupon == "yes" and member == "yes":
    print("Maximum Discount")
elif amount > 5000 and coupon == "yes":
    print("Medium Discount")
else:
    print("No Discount")