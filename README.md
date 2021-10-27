# Module_3_Election_Analysis
Module 3 (Python) Election Analysis

# Overview of Election Audit

This election audit was performed in order to succintly provide an analysis of turnout and results to a Colorado Board of Elections. Using the programming language Python, this audit has sorted through election data from Arapahoe, Denver, and Jefferson counties and provided a clear summation of the election's outcome.

# Election Audit Results

- In total, 369,711 votes were cast in the election between the counties of Arapahoe, Denver, and Jefferson. The code below illustrates how this tally was determined: by opening the data file, skipping the header row, and counting the number of rows in the file (each row corresponds to one vote):

![Q1](https://user-images.githubusercontent.com/91569387/139002011-4b4dc2e4-d220-4013-a4c2-09e7977c4449.PNG)

- Breakdown of votes by county:
  - Arapahoe county received 24,801 votes (6.7% of the total votes)
  - Denver county received 306,055 votes (82.8% of the total votes)
  - Jefferson county received 38,855 votes (10.5% of the total votes)

  These calculations were made using the following code, which for each vote determines the county and tallies the three separate vote totals:
  
  ![Q2 1](https://user-images.githubusercontent.com/91569387/139002988-c63be492-735b-40ee-b5c7-a8d841e97eb6.PNG)
  
  This code is used to calculate the county vote tallies as a percentage of the total vote:

  ![Q2 2](https://user-images.githubusercontent.com/91569387/139002999-8d7970e8-cc2f-4b13-9ab4-b488c5174c4b.PNG)

- Denver County had the largest voter turnout with 306,055 votes. The code below is used to determine which county had the largest turnout:

  ![Q3](https://user-images.githubusercontent.com/91569387/139003195-4291cd7b-c8f0-4d8d-b2fa-1ab4f538717e.PNG)

- Breakdown of votes by candidate:
  - Charles Casper Stockham received 85,213 votes (23.0% of the total votes)
  - Diana DeGette received 272,892 votes (73.8% of the total votes)
  - Raymon Anthony Doane received 11,606 votes (3.1% of the total votes)

  These calculations were made using the following code, which for each vote determines the candidate and tallies the three separate vote totals:
  
  ![Q4 1](https://user-images.githubusercontent.com/91569387/139003829-d560f020-90f6-4cb0-b98b-57d9de86c0f7.PNG)
  
  This code is used to calculate the candidate vote tallies as a percentage of the total vote:

  ![Q4 2](https://user-images.githubusercontent.com/91569387/139003846-5991c47d-5de1-4f5f-9ccb-ac7f68da6ee5.PNG)
  
- With a total of 272,892 votes and 73.8%, Diana DeGette won the election. The following code is used to determine the winning candidate:
    
  ![Q5](https://user-images.githubusercontent.com/91569387/139004232-2ddb3fd3-b7ca-48c5-9a1f-3b3ef7d86e97.PNG)
  
 # Election Audit Summary
  
With only minor modifications, this basic script can be applied to function in a wide variety of electoral scenarios. The only major change neccesary would be to alter the imported data file. From there, the script can be altered to fit different needs in accordance with different data files. Care must be taken to make sure the code draws from the correct columns and rows of a data set, as the structure of the file may not be identical to this example. Additionally, terminology throughout the script can be adapted, whether it be states or municipalities rather than counties or other such variations. Generally though, this script should be able to provide outcomes for many different scenarios.

