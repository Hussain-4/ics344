import smtplib

target_ip = "192.168.153.130"
port = 25

usernames = ["root", "admin", "msfadmin", "user", "guest", "mail", "www", "service"]

def smtp_user_enum(target_ip, port, usernames):
    server = smtplib.SMTP(target_ip, port)
    print("Starting user enumeration...")
    
    for user in usernames:
        response_code, response_message = server.docmd("VRFY", user)
        
        if response_code == 252:
            print(f"[+] User found: {user}")
        else:
            print(f"[-] User not found: {user}")
    
    server.quit()

smtp_user_enum(target_ip, port, usernames)
