import argparse
import json
import os
import requests

# Banner
print("")
print("            ,█M                                                           █▌             ")
print("            █▀                                                              ██           ")
print("          ,█▌                                                                 █▌         ")
print("         ▓█          █▌                    ▄██▌                    ██µ         ▀▌        ")
print("        ▓█         ██                      ▓██▌                      ▀▌         █▌       ")
print("       ▄█         █▌                       ▓██▌             ,         ██         ▀█      ")
print("       █         █▌         █▀             ▓██▌  J██        ██         ▀█          █▄    ")
print("      ██        █▌         █▌         ██ ██▓██▌  J██          █▄        ██       ² █     ")
print("      █         █         █╚          ██ █████▌  J██           █▄        ██        █▌    ")
print("     █▌        ██        ██           ██ ██▓████████            █         █        █▌    ")
print("     ██        █         █            ████████▌  J██            █▌        █         █    ")
print("     █▌        █        ▀▌            ██   █▐▌ ██J██            █▌        █▌        █    ")
print("     █▌        █        ▐█            ██ ▄ ██▌ █▌J██            █▌        █▄        █    ")
print("     ██        █         █            ██ █▌▌▐▌╙█▌ ▀▀            █┐        █        █     ")
print("     ▀▌        █▌        █▌           ██ ████▌ ██              ██        ▓▌        █▌    ")
print("      █         █         ▀▌             █▌ ▐▌      ███       ▓█         █         █     ")
print("      █▌        ▐█         ██            ██ ▐▌     ████      █▀         ██        █▌     ")
print("       ██        ██         ╙█═         ▓─██▐██████████▌    ██         █▌         █      ")
print("        █▄        ▀█                    █▌███▌ █   ████               ██         █╝      ")
print("         █▄         ▀▌                  ▓W██▐▌██    ███             ▓█╨         █▀       ")
print("          ██         ▌█                     ╟▌ ▀      L            ██         ╥█Γ        ")
print("           ██                               ██¿                              █▀          ")
print("            ╙██                            ██▌█                            ▄██           ")
print("              █F                          ,█▀▌▓▌                           █             ")
print("                                          █ ▀▌ █▄                                        ")
print("                                         █▌ ▀▌  █                                        ")
print("                                        J████▌███▌                                       ")
print("                                        █  █████ █▄                                      ")
print("                                       █▌   ▓▌    █                                      ")
print("                                      ▐██████▌█████▌                                     ")
print("                                      █ ██▌ ▓▌ ,██└█▌                                    ")
print("                                     █▀    ████╙    █                                    ")
print("                                    ▄████████████████▌                                   ")
print("                                    █  ▀██  █▌  ▓██  █▌                                  ")
print("                                   `╙     ███▌██▀     ▌                                  ")
print("                                            ██                                           ")
print("                                            █▌                                           ")
print("  =======================================================================================")
print("                                    D E E P     H L R                                    ")
print("  =======================================================================================")
print("                                   author: Edgar Medina                                  ")
print("  =======================================================================================")
print("")

def main(api_key, phone):
    url = "https://api.defastra.com/deep_phone_check"
    headers = {"X-API-KEY": api_key, "Content-Type": "application/x-www-form-urlencoded"}
    data = {"phone": phone}

    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200:
        print(json.dumps(response.json(), indent=4))
    else:
        error_msg = response.json()["error_message"]
        print(f"Error: {error_msg}")


if __name__ == "__main__":
    # Define the command-line arguments
    parser = argparse.ArgumentParser(description="Retrieve a full profile to a phone number including rep, hlr, carrier, geo, social, device, plus more...")
    parser.add_argument("phone", help="The phone number to check in international format with the country code.")

    # Parse the arguments
    args = parser.parse_args()

    # Read the API key from the config file
    config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.json")
    with open(config_file) as f:
        config = json.load(f)
        api_key = config.get("api_key")

    if not api_key:
        print("Error: API key not found in config file.")
        exit(1)

    main(api_key, args.phone)
