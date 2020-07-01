# Titanic: ML from Disaster


**Classification Problem**: <br>
Predict what sorts of people were most likely to survive the Titanic disaster.

<u>Objectives: </u><br><br>
On the basis of the training data we would like to:
- accurately predict unseen test cases
- understand which inputs affect the outcome, and how
- assess the quality of our predictions and inferences

## Dataset

- Outcome measurement $Y$
- Vector of $p$ predictor measurements $X$

**Training data**
$$
(X_{1},y_{1}), ... (X_{N},y_{N})\\
where\, N\ is\, the\, number\, of\, observations.
$$

Binary outcomes $Y$:

|  | outcome |
| -- |:----:|
| survivor|1 |
| victim | 0 |

A common analytical challenge is classifying an observation as a member of a group, 0 or 1. As we explore the data in depth, we shall find some patterns.



## EDA

<br>
The sample datasets have the dependent variable $$y: Survived$$ 
and 10 predictors.
<br>

| predictor | Definition | explanation | 
|----------|------------|-------------|
| $p_{1i}$   | Pclass | Ticket Class |
| $p_{2i}$ | Name |  
| $p_{3i}$ | Sex |
| $p_{4i}$ | Age |
| $p_{5i}$ | SibSp | # of siblings / spouses aboard the Titanic |
| $p_{6i}$ | Parch | # of parents / children aboard the Titanic  
| $p_{7i}$ | Ticket | Ticket number |
| $p_{8i}$ | Fare | Passenger Fare |
| $p_{9i}$ | Cabin | Cabin number |
| $p_{10i}$ | Embarked | Port of Embarkation |

<br>
$$y = f(\vec{X})$$
where $i$ is the passanger ID,
$i = 1,2,3,...,891$
<br>
<br>

### Datasets


