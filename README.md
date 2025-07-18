# KAGGLE-Introverts-Extroverts



# Explanation: Correlation Heatmap Code

This section breaks down each line of the heatmap plotting code in Python using `matplotlib` and `seaborn`.

---

##  `plt.figure(figsize=(10, 8))`
Creates a new figure (canvas) for plotting.

- `figsize=(10, 8)` sets the width to **10 inches** and height to **8 inches**.
- Without this, your plot may appear too small or cramped in a Jupyter notebook.

---

##  `sns.heatmap(corr_matrix, annot=True, fmt='.2f', cmap='coolwarm')`
Generates a heatmap based on a correlation matrix.

### Parameters:

| Argument        | Description                                                                 |
|-----------------|-----------------------------------------------------------------------------|
| `corr_matrix`   | A DataFrame of correlation values (e.g., from `df.corr()`)                  |
| `annot=True`    | Displays the numeric correlation values on each square                      |
| `fmt=".2f"`     | Formats the annotation values to **2 decimal places**                       |
| `cmap='coolwarm'` | Applies a blue-to-red gradient (blue = negative, red = positive correlation) |

---

##  `plt.title('Correlation Heatmap of Numeric Features')`
Adds a title to the top of your heatmap for context.

---

##  `plt.show()`
Renders the plot inside the notebook cell.
