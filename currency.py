title = r"""
|#######====================#######|
|#(1)*FREEDOM HACKER  KINGDOM *(1)#|
|#**          /===\   ********  **#|
|*# {G}      | (") |             #*|
|#*  ******  | /v\ |    O N E    *#|
|#(1)         \===/            (1)#|
|##=========  ONE BTC ===========##|
------------------------------------
THIS IS THE EXCHANGE TERMINAL TOOL 
Develop by Xenon, Mon, Aug, 18 , 1:10:57AM
------------------------------------
"""

def get_exchange_rate():
    base_currency = input("Enter the base currency (e.g., USD, EUR): ").upper()
    target_currency = input("Enter the target currency (e.g., MMK, GBP): ").upper()
    try:
        rate = float(input(f"Enter the rate to calculate for {base_currency}/{target_currency}: "))
    except ValueError:
        print("Invalid rate entered. Please enter a valid number.")
        return
    try:
        amount = float(input(f"Enter the amount of {target_currency} to Exchange {base_currency}: "))
    except ValueError:
        print("Invalid amount entered. Please enter a valid number.")
        return
    calculate_rate = amount / rate  
    print(f"That is the amount of {base_currency}: {calculate_rate:.2f} {base_currency}")
    return base_currency, target_currency, rate

def main():
  while 1 == 1:
    print(title)
    get_exchange_rate()
    response = input("Do you want to do again?(Y/N):").lower()
    if response == 'y':
      print("Okay , We will do again!")
    else:
      print("We'll stop this tool see ya !")
      break





if __name__ == "__main__":
    main()