#### Sex and Ticket Class
![Figure 1](
http://localhost:8888/files/Documents/Kaggle/titanic/Survivor%20by%20Gender%20and%20Pclass.png?_xsrf=2%7Cf8c0a0bb%7C21ed074352ba65bb10f13c1e78789f79%7C1592452182)


Figure 1 shows that 233 female passengers survived the titanic disaster while only 109 male passengers survived. The male death constitutes 85.25% of the total number of victims. In addition, the second graphh illustrates people from 3rd class ticket makes up  67.76% of the victims.

<style  type="text/css" >    #T_c157ba5a_b463_11ea_a784_88e9fe4f3014row0_col4 {            background-color:  #00441b;            color:  #f1f1f1;        }    #T_c157ba5a_b463_11ea_a784_88e9fe4f3014row0_col5 {            background-color:  #067230;            color:  #f1f1f1;        }    #T_c157ba5a_b463_11ea_a784_88e9fe4f3014row1_col4 {            background-color:  #c0e7df;            color:  #000000;        }    #T_c157ba5a_b463_11ea_a784_88e9fe4f3014row1_col5 {            background-color:  #005a24;            color:  #f1f1f1;        }    #T_c157ba5a_b463_11ea_a784_88e9fe4f3014row2_col4 {            background-color:  #005622;            color:  #f1f1f1;        }    #T_c157ba5a_b463_11ea_a784_88e9fe4f3014row2_col5 {            background-color:  #5ebe9b;            color:  #000000;        }    #T_c157ba5a_b463_11ea_a784_88e9fe4f3014row3_col4 {            background-color:  #f4fbfc;            color:  #000000;        }    #T_c157ba5a_b463_11ea_a784_88e9fe4f3014row3_col5 {            background-color:  #f7fcfd;            color:  #000000;        }    #T_c157ba5a_b463_11ea_a784_88e9fe4f3014row4_col4 {            background-color:  #7fcdb6;            color:  #000000;        }    #T_c157ba5a_b463_11ea_a784_88e9fe4f3014row4_col5 {            background-color:  #55b98f;            color:  #000000;        }    #T_c157ba5a_b463_11ea_a784_88e9fe4f3014row5_col4 {            background-color:  #f7fcfd;            color:  #000000;        }    #T_c157ba5a_b463_11ea_a784_88e9fe4f3014row5_col5 {            background-color:  #00441b;            color:  #f1f1f1;        }</style><table id="T_c157ba5a_b463_11ea_a784_88e9fe4f3014" ><thead>    <tr>        <th class="col_heading level0 col0" >Pclass</th>        <th class="col_heading level0 col1" >Sex</th>        <th class="col_heading level0 col2" >survivor</th>        <th class="col_heading level0 col3" >tot</th>        <th class="col_heading level0 col4" >tot_pct</th>        <th class="col_heading level0 col5" >survival rate of each sex</th>    </tr></thead><tbody>                <tr>                                <td id="T_c157ba5a_b463_11ea_a784_88e9fe4f3014row0_col0" class="data row0 col0" >1</td>                        <td id="T_c157ba5a_b463_11ea_a784_88e9fe4f3014row0_col1" class="data row0 col1" >female</td>                        <td id="T_c157ba5a_b463_11ea_a784_88e9fe4f3014row0_col2" class="data row0 col2" >91</td>                        <td id="T_c157ba5a_b463_11ea_a784_88e9fe4f3014row0_col3" class="data row0 col3" >94</td>                        <td id="T_c157ba5a_b463_11ea_a784_88e9fe4f3014row0_col4" class="data row0 col4" >96.81%</td>                        <td id="T_c157ba5a_b463_11ea_a784_88e9fe4f3014row0_col5" class="data row0 col5" >39.06%</td>            </tr>            <tr>                                <td id="T_c157ba5a_b463_11ea_a784_88e9fe4f3014row1_col0" class="data row1 col0" >1</td>                        <td id="T_c157ba5a_b463_11ea_a784_88e9fe4f3014row1_col1" class="data row1 col1" >male</td>                        <td id="T_c157ba5a_b463_11ea_a784_88e9fe4f3014row1_col2" class="data row1 col2" >45</td>                        <td id="T_c157ba5a_b463_11ea_a784_88e9fe4f3014row1_col3" class="data row1 col3" >122</td>                        <td id="T_c157ba5a_b463_11ea_a784_88e9fe4f3014row1_col4" class="data row1 col4" >36.89%</td>                        <td id="T_c157ba5a_b463_11ea_a784_88e9fe4f3014row1_col5" class="data row1 col5" >41.28%</td>            </tr>            <tr>                                <td id="T_c157ba5a_b463_11ea_a784_88e9fe4f3014row2_col0" class="data row2 col0" >2</td>                        <td id="T_c157ba5a_b463_11ea_a784_88e9fe4f3014row2_col1" class="data row2 col1" >female</td>                        <td id="T_c157ba5a_b463_11ea_a784_88e9fe4f3014row2_col2" class="data row2 col2" >70</td>                        <td id="T_c157ba5a_b463_11ea_a784_88e9fe4f3014row2_col3" class="data row2 col3" >76</td>                        <td id="T_c157ba5a_b463_11ea_a784_88e9fe4f3014row2_col4" class="data row2 col4" >92.11%</td>                        <td id="T_c157ba5a_b463_11ea_a784_88e9fe4f3014row2_col5" class="data row2 col5" >30.04%</td>            </tr>            <tr>                                <td id="T_c157ba5a_b463_11ea_a784_88e9fe4f3014row3_col0" class="data row3 col0" >2</td>                        <td id="T_c157ba5a_b463_11ea_a784_88e9fe4f3014row3_col1" class="data row3 col1" >male</td>                        <td id="T_c157ba5a_b463_11ea_a784_88e9fe4f3014row3_col2" class="data row3 col2" >17</td>                        <td id="T_c157ba5a_b463_11ea_a784_88e9fe4f3014row3_col3" class="data row3 col3" >108</td>                        <td id="T_c157ba5a_b463_11ea_a784_88e9fe4f3014row3_col4" class="data row3 col4" >15.74%</td>                        <td id="T_c157ba5a_b463_11ea_a784_88e9fe4f3014row3_col5" class="data row3 col5" >15.60%</td>            </tr>            <tr>                                <td id="T_c157ba5a_b463_11ea_a784_88e9fe4f3014row4_col0" class="data row4 col0" >3</td>                        <td id="T_c157ba5a_b463_11ea_a784_88e9fe4f3014row4_col1" class="data row4 col1" >female</td>                        <td id="T_c157ba5a_b463_11ea_a784_88e9fe4f3014row4_col2" class="data row4 col2" >72</td>                        <td id="T_c157ba5a_b463_11ea_a784_88e9fe4f3014row4_col3" class="data row4 col3" >144</td>                        <td id="T_c157ba5a_b463_11ea_a784_88e9fe4f3014row4_col4" class="data row4 col4" >50.00%</td>                        <td id="T_c157ba5a_b463_11ea_a784_88e9fe4f3014row4_col5" class="data row4 col5" >30.90%</td>            </tr>            <tr>                                <td id="T_c157ba5a_b463_11ea_a784_88e9fe4f3014row5_col0" class="data row5 col0" >3</td>                        <td id="T_c157ba5a_b463_11ea_a784_88e9fe4f3014row5_col1" class="data row5 col1" >male</td>                        <td id="T_c157ba5a_b463_11ea_a784_88e9fe4f3014row5_col2" class="data row5 col2" >47</td>                        <td id="T_c157ba5a_b463_11ea_a784_88e9fe4f3014row5_col3" class="data row5 col3" >347</td>                        <td id="T_c157ba5a_b463_11ea_a784_88e9fe4f3014row5_col4" class="data row5 col4" >13.54%</td>                        <td id="T_c157ba5a_b463_11ea_a784_88e9fe4f3014row5_col5" class="data row5 col5" >43.12%</td>            </tr>    </tbody></table>


From the above table, it shows that 1st and 3rd class male passengers are the main part of male survivors, over 84.4%. Also, 36.89% of 122 1st class male passengers survived the shipwrack. Female passengers from 1st and 2nd class have over 90% survivors respectively. 

The findings reveal an obvious fact that <mark>female tends to have a bigger chance of survival over male passengers</mark> from the tinanic disaster. <mark>Passenger from a higher ticket class has a better chance of survival over the lower one </mark>except male from 2nd class, which only constitutes 15.6% of 109 male survivors.

Looking into other predictors might be able explain this phenomenon. 





__Note: the datatype of Pclass should be categorical.__ 


### Correlations

Pearson's Product Moment between every two variables.


|          |   Survived |     Pclass |        Age |      SibSp |      Parch |       Fare |
|:---------|-----------:|-----------:|-----------:|-----------:|-----------:|-----------:|
| Survived |  1         | -0.338481  | -0.0772211 | -0.0353225 |  0.0816294 |  0.257307  |
| Pclass   | -0.338481  |  1         | -0.369226  |  0.0830814 |  0.0184427 | -0.5495    |
| Age      | -0.0772211 | -0.369226  |  1         | -0.308247  | -0.189119  |  0.0960667 |
| SibSp    | -0.0353225 |  0.0830814 | -0.308247  |  1         |  0.414838  |  0.159651  |
| Parch    |  0.0816294 |  0.0184427 | -0.189119  |  0.414838  |  1         |  0.216225  |
| Fare     |  0.257307  | -0.5495    |  0.0960667 |  0.159651  |  0.216225  |  1         |



$Fare$ and $Pclass$ have the highest correlation coefficient, $r_{x_{1},x_{8}} = -0.5495$. It's logical to understand the corrlation between $Fare$ and $Pclass$ is high since 1st class ticket is much more expensive than 3rd class ticket.

From the correlations between two variables we got, independent variable Pclass is the statistically significant to dependent varibale Survived. It would be interesting to look further into it.

The feature most related to the outcome of interest is the Pclass of each passenger. 

It's likely 15 $Fare$ entries are missing. Thus, we will choose $Pclass$ over $Fare$ as one of our predictors.


#### Sex variable

Sex variable is a dummy variable, either male or female. 

Aparently, the number of survivors who have relatives or families aboard is much smaller than the ones who don't.


#### Age variable

![figure2](http://localhost:8888/files/Documents/Kaggle/titanic/Age%20of%20survivors%20from%203%20ticket%20class.png?_xsrf=2%7Cf8c0a0bb%7C21ed074352ba65bb10f13c1e78789f79%7C1592452182)

$Age$ has a right-skewed distribution, and means from the different groups are higher than modes from the corresponding groups. Let's test imputation later with mode and mean later respectively.


####

# Data Preprocessing
- define processing steps
- define the model
- create and evaluate the pipeline


### Categorical Data

| predictor | dtype | definition |
| --------- | ------------- | -------- |
| $Pclass$ | ordinal variable | 1,2,3 |
| $Sex$ | nominal variable | male, female | 

### Missing value

| predictor | missing value | solution |
| --------- | ------------- | -------- |
| $Age$ | 177 | 2 imputation options: mean and mode |
| $Cabin$ | 687 | drop the predictor | 
        
# Statistical Models

- Logistic Regression
- 

## Logistic Regression

There are a variety of statistical and machine learning techniques one could use to predict a binary outcome, though a popular one is the logistic regression (more on that another time).

Here, we can model the probability of survival using only the Pclass attribute.

Accuracy= TotalCases/CorrectPredictions

$$ Accuracy = \Sigma_{n=i}^{N} \frac{1-|\hat{y}_i - y_i|}{N}$$


- True Positives (TP): The model predicts a case (and the case is true in the data)
- False Positives (FP): The model predicts a case (and the case is not true in the data)
- True Negatives (TN): The model does not predict a case (and the case is not true in the data)
- False Negatives (FN): The model does not predict a case (and the case is true in the data)



# Machine Learning Models

- Decision Tree Model
- Random Forest

## Decision Tree Model

Intuitively, I will select two independent variables to predict the survival results of Titanic crash: **Sex** and **Class**  


