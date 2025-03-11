def classify_age(age):
    if age < 0:
        print("Invalid age.")
    elif age <= 12:
        print("You are a Child.")
    elif age <= 19:
        print("You are a Teen.")
    elif age <= 64:
        print("You are an Adult.")
    elif age >=65:
        print("You are a Senior.")
    else:
     	print("invalid age")

classify_age(10)   
classify_age(18)
classify_age(55)
classify_age(68)