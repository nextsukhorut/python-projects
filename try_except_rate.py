def main():
    try:
        hours_input = input("Enter hour: ")
        hours = float(hours_input)
        rate_input = input("Enter rate: ")
        rate = float(rate_input)

        if hours <= 40:
            pay = hours * rate
        else:
            overtime = hours - 40
            pay = 40 * rate + overtime * (rate * 1.5)

        print(f"Salary: {pay}")
    except ValueError:
        print("❌ Error: Please enter a valid number!")
        quit()

if __name__ == "__main__":
    main()