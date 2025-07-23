# LIBRARIES: 


# CONFIGURATIONS: 


# FUNCTIONS: 

# Make a grid search selecting modularly the models
def grid_search(models, X_train, y_train, X_test=None, y_test=None, scoring='accuracy', cv=5):
    """
    Performs a grid search over the provided models and their hyperparameters.
    
    Parameters:
    - models: A dictionary where keys are model names and values are tuples of (model, param_grid).
    - X_train: Training features.
    - y_train: Training labels.
    - X_test: Optional test features for evaluation.
    - y_test: Optional test labels for evaluation.
    - scoring: Scoring metric to use for evaluation.
    - cv: Number of cross-validation folds.
    
    Returns:
    - results: A DataFrame containing the results of the grid search.
    """
    from sklearn.model_selection import GridSearchCV
    import pandas as pd
    
    results = []
    
    for name, (model, param_grid) in models.items():
        grid_search = GridSearchCV(model, param_grid, scoring=scoring, cv=cv)
        grid_search.fit(X_train, y_train)
        
        if X_test is not None and y_test is not None:
            score = grid_search.score(X_test, y_test)
        else:
            score = None
        
        results.append({
            'Model': name,
            'Best Params': grid_search.best_params_,
            'Best Score': grid_search.best_score_,
            'Test Score': score
        })
    
    return pd.DataFrame(results)


