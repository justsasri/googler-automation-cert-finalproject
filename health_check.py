#!/usr/bin/env python3

from cmath import exp
import logging
import os
import sys
import psutil
import shutil
import requests
import emails

def send_email(title):
  sender = "sender@example.com"
  receiver = "{}@example.com".format(os.environ.get('USER'))
  subject = title
  message = emails.generate(sender, receiver, subject, title + "\nPlease check your system and resolve the issue as soon as possible.")
  emails.send(message)

def check_cpu():
    """ Report an error if CPU usage is over 80% """
    cpu = psutil.cpu_percent()
    if cpu >= 80:
        send_email("Error - CPU usage is over 80%")
    print("Checking CPU: {:.2f}%".format(cpu))

def check_avalable_disk():
    """ Report an error if available disk space is lower than 20% """
    available_dist = psutil.disk_usage('/')
    if available_dist.percent <= 20:
        current = available_dist.percent
        send_email("Error - CPU usage is over 80%")
    print("Checking Disk: {:.2f}%".format(current))

def check_memory():
    """ Report an error if available memory is less than 500MB """
    mem = psutil.virtual_memory()
    mem_in_mega = mem.free / 1_000_000
    if mem.free <= mem_in_mega:
        send_email("Error - Available memory is less than 500MB")
    print("Checking RAM: {:.2f}%".format(mem_in_mega))

def check_localhost_online():
    """ Report an error if the hostname "localhost" cannot be resolved to "127.0.0.1" """
    try:
        response = requests.get("http://localhost/")
        response.status_code
    except Exception as err:
        send_email("Error - localhost cannot be resolved to 127.0.0.1")


def main():
    check_cpu()
    check_memory()
    check_avalable_disk()
    check_localhost_online()

if __name__ == "__main__":
    main()
