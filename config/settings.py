import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class Settings:
    # SMTP Configuration
    SMTP_SERVER = os.getenv('SMTP_SERVER', 'smtp.gmail.com')
    SMTP_PORT = int(os.getenv('SMTP_PORT', 587))

    # Email Settings
    SENDER_EMAIL = os.getenv('SENDER_EMAIL', '')
    SENDER_PASSWORD = os.getenv('SENDER_PASSWORD', '')

    # Sending Limits
    MAX_EMAILS_PER_MINUTE = 30
    MAX_RETRIES = 3

    # Logging
    LOG_FILE = 'email_logs.log'

    # Attachment Limits
    MAX_ATTACHMENT_SIZE_MB = 25

    @classmethod
    def validate(cls):
        """Validate critical configuration settings"""
        errors = []

        if not cls.SENDER_EMAIL:
            errors.append("Sender email is not configured")

        if not cls.SENDER_PASSWORD:
            errors.append("SMTP password is not configured")

        return errors
