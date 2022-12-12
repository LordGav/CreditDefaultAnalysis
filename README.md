# Credit Default Analysis

This project is designed to help users analyze credit default data. The data set contains information on credit card clients in Taiwan in the year 2005. It includes information on the clients' credit limit, sex, education, marriage status, age, and whether they defaulted on their credit card payment the following month.

## Requirements

To run this project, you will need the following:
- Python 3.6 or higher
- The pandas library
- The streamlit library

## Getting Started

First, clone this repository to your local machine:

    git clone https://github.com/<your-username>/credit-default-analysis.git

Next, navigate to the project directory and install the required libraries:

    pip install -r requirements.txt

Now you can run the project by using the following command:

    streamlit run app.py

This will launch the streamlit app in your default web browser. You can then use the sidebar on the left side of the page to select which categories you want to see in the histogram.

## Data Preprocessing

Before the data is visualized, it is preprocessed to group the data into more useful categories. For example, the EDUCATION column is transformed to group clients into three categories: "Graduate", "University", and "High School". The LIMIT_BAL column is transformed to group clients into three categories based on their credit limit: "High", "Medium", and "Low".

## Visualization & Screenshots

Once the data is prepared, a histogram is generated to show the proportion of clients who defaulted on their credit card payment in each category. The user can use the checkboxes in the sidebar to select which categories they want to include in the histogram.

![image](https://user-images.githubusercontent.com/30123626/207043090-e374ffd3-022d-4d17-b3cc-e2e16c6fae92.png)

![image](https://user-images.githubusercontent.com/30123626/207043359-20f886e0-6caf-4fd1-8442-e96387bde125.png)

![image](https://user-images.githubusercontent.com/30123626/207043478-9c19b318-6516-44e2-9676-a47d1837b4c3.png)


## Conclusion

This project provides a simple tool for analyzing credit default data. By allowing the user to select which categories they want to see, it makes it easier to spot trends and patterns in the data. This can help credit card companies understand which groups of clients are more likely to default on their payments, which can help them make better decisions about who to approve for credit cards and what credit limits to assign.
