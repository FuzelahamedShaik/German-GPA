# German-GPA

Trend of going to european countries specifically to germany is increasing every very. This is mainly due to the quality of education and no tuition fee. While applying to german universities the grades of every student is converted into german grade system where 4 is the lowest and 1 is the highest grade.

Hence student's has no answer for "How can I convert my cgpa to german gpa?".

This is a data science application for this problem statement. There are some online converters for this for example "Technical University of Munich" has a grade converter in it's webs
So, to make it using machine learning techniques we need a data set in which we should have data for maximum and minimum grade that can be scored from each university and cgpa obtained from an individual along with a respective german gpa.

I couldn't find such dataset from the online sources. Hence I have created my own dataset with 200 observations in it and 5 features (Name of university/college, Max.Cgpa, Min. Cgpa, Grade Obtained and Converted GPA). 

After performing the training and testing of the data using different regression algorithms I found RandomForestRegressor has a training accuracy of 99.3%(nearly) and a testing accuracy of 98.6%(nearly). The code was uploaded here.

The web application was developed using flask frame work. These code is also uploaded here in this repository.
