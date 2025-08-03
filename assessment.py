def main():
    try:
        score = float(input("Enter the result(from 0.0 to 1.0): "))

        if score < 0.0 or score > 1.0:
            raise ValueError("Result outside acceptable range!")
        
        if score >= 0.9:
            print("Assessment.py: A")
        elif score >= 0.8:
            print("Assessment: B")
        elif score >= 0.7:
            print("Assessment: C")
        elif score >= 0.6:
            print("Assessment: D")
        else:
            print("Assessment: F")

    except ValueError as e:
        print("❌ Error", e)

if __name__ == "__main__":
    main()