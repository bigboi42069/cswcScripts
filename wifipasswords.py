import subprocess

# ASCII art
ascii_art = """
 █     █░ ██▓  █████▒██▓    ▄████▄   ██▀███   ▄▄▄       ▄████▄   ██ ▄█▀
▓█░ █ ░█░▓██▒▓██   ▒▓██▒   ▒██▀ ▀█  ▓██ ▒ ██▒▒████▄    ▒██▀ ▀█   ██▄█▒ 
▒█░ █ ░█ ▒██▒▒████ ░▒██▒   ▒▓█    ▄ ▓██ ░▄█ ▒▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ 
░█░ █ ░█ ░██░░▓█▒  ░░██░   ▒▓▓▄ ▄██▒▒██▀▀█▄  ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ 
░░██▒██▓ ░██░░▒█░   ░██░   ▒ ▓███▀ ░░██▓ ▒██▒ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄
░ ▓░▒ ▒  ░▓   ▒ ░   ░▓     ░ ░▒ ▒  ░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒
  ▒ ░ ░   ▒ ░ ░      ▒ ░     ░  ▒     ░▒ ░ ▒░  ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░
  ░   ░   ▒ ░ ░ ░    ▒ ░   ░          ░░   ░   ░   ▒   ░        ░ ░░ ░ 
    ░     ░          ░     ░ ░         ░           ░  ░░ ░      ░  ░   
                           ░                           ░               
"""

def get_wifi_password(wifi_name):
    command = f"netsh wlan show profile \"{wifi_name}\" key=clear"
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    output_lines = result.stdout.split('\n')
    password_line = [line.split(":")[1].strip() for line in output_lines if "Key Content" in line]
    if password_line:
        return password_line[0]
    else:
        return "Password not found or Wi-Fi name is incorrect."

def get_wifi_profiles():
    command = "netsh wlan show profiles"
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    profile_names = [line.split(":")[1].strip() for line in result.stdout.split('\n') if "All User Profile" in line]
    return profile_names

def main():
    while True:  # Loop indefinitely
        print(ascii_art)  # Print the ASCII art
        wifi_profiles = get_wifi_profiles()
        for profile_name in wifi_profiles:
            password = get_wifi_password(profile_name)
            print(f"Name: {profile_name} / Password: {password}")
        input("Press Enter to rescan Wi-Fi passwords (type 'exit' to quit)...")  # Prompt for rescan
        print("\n")

if __name__ == "__main__":
    main()