import smtplib
import openai
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def generate_email(professor_name, research_area, your_name, your_background, purpose):
    prompt = f"""
    Write a professional cold email to Professor {professor_name}, who specializes in {research_area}. 
    Introduce yourself as {your_name}, mention your background ({your_background}), 
    and express interest in their work. Clearly state your purpose: {purpose}. 
    Keep it concise, polite, and professional.
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are an AI that drafts professional emails."},
                  {"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

def send_email(sender_email, sender_password, recipient_email, subject, body):
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    
    msg.attach(MIMEText(body, 'plain'))
    
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())

if __name__ == "__main__":
    openai.api_key = "your_openai_api_key"
    
    professor_name = "Dr. Smith"
    research_area = "Machine Learning"
    your_name = "John Doe"
    your_background = "Undergraduate student in Computer Science at XYZ University"
    purpose = "Seeking research opportunities in your lab."
    
    email_body = generate_email(professor_name, research_area, your_name, your_background, purpose)
    
    sender_email = "your_email@gmail.com"
    sender_password = "your_email_password"
    recipient_email = "professor_email@university.edu"
    subject = "Inquiry about Research Opportunities"
    
    send_email(sender_email, sender_password, recipient_email, subject, email_body)
    
    print("Email sent successfully!")
