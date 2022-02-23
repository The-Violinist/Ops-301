# AD
## David Armstrong 09-09-2020

Active Directory is a set of 5 services that manage access and permissions to a network; the most common of these is Active Directory Domain Services (ADDS, but commonly referred to as AD). When deploying AD, the administrator must pay careful attention to 2 main areas: the physical (how will it be implemented on the physical network) and logical (consider how well the policies fit with the business structure).

At the center of AD is a server which acts as a domain controller (DC). This is where the authentication and authorization take place. One of the methods in which AD is used is the implementation of role based access control. This is done by grouping different objects or users into groups known as organizational units. An OU could be a group of users or objects based on department, job title, device type, etc. OUs are useful not only for granting access and abilities uniformly, but also for facilitating group policy updates and making management of objects efficient.
