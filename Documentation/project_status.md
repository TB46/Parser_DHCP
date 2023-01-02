
<img src="atu.jpg" width="100%">

# Infrastructure as Code Assignment 1 #
## Project Status ##
The aim of the project **'DHCP Logfile Parser'** is to create a basic Python program to process a series of DHCP logs in a logfile taken from a *production* Ubuntu server, in order to identify the devices on a client and CCTV networks.

Each log is in the following format:<div align = "center"><font size = "1">Oct 20 15:25:01 dns1 dhcpd[1838]: DHCPACK on 192.168.5.168 to c8:4b:d6:0a:77:2d (A-76MRRL3) via eth0</font></div>

The log records that a node called A-76MRRRL3 with a MAC address of c8:4b:d6:0a:77:2d was assigned an IP address of 192.168.5.168.

The program will identify each unique node/device on the network and write the details to a file called **Nodes.csv**

This project is not fully complete based on the specification in the project readme file.

The prototype works and does extract the required information, however the manner in which this is done may be less than efficient.

## Methodology ##
Each log is parsed and processed to extract the following fields of data which are of interest:
1. IPv4 address 
2. MAC address 
3. Node name
4. OUI OEM

The required data fields can be extracted and the MAC addresses examined. An inspection of the MAC address will reveal the Organisational Unique Identifier (OUI) code which in turn can reveal the identity of the Original Equipment Manufacturer (OEM).

A database at [MAC Address Vendor Lookup](https://macaddress.io/) holds information on all MAC Addresses.

## How OUI works ## 
An Organisationally Unique Identifier (OUI) is a 24-bit number that uniquely identifies a vendor or manufacturer of a piece of equipment. They are purchased from the Institute of Electrical and Engineers (IEEE) Registration Authority. The OUI is combined with another 24-bit number to form a Media Access Control (MAC) address. The first three octets of a MAC address are the OUI.

## Program Structure ##
The code is stored in a modular fashion with various directories containing functions necessary for the program to run correctly. This directory structure was created using a batch file to automate the process.

The root directory is DHCP_logfile_parser. This contains the other directories, the main.py code and a readme document. The final Nodes.csv docuemnt writes out to this directory.

The sub-directories are:
1. Documentation - Information on the project and status
2. MAC - Contains list of known OUI data to compare against
3. Unprocessed - Contains the unprocessed DHCP log files
4. Processed - The processed log files are written here
5. Utilities - Contains the functions necessary to parse the data and write out the results
6. Project_tests - Contains unit testing scripts



## Project Limitations ##
Unit testing scripts that have been written do not run correctly. These are currrently under review.

## Conclusion ##
It would be more efficient to filter out the duplicate results and write them directly to the Nodes.csv file rather than writing them all to an Output file and then filtering to the Nodes file. An effective means to achieve this is being considered.












