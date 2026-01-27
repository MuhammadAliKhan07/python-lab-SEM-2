
import math
BS = int(input("Enter your Basic Salary(BA): "))
da = BS * (70/100)
ta = BS * (30/100)
hra = BS * (10/100)
gross = BS + da + ta + hra 
print(f"Dearness Allowance: {da}Rs")
print(f"Travel Allowance: {ta}Rs")
print(f"House Rent Allowance: {hra}Rs")
print(f"Gross Salary: {gross}Rs")
print("UIN: 251A028, Date: 27/01/2026")
