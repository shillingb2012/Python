# string concatenation 
# Input the name of the company and position title to input into the cover letter
from datetime import datetime
import calendar

company = input("What is the name of company? ")
position = input("What is the position? ")

currentDate = datetime.now()

dateFormatted = f"{currentDate.day} {calendar.month_name[currentDate.month]} {currentDate.year}"

content = f"The purpose of this letter is to express my interest in the {position} position at {company}. I believe I would be a great fit for the role due to my background and experience in software development, business analytics, and problem solving. I’d be able to perform the {position} role at a high level and be ready to contribute to the team right away.\n\nBased on my prior work and interests, I have the necessary, all-around experience for the role. At my current job with MG&E, I frequently create and update SQL queries to use in PowerBI to provide analytics and dashboards for operational managers. Additionally, I have experience using Power Automate to achieve routine, scheduled reporting extracts. Before MG&E, I was at Exact Sciences where I was a subject matter expert in software for automatic pipetting instruments used for chemical assays. While at Exact Sciences, I wrote a .NET application to streamline and reliably set up automation equipment for internal R&D scientists at multiple laboratory sites. This project, as well as others, involved the entire software lifecycle such as documenting user requirements, designing the application, creating tests for validation, and deploying. With these experiences, as well as prior roles in technical support, I believe I would do well in the {position} role.\n\nBesides work, I have a strong interest in continuing to develop and learn, especially frontend technologies. I’ve completed several courses in HTML, CSS, React, Javascript, REST APIs, and Node, and I have personal experience with website creation and management. In each of my prior positions as well as my life, I’ve shown a consistent energy for learning and building upon my skills, which I plan to continue at Promega.\n\nWith my background in software engineering, technical support, and analytics, I know I’d perform well in the role and completely enjoy the work. I look forward to hearing more about this great opportunity in the near future. Thank you for taking the time to review my application.\n\nBest,\nBrock Shilling"

print(f"{dateFormatted}\n\n{company}\n\n{content}")
