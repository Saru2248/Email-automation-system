import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_email_data():
    file_path = os.path.join(BASE_DIR, 'data', 'Email Analysis Dataset.csv')
    df = pd.read_csv(file_path)
    
    mapped_data = []
    for _, row in df.iterrows():
        # Create a mock email out of the To Name
        to_name_str = str(row['To Name']).lower().replace(' ', '.')
        email = f"{to_name_str}@example.com"
        
        # Topic as subject
        subject = str(row['Email topic'])
        
        # Faked generic message body
        message = f"Hello {row['To Name']},\n\nThis is an automated follow-up regarding {subject}."
        
        # Injecting a specific default time because Date has no time component
        # We default to sending these at 09:00 AM
        schedule_time = f"{row['Date']} 09:00"
        
        mapped_data.append({
            'email': email,
            'subject': subject,
            'message': message,
            'schedule_time': schedule_time
        })
        
    return mapped_data