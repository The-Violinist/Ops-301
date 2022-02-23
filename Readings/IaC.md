# IaC
## David Armstrong 09-15-2020

Infrastructure as code is the use of code to accomplish implementation of everything from apps to operating systems to network structures. Traditionally all of these would have required manual installation and and most likely updating or substantial configuration out of the box. With IaC, it is possible to package complete setups with OS and specific applications (all with specific builds) and use them for configuration on other machines.

This not only cuts down on installation time and accuracy, but it also makes it easier to have a uniform setup across a network by means of version control. IaC also allows for testing and making small changes frequently thereby fitting in with Agile methodology. There are many configuration and provisioning tools available for accomplishing this: Chef, Puppet, Ansible, and Salt Stack to name a few.

All of this plays into the DevOps environment with its overarching ideas of Continuous Integration (CI), Continuous delivery (CD), Continuous testing, and Continuous monitoring. Each one of these can be accomplished with IaC. DevOps as a model, with its integration of both sides of production (development and operations), brings the 2 sides together in being able to meet the goals of both.
