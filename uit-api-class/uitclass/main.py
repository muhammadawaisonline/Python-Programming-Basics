# fastapi_neon/main.py
def main():
   while True:
         try:
             x = int(input("Put Number "))
             print(f"x is {x}")
         except ValueError:
          print(f"{x} is not number")
main()

