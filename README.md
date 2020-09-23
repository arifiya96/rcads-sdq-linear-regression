# RCADS and SDQ linear regression: can we use data from these questionnaire completions to predict behaviour based on mood?

<b>Introduction</b>
The Revised Child Anxiety and Depression Scale (RCADS) is a 47-item, youth self-report questionnaire with subscales (Chorpita et al, 2008) and the Strengths and Difficulties Questionnaire (SDQ) is a brief emotional and behavioural screening questionnaire for children and young people. In clincial use, the RCADS is used as an outcome measure for tracking mood and the SDQ is used as an outcome measure to behaviour. If there is a linear relationship between the two, can we create a model that can predict behaviour based on mood? In this analysis, I will use the RCADS as a measure of mood and the SDQ as a measure of behaviour. The limitations of using these as a measure of mood and behaviour is mentioned below. 

<b>The Dataset</b>
The dataset is taken from the Child Wellbeing Practitioner (CWP - https://www.ucl.ac.uk/prospective-students/graduate/taught-degrees/child-young-persons-psychological-wellbeing-practice-pg-cert) and Educational Mental Health Practioner (EMHP - https://www.healthcareers.nhs.uk/explore-roles/psychological-therapies/roles-psychological-therapies/education-mental-health-practitioner) programmes. All of the data is taken from real cases that trainees worked with during their training year. These scores were used as evidence to track patient progress over time. Hopefully this reflects the ecological validity of the dataset. You can find the dataset under the 'data.json' file. 

<b>The Analysis</b>
For the detailed analysis, please see the 'rcads_sdq_linear_regression.ipynb' file. 
1. Data cleaning
2. Calculations on the dataset to get the r value parameters 
3. Create the regression model (y = mx + b)
4. Calculate accuracy (r sqaured)

<b>Running the analysis</b>
Open rcads_sdq_linear_regression.ipynb in Jupyter Notebook. To install Jupyter Notebook, I recommend installing Anaconda (https://www.anaconda.com/) which will have the Jupyter Notebook IDE. Make sure the data.json file is in the same file location as the rcads_sdq_linear_regression.ipynb. 

<b>Results</b>
The linear relationship between the RCADS total score and SDQ total score is weak (pearsons correlation coefficient value, r = 0.4). Therefore, the accuracy of the model will be quite low. In this case, only 16% of the variability in the SDQ total scores can be explained by the linear relationship with the RCADS total score. Regardless, I still created a regression model of SDQ_Score(Y) = 0.09x + 7.95.

<b>Web Interface</b>
Inspired by the work done by Asai Kentaro (https://asai-kentaro.github.io/plotshop_server/) from Tokyo University, I created a web interface where you can input a RCADS total score into the regression model and get the SDQ score as the output as well as the coordinates on the graph. Even though this is an incredibly simplified version of the work done by Asai Kentaro, this should hopefully faciliate a human computer interaction (human in the loop) design approach. You can test the web interface by running the html file offline or in a local server. 

<b>Conclusion</b>
Based on this data, mood may not be a good predictor on behaviour. However, this may indicate that RCADS and SDQ may not be good measures to use for this analysis. Some future analysis that I could do:
- Use other properties of the RCADS and SDQ rather than just the total scores (i.e. subscales)
