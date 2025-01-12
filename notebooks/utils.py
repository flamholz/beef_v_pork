import numpy as np
from scipy.stats import gmean

# Orders that are not placental, i.e. are marsupial or monotreme. 
METATHERIAN_ORDERS = [
    'Monotremata',
    'Didelphimorphia',
    'Paucituberculata',
    'Microbiotheria',
    'Dasyuromorphia',
    'Peramelemorphia',
    'Notoryctemorphia',
    'Diprotodontia'
]

# Estimate the number of young per year as the geometric mean of the two values.
def nan_gmean(a):
    """Geometric mean of pd.Series that handles NaNs."""
    if not a.any():
        return np.NaN
    my_a = a[a.notnull()]
    return gmean(a[a.notnull()])