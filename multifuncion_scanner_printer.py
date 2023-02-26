# Objectives
# Creation of abstract classes and abstract methods;
# multiple inheritance of abstract classes;
# overriding abstract methods;
# delivering multiple child classes.
#
# Scenario
# You are about to create a multifunction device (MFD) that can scan
# and print documents;
# the system consists of a scanner and a printer;
# your task is to create blueprints for it and deliver the implementations;
# create an abstract class representing a scanner that
# enforces the following methods:
#   scan_document – returns a string indicating that the document
#   has been scanned;
#   get_scanner_status – returns information about the scanner
#   (max. resolution, serial number)
#
# Create an abstract class representing a printer that enforces
# the following methods:
#    print_document – returns a string indicating that the
#    document has been printed;
#   get_printer_status – returns information about the printer
#   (max. resolution, serial number)
# Create MFD1, MFD2 and MFD3 classes that inherit the abstract
# classes responsible for scanning and printing:
#   MFD1 – should be a cheap device, made of a cheap printer and
#   a cheap scanner, so device capabilities (resolution) should be low;
#   MFD2 – should be a medium-priced device allowing additional
#   operations like printing operation history, and the resolution
#   is better than the lower-priced device;
#   MFD3 – should be a premium device allowing additional operations
#   like printing operation history and fax machine.
# Instantiate MFD1, MFD2 and MFD3 to demonstrate their abilities.
# All devices should be capable of serving generic feature sets.

import abc


class Scanner(abc.ABC):

    @abc.abstractmethod
    def scan_document(self):
        pass

    @abc.abstractmethod
    def get_scanner_status(self):
        pass


class Printer(abc.ABC):

    @abc.abstractmethod
    def print_document(self):
        pass

    @abc.abstractmethod
    def get_printer_status(self):
        pass


class Mdf1(Scanner, Printer):

    def scan_document(self):
        print("Scan successful")

    def get_scanner_status(self):
        print("Scan max resolution: {}\n\tSerial number: {}".
              format('200dpi', 2000))

    def print_document(self):
        print("Print completed")

    def get_printer_status(self):
        print("Printer max resolution: {}\n\tSerial number: {}".
              format('200dpi', 2000))


class Mdf2(Scanner, Printer):
    def scan_document(self):
        print("Scan successful")

    def get_scanner_status(self):
        print("Scan max resolution: {}\n\tSerial number: {}".
              format('400dpi', 4000))

    def print_document(self):
        print("Print completed")

    def get_printer_status(self):
        print("Printer max resolution: {}\n\tSerial number: {}".
              format('400dpi', 4000))


class Mdf3(Scanner, Printer):
    def scan_document(self):
        print("Scan successful")

    def get_scanner_status(self):
        print("Scan max resolution: {}\n\tSerial number: {}".
              format('600dpi', 6000))

    def print_document(self):
        print("Print completed")

    def get_printer_status(self):
        print("Printer max resolution: {}\n\tSerial number: {}".
              format('600dpi', 6000))

    def fax_document(self):
        print("Faxing document")

    def get_fax_status(self):
        print("Fax max resolution: {}\n\tSerial number: {}".
              format('600dpi', 6000))


scan1 = Mdf1()
scan1.print_document()
scan1.get_scanner_status()

scan2 = Mdf2()
scan2.print_document()
scan2.get_scanner_status()

scan3 = Mdf3()
scan3.print_document()
scan3.get_scanner_status()

# Outputs...
# Print completed
# Scan max resolution: 200dpi
# 	Serial number: 2000
# Print completed
# Scan max resolution: 400dpi
# 	Serial number: 4000
# Print completed
# Scan max resolution: 600dpi
# 	Serial number: 6000
#
# Process finished with exit code 0
