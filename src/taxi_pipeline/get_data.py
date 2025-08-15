import os
import requests
from typing import Optional
from dotenv import load_dotenv

# Configure logging
from .loggins import configure_logging
logger = configure_logging(log_file="get_data.log", logger_name="get_data")

# Charger .env dans os.environ
load_dotenv()
# Define constants
TAXI_TRIPS_TEMPLATE_FILE_PATH = os.getenv("TAXI_TRIPS_TEMPLATE_FILE_PATH")
TAXI_ZONES_FILE_PATH = os.getenv("TAXI_ZONES_FILE_PATH")

def taxi_trips_file(month_to_fetch: str = "2025-06") -> Optional[bool]:
    """
    The raw parquet files for the taxi trips dataset. Sourced from the NYC Open Data portal.
    
    Args:
        month_to_fetch: The month to fetch the data for. Defaults to "2025-06".
    
    Returns:
        Optional[bool]: True if successful, False if failed, None if early return
    """
    try:
        url = f"https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_{month_to_fetch}.parquet"
        
        logger.info(f"Fetching taxi trips data for {month_to_fetch}")
        raw_trips = requests.get(url)
        
        if raw_trips.status_code != 200:
            logger.error(f"Failed to fetch taxi trips data. Status code: {raw_trips.status_code}")
            return None

        output_path = TAXI_TRIPS_TEMPLATE_FILE_PATH.format(month_to_fetch)
        logger.info(f"Writing taxi trips data to {output_path}")
        
        os.makedirs(output_path, exist_ok=True)
        
        try:
            with open(output_path+f"/{month_to_fetch}.parquet", "wb") as output_file:
                output_file.write(raw_trips.content)
            logger.info(f"Successfully wrote taxi trips data to {output_path+f'/{month_to_fetch}.parquet'}")
            return True
        except Exception as e:
            logger.error(f"Failed to write taxi trips data: {str(e)}")
            return False
            
    except requests.exceptions.RequestException as e:
        logger.error(f"Network error while fetching taxi trips data: {str(e)}")
        return False
    except Exception as e:
        logger.error(f"Unexpected error in taxi_trips_file: {str(e)}")
        return False

def taxi_zones_file() -> Optional[bool]:
    """
    The raw CSV file for the taxi zones dataset. Sourced from the NYC Open Data portal.
    
    Returns:
        Optional[bool]: True if successful, False if failed, None if early return
    """
    try:
        url = "https://community-engineering-artifacts.s3.us-west-2.amazonaws.com/dagster-university/data/taxi_zones.csv"
        
        logger.info("Fetching taxi zones data")
        raw_taxi_zones = requests.get(url)
        
        if raw_taxi_zones.status_code != 200:
            logger.error(f"Failed to fetch taxi zones data. Status code: {raw_taxi_zones.status_code}")
            return None

        logger.info(f"Writing taxi zones data to {TAXI_ZONES_FILE_PATH}")
        
        os.makedirs(TAXI_ZONES_FILE_PATH, exist_ok=True)
        
        try:
            with open(TAXI_ZONES_FILE_PATH+"/taxi_zones.csv", "wb") as output_file:
                output_file.write(raw_taxi_zones.content)
            logger.info(f"Successfully wrote taxi zones data to {TAXI_ZONES_FILE_PATH+"/taxi_zones.csv"}")
            return True
        except Exception as e:
            logger.error(f"Failed to write taxi zones data: {str(e)}")
            return False
            
    except requests.exceptions.RequestException as e:
        logger.error(f"Network error while fetching taxi zones data: {str(e)}")
        return False
    except Exception as e:
        logger.error(f"Unexpected error in taxi_zones_file: {str(e)}")
        return False
