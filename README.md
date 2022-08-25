# 2022 Formula 1 Analysis

## Project Summary
With half of the 2022 Formula 1 season completed and all the race data freely available on the Formula 1 website, we as a team thought it'd be a great capstone project to create a flask webapp that scrapes the 13 races worth of data, cleans it, inserts it into a MongoDB, and displays it to be viewed. Once completed, we took the dataset and fit it to a LightGBM model to see what results we could get. Take a look below for our findings!

## Resources
- Data Source: master_1.csv (scraped from the web)
- Software: Python 3.7, Tableau
- IDEs: Jupyter Notebook, Visual Studio Code
- Main Packages Used: Pandas, Splinter, BeautifulSoup, Flask, Flask_PyMongo, LightGBM, Scikit-Learn

## How To Run Flask App
  - Install required packages
  - If using FireFox, no editing of the scraping.py file is required, but if using another browser, you will need to change the webdriver_manager package (lines 6, 14, 15)
  - If you're using an env, make sure to activate the env you installed the packages in
  - Run mongo database instance by typing `mongod` in terminal. You may have to specify the mongodb path with `mongod --dbpath PATH_NAME`
  - Run `mongo` in another terminal tab
  - With mongo active, enter `use f1_app`
  - In your Flask app.py path, enter `flask run`
  - The app should run on http://127.0.0.1:5000/
  - Once the "Scrape New Data" button has been clicked, the program will take a minute or two to display the table of data

## Topic:
### F1 Racing
![GettyImages-1239881348](https://user-images.githubusercontent.com/101272613/184259961-96f2065a-4841-4681-b628-a482d259631d.jpg)

## Reason why they selected their topic:
### Interesting sport due to many strategies to be a WCC/WDC. 
![image2](https://user-images.githubusercontent.com/101272613/184259890-a0c3cd00-d7b7-4092-ab1c-eb609ca8cbb7.jpg)

## Description of their source of data: 
### Extracting from their website by web-scraping.
![Image1](https://user-images.githubusercontent.com/101272613/184259797-4b496577-4cbd-4957-bdef-3f2ec329c597.PNG)

## Questions they hope to answer with the data: 
### Stats data to drive which features make up the top drivers/constructors. Using the features to predict which driver/constructors will be the top 3. 
![image0](https://user-images.githubusercontent.com/101272613/184259791-09daca79-e767-4ae2-ac07-23648d37b0f2.PNG)

## Data Extraction: HTML Webscraping
### Pulling data from F1 website with webscraping and dependencies: Beautifulsoup, GeckoDriverManager, StaleElementReferenceException

![image](https://user-images.githubusercontent.com/101272613/185523289-1b70c4ba-8f56-4662-a293-42231f4648e3.png)
![image](https://user-images.githubusercontent.com/101272613/185523417-549419fa-f287-452d-8ec9-f0b4d71a2d21.png)
![image](https://user-images.githubusercontent.com/101272613/185523500-00a3f8c8-80eb-49a7-88dd-c3f6842cfeb6.png)

## Transform and Cleaning Data
### Cleaning the extracted data with pandas and numpy.
![image](https://user-images.githubusercontent.com/101272613/185523798-664f7072-96d7-4f3a-ad6b-738230ffbf97.png)
![image](https://user-images.githubusercontent.com/101272613/185523955-281a0c90-7a50-4f00-badc-8ec6868bcd37.png)
![image](https://user-images.githubusercontent.com/101272613/185523903-cd9ed28b-4a03-4c98-87dd-03b6531235ee.png)

## Database
### Loading the Data into MongoDB
![image](https://user-images.githubusercontent.com/101272613/185524116-f8ab40b4-9e73-4b7c-bf18-a236778af574.png)
![image](https://user-images.githubusercontent.com/101272613/185524204-b72b0b93-efb9-41d6-b071-02d01bdd028a.png)

## Machine Learning
### Using lightgbm model to predict the winner for F1 season 2022.
![image](https://user-images.githubusercontent.com/101272613/185524643-8ea32b1e-cd86-4e9c-b86d-6d20d121e890.png)
![image](https://user-images.githubusercontent.com/101272613/185524689-ab5b788f-daa6-4699-b360-60b24bf7300d.png)
![image](https://user-images.githubusercontent.com/101272613/185524731-fe4c524c-ae35-4ed0-9a73-d0344e3becb6.png)

### Revision of the ML: Fixed some of the over-fitting and increased accuracy score. 
![image](https://user-images.githubusercontent.com/101272613/185822821-618bbaf0-0462-437b-9a31-1d8d0804ddf9.png)

## Visualization
### Displaying the data analysis in Tableau

![image](https://user-images.githubusercontent.com/101272613/185524367-eeaa491e-0fe2-4d7b-aba7-f70377bf1d0b.png)
![image](https://user-images.githubusercontent.com/101272613/185524485-fab6dd4e-b129-46f9-a5eb-4d5d0127a19a.png)
![image](https://user-images.githubusercontent.com/101272613/185524544-ab8a8121-999f-4ca6-a8fe-82deeb742e3a.png) 

![alt text](https://github.com//Spakicey/2022-Formula1-Analysis/blob/ajl_branch/2021%20Stops%20and%20position.png?raw=true)

This first graph shows the number of stops and how it relates to the position of finish of the driver and seperated by each race

![alt text](https://github.com/Spakicey/2022-Formula1-Analysis/blob/ajl_branch/Car%20and%20.png?raw=true)

The following pie chart represents each car type or team and the slices are representative of the Sprint times

![alt text](https://github.com/Spakicey/2022-Formula1-Analysis/blob/ajl_branch/Pit%20stop%20and%20time%20to%20Results.png?raw=true)

Hear we are looking at the Pit stops and times and how it results in the Final position of the first 10 races of the 2022 season.

![alt text](https://github.com/Spakicey/2022-Formula1-Analysis/blob/ajl_branch/Starting%20grid.png?raw=true)

Seperated by each driver looking into any coorelation between the Starting grid positon and the final positioning of each race.

![alt text](https://github.com/Spakicey/2022-Formula1-Analysis/blob/ajl_branch/Top%206%20per%20race.png?raw=true)

Finally visualization of the top 6 finishers for each race
