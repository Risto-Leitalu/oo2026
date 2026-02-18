class smart_thermostat:
    def __init__(self, room_name, initial_temp, target_temp):
        self.room_name = room_name
        self.current_temp = initial_temp
        self.target_temp = target_temp
        self.is_heating = False

    def update_temperature(self):
        if self.current_temp < self.target_temp:
            self.is_heating = True
            self.current_temp += 0.5
            print(f"[{self.room_name}] Heating Up... Current: {self.current_temp}°C")
        elif self.current_temp > self.target_temp:
            self.is_heating = False
            self.current_temp -= 0.5
            print(f"[{self.room_name}] Cooling down... Current: {self.current_temp}°C")
        else:
            self.is_heating = False
            print(f"[{self.room_name}] Target reached: {self.current_temp}°C\n")

    def set_new_target(self, new_target):
        print(f"\n Changing {self.room_name} target to {new_target}°C...")
        self.target_temp = new_target

    def display_status(self):
        status = "HEATING" if self.is_heating else "IDLE"
        print(f"--- {self.room_name} Status ---")
        print(f"Current: {self.current_temp}°C | Target: {self.target_temp}°C | State: {status}\n")


living_room = smart_thermostat("Elutuba", 19.0, 21.0)

sauna = smart_thermostat("Saun", 60, 80.0)

#Showing current living room status
living_room.display_status()

#Showing current sauna status
sauna.display_status()

#Updating Living room temperature
living_room.update_temperature()

#Updating Sauna temperature
sauna.update_temperature()

# Setting living room target temperature to 15°C and looping until the target is reached.
living_room.set_new_target(15.0)

while living_room.current_temp != living_room.target_temp:
    living_room.update_temperature()

living_room.update_temperature()

living_room.display_status()