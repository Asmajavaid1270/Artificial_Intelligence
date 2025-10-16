# Scholarship Eligibility System
def decide_scholarship(cgpa, family_income, achievements):
    # normalize achievements
    ach = [a.strip().lower() for a in (achievements or [])]

    has_national = any("national" in a for a in ach)

    # Full scholarship: high CGPA and low income
    if cgpa >= 3.7 and family_income < 60000:
        return "Full Scholarship"
    # Partial scholarship for national-level achievements (priority over simple CGPA-income rule)
    elif cgpa >= 3.5 and has_national:
        return "Partial Scholarship"
    # Partial scholarship: decent CGPA and moderate income
    elif cgpa >= 3.0 and family_income < 120000:
        return "Partial Scholarship"
    else:
        return "Not Eligible"


def read_float(prompt, lo=None, hi=None):
    while True:
        try:
            x = float(input(prompt))
            if lo is not None and x < lo:
                print(f"Value must be >= {lo}.")
                continue
            if hi is not None and x > hi:
                print(f"Value must be <= {hi}.")
                continue
            return x
        except ValueError:
            print("Please enter a valid number.")


def read_int(prompt, lo=None, hi=None):
    while True:
        try:
            x = int(input(prompt))
            if lo is not None and x < lo:
                print(f"Value must be >= {lo}.")
                continue
            if hi is not None and x > hi:
                print(f"Value must be <= {hi}.")
                continue
            return x
        except ValueError:
            print("Please enter a valid integer.")


if __name__ == "__main__":
    while True:
        raw = input("\nEnter candidate info (or type 'exit' to stop): ").strip()
        if raw.lower() == "exit":
            print("Stopped Task 2.")
            break

        # Use the provided raw input only as a trigger; collect the real fields next
        cgpa = read_float("CGPA (0.0-4.0): ", 0.0, 4.0)
        family_income = read_int("Family income PKR (per month): ", 0)
        ach_str = input("Achievements (comma separated, leave blank if none): ").strip()

        # clean achievements: remove empty items
        achievements = [a.strip() for a in ach_str.split(',') if a.strip()]

        decision = decide_scholarship(cgpa, family_income, achievements)
        print(f"Decision: {decision}")
