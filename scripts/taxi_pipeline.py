import sys
import os


# Add project root to Python path to allow imports from src
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(project_root)

from src.taxi_pipeline.get_data import (
                        taxi_trips_file,
                        taxi_zones_file,
                    )
#from src.taxi_pipeline.duckdb_utils import create_taxi_trips_table, create_taxi_zone_table,create_nyc_database


# Configure logging
from src.taxi_pipeline.loggins import configure_logging
logger = configure_logging(
                        log_file="taxi_pipeline.log"
        )


if __name__ == "__main__":
    taxi_trips_file()
    taxi_zones_file()
    # create_nyc_database()
    # create_taxi_trips_table()
    # create_taxi_zone_table()
