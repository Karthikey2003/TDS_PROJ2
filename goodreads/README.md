# Analysis of Goodreads Dataset

## The Data Received
The dataset collected from Goodreads contains detailed information about books, including attributes like `book_id`, `isbn`, `authors`, `title`, `language_code`, `average_rating`, and various measures of reader engagement (e.g., `ratings_count`, `work_text_reviews_count`, and `ratings_1` through `ratings_5`). It spans metadata such as publication years, unique book identifiers, and even URLs for book images. While comprehensive, the dataset contains some missing values in columns like `isbn`, `authors`, and `original_title`.

## Summary Statistics

|                           |   count |   unique | top                                                                                      |   freq |            mean |              std |            min |             25% |              50% |             75% |              max |
|:--------------------------|--------:|---------:|:-----------------------------------------------------------------------------------------|-------:|----------------:|-----------------:|---------------:|----------------:|-----------------:|----------------:|-----------------:|
| book_id                   |   10000 |      nan | nan                                                                                      |    nan |  5000.5         |   2886.9         |     1          |  2500.75        |   5000.5         |  7500.25        |  10000           |
| goodreads_book_id         |   10000 |      nan | nan                                                                                      |    nan |     5.2647e+06  |      7.57546e+06 |     1          | 46275.8         | 394966           |     9.38223e+06 |      3.32886e+07 |
| best_book_id              |   10000 |      nan | nan                                                                                      |    nan |     5.47121e+06 |      7.82733e+06 |     1          | 47911.8         | 425124           |     9.63611e+06 |      3.55342e+07 |
| work_id                   |   10000 |      nan | nan                                                                                      |    nan |     8.64618e+06 |      1.17511e+07 |    87          |     1.00884e+06 |      2.71952e+06 |     1.45177e+07 |      5.63996e+07 |
| books_count               |   10000 |      nan | nan                                                                                      |    nan |    75.7127      |    170.471       |     1          |    23           |     40           |    67           |   3455           |
| isbn                      |    9300 |     9300 | 439023483                                                                                |      1 |   nan           |    nan           |   nan          |   nan           |    nan           |   nan           |    nan           |
| isbn13                    |    9415 |      nan | nan                                                                                      |    nan |     9.75504e+12 |      4.42862e+11 |     1.9517e+08 |     9.78032e+12 |      9.78045e+12 |     9.78083e+12 |      9.79001e+12 |
| authors                   |   10000 |     4664 | Stephen King                                                                             |     60 |   nan           |    nan           |   nan          |   nan           |    nan           |   nan           |    nan           |
| original_publication_year |    9979 |      nan | nan                                                                                      |    nan |  1981.99        |    152.577       | -1750          |  1990           |   2004           |  2011           |   2017           |
| original_title            |    9415 |     9274 |                                                                                          |      5 |   nan           |    nan           |   nan          |   nan           |    nan           |   nan           |    nan           |
| title                     |   10000 |     9964 | Selected Poems                                                                           |      4 |   nan           |    nan           |   nan          |   nan           |    nan           |   nan           |    nan           |
| language_code             |    8916 |       25 | eng                                                                                      |   6341 |   nan           |    nan           |   nan          |   nan           |    nan           |   nan           |    nan           |
| average_rating            |   10000 |      nan | nan                                                                                      |    nan |     4.00219     |      0.254427    |     2.47       |     3.85        |      4.02        |     4.18        |      4.82        |
| ratings_count             |   10000 |      nan | nan                                                                                      |    nan | 54001.2         | 157370           |  2716          | 13568.8         |  21155.5         | 41053.5         |      4.78065e+06 |
| work_ratings_count        |   10000 |      nan | nan                                                                                      |    nan | 59687.3         | 167804           |  5510          | 15438.8         |  23832.5         | 45915           |      4.94236e+06 |
| work_text_reviews_count   |   10000 |      nan | nan                                                                                      |    nan |  2919.96        |   6124.38        |     3          |   694           |   1402           |  2744.25        | 155254           |
| ratings_1                 |   10000 |      nan | nan                                                                                      |    nan |  1345.04        |   6635.63        |    11          |   196           |    391           |   885           | 456191           |
| ratings_2                 |   10000 |      nan | nan                                                                                      |    nan |  3110.89        |   9717.12        |    30          |   656           |   1163           |  2353.25        | 436802           |
| ratings_3                 |   10000 |      nan | nan                                                                                      |    nan | 11475.9         |  28546.4         |   323          |  3112           |   4894           |  9287           | 793319           |
| ratings_4                 |   10000 |      nan | nan                                                                                      |    nan | 19965.7         |  51447.4         |   750          |  5405.75        |   8269.5         | 16023.5         |      1.4813e+06  |
| ratings_5                 |   10000 |      nan | nan                                                                                      |    nan | 23789.8         |  79768.9         |   754          |  5334           |   8836           | 17304.5         |      3.01154e+06 |
| image_url                 |   10000 |     6669 | https://s.gr-assets.com/assets/nophoto/book/111x148-bcc042a9c91a29c1d680899eff700a03.png |   3332 |   nan           |    nan           |   nan          |   nan           |    nan           |   nan           |    nan           |
| small_image_url           |   10000 |     6669 | https://s.gr-assets.com/assets/nophoto/book/50x75-a91bf249278a81aabab721ef782c4a74.png   |   3332 |   nan           |    nan           |   nan          |   nan           |    nan           |   nan           |    nan           |

