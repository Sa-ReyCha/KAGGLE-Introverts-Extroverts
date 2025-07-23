# LIBRARIES: 

import pandas as pd
import matplotlib.pyplot as plt

# CONFIGURATIONS:


# LIBRARIES:


# FUNCTIONS:


def plot_nulls(df1, df2=None, labels=('DF1', 'DF2')):
    """
    Plots the percentage of null values in each column of one or two dataframes,
    showing the count of nulls as labels on each bar.
    If two dataframes are provided, plots them side by side.
    """
    if df2 is None:
        dfs = [df1]
        plot_labels = [labels[0]]
    else:
        dfs = [df1, df2]
        plot_labels = labels[:2]

    fig, axes = plt.subplots(1, len(dfs), figsize=(12 * len(dfs), 6), sharey=True)

    if len(dfs) == 1:
        axes = [axes]

    for ax, df, label in zip(axes, dfs, plot_labels):
        null_counts = df.isnull().sum()
        null_percentage = (null_counts / len(df)) * 100
        bars = ax.bar(null_percentage.index, null_percentage, color='orange', alpha=0.7, label='Percentage of Nulls')
        for bar, count in zip(bars, null_counts):
            ax.text(
                bar.get_x() + bar.get_width() / 2,
                bar.get_height(),
                f'{int(count)}',
                ha='center',
                va='bottom',
                fontsize=10,
                color='black'
            )
        ax.tick_params(axis='x', rotation=45)
        ax.set_title(f'Null Values in {label}')
        ax.set_xlabel('Columns')
        ax.set_ylabel('Percentage of Nulls (%)')
        ax.legend()
    plt.tight_layout()
    plt.show()


def investigate_null_imputation(df1):
    df_nulos = df1.loc[:, df1.isnull().any()]

    listas_columnas = {}
    for col in df_nulos.columns:
        listas_columnas[col] = df_nulos[col].dropna().tolist()


    items = list(listas_columnas.items())
    bloques = [items[i:i+4] for i in range(0, len(items), 4)]

    for idx, bloque in enumerate(bloques):
        fig, axes = plt.subplots(2, 4, figsize=(20, 8))  # 2 filas, 4 columnas
        for i, (col, valores) in enumerate(bloque):
            axes[0, i].hist(valores, bins=30, color='skyblue', edgecolor='black')
            axes[0, i].set_title(f'Histograma de {col}')
            # axes[0, i].set_xlabel(col)
            axes[0, i].set_ylabel('Frecuencia')

        for i, (col, valores) in enumerate(bloque):
            if all(isinstance(v, (int, float)) for v in valores):
                axes[1, i].boxplot(valores, vert=False, patch_artist=True, boxprops=dict(facecolor='orange', color='black'))
                axes[1, i].set_xlabel(col)
                axes[1, i].set_yticks([])
            else:
                value_counts = pd.Series(valores).value_counts()
                axes[1, i].pie(value_counts, labels=value_counts.index, autopct='%1.1f%%', startangle=90)
                axes[1, i].set_xlabel(col)

        if len(bloque) < 4:
            for j in range(len(bloque), 4):
                fig.delaxes(axes[0, j])
                fig.delaxes(axes[1, j])
        plt.tight_layout()
        plt.show()


def investigate_null_deletion(df1, df2=None, labels=('DF1', 'DF2')):
    """
    Plots a horizontal bar chart comparing the number of records in the original DataFrame
    vs. the number of records after dropping all rows with any nulls.
    If a second DataFrame is provided, compares both side by side.
    """
    
    dfs = [df1] if df2 is None else [df1, df2]
    plot_labels = [labels[0]] if df2 is None else labels[:2]

    counts = []
    dropped_counts = []
    for df in dfs:
        counts.append(len(df))
        dropped_counts.append(len(df.dropna()))

    bar_labels = []
    for label in plot_labels:
        bar_labels.extend([f'{label} original', f'{label} sin nulos'])

    values = []
    for orig, drop in zip(counts, dropped_counts):
        values.extend([orig, drop])

    plt.figure(figsize=(20, 3 + 2 * len(dfs)))
    plt.barh(bar_labels, values, color=['orange', 'skyblue'] * len(dfs))
    for i, v in enumerate(values):
        plt.text(v + max(values) * 0.01, i, str(v), va='center', fontsize=12)
    plt.title('Comparación de registros: original vs. sin nulos')
    plt.xlabel('Cantidad de registros')
    plt.tight_layout()
    plt.show()