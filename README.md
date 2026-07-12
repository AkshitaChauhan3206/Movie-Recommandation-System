### Assignment 20: Building \& Deploying a Recommendation System



**## Student Information**



Student Name: Akshita Chauhan



Assignment Number: 20



Project Title: Content-Based Movie Recommendation System





**# Project Description**



This project builds a Content-Based Movie Recommendation System using TF-IDF Vectorization and Cosine Similarity. A Streamlit application is created to recommend similar movies based on the selected movie.





**# Dataset Information**



Dataset Name: TMDB 5000 Movie Dataset



Dataset file name : movie.csv



Dataset Source: Kaggle



Dataset Link: https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata





**# Technologies Used**



\* Python

\* Pandas

\* NumPy

\* Scikit-learn

\* Streamlit

\* Pickle





**# Project Files**



Assignment20\_Recommandation\_System

|\_\_ dataset/

&#x20;   |\_\_ movie.csv

| 

|\_\_ Assignment20\_allTask.ipynb 

| 

|\_\_ app.py                     

|\_\_ movies.csv                 

|\_\_ movies\_data.pkl            

|\_\_ similarity.pkl             

|\_\_ requirements.txt           

|\_\_ README.md                 







**# Assignment Workflow**



Step 1: Load the movie dataset using Pandas.



Step 2: Clean the movie descriptions by converting text to lowercase, removing punctuation, removing stopwords, and handling missing values.



Step 3: Convert cleaned text into numerical vectors using TF-IDF Vectorizer.



Step 4: Calculate Cosine Similarity between all movies.



Step 5: Create a recommendation function to suggest similar movies.



Step 6: Build a Streamlit application with a movie selection dropdown and recommendation button.



Step 7: Upload the project to GitHub.



Step 8: Deploy the application on Render.







**# How to Run the Notebook**



Step 1: Install Python (3.10 or later).



Step 2: Open the project folder in Visual Studio Code.



Step 3: Open \*\*Assignment20\_allTask.ipynb\*\*.



Step 4: Select the Python Interpreter.



Step 5: Run all notebook cells from top to bottom.







**# How to Run the Streamlit Application**



Step 1: Open the project folder in Visual Studio Code.



Step 2: Open the Terminal.



Step 3: Install Streamlit.



bash

pip install streamlit





Step 4: Start the application.



bash

python -m streamlit run app.py





Step 5: Wait for the browser to open automatically.



Step 6: Select a movie from the dropdown list.



Step 7: Click the \*\*Get Recommendations\*\* button.



Step 8: View the Top 5 recommended movies.







**# GitHub Commands**



Initialize Git Repository



bash

git init





Add Project Files



bash

git add .





Commit Changes



bash

git commit -m "Assignment 20 Completed"





Rename Branch



bash

git branch -M main





Connect GitHub Repository



bash

git remote add origin YOUR\_REPOSITORY\_LINK





Push Project



bash

git push -u origin main









**# Render Deployment**



Build Command:



text

pip install -r requirements.txt





Start Command:



text

streamlit run app.py --server.port=$PORT --server.address=0.0.0.0









**# Expected Output**



\* User selects a movie from the dropdown list.

\* The system calculates movie similarity.

\* Top 5 similar movies are displayed on the screen.







**# Conclusion**



This project demonstrates the complete workflow of building a Content-Based Recommendation System, creating a Streamlit web application, using GitHub for version control, and deploying the project on Render.



