# Happiness Dataset Analysis: A Knight's Journey Through Joy and Shadows

## The Dataset: Mapping the World's Smiles and Sorrows
In the depths of global data, the Happiness Dataset emerges as a beacon of insight, revealing the pulse of human contentment across nations. This treasure trove contains:

- **Metrics of Well-being**: Life Ladder, Social Support, and Freedom to Make Life Choices—factors shaping happiness.
- **Economic Indicators**: GDP per capita and perceptions of corruption—mirrors of societal structure.
- **Affective Measures**: Positive and Negative Affect—fleeting emotions captured in numbers.
- **Health and Longevity**: Healthy Life Expectancy—years filled with hope or despair.

But even data isn't flawless—missing values cast shadows over certain variables, waiting to be uncovered.

## Summary Statistics: The Numbers Beneath the Mask
Even in chaos, numbers whisper truths. Here's what they reveal:

- **Life Ladder**: The average score is 5.48, with extremes ranging from 1.28 to 8.02.
- **GDP per capita**: A global spread, from 5.53 to 11.68, mirrors the disparity between nations.
- **Social Support**: A strong average of 0.81 suggests a collective reliance in hard times.
- **Healthy Life Expectancy**: Spanning from a mere 6.72 to 74.6 years, it highlights the diversity in global health.
- **Missing Data**: Shadows linger—key metrics like perceptions of corruption and generosity carry notable gaps.
## 
|                                  |   count |   unique | top     |   freq |           mean |         std |      min |       25% |       50% |        75% |      max |
|:---------------------------------|--------:|---------:|:--------|-------:|---------------:|------------:|---------:|----------:|----------:|-----------:|---------:|
| Country name                     |    2363 |      165 | Lebanon |     18 |  nan           | nan         |  nan     |  nan      |  nan      |  nan       |  nan     |
| year                             |    2363 |      nan | nan     |    nan | 2014.76        |   5.05944   | 2005     | 2011      | 2015      | 2019       | 2023     |
| Life Ladder                      |    2363 |      nan | nan     |    nan |    5.48357     |   1.12552   |    1.281 |    4.647  |    5.449  |    6.3235  |    8.019 |
| Log GDP per capita               |    2335 |      nan | nan     |    nan |    9.39967     |   1.15207   |    5.527 |    8.5065 |    9.503  |   10.3925  |   11.676 |
| Social support                   |    2350 |      nan | nan     |    nan |    0.809369    |   0.121212  |    0.228 |    0.744  |    0.8345 |    0.904   |    0.987 |
| Healthy life expectancy at birth |    2300 |      nan | nan     |    nan |   63.4018      |   6.84264   |    6.72  |   59.195  |   65.1    |   68.5525  |   74.6   |
| Freedom to make life choices     |    2327 |      nan | nan     |    nan |    0.750282    |   0.139357  |    0.228 |    0.661  |    0.771  |    0.862   |    0.985 |
| Generosity                       |    2282 |      nan | nan     |    nan |    9.77213e-05 |   0.161388  |   -0.34  |   -0.112  |   -0.022  |    0.09375 |    0.7   |
| Perceptions of corruption        |    2238 |      nan | nan     |    nan |    0.743971    |   0.184865  |    0.035 |    0.687  |    0.7985 |    0.86775 |    0.983 |
| Positive affect                  |    2339 |      nan | nan     |    nan |    0.651882    |   0.10624   |    0.179 |    0.572  |    0.663  |    0.737   |    0.884 |
| Negative affect                  |    2347 |      nan | nan     |    nan |    0.273151    |   0.0871311 |    0.083 |    0.209  |    0.262  |    0.326   |    0.705 |

## Missing Values
|                                  |   0 |
|:---------------------------------|----:|
| Country name                     |   0 |
| year                             |   0 |
| Life Ladder                      |   0 |
| Log GDP per capita               |  28 |
| Social support                   |  13 |
| Healthy life expectancy at birth |  63 |
| Freedom to make life choices     |  36 |
| Generosity                       |  81 |
| Perceptions of corruption        | 125 |
| Positive affect                  |  24 |
| Negative affect                  |  16 |


## The Analysis Carried Out: Strategies of the Knight
### Step 1: Confronting the Shadows (Data Cleaning)
Missing values were identified and prepared for further handling—ensuring no secret is left untold.

### Step 2: Summarizing Gotham (Descriptive Statistics)
Summary statistics painted a vivid image of the data's scope and its gaps.

### Step 3: Following the Threads (Correlation Analysis)
Relationships between metrics, such as Life Ladder and GDP, were uncovered through a heatmap of connections.

### Step 4: Building the Bat-Signal (Data Visualizations)
- **Correlation Heatmap**: A grid of relationships revealed surprising links between variables.
- **Missing Values Bar Plot**: A spotlight on what’s been lost.
- **Year Distribution Plot**: A timeline of observations, showing how happiness has evolved.

## The Insights Discovered: The Truth Beneath the Mask
1. **The Wealth-Happiness Paradox**  
   GDP per capita shows a strong correlation (0.82) with Life Ladder, affirming the role of wealth in well-being—but not all is gold.

2. **The Pillars of Happiness**  
   Social Support and Healthy Life Expectancy also exhibit strong ties to happiness, suggesting that relationships and health are as critical as wealth.

3. **Shadows in Data**  
   Generosity and Perceptions of Corruption hold weaker, even negative correlations with Life Ladder, pointing to the complexity of moral and ethical factors.

4. **Emotional Duality**  
   Positive Affect bolsters happiness, but Negative Affect weighs it down—a constant push and pull in the human experience.

## Visualizations: Illuminating the Shadows
### 1. Correlation Heatmap
A map of connections, showing how variables intertwine to shape happiness.  
**Key Observation**: GDP per capita and Social Support stand out as the strongest predictors of Life Ladder, while perceptions of corruption have a negative influence.
        ![correlation_heatmap](https://github.com/user-attachments/assets/a823b809-9870-478f-a6b0-2890344b525a)

### 2. Missing Values Bar Plot
A reminder of what’s been lost in the dataset—key insights obscured by missing data.  
**Key Observation**: Variables like Perceptions of Corruption and Generosity have the highest missing values, potentially skewing deeper analyses.
      ![year_distribution](https://github.com/user-attachments/assets/864f2453-9135-4cfc-9c94-945f49c574ed)

### 3. Year Distribution Plot
A timeline of data collection, highlighting trends across years.  
**Key Observation**: Data becomes more abundant after 2010, offering a richer view of modern happiness trends.
       ![missing_values](https://github.com/user-attachments/assets/ea9c542d-85c6-4293-8944-ed9399ecd1e9)

## The Implications: A Plan to Forge Brighter Futures
1. **Wealth Alone Cannot Buy Happiness**  
   While GDP is crucial, fostering health, social support, and freedom is equally important in building a happy society.

2. **Addressing the Shadows**  
   Missing data in critical areas, like perceptions of corruption, must be handled—through imputation or cautious exclusion.

3. **Building New Horizons**  
   - **Temporal Trends**: How does happiness evolve with time in response to global challenges?
   - **Regional Analysis**: Breaking down happiness by geography to discover unique cultural insights.

## Final Notes: A Quest for Happiness
The Happiness Dataset is more than a collection of numbers—it’s a reflection of humanity’s pursuit of joy. By analyzing its secrets, we can identify the factors that truly matter, address societal inequities, and foster brighter futures for all.

Even in the darkest corners of the dataset, hope remains—the hope to understand, to learn, and to improve. With the right tools and strategies, we can all work towards a happier world.


