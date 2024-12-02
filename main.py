from utils.email_sender import EmailSender
from utils.file_handler import FileHandler
from config.settings import Settings
import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import logging

# Ensure the script can find the local modules
import sys
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))


class BulkEmailApp:
    def __init__(self, master):
        self.master = master
        master.title("Bulk Email Sender")
        master.geometry("600x700")

        self.file_handler = FileHandler()
        self.email_sender = EmailSender()

        self._create_widgets()

    def _create_widgets(self):
        # Email Composition Frame
        email_frame = ttk.LabelFrame(self.master, text="Email Composition")
        email_frame.pack(padx=10, pady=10, fill='both', expand=True)

        ttk.Label(email_frame, text="Recipient List (CSV/Excel):").pack()
        ttk.Button(email_frame, text="Load Recipients",
                   command=self._load_recipients).pack()

        self.recipients_listbox = tk.Listbox(email_frame, height=5)
        self.recipients_listbox.pack(fill='x', padx=10, pady=5)

        ttk.Label(email_frame, text="Subject:").pack()
        self.subject_entry = ttk.Entry(email_frame, width=50)
        self.subject_entry.pack()

        ttk.Label(
            email_frame, text="Email Body (use {{name}} for personalization):").pack()
        self.body_text = tk.Text(email_frame, height=10, width=50)
        self.body_text.pack()

        ttk.Button(self.master, text="Send Bulk Emails",
                   command=self._send_bulk_emails).pack(pady=10)

    def _load_recipients(self):
        try:
            file_path = filedialog.askopenfilename(
                filetypes=[("CSV files", "*.csv"),
                           ("Excel files", "*.xlsx *.xls")]
            )
            if file_path:
                self.recipients = self.file_handler.load_recipients(file_path)

                # Clear existing listbox
                self.recipients_listbox.delete(0, tk.END)

                # Populate listbox with emails
                for recipient in self.recipients:
                    self.recipients_listbox.insert(tk.END, recipient['email'])

                messagebox.showinfo("Success", f"Loaded {
                                    len(self.recipients)} recipients")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def _send_bulk_emails(self):
        try:
            # Validate inputs
            if not hasattr(self, 'recipients'):
                raise ValueError("Please load recipients first")

            subject = self.subject_entry.get()
            body_template = self.body_text.get("1.0", tk.END).strip()

            if not subject or not body_template:
                raise ValueError("Subject and email body are required")

            # Send emails
            successful, failed = self.email_sender.send_bulk_emails(
                recipients=self.recipients,
                subject=subject,
                template=body_template
            )

            messagebox.showinfo(
                "Bulk Email Results",
                f"Emails sent successfully: {successful}\n"
                f"Emails failed: {failed}"
            )

        except Exception as e:
            messagebox.showerror("Error", str(e))


def main():
    # Configure logging
    logging.basicConfig(
        filename=Settings.LOG_FILE,
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s: %(message)s'
    )

    # Check configuration
    config_errors = Settings.validate()
    if config_errors:
        print("Configuration Errors:")
        for error in config_errors:
            print(f"- {error}")
        return

    # Launch GUI
    root = tk.Tk()
    app = BulkEmailApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
