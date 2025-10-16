# --- Task 5 (Interactive) ---
def read_nonempty(prompt):
    while True:
        s = input(prompt).strip()
        if s:
            return s
        print("Input cannot be empty, try again.")

def read_choice(prompt, choices):
    choices_lower = [c.lower() for c in choices]
    while True:
        s = input(f"{prompt} ({'/'.join(choices)}): ").strip().lower()
        if s in choices_lower:
            return s
        print(f"Please enter one of {choices}.")

def read_float_range(prompt, lo, hi):
    while True:
        try:
            x = float(input(prompt))
            if lo <= x <= hi:
                return x
            else:
                print(f"Value must be between ({lo}) and ({hi}).")
        except ValueError:
            print("Please enter a number.")

# Fill the form below
name = read_nonempty("Your name: ")
activity = read_choice("Preferred activity?", ["read", "walk", "nap", "music"])
cgpa = read_float_range("Your CGPA (0.0-4.0): ", 0.0, 4.0)

print(f"Summary -> Name: {name}, Activity: {activity}, CGPA: {cgpa}")