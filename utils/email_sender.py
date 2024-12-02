import smtplib
import logging
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from typing import List, Dict, Optional

from config.settings import Settings


class EmailSender:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self._setup_logging()

    def _setup_logging(self):
        """Configure logging for email operations"""
        logging.basicConfig(
            filename=Settings.LOG_FILE,
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s: %(message)s'
        )

    def send_personalized_email(
        self,
        recipient: Dict[str, str],
        subject: str,
        template: str
    ) -> bool:
        """
        Send a personalized email to a recipient

        Args:
            recipient: Dictionary with recipient details
            subject: Email subject
            template: Email body template

        Returns:
            Boolean indicating email send success
        """
        try:
            # Create message
            msg = MIMEMultipart()
            msg['From'] = Settings.SENDER_EMAIL
            msg['To'] = recipient['email']
            msg['Subject'] = subject

            # Personalize email body
            personalized_body = template.format(**recipient)
            msg.attach(MIMEText(personalized_body, 'plain'))

            # Send email
            with smtplib.SMTP(Settings.SMTP_SERVER, Settings.SMTP_PORT) as server:
                server.starttls()
                server.login(Settings.SENDER_EMAIL, Settings.SENDER_PASSWORD)
                server.send_message(msg)

            self.logger.info(f"Email sent successfully to {
                             recipient['email']}")
            return True

        except Exception as e:
            self.logger.error(f"Failed to send email to {
                              recipient['email']}: {str(e)}")
            return False

    def send_bulk_emails(
        self,
        recipients: List[Dict[str, str]],
        subject: str,
        template: str
    ):
        """
        Send bulk personalized emails with rate limiting

        Args:
            recipients: List of recipient dictionaries
            subject: Email subject
            template: Email body template

        Returns:
            Tuple of (successful emails, failed emails)
        """
        successful_emails = 0
        failed_emails = 0

        for idx, recipient in enumerate(recipients, 1):
            # Send email
            if self.send_personalized_email(recipient, subject, template):
                successful_emails += 1
            else:
                failed_emails += 1

            # Rate limiting
            if idx % Settings.MAX_EMAILS_PER_MINUTE == 0:
                # Wait for a minute after sending MAX_EMAILS_PER_MINUTE
                time.sleep(60)

        return successful_emails, failed_emails
