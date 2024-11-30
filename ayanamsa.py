from datetime import datetime
from dateutil.relativedelta import relativedelta

def calculate_ayanamsa(date: datetime, method: str = "Lahiri") -> float:
    """
    Calculate Ayanamsa based on the chosen method.
    
    Parameters:
    - date (datetime): The date for which to calculate Ayanamsa.
    - method (str): The Ayanamsa method to use. Options: "Lahiri", "Fagan-Bradley", "Krishnamurti", "Raman".
    
    Returns:
    - float: The Ayanamsa value in degrees.
    """
    # Precession rate in arcseconds per year
    PRECESSION_RATE = 50.290966  # arcseconds/year
    
    # Reference epochs for different Ayanamsa methods
    epochs = {
        "Lahiri": datetime(285, 1, 1),
        "Fagan-Bradley": datetime(221, 1, 1),
        "Krishnamurti": datetime(291, 1, 1),
        "Raman": datetime(397, 1, 1),
    }
    
    if method not in epochs:
        raise ValueError(f"Invalid method: {method}. Choose from {list(epochs.keys())}")
    
    # Calculate the time elapsed since the epoch
    epoch_date = epochs[method]
    elapsed_years = (date - epoch_date).total_seconds() / (365.25 * 24 * 3600)
    
    # Ayanamsa in arcseconds
    ayanamsa_arcseconds = elapsed_years * PRECESSION_RATE
    
    # Convert to degrees
    ayanamsa_degrees = ayanamsa_arcseconds / 3600
    return round(ayanamsa_degrees, 6)

# Example usage
if __name__ == "__main__":
    # User input
    input_date = datetime(2024, 11, 30)  # Change this to your desired date
    methods = ["Lahiri", "Fagan-Bradley", "Krishnamurti", "Raman"]
    
    print(f"Ayanamsa values for {input_date.strftime('%Y-%m-%d')}:")
    for method in methods:
        ayanamsa = calculate_ayanamsa(input_date, method)
        print(f"{method}: {ayanamsa}°")
