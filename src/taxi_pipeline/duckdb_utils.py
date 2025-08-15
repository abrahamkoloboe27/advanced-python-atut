import logging
import os

from typing import Optional
from dotenv import load_dotenv
import duckdb

# Configure logging
from .loggins import configure_logging
logger = configure_logging(log_file="duckdb.log", logger_name="duckdb")

# Charger .env dans os.environ
load_dotenv()


DUCKDB_DATABASE = os.getenv("DUCKDB_DATABASE", "../data/nyc.duckdb")
DUCKDB_TABLE_TAXI_TRIPS = os.getenv("DUCKDB_TABLE_TAXI_TRIPS", "taxi_trips")
DUCKDB_TABLE_TAXI_ZONES = os.getenv("DUCKDB_TABLE_TAXI_ZONES", "taxi_zones")


def create_duckdb_connection(
            db_path: Optional[str] = None
) -> duckdb.DuckDBPyConnection:
    """
        Create a connection to duckdb database
        Args:
            db_path: Path to the duckdb database
        Returns:
            duckdb.DuckDBPyConnection: Connection to duckdb database
    """
    db_path = DUCKDB_DATABASE if db_path is None else db_path
    if db_path != ":memory:":
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
    conn = duckdb.connect(database=db_path, read_only=False)
    logger.info("Connexion DuckDB ouverte -> %s", db_path)
    return conn


def create_nyc_database(
            db_path: Optional[str] = None
) -> None:
    """
        Create the nyc database
        Args:
            db_path: Path to the duckdb database
        Returns:
            None
    """
    logger.info("Create the nyc database")
    conn = create_duckdb_connection(db_path)   
    #conn.execute("CREATE DATABASE IF NOT EXISTS nyc")
    logger.info("Create the nyc database")
    conn.close()
    
def create_taxi_zone_table(month: str="2023-03") -> None:
    """
        Create the taxi_zone table
        Args:
            None
        Returns:
            None
    """
    logger.info("Create the taxi_zone table")
    conn = create_duckdb_connection()
    conn.execute(
        f"""
        CREATE OR REPLACE TABLE zones as (
            SELECT
                LocationID AS zone_id,
                zone,
                borough,
                the_geom AS geometry
            FROM '{DUCKDB_TABLE_TAXI_ZONES}'
        );
    """
    )
    #conn.commit()
    logger.info("Create the taxi_zone table")
    conn.close()
    logger.info("Create the taxi_zone table")
    
    
    
def create_taxi_trips_table(month: str="2025-06") -> None:
    """
        Create the taxi_trips table
        Args:
            month: The month to fetch the data for. Defaults to "2023-03".
        Returns:
            None
    """
    logger.info("Create the taxi_trips table")
    conn = create_duckdb_connection()
    conn.execute(
        f"""
        CREATE OR REPLACE TABLE {DUCKDB_TABLE_TAXI_TRIPS} AS (
          SELECT
            VendorID AS vendor_id,
            PULocationID AS pickup_zone_id,
            DOLocationID AS dropoff_zone_id,
            RatecodeID AS rate_code_id,
            payment_type AS payment_type,
            tpep_dropoff_datetime AS dropoff_datetime,
            tpep_pickup_datetime AS pickup_datetime,
            trip_distance AS trip_distance,
            passenger_count AS passenger_count,
            total_amount AS total_amount
          FROM 'data/raw/taxi_trips_{month}.parquet'
            );
        """
    )
    logging.info("Create the taxi_trips table")
    #conn.commit()
    conn.close()
    logger.info("Create the taxi_trips table")