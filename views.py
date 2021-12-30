#I have created this file - Shivam
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>SHIVAM RANJAN</h1>")

def resume(request):
    a ='''<h1>Shivam Ranjan</h1>
    <p><h2>Summary</h2></p>
    <hr/>
     I am a B.Tech fourth year student pursuing the field of computer science. 
     I am a Practical knowledge seeker, who is passionate about coding and solving logical problems. 
     I am an hardworking individual who excels at analyzing, and logical thinking. 
     I am highly attentive and organized person who plans and implements procedures with high quality. 
     I have computer science skills that can support an organization through innovative software development processes.
     <p>I am looking forward to effectively contribute to an organization by utilizing prior technical knowledge
     and skills to succeed in a dynamic environment of growth and excellence.</p>
      
     <p><h2>Technical Skills</h2></p>
     <hr/>
     C, Java, Python, libraries of python- numpy, matplotlib, seaborn and pandas.
     HTML, SQL in MySQL, Django, MS Excel, MS Word, MS PowerPoint.
      
     <p><h2>Education and Qualifications</h2></p>
     <hr/>
     Joginpally BR Engineering College: 
     Bachelor of Technology Computer Science – IV Year I Semester in July 2018, to present - 7.0 gpa over VI Semesters
      
     <p> PAGE Junior College(Telangana State Secondary Board): MPC, Intermediate I and II, July 2016 to April 2018 - 87%</p>
      
     <p>St. Peter’s Public School(Central Board of Secondary Education): July 2005 to July 2016 - 9.8 gpa in standard 10.</p>
     
     <p><h2>Degree Related Projects</h2></p>
     <hr/>
     <h4>Fraud Detection Using Machine Learning/AI in Microsoft Azure ML Studio JBREC, 2021:</h4>
     <p>Project Brief:
     The Fraud Detection is a Console Application to help the Banks in preventing Fraud Transactions by detecting abnormal behavior in the Transaction Dataset. 
     It was created using the Microsoft Azure Cognitive Service where the model was trained using One Class SVM Anomaly Detection Algorithm, 
     and implemented using C# code to create a Console Application that labels anomalies for the Input file.
     <p>Main Tasks:
     •	Understanding the concept of Anomaly Detection.
     •	Data Acquisition for training and testing model.
     •	Creating Microsoft Azure Workspace and storage account.
     •	Training Model by implementing One Class SVM on training dataset.
     •	Deploying Model as Web service.
     •	Implementing the URL and API through C# code to create a console application.
     •	Testing and Exception Handling</p>
     <p>Outcome:
     •	Created a Model in Azure to detect anomalies.
     •	Deployed model as web service that Request Response for single data entry and Batch Response for a dataset.
     •	Created a Console Application that reads an excel sheet and outputs the same with a new column labeling anomaly transactions, thus helping banks to prevent frauds.
     </p>
     
     <p><h2>Hobbies and Interests</h2><p>
     <hr/>
     Reading Newspaper and staying up-to-date, Reading Novels, Solving Sudoku & Puzzles, Playing Cricket, Bdminton, Lawn & Table Tennis 
     Fantasy novel critiquing.
     '''
    return HttpResponse(a)
