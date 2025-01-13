# 1. Introduction
  Employee performance is a critical factor in the success of any organization.
   It directly impacts productivity, employee satisfaction, and overall business outcomes.
   Managing and tracking performance reviews manually can be inefficient, prone to errors, and time-consuming.
   To address this challenge, Employee Performance Review System is designed as a comprehensive web-based platform
   that streamlines the process of evaluating employee performance, setting professional development goals, and generating insights through analytics.

  This system aims to create a transparent and organized approach to performance management, benefiting both employers and employees.
  It provides a user-friendly interface for employees to access feedback, track progress, and engage in self-assessment.
  For admins and managers, it simplifies the process of reviewing performance, setting goals, and generating detailed reports.

# 2. Features
## User Review Dashboard:
  A personalized dashboard for office workers and interns to view their performance reviews, feedback from managers, and assigned goals.
  Enables users progress updates, fostering personal accountability.

## Admin/Manager Review Panel:
  Centralized panel for managers to create and edit performance reviews for employees and interns.
  Provides feedback on various metrics such as productivity, punctuality, collaboration, and goal achievement.
  Facilitates scheduling periodic reviews and sending automated reminders.
  
## Goal Setting and Tracking:
  Enables both users and managers to set professional goals (short-term and long-term).
  Tracks progress toward goals in real-time and displays updates to users and managers.
  
## Performance Metrics:
  Incorporates customizable KPIs such as attendance, task completion, and initiative, tailored to each role.
  Provides a quantifiable framework for assessing performance.
  
## Review Scheduling:
Simplifies the review process by allowing admins to schedule periodic reviews.
Sends automated reminders to employees and reviewers about upcoming evaluations.
  
## Performance Analytics:  
  Generates visual reports (graphs, tables) that highlight trends, areas for improvement, and top-performing employees.
  Provides export options for reports in PDF and Excel formats.
  
## 3. Problem Scenario
Managing employee performance manually can lead to several challenges:
Inefficiency: Paper-based or spreadsheet-based performance reviews can be time-consuming and error-prone.
Lack of Transparency: Employees may not have a clear view of their goals, feedback, or progress, leading to disengagement.
Inconsistent Evaluation: Without a structured system, performance evaluations may lack standardization, causing bias or inconsistency.
Missed Opportunities for Development: Absence of real-time tracking and reminders can delay feedback and goal completion.
Limited Insights: Manually analyzing performance data is cumbersome and can result in missed trends or opportunities for improvement.
The Employee Performance Review System addresses these issues by digitizing and automating the performance management process.
It ensures transparency, consistency, and efficiency, fostering a culture of continuous improvement within the organization.

# 4. Requirements
## Functional Requirements:
  Role-based access for employees, interns, managers, and admins.
  User dashboards for employees and interns with personalized performance data.
  Manager dashboards for Manager with personalized performance data.
  Review creation, editing, and scheduling capabilities for managers and admins.
  Goal Creation for Interns progress updates.

## Non-Functional Requirements:
  Scalability: Support multiple users concurrently as the organization grows.
  Security: Ensure data privacy through role-based access control and secure storage of sensitive information.
  Usability: Provide a responsive and intuitive interface for all user roles.
  Performance: Optimize the system to handle real-time updates and analytics without delays.
  Portability: Support various devices (desktops, tablets, smartphones) for ease of access.

## Technical Requirements:
Backend: Django framework for managing business logic and database interactions.
Database: PostgreSQL or SQLite for storing user data, reviews, and performance metrics.
Frontend: HTML, CSS, and JavaScript for designing user interfaces, with Bootstrap for responsiveness.

# 5. Functional Features in Detail
## For Interns:
### 1. Register
![Register](https://github.com/user-attachments/assets/b0910276-73b8-4b18-9b26-ab83f7692791)

### 2. Login
![Login](https://github.com/user-attachments/assets/87c73498-e811-44f2-87a9-eb48d9bdf927)

### 3. Dashboard
![Dashboard](https://github.com/user-attachments/assets/2079ce9f-a54f-4dde-8b30-6a7b56e233e9)
### 3.1 After clicking view detail of any individual review from performance review section of intern dashboard, The whole detail of that individual performance review will open.
![image](https://github.com/user-attachments/assets/e95c9b10-df72-4d4b-ab6c-3056ce068230)
### 3.2 Below Performance Review section in intern dashboard there is a feedback section which contain feedbacks from manager. After Clicking view button of individual feedback from the feedback section, It will open modal that will include whole Feedback givem from manager.
![image](https://github.com/user-attachments/assets/773c1464-3f68-440e-b451-8580b92b1d0f)
### 3.3 In the Goal section from intern portal there is a goal section that includes 3 individual goals assigend to the individual imtern.
![image](https://github.com/user-attachments/assets/eb97699e-bf28-424d-8753-7fa47edcf286)
###3.4 CLick View Goal History button, It will redirect to all that individual all assigned goals including pending and complete goals and aslo can set pending goals to completed.
![image](https://github.com/user-attachments/assets/aea22240-32de-4b1c-bf72-7a7f6bcb0ab1)




