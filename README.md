# Bulk Email Sender Application

## Overview
A Python-based bulk email sending application with a user-friendly GUI, personalization features, and robust error handling.

## Features
- Load recipient lists from CSV/Excel
- Personalized email templates with placeholders
- SMTP configuration
- Rate-limited email sending
- Comprehensive logging
- Attachment support
- Email validation
- Unsubscribe link generation

## Prerequisites
- Python 3.8+
- Libraries listed in `requirements.txt`

## Setup

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/bulk-email-sender.git
cd bulk-email-sender
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the project root with the following:
```
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SENDER_EMAIL=your_email@gmail.com
SENDER_PASSWORD=your_app_password
```

**Note**: For Gmail, use an App Password, not your regular password.

## Usage

### Running the Application
```bash
python main.py
```

### Preparing Recipient List
- Create a CSV or Excel file with columns:
  - `email`: Recipient email address
  - `name`: Recipient name
  - Add any additional columns for personalization

### Email Template Placeholders
Use `{{placeholder}}` in your email body to insert personalized content:
```
Hello {{name}},

We're excited to share our latest update with you!

Best regards,
Your Company
```

## Configuration Options
Adjust settings in `config/settings.py`:
- SMTP server details
- Email sending rate limits
- Attachment size limits
- Logging configuration

## Logging
Logs are stored in `logs/email_logs.log`

## Security Considerations
- Use App Passwords for email accounts
- Keep `.env` file private
- Validate recipient email addresses
- Comply with anti-spam regulations

## Troubleshooting
- Ensure all dependencies are installed
- Check SMTP server settings
- Verify email credentials
- Review log files for detailed error information

## Contributing
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License
@DilmithPathirana

## Disclaimer
This tool is for legitimate, consent-based email communication. Always respect email recipients' privacy and adhere to anti-spam laws.
