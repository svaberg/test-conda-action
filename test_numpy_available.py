print("Importing numpy...")
try:
    import numpy as np
    print(f"numpy version: {np.__version__}")
except ModuleNotFoundError as e:
    print(f"numpy modudule not found: {str(e)}")
print("Done.")