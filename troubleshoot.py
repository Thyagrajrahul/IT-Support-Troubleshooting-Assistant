
def show_wifi_steps():
    print("\nWi-Fi Troubleshooting")
    print("1. Check that Wi-Fi is switched on.")
    print("2. Confirm you selected the correct network.")
    print("3. Restart the router if you are allowed to.")


def show_slow_computer_steps():
    print("\nSlow Computer Troubleshooting")
    print("1. Close applications you are not using.")
    print("2. Check available storage space.")
    print("3. Restart the computer if appropriate.")


def show_printer_steps():
    print("\nPrinter Troubleshooting")
    print("1. Check whether the printer is switched on.")
    print("2. Check the paper and printer connection.")
    print("3. Confirm that the correct printer is selected.")


def save_support_request(name, problem, status):
    with open("support_requests.txt", "a", encoding="utf-8") as file:
        file.write(f"Name: {name}\n")
        file.write(f"Problem: {problem}\n")
        file.write(f"Status: {status}\n")
        file.write("-" * 30 + "\n")

    print("\nSupport request saved successfully!")


def main():
    print("=== IT Support Troubleshooting Assistant ===")

    name = input("Enter your name: ").strip()

    problem = input(
        "Enter your problem (wifi / slow computer / printer): "
    ).strip().lower()

    if problem == "wifi":
        show_wifi_steps()
        status = "Troubleshooting guide provided"

    elif problem == "slow computer":
        show_slow_computer_steps()
        status = "Troubleshooting guide provided"

    elif problem == "printer":
        show_printer_steps()
        status = "Troubleshooting guide provided"

    else:
        print("\nNo guide is available for that issue yet.")
        print("Please contact your IT support team.")
        status = "Needs IT support"

    save_support_request(name, problem, status)


if __name__ == "__main__":
    main()
