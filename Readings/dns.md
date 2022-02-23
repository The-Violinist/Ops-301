# What is DNS?
## David Armstrong 09-04-2020

DNS, or the domain name system, is the means by which human readable web addresses are translated into numbers which computers understand. When the Internet began addresses had to be entered in they “computer” form — IP addresses consisting of 4 sets of octets. In order to make this manageable, a system was created that mapped IP addresses to their human readable counterparts. 

These mappings were stored on nameservers. The first step is the web browser attempting to resolve the address. If it is unable, it proceeds to the resolve server (ISP), to the root server — 13 sets of servers placed around the globe. The root server directs the resolver to the top level domain server (TLD) which directs the resolver to domain specific (.com .org etc) information. The resolver finally gets directed to the authoritative name server which provides the mapping.
