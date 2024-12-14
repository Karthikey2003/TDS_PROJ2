# **Movie Ratings Dataset Analysis: A Dark Knight's Investigation**

---

## **The Dataset: A Cinematic Mystery**

In the shadows of the dataset, a story unfolds—a story of movies, their quality, their repeatability, and the people who rated them. The data, riddled with missing values, reveals glimpses of the truth:

- **Columns of Interest:**
  - **Date:** When the ratings were given.
  - **Language:** The language of the movie.
  - **Type:** Categorizing the content, with movies dominating the count.
  - **Title:** Movie titles repeating, hinting at popular choices.
  - **By:** Names associated with the movies—actors, directors, or contributors.
  - **Overall, Quality, and Repeatability Ratings:** Key metrics defining audience perception.

Yet, beneath the surface, the data harbors gaps—missing values in **date** and **by**, like missing scenes in an unsolved case.

---

## **Summary Statistics: The Silent Truth**

### **Descriptive Overview**

| Column            | Count | Unique | Top                  | Freq | Mean   | Std Dev | Min | 25%  | 50%  | 75%  | Max |
|:------------------|-------|--------|:---------------------|------|--------|---------|-----|------|------|------|-----|
| **date**          | 2553  | 2055   | 21-May-06            | 8    | nan    | nan     | nan | nan  | nan  | nan  | nan |
| **language**      | 2652  | 11     | English              | 1306 | nan    | nan     | nan | nan  | nan  | nan  | nan |
| **type**          | 2652  | 8      | movie                | 2211 | nan    | nan     | nan | nan  | nan  | nan  | nan |
| **title**         | 2652  | 2312   | Kanda Naal Mudhal    | 9    | nan    | nan     | nan | nan  | nan  | nan  | nan |
| **by**            | 2390  | 1528   | Kiefer Sutherland    | 48   | nan    | nan     | nan | nan  | nan  | nan  | nan |
| **overall**       | 2652  | nan    | nan                  | nan  | 3.05   | 0.76    | 1   | 3    | 3    | 3    | 5   |
| **quality**       | 2652  | nan    | nan                  | nan  | 3.21   | 0.80    | 1   | 3    | 3    | 4    | 5   |
| **repeatability** | 2652  | nan    | nan                  | nan  | 1.49   | 0.60    | 1   | 1    | 1    | 2    | 3   |

---

## **The Investigation: Visual Clues**

### **1. Missing Values: Gotham's Dark Patches**

The **Missing Values Bar Chart** shines light on the gaps:
![missing_values](https://github.com/user-attachments/assets/96ba06d1-e020-418f-b80f-5fcb4ec18ab5)



**Analysis:**  
- **262 missing values** in the `by` column.
- **99 missing values** in the `date` column.

The `by` column—critical for identifying movie associations—has significant gaps. Missing dates disrupt timelines and analysis of trends. These holes must be addressed to restore the dataset’s integrity.

---

### **2. Correlation Heatmap: Connections in the Chaos**

The **Correlation Heatmap** reveals relationships between ratings:
![correlation_heatmap](https://github.com/user-attachments/assets/a68a58ec-bb21-48a7-9101-53c405b0feb9)


| **Metric**       | **Overall** | **Quality** | **Repeatability** |
|------------------:|------------:|------------:|------------------:|
| **Overall**       | 1.00        | 0.83        | 0.51             |
| **Quality**       | 0.83        | 1.00        | 0.31             |
| **Repeatability** | 0.51        | 0.31        | 1.00             |

**Key Insights:**
- **Strong correlation** (0.83) between **Overall** and **Quality** suggests that higher quality movies drive overall ratings.
- A **weak correlation** (0.31) between **Quality** and **Repeatability** indicates that movies considered "good" aren’t necessarily rewatchable.
- Repeatability’s **low correlation** (0.51) with Overall confirms that some movies are one-time watches despite high ratings.

---

### **3. Distribution of Overall Ratings: Gotham's Audience Speaks**

The **Overall Ratings Distribution** reveals audience tendencies:
![overall_distribution](https://github.com/user-attachments/assets/15040e02-5ff5-402b-8948-bf2eab87d912)


**Observations:**
- **Overall Ratings** cluster around **3.0**, reflecting a neutral sentiment from viewers.
- Ratings at **2.0** and **4.0** suggest polarization—some movies underwhelm, while others impress.
- Very few ratings are **1.0** or **5.0**, showing that extreme opinions are rare.

---

## **Insights Uncovered: Truths in the Darkness**

1. **Quality Drives Overall Ratings**  
   Strong alignment between **Overall** and **Quality** suggests that audiences prioritize a movie's perceived quality when rating it.

2. **Repeatability Is Its Own Beast**  
   While movies can have high **Quality**, they may lack **Repeatability**, showing a divergence between one-time hits and rewatchable classics.

3. **Data Gaps Disrupt the Analysis**  
   Missing values in **by** and **date** weaken the dataset’s strength. Addressing these through imputation or removal will strengthen future analysis.

---

## **Implications and Next Steps: Cleaning the Streets**

### **1. Address Missing Values**
- **Impute missing `by` and `date` values** where feasible.
- Drop rows with irreparable missing data.

### **2. Further Investigations**
- **Time Trends:** Analyze ratings over time using the `date` column.
- **Language Insights:** Segment data by **language** to reveal cultural preferences.
- **Type Analysis:** Compare movies to other content types for unique trends.

### **3. Predictive Power**
Build a model to predict **Overall Ratings** using **Quality** and **Repeatability** as features.

---

## **Final Notes: Gotham's Data Never Lies**

The ratings dataset reveals audience behavior, preferences, and trends hidden beneath layers of missing data. Like Gotham, the truth lies in the connections—between Quality, Overall ratings, and Repeatability. By addressing data gaps and expanding the analysis, we can uncover the stories audiences truly cherish.

With vigilance and careful analysis, every rating tells a tale.

---
