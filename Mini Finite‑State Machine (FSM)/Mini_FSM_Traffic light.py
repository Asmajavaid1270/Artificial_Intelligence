# Traffic Light Finite State Machine (FSM) Simulation
# --- Task 4 (Interactive) ---
import time

fsm = {
    "RED": {"next": "GREEN", "duration": 2},
    "GREEN": {"next": "YELLOW", "duration": 1},
    "YELLOW": {"next": "RED", "duration": 1},
}

def run_traffic_light(cycles=2, real_delay=False):
    state = "RED"
    history = []
    for _ in range(cycles * len(fsm)):
        info = fsm[state]
        print(f"State: {state} (wait [{info['duration']}s])")
        history.append(state)
        time.sleep(info["duration"]) if real_delay else False
        state = info["next"]
    return history

while True:
    cont = input("\nTraffic light simulation (type 'exit' to stop)").strip().lower()
    if cont == "exit":
        print("Stopped Task 4.")
        break

    while True:
        try:
            cycles = int(input("Number of cycles (e.g., 2): "))
            if cycles <= 0:
                print("Enter a positive integer.")
                continue
            break
        except ValueError:
            print("Please enter an integer.")

    delay_ans = input("Run traffic light with real delays (y/n): ").strip().lower()
    history = run_traffic_light(cycles, real_delay=(delay_ans == 'y'))
    print("Visited states:", history)