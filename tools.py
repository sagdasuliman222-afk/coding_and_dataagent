import pandas as pd
from agents import function_tool

@function_tool
def read_csv(file_path: str) -> str:
    """Read a CSV file and return basic information."""

    df = pd.read_csv(file_path)

    return f"""
    Shape: {df.shape}

    Columns:
    {list(df.columns)}

    First 5 rows:
    {df.head().to_string()}
    """
