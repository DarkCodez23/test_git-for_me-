import pandas as pd

data = {
    "src_bytes": [100, 200, 300],
    "failed_logins": [0, 1, 3],
    "label": ["Normal", "Normal", "Attack"]
}

df = pd.DataFrame(data)
print(df)
