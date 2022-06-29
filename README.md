# QA-Practical-Project
___
## Table of content 
___
[Project Introduction](#Project-Introduction)

[Application Idea and Design](#Application-Idea-and-Design)

[Project tracking](#Project-tracking)

[Risk assesment](#Risk-assesment)

[Unit Test](#Unit-Test)

[The application](#The-application)

[CICD Pipeline](#CICD-Pipeline)

[Known application issues](#Known-application-issues)

[Challenges faced](#Challenges-faced)

[Possible future changes to application](#Possible-future-changes-to-application)

[Conclusion and learning from this project](#Conclusion-and-learning-from-this-project)

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

**Service 1**
> This will interact and provide rating output to the user. The rating output will be aquired from the information on Service 4. 

**Service 2**
> Generate a random pick of drivers from a list.

**Service 3**
> Generate a random pick of cars from a list.

**Service 4**
> Take in the output from Service 2 and 3 and calcualte their ratings based on the car and driver that was generated.

**Service 5**
> Nginx reverse proxy

#### Design

After I confirmed my idea, I started to work on the design of the application that it'd like the fron end user to see. I decided to go with a very simple design for the front end. 

The information that will be provided are
- The random driver that was generated.
- The random car that was generated.
- The final rating output.

A visual design of the application front end can be seen below. 


