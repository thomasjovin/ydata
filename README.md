Working on the ydata-quality library to evalutate issues with datasets.
    - pip install ydata-quality
        - ISSUE: Not Updated --> Python Version is 3.8 (as of July 2023)

Sample Output:

Warnings:
        TOTAL: 7 warning(s)
        Priority 1: 2 warning(s)
        Priority 2: 5 warning(s)

Priority 1 - heavy impact expected:
        * [LABELS - TEST NORMALITY] 
                    The label distribution failed to pass a normality test as-is and following a battery of transforms.
It is possible that the data originates from an exotic distribution, there is heavy outlier presence or it is multimodal. Addressing this issue might prove critical for regressor performance.
        * [DUPLICATES - DUPLICATE COLUMNS] Found 1 columns with exactly the same feature values as other columns.

        
Priority 2 - usage allowed, limited human intelligibility:
        * [DATA RELATIONS - HIGH COLLINEARITY - NUMERICAL] Found 4 numerical variables with high Variance Inflation Factor (VIF>5.0). The variables listed in results are highly collinear with other variables in the dataset. These will make model explainability harder and potentially give way to issues like overfitting.Depending on your end goal you might want to remove the highest VIF variables.
        * [DATA RELATIONS - HIGH COLLINEARITY - CATEGORICAL] Found 3 categorical variables with significant collinearity (p-value < 0.05). The variables listed in results are highly collinear with other variables in the dataset and sorted descending according to propensity. These will make model explainability harder and potentially give way to issues like overfitting.Depending on your end goal you might want to remove variables following the provided order.
        * [LABELS - OUTLIER DETECTION] 
                    Found 2 potential outliers across the full dataset.                     A distance bigger than 3.0 standard deviations of intra-cluster distances                     to the respective centroids was used to define the potential outliers.
        * [BIAS&FAIRNESS - PROXY IDENTIFICATION] Found 5 feature pairs of correlation to sensitive attributes with values higher than defined threshold (0.5).
        * [DUPLICATES - EXACT DUPLICATES] Found 20 instances with exact duplicate feature values.