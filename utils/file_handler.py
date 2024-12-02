import pandas as pd
import re
from typing import List, Dict, Optional


class FileHandler:
    @staticmethod
    def validate_email(email: str) -> bool:
        """
        Validate email address using regex

        Args:
            email: Email address to validate

        Returns:
            Boolean indicating email validity
        """
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(email_regex, email) is not None

    @classmethod
    def load_recipients(cls, file_path: str) -> List[Dict[str, str]]:
        """
        Load recipients from CSV or Excel file

        Args:
            file_path: Path to the file containing recipient details

        Returns:
            List of validated recipient dictionaries

        Raises:
            ValueError: If file format is unsupported or no valid recipients found
        """
        # Determine file type
        if file_path.endswith('.csv'):
            df = pd.read_csv(file_path)
        elif file_path.endswith(('.xls', '.xlsx')):
            df = pd.read_excel(file_path)
        else:
            raise ValueError("Unsupported file format. Use CSV or Excel.")

        # Validate columns
        required_columns = ['email', 'name']
        for col in required_columns:
            if col not in df.columns:
                raise ValueError(f"Missing required column: {col}")

        # Validate and filter recipients
        valid_recipients = []
        for _, row in df.iterrows():
            recipient = row.to_dict()
            if cls.validate_email(recipient['email']):
                valid_recipients.append(recipient)

        if not valid_recipients:
            raise ValueError("No valid recipients found in the file")

        return valid_recipients
