#Made by Abhishek
print("FIND AND REPLACE")
n = input("Enter your Paragraph: ")
while n:
  f = input("Find What: ")
  r = input("Replace with: ")
  new = n.replace(f,r)
  if new == n:
     print(f"{f} not found\n")
  else:
     print("Replaced Successfully.\n")
     print(new)
  n = new
