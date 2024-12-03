import smtplib
import openpyxl
from tkinter import Tk, Label, Entry, Button, messagebox, Text
from tkinter import ttk
from msal import PublicClientApplication


class EmailService:
    def __init__(self, smtp_server, sender_email, sender_password):
        self.smtp_server = smtp_server
        self.sender_email = sender_email
        self.sender_password = sender_password

    def send_email(self, receiver_email, subject, body):
        message = f"Subject: {subject}\n\n{body}"
        with smtplib.SMTP(self.smtp_server, 587) as server:
            server.starttls()
            server.login(self.sender_email, self.sender_password, initial_response_ok=True)
            server.sendmail(self.sender_email, receiver_email, message)

    def send_emails_from_spreadsheet(self, filename, sheet_name, subject, body_template):
        workbook = openpyxl.load_workbook(filename)
        sheet = workbook[sheet_name]
        max_row = sheet.max_row

        for row in range(2, max_row + 1):
            receiver_email = sheet[f'A{row}'].value
            name = sheet[f'B{row}'].value
            college = sheet[f'C{row}'].value
            personalized_body = body_template.replace("[name]", str(name)).replace("[college]", str(college))
            self.send_email(receiver_email, subject, personalized_body)


class EmailServiceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Email Service")
        self.root.geometry('400x500')

        # Create labels and entry fields for each input
        self.create_label_and_combobox("File Name", ["Basketball.xlsx", "Rugby.xlsx", "Football.xlsx"])
        self.create_label_and_entry("Sheet Name")
        self.create_label_and_entry("Sender Email")
        self.create_label_and_entry("Sender Password")
        self.create_label_and_entry("Subject")
        self.create_label_and_textbox("Body Template")

        send_email_button = Button(self.root, text="Send Emails", command=self.send_emails)
        send_email_button.pack()

    def create_label_and_entry(self, text):
        label = Label(self.root, text=text)
        label.pack()
        entry = Entry(self.root)
        entry.pack()
        setattr(self, f"{text.lower().replace(' ', '_')}Entry", entry)

    def create_label_and_combobox(self, text, values):
        label = Label(self.root, text=text)
        label.pack()
        combobox = ttk.Combobox(self.root, state="readonly", values=values)
        combobox.pack()
        setattr(self, f"{text.lower().replace(' ', '_')}Combobox", combobox)

    def create_label_and_textbox(self, text):
        label = Label(self.root, text=text)
        label.pack()
        textbox = Text(self.root, height=10, width=30)
        textbox.pack()
        setattr(self, f"{text.lower().replace(' ', '_')}Textbox", textbox)

    def send_emails(self):
        filename = self.file_nameCombobox.get()
        sheet_name = self.sheet_nameEntry.get()
        sender_email = self.sender_emailEntry.get()
        sender_password = self.sender_passwordEntry.get()
        subject = self.subjectEntry.get()
        body_template = self.body_templateTextbox.get("1.0", "end-1c")
        smtp_server = "smtp.outlook.com"
        email_service = EmailService(smtp_server, sender_email, sender_password)
        email_service.send_emails_from_spreadsheet(filename, sheet_name, subject, body_template)
        messagebox.showinfo("Success", "Emails sent successfully!")


if __name__ == "__main__":
    root = Tk()
    app = EmailServiceApp(root)
    root.mainloop()
