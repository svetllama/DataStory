import pandas as pd

def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)

    # Basic cleaning
    df = df.copy()

    # Convert date column
    df['reservation_status_date'] = pd.to_datetime(df['reservation_status_date'], errors='coerce')

    # Replace missing values
    df['children'] = df['children'].fillna(0)
    df['country'] = df['country'].fillna("Unknown")

    # Create total nights feature
    df['total_nights'] = df['stays_in_week_nights'] + df['stays_in_weekend_nights']

    # Create revenue proxy
    df['revenue'] = df['adr'] * df['total_nights']

    return df