# Group 06 - The effect of different lifestyle factors on human well-being

## Introduction
Our project aims to explore factors nested within five dimensions that contribute to work-life balance. Many strive to achieve an ideal work-life balance but have yet to reach them due to the multifaceted nature of work-life balance itself. One with a poor work-life balance may then be impacted by a wider range of negative outcomes, such as health and life satisfaction. By possessing a deeper understanding of this dataset, we are able to better understand how these factors interact with each other, and how to improve one’s work-life balance overall. The outcomes of this project may have the potential to develop a user-facing dashboard that provides personalized recommendations to individuals seeking to achieve a better work-life balance

<br/>

## Exploratory Data Analysis
- Most of the columns in this dataset are numeric variables, and there is no missing variable.
- However, there is one incorrectly reported value in the daily stress level column (‘1/1/00’). It needs to be dropped to prevent errors in analysis.


<br/>

## Research Question 1
### "Overall, does a healthy mind dimension help to maintain low-stress levels? If so, which factors of the healthy mind dimension are related to low-stress levels and how does it differ based on one's demographic information?"

<br/>

This section, it is to analyze the relationship between daily stress levels and the healthy mind dimension in this dataset. This research question will be analyzed into 3 parts: firstly, the relationship between daily stress level and variables in the healthy mind dimension overall, secondly, the relationship between each variable in the healthy mind dimension and daily stress level will be explored to determine the variables with the strongest association, lastly, it is to be investigated how these relationships differ based on one’s demographic information such as gender and age.

<br/>

<img src ="images/rq01_1.png">
This box plot is used to see the trend of each daily stress level (0, 1, 2, 3, 4, 5) with an overall healthy mind score. Overall healthy mind score is computed by summing the number of flow, number of weekly meditations, and number of daily shouting, while the number of daily shouting is reverse coded. This plot shows the positive relationship that as daily stress level increases, the average of weighted healthy mind scores increases. It implies that people with a healthy mind are likely to have a low-stress level.  

<br/>

<img src ="images/rq01_2.png">
The correlation matrix heat map explains the second part of my research question, the relationship between each variable in the healthy mind dimension and daily stress level. The correlation coefficient r of the relationship between daily stress level and flow is -0.13, of the relationship between daily stress level and weekly meditation is -0.22, and of the relationship between daily stress level and daily shouting is 0.3. This finding can answer the second part of my research question that the number of daily shouting has the strongest association with daily stress level.

<br/>

<img src ="images/rq01_3.png">
<img src ="images/rq01_4.png">
These graphs show the differences in relationships based on one’s demographic information. First, the relationships based on gender, overall trends are similar both in males and females. In the relationship between the number of weekly meditation and daily stress level, males reported more the number of weekly meditation than females throughout the daily stress levels, while in the relationship between the number of daily shouting and daily stress level, females reported more the number of daily shouting than male through the daily stress levels. In the relationships based on age, the age group of '51 or more' always reported the highest number of weekly meditation level among age groups throughout all daily stress levels in the relationship between the number of weekly meditation and daily stress level, whereas this group reported lowest number of daily shouting throughout all daily stress level in the relationship between the number of daily shouting and the daily stress level.

<br/>

## Research Question 2

## Research Question 3

## Conclusion