## Missing Values

|                           |    0 |
|:--------------------------|-----:|
| book_id                   |    0 |
| goodreads_book_id         |    0 |
| best_book_id              |    0 |
| work_id                   |    0 |
| books_count               |    0 |
| isbn                      |  700 |
| isbn13                    |  585 |
| authors                   |    0 |
| original_publication_year |   21 |
| original_title            |  585 |
| title                     |    0 |
| language_code             | 1084 |
| average_rating            |    0 |
| ratings_count             |    0 |
| work_ratings_count        |    0 |
| work_text_reviews_count   |    0 |
| ratings_1                 |    0 |
| ratings_2                 |    0 |
| ratings_3                 |    0 |
| ratings_4                 |    0 |
| ratings_5                 |    0 |
| image_url                 |    0 |
| small_image_url           |    0 |


## The Analysis Carried Out
1. **Data Cleaning**:
   - Assessed the completeness of the dataset by analyzing missing values in each column.
2. **Summary Statistics**:
   - Generated descriptive statistics to understand data distributions.
3. **Correlation Analysis**:
   - Constructed a heatmap to study relationships among numerical variables, such as `ratings_count`, `average_rating`, and `work_text_reviews_count`.
4. **Data Visualizations**:
   - Created the following key visualizations:
     - **Missing Values Bar Plot**: To visualize which columns have significant missing data.
     - **Correlation Heatmap**: To explore interdependencies among numerical features.
     - **Distribution Plot**: Highlighting the spread of unique `book_id` values, showing an even distribution.

## The Insights Discovered
1. **Uniform Data Spread**:
   - The uniform distribution of `book_id` indicates balanced representation across the dataset, with no clustering or bias in book entries.
     ![book_id_distribution](https://github.com/user-attachments/assets/32b188f0-f570-452e-b70d-73771798df78)


2. **Relationships Among Metrics**:
   - Strong correlations exist among `ratings_count`, `work_ratings_count`, and `work_text_reviews_count`, indicating that books with high ratings counts tend to also have more text reviews. This reflects user engagement trends.
   - `average_rating` is only moderately correlated with these popularity metrics, suggesting that a book's quality (as perceived by readers) is not solely determined by how many people rate or review it.
     ![correlation_heatmap](https://github.com/user-attachments/assets/2fa0d23e-f656-4a05-9800-c26d8a8b79a8)


3. **Missing Data Challenge**:
   - Columns like `isbn`, `authors`, and `original_title` have significant missing values, potentially impacting the reliability of analyses related to those fields.
     
![missing_values](https://github.com/user-attachments/assets/7262b209-45c8-4d35-a9a1-bed74e72ce0e)

## The Implications of Findings
1. **Actionable Insights**:
   - Books with higher ratings counts and text reviews could be highlighted as "popular" in recommendation systems, while their average ratings can add another layer of quality-based sorting.
   - High correlations between user engagement metrics suggest these features could be combined into a single "engagement score" for streamlined analysis.

2. **Data Cleaning**:
   - Columns with significant missing values should be handled strategically:
     - Impute missing data for critical columns (e.g., `authors`).
     - Drop less important columns like `isbn` if missing values are too frequent and cannot be accurately imputed.

3. **Future Exploration**:
   - Analyze trends in `average_rating` across `original_publication_year` to uncover how books from different eras perform.
   - Segment books by `language_code` to study regional differences in popularity and ratings.

4. **Visualization-Driven Insights**:
   - The strong correlations between user engagement metrics indicate they should be used in tandem to identify the most impactful books.
   - Missing data plots highlight areas of concern for preprocessing before any machine learning or deeper analysis is conducted.

## Final Notes
The Goodreads dataset is a rich resource for exploring patterns in book popularity, quality, and user engagement. By addressing missing data and leveraging the insights gained from correlations, one can build powerful models for recommendation systems or trend analyses.
