# Deep-HLR 
## A complete profile to a phone number using the Defastra API. 

This script uses the Defastra Deep Phone HLR Check API, aiming to be a tool in fraud prevention and osint research scenarios. The following data points are obtained: retrieves social media accounts suscribed to the number (Amazon, Badoo, Bumble, Microsoft, Skype, Telegram, Twitter, Uber, Xiaomi, Bukalapak, Google Duo, Kakaotalk, TikTok, Google Account, Linkedin, Battlenet, Instagram, CallerID, Yandex, VK, Economic Times, WhatsApp, Line, NextDoor, Remind, Flipkart, JD, Viber and Venmo), validates availability, connection, portability, and scores risk, retrieves carrier, verify if its included in data breaches, gets geographical location, and device info linked to a phone number in json format.

Prerequisites

To use this script, you'll need:

- Python 3.x
- A Deep Phone Check API key from Defastra

## Installation

Clone this repository or copy the check_phone.py file to your local machine.
Create a config.json file in the same directory as the script with your actual API key. See config.example.json for an example.
Install the required Python packages by running pip3 install -r requirements.txt in the script's directory.

## Usage

		python3 Deep-HLR.py --help
		

			    ,█M                                                           █▌             
			    █▀                                                              ██           
			  ,█▌                                                                 █▌         
			 ▓█          █▌                    ▄██▌                    ██µ         ▀▌        
			▓█         ██                      ▓██▌                      ▀▌         █▌       
		       ▄█         █▌                       ▓██▌             ,         ██         ▀█      
		       █         █▌         █▀             ▓██▌  J██        ██         ▀█          █▄    
		      ██        █▌         █▌         ██ ██▓██▌  J██          █▄        ██       ² █     
		      █         █         █╚          ██ █████▌  J██           █▄        ██        █▌    
		     █▌        ██        ██           ██ ██▓████████            █         █        █▌    
		     ██        █         █            ████████▌  J██            █▌        █         █    
		     █▌        █        ▀▌            ██   █▐▌ ██J██            █▌        █▌        █    
		     █▌        █        ▐█            ██ ▄ ██▌ █▌J██            █▌        █▄        █    
		     ██        █         █            ██ █▌▌▐▌╙█▌ ▀▀            █┐        █        █     
		     ▀▌        █▌        █▌           ██ ████▌ ██              ██        ▓▌        █▌    
		      █         █         ▀▌             █▌ ▐▌      ███       ▓█         █         █     
		      █▌        ▐█         ██            ██ ▐▌     ████      █▀         ██        █▌     
		       ██        ██         ╙█═         ▓─██▐██████████▌    ██         █▌         █      
			█▄        ▀█                    █▌███▌ █   ████               ██         █╝      
			 █▄         ▀▌                  ▓W██▐▌██    ███             ▓█╨         █▀       
			  ██         ▌█                     ╟▌ ▀      L            ██         ╥█Γ        
			   ██                               ██¿                              █▀          
			    ╙██                            ██▌█                            ▄██           
			      █F                          ,█▀▌▓▌                           █             
					                  █ ▀▌ █▄                                        
					                 █▌ ▀▌  █                                        
					                J████▌███▌                                       
					                █  █████ █▄                                      
					               █▌   ▓▌    █                                      
					              ▐██████▌█████▌                                     
					              █ ██▌ ▓▌ ,██└█▌                                    
					             █▀    ████╙    █                                    
					            ▄████████████████▌                                   
					            █  ▀██  █▌  ▓██  █▌                                  
					           `╙     ███▌██▀     ▌                                  
					                    ██                                           
					                    █▌                                           
		  =======================================================================================
					            D E E P     H L R                                    
		  =======================================================================================
					           author: Edgar Medina                                  
		  =======================================================================================

		  usage: Deep-HLR.py [-h] phone

		  Retrieve a full profile to a phone number including rep, hlr, carrier, geo, social, device, 
		  plus more...

		  positional arguments:
		      phone       The phone number to check in international format with the country code.

		  options:
		      -h, --help  show this help message and exit


## License
Author: Edgar Medina --
This script is licensed under the MIT License.
