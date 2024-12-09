import smtplib

target_ip = "192.168.153.129"
port = 25

def send_example_email(target_ip, port):
    try:
        server = smtplib.SMTP(target_ip, port)
        from_address = "example@example.com"
        to_address = "root@localhost"
        subject = "Test Email"
        body = "This is a test email."
        message = f"Subject: {subject}\n\n{body}"
        
        server.sendmail(from_address, to_address, message)
        print("[+] Email sent successfully")
        server.quit()
    except Exception as e:
        print("[-] Failed to send email:", e)

print("Attempting to send an example email...")
send_example_email(target_ip, port)
