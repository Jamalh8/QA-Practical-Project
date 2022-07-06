# QA-Practical-Project

## Table of content 

[Project Introduction](#Project-Introduction)

[Application Idea and Design](#Application-Idea-and-Design)

[Project tracking](#Project-tracking)

[Risk assesment](#Risk-assesment)

[Unit Test](#Unit-Test)

[Application Overview](#Application-Overview)

[Ansible Playbook](#Ansible-Playbook)

[CICD Pipeline](#CICD-Pipeline)

[Known application issues](#Known-application-issues)

[Challenges faced](#Challenges-faced)

[Future Improvements](#Future-Improvements)

[Conclusion](#Conclusion)

[Credits](#Credits)

### Project Introduction
___
The minimum requirements of the project are as follows:

- An Asana board (or equivalent Kanban board tech) with full expansion on tasks needed to complete the project.
- This could also provide a record of any issues or risks that you faced creating your project.
- Jenkins Webhooks should be used to recreates and redeploys any changes made to the application.
- The project must follow Service-oriented architecture.
- The project must be deployed using containerisation and an orchestration tool.
- Use an Ansible Playbook that will provision the environment that your application needs to run.
- The project must make use of a reverse proxy to make your application accessible to the user.

### Application Idea and Design
___
**Requirements** 

>To create a service-orientated architecture for my application, this application must be composed of at least 4 services that work together.
___

#### Idea

Based on the requirements I came up with the idea to create a Formula 1 rating generator.

`Service 1`
> This will interact and provide rating output to the user. The rating output will be aquired from the information on Service 4. 

`Service 2`
> Generate a random pick of drivers from a list.

`Service 3`
> Generate a random pick of cars from a list.

`Service 4`
> Take in the output from Service 2 and 3 and calcualte their ratings based on the car and driver that was generated.

`Service 5`
> Nginx reverse proxy

#### Design

Once I was commit to my idea, I started to work on the design of the application that it'd like the fron end user to see. I decided to go with a very simple design for the front end. 

The information that will be provided are
- The random driver that was generated.
- The random car that was generated.
- The final rating output.
- A button that user can click to generate a new set of random driver,car, and ratings.

A visual design of the application front end can be seen below. 

<p><img src="https://github.com/Jamalh8/QA-Practical-Project/blob/feature/jenkinsfile/images_and_diagram/Application-design.png" alt="test" width="1000" height="450"></p>

### Project tracking
___

**Requirements** 

> An Asana board (or equivalent Kanban board tech) with full expansion on tasks needed to complete the project.
___

To meet the requirements I used Trello for my project tracking. I assigned tasks that were required to meet the acceptance criteria of this project.

MoSCoW prioritisation was used and this dictated the tasks that were put into the sprint backlog. A visual of my Trello board can be down below to help understand this. 

<p><img src="https://github.com/Jamalh8/QA-Practical-Project/blob/feature/jenkinsfile/images_and_diagram/Trello-%20In%20progress.png" alt="test" width="1000" height="450"></p>

You can view my trello board directly by clicking [here](https://trello.com/b/r4G0troy/qa-practical-proj).

### Risk assesment
___

A short risk assesment was carried out prior to the start of this project. I indentfied some possible risks that may occur along the way, the probability of this happening, the impact this will have, and how I can mitigate these.

I used [this risk assesment matrix](https://www.researchgate.net/profile/Gulsum-Kaya/publication/323570642/figure/fig7/AS:625770716217345@1526206773610/A-standard-risk-matrix.png) to help me carry out the assesment. 

<p><img src="https://github.com/Jamalh8/QA-Practical-Project/blob/feature/ansible/images_and_diagram/risk-assesment.png" alt="test" width="1250" height="275"></p>

### Unit Test
___

>Unit tests were carried out against 4 of my services. Separate tests were created for the front-end, car-api, driver-api, and rating-api. To further automate testing, rather than going into each directory to run the tests, I ran these through the `test.sh` script. This script would loop through the specified directories, install the dependencies to run the tests, and run these tests. Once the tests are complete it would provide a html coverage report.

The images below shows the results of the tests that were ran against the 4 services.

`Front-end test`

<p><img src="https://github.com/Jamalh8/QA-Practical-Project/blob/feature/jenkinsfile/images_and_diagram/test-front.png" alt="test" width="1000" height="450"></p>

`Car-api test`

<p><img src="https://github.com/Jamalh8/QA-Practical-Project/blob/feature/jenkinsfile/images_and_diagram/test-car.png" alt="test" width="1000" height="450"></p>

`Driver-api test`

<p><img src="https://github.com/Jamalh8/QA-Practical-Project/blob/feature/jenkinsfile/images_and_diagram/test-driver.png" alt="test" width="1000" height="450"></p>

`Rating-api test`

<p><img src="https://github.com/Jamalh8/QA-Practical-Project/blob/feature/jenkinsfile/images_and_diagram/test-rating.png" alt="test" width="1000" height="450"></p>

### Application Overview
___

This section will very briefly give a quick overview of the application itself.

***Home Page***

The user will be greeted with the below home page. There will be no information displayed until the 'generate' button is clicked.

<p><img src="https://github.com/Jamalh8/QA-Practical-Project/blob/feature/jenkinsfile/images_and_diagram/app-home.png" alt="test" width="1000" height="450"></p>

***Generate***

When the user clicks the 'generate' button, their randomly generated driver and car will be shown along with the ratings they recieved. The ratings is based on the driver and car that was generated.

<p><img src="https://github.com/Jamalh8/QA-Practical-Project/blob/feature/jenkinsfile/images_and_diagram/app-generate-1.png" alt="test" width="1000" height="450"></p>

***Second Generate***

If the user clicks 'generate' again, another set of random driver and car is generated along with the ratings based on the newly generated driver and car.

<p><img src="https://github.com/Jamalh8/QA-Practical-Project/blob/feature/jenkinsfile/images_and_diagram/app-generate-2.png" alt="test" width="1000" height="450"></p>

### Ansible Playbook
___

Ansible was used to configure and install dependencies on the VM's that will deploy my application. This was done through the use of roles and an ansible-playbook. 

Ansible was used for the following tasks:
- Install docker onto `swarm-manager` `swarm-worker` and `nginx-lb` VM.
- Initiate a swarm on `swarm-manager` and get `swarm-worker` to join the swarm.
- Copy over my nginx config and nginx load balancer script to my `nginx-lb` VM.

***First Playbook***

On my first playbook run I installed docker onto my `swarm-manager` and `swarm-worker` VM. The below image will show the result of this.

<p><img src="https://github.com/Jamalh8/QA-Practical-Project/blob/feature/ansible/images_and_diagram/ansible-playbook-install-docker.png" alt="test" width="1000" height="450"></p>

I ran the playbook again to confirm that everything has been installed correctly. The below image will show the result of this.

<p><img src="https://github.com/Jamalh8/QA-Practical-Project/blob/feature/ansible/images_and_diagram/ansible-playbook-install-docker-after.png" alt="test" width="1000" height="450"></p>

***Extended Playbook***

Once I successfully implemented my playbook to install docker onto both my `swarm-manager` and `swarm-worker` VM, I extended the playbook.

The extension included:
- Install docker onto `nginx-lb` VM.
- Initialise a swarm on `swarm-manager` VM and have the `swarm-worker` join.

The below image shows my first run of this extended playbook.

<p><img src="https://github.com/Jamalh8/QA-Practical-Project/blob/feature/ansible/images_and_diagram/ansible-playbook-install-before.png" alt="test" width="1000" height="800"></p>

Once again I ran the extended playbook again to ensure that all changes have been implemented.

<p><img src="https://github.com/Jamalh8/QA-Practical-Project/blob/feature/ansible/images_and_diagram/ansible-playbook-install-after.png" alt="test" width="1000" height="800"></p>

---

To confirm that these changes have been implemented, I checked all 3 VM's for docker. The below images will show you how I started off with no docker installed and then those VM's having docker installed via the playbook.

***swarm-manager VM***

<p><img src="https://github.com/Jamalh8/QA-Practical-Project/blob/feature/ansible/images_and_diagram/swarm-manager-after-docker.png" alt="test" width="1000" height="450"></p>

***swarm-worker VM***

<p><img src="https://github.com/Jamalh8/QA-Practical-Project/blob/feature/ansible/images_and_diagram/swarm-worker-after-docker.png" alt="test" width="1000" height="450"></p>

***nginx-lb VM***

<p><img src="https://github.com/Jamalh8/QA-Practical-Project/blob/feature/ansible/images_and_diagram/nginx-lb-after-docker.png" alt="test" width="1000" height="450"></p>

Upon success of my playbook I implemented Ansible with Jenkins to automate this process. This section will be better explained in the next section of CI/CD Pipeline.

### CICD Pipeline
___

`Project Tracking`
> As mentioned previously a Trello Board used for my project tracking software. I used this to organision my workload and set myself goals to deliver the application by deadline.

`Version Control`
> Git was used as the version control for my project.

`Version Control System`
> GitHub was used as my version control system as this intergrates with my Version Control. 
> Several feature branch were used to ensure that a stable version of the application is available for use.

`Development Environment`
> My development environment was an Ubuntu 20.04 LTS virtual machine (VM) hosted on Google Cloud Platform (GCP). I used SSH to connect my Visual Studio code to the GCP VM where I developed my application. 

`CI/CD Server`
> Jenkins was used as the CI/CD server as my automation environment. 
> A GitHub webhook was intergrated with Jenkins. This allows Jenkins to automatically test, build, push docker images, and deploy my application anytime I make changes to it.
> Separate tests were created for all services except Nginx service. In order to make ease of automation a script called `test.sh` was written so that each services are tested reccursively 

`Containerisation`
> Docker was used as my containerisation tool. There are many advantages to containeration my application. Using containers can create predictable environments that are isolated from other apps. We can have a cost-effective and a speedy deployment. I can also roll back to a previous of my application by using a different image. There are just a few advantages of containerising my application.

`Ansible`
> Ansible was used as my configuration management tool. As mentioned previously, I used this to configure and set up my deployment VM's.

***Pipeline Diagram***

To help understand the flow of my CI/CD, and how automation was implemented, a diagram is shown below to explain this.



### Challenges faced
___

There were several difficulties I face during this project. I'll be noting the 3 most difficult ones below.

***1. Creating the ansible playbook.***

This was a new tool that I've not used before and had to learn this from scratch. I was lucky enough to have been taught the basics of ansible by my tutors. This provided me with the platform to build upon and take the step into the unknown and try something new. I learnt to use ansible-doc and ansible-galaxy to find the relevant information required to create my playbook. 

I had several playbook failures during this project. However, it was a great learning process as it helped understand the issues and research how I can correct these.

***2. Creating a successful Jenkins Pipeline.***

A Jenkins pipeline job was another section that I've not used before. Although I used Jenkins in the past I only used freestyle to do my automation.

I had several build failures. The below image will show that I had 130 build failures before I finally got the automation to work as intended.

<p><img src="https://github.com/Jamalh8/QA-Practical-Project/blob/feature/ansible/images_and_diagram/jenkins-builds.png" alt="test" width="500" height="450"></p>

The most difficult part of the pipeline for me was to implement Ansible, build and push new images to dockerhub, and deploy to the swarm. I stayed resilient and kept trying. In the end I was rewarded with a working pipeline that automated my testing, infastructure and dependecies installation, building and pushing images to dockerhub, and deploying the application. 

***3.Building of several Micro-services***

I have used Flask to build a single web application in the past but this was my first time dipping my toes into micro-services that communicate with each other. Once again, I was lucky to have tutors that gave me the basic knowledge to create my own micro-services application. 

Most noteably, the difficult part of this section was to obtain the random information from service 2 and 3 and use service 4 to provide a logical output. 

### Future Improvements
___

### Conclusion
___

### Credits
___

I'd like to thank Leon, Adam, and Earl for their support in helping me deliver this project.
