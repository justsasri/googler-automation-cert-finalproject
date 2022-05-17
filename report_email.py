#!/usr/bin/env python3

import datetime
import emails
import os
import reports
import run


def main():
  data = run.generate_data()
  today = datetime.datetime.now().strftime("%mm %d, %Y")
  report_title = "Processed Update on {}".format(today)
  attachment_file = "/tmp/processed.pdf"
  reports.generate_report(attachment_file, report_title, "This is all my fruit.", data,)
  
  sender = "sender@example.com"
  receiver = "{}@example.com".format(os.environ.get('USER'))
  subject = "Upload Completed - Online Fruit Store"
  body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."

  message = emails.generate(sender, receiver, subject, body, attachment_file)
  emails.send(message)

if __name__ == "__main__":
  main()