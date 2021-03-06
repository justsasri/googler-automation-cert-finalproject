#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

def dict_to_table(header, data):
  """Turns the data in car_data into a list of lists."""
  table_data = [header]
  table_data.append(data)
  return table_data


def generate(filename, title, additional_info, table_data):
  styles = getSampleStyleSheet()
  report = SimpleDocTemplate(filename)
  report_title = Paragraph(title, styles["h1"])
  report_info = Paragraph(additional_info, styles["BodyText"])
  table_style = [('GRID', (0,0), (-1,-1), 1, colors.black),
                ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
                ('ALIGN', (0,0), (-1,-1), 'CENTER')]
  report_table = Table(data=table_data, style=table_style, hAlign="LEFT")
  empty_line = Spacer(1,20)
  report.build([report_title, empty_line, report_info, empty_line, report_table])


def generate_report(filename, title, additional_info, table_data):
  styles = getSampleStyleSheet()
  report = SimpleDocTemplate(filename)
  report_title = Paragraph(title, styles["h1"])
  report_info = Paragraph(additional_info, styles["BodyText"])
  empty_line = Spacer(1,20)
  items = []
  for item in table_data:
    items.append(Paragraph("Name: " + item["name"], styles["BodyText"]))
    items.append(Paragraph("Weight: " + item["weight"] + " lbs", styles["BodyText"]))
    items.append(empty_line)
  report.build([report_title, empty_line, report_info, empty_line, *items])