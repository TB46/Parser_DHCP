# Infrastructure as Code - Assignment 1 #
## DHCP Logfile Parser ##
The aim of this project is to create a simple Python program to process a series of logfiles for DHCP logs from a *production* Ubuntu server, to enable identification of the devices on a client (192.168.5.0/24) and CCTV (192.168.12.0/24) networks.

One hundred lines have been extracted from the DHCP server log. The logs are in the following format:<div align = "center"><font size = "1">Oct 20 15:25:01 dns1 dhcpd[1838]: DHCPACK on 192.168.5.168 to c8:4b:d6:0a:77:2d (A-76MRRL3) via eth0</font></div>                                            
    
The log records that a node called A-76MRRRL3 with a MAC address of c8:4b:d6:0a:77:2d was assigned an IP address of 192.168.5.168.

Each log is parsed and processed to extract the following fields of data which are of interest:
| No | Item | Description |
| ----- | --------| --------|
|1|IPv4 address |Internet protocol address|
|2|MAC address | Media access control address|
|3|Node name|Device attached to network
|4| OUI OEM| Organisational Unique Identifier Original equipent manufacturer|

The required data fields can be extracted and the MAC addresses examined. An inspection of the MAC address will reveal the Organisational Unique Identifier (OUI) code which in turn can reveal the identity of the equipment manufacturer.

A database at [MAC Address Vendor Lookup](https://macaddress.io/) holds information on all MAC Addresses.

The program will identify each unique node/device on the network and write the details to a file called **Nodes.csv**






`


