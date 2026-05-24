"""try:
    x = int(input())
    result = 10 / x2
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("You can't divide by a letter!")
else:
    print(result)
finally:
    print("end")"""
try:
    age = int(input())
    if age < 0:
        raise ValueError("Age can't be less than 0!")
    if age == 0:
        raise ValueError("Age can't be 0!")
    print("ok")

except ValueError as e:
    print("error:" , e)
except ValueError as i:
    print("error:" , i)