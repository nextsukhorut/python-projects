def computepay(hours, rate):
    if hours > 40:
        overtime =hours-40
        pay = 40 * rate + overtime * (rate * 1.5)
    else:
        pay = hours * rate
    return pay

hours = 45
rate = 10
total_pay = computepay(hours, rate)

print("Pay:", total_pay)