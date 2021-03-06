# King County Home Price Analysis

This repository offers an analysis of factors that influence housing prices in King County, WA

## This Repository

### Repository Directory

```
├── README.md        <-- Main README file explaining the project's business case,
│                        methodology, and findings
│
├── data             <-- Data in CSV format
│   ├── processed    <-- Processed (combined, cleaned) data used for modeling
│   └── raw          <-- Original (immutable) data dump
│
├── notebooks        <-- Jupyter Notebooks for exploration and presentation
│   ├── exploratory  <-- Unpolished exploratory data analysis (EDA) notebooks
│   └── report       <-- Polished final notebook(s)
│
├── references       <-- Data dictionaries, manuals, and project instructions
│
└── reports          <-- Generated analysis (including presentation.pdf)
    └── figures      <-- Generated graphics and figures to be used in reporting
```

### Quick Links

1. [Final Analysis Notebook](notebooks/stats.ipynb)
2. [Presentation Slides](reports/presentation.pdf)

### Setup Instructions

1. Go into king-county repository.
- `cd ../../king-county`
2. Create your environment by running the following code:
- `conda env create --file project.yml`
3. Acvitvate your already created environment
- `conda activate project`


## Business Understanding

Based on the findings of our [notebook](notebooks/stats.ipynb), it is recommneded for homeowners to do projects that increase their total livigin space, as in doing so, it would substantially increase their home valuation. Using historical data on the Sales Price of different homes, it was found that the more the total living space of a home, the more the Sale would increase.

## Data Understanding

TODO: add data understanding, including at least 3 high-quality visualizations

## Data Preparation

TODO: add data preparation (which can be quite brief, but make sure you explain any dropped records)

## Modeling

TODO: add modeling.  What are the features of your final model?

## Evaluation

TODO: add evaluation.  How well does your model meet the assumptions of linear regression?

## Conclusion

TODO: add conclusion.  How does your model answer the business question?
