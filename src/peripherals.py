# peripherals.py

def simulate_device(device_type):
    # Simuler le périphérique (par exemple : joystick, télécommande)
    return f"Simulation de {device_type} en cours..."

def select_hardware(hardware_list):
    print("Sélectionnez le matériel à tester :")
    for i, hardware in enumerate(hardware_list):
        print(f"{i+1} - {hardware}")
    choice = int(input("Votre choix : "))
    return hardware_list[choice - 1]
