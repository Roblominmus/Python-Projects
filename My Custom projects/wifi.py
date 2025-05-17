import subprocess
import re
import os

def get_wifi_profiles():
    try:
        # Get all Wi-Fi profiles
        profiles_output = subprocess.run(['netsh', 'wlan', 'show', 'profiles'], 
                                       capture_output=True, text=True, check=True)
        profiles = re.findall(r':\s(.*?)\r', profiles_output.stdout)
        return profiles
    except subprocess.CalledProcessError as e:
        print(f"Error getting Wi-Fi profiles: {e}")
        return []

def get_wifi_password(profile):
    try:
        # Get password for a specific profile
        key_output = subprocess.run(['netsh', 'wlan', 'show', 'profile', 
                                  profile, 'key=clear'], 
                                 capture_output=True, text=True, check=True)
        key_content = re.search(r'Key Content\s*:\s(.*?)\r', key_output.stdout)
        print("Passwords found")
        return key_content.group(1) if key_content else "No password found"
    except subprocess.CalledProcessError as e:
        print(f"Error getting password for {profile}: {e}")
        return "Error retrieving password"

def save_to_file(profiles_with_passwords, filename="wifi_passwords.txt"):
    try:
        with open(filename, 'w') as f:
            f.write("Stored Wi-Fi Networks and Passwords:\n")
            f.write("="*40 + "\n")
            for profile, password in profiles_with_passwords.items():
                f.write(f"SSID: {profile}\nPassword: {password}\n\n")
        print(f"Successfully saved to {os.path.abspath(filename)}")
    except IOError as e:
        print(f"Error saving to file: {e}")

def main():
    print("Retrieving stored Wi-Fi networks and passwords...")
    profiles = get_wifi_profiles()
    
    if not profiles:
        print("No Wi-Fi profiles found or access denied.")
        return
    
    profiles_with_passwords = {}
    for profile in profiles:
        password = get_wifi_password(profile)
        profiles_with_passwords[profile] = password
    
    save_to_file(profiles_with_passwords)

if __name__ == "__main__":
    main()