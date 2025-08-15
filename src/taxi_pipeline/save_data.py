import os
import requests
import logging
from typing import Optional
from dotenv import load_dotenv

# Configure logging
from .loggins import configure_logging
logger = configure_logging(log_file="save_data.log", logger_name="save_data")

# Charger .env dans os.environ
load_dotenv()
# Define constants
TAXI_TRIPS_TEMPLATE_FILE_PATH = os.getenv("TAXI_TRIPS_TEMPLATE_FILE_PATH")
TAXI_ZONES_FILE_PATH = os.getenv("TAXI_ZONES_FILE_PATH")
DUCKDB_FILE_PATH = os.getenv("DUCKDB_FILE_PATH")

def save_taxi_zones() -> None:
    """
        Save the taxi zone file in duckdb database
        Args:
            None
        Returns:
            None
    """
    logger.info("Save taxi zones file in duckdb database")

def save_taxi_trips_file() -> None:
    """
        Save the taxi trips file in duckdb database
        Args:
            None
        Returns:
            None
    """