# write code to implement a turnstile
#state = 0 is locked, 1 is unlocked
state = "locked"
while True:
    if state == "locked":
        scamming_device = input("tap to pay please")
        if scamming_device ==  "tap":
                state = "unlocked"
                ok = input("pass also we took $100,000.00 from your bank account due to tariffs these days, come through")
                if ok == "hail Trump":
                        print("thank you")
                elif ok == "never":
                        print("DEMOCRAT!!! ARREST THEM NOW!!!!")
        else:
            print("SECURITY WE HAVE AN ILLEGAL HERE")
    if state == "unlocked":
        please = input("DONATE TO MY PERSONAL SA- I MEAN LIBRARY FUND!!!")
        if please == "yes":
              print("thank you")
        if please == "no":
              print("SECURITY WE HAVE A LOWER CLASS IMMIGRANT HERE!!!!")
              state = "locked"
