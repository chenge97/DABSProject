import pytest
from pyspark.sql import SparkSession
import os

spark = SparkSession.builder.getOrCreate()
schema = os.environ.get("schema")

def test_bronze_table_record_count():
    """Test that bronze table has expected number of records"""
    
    expected_count = 6896317  # Assuming some records were filtered out
    
    df = spark.sql(f"select * from medallion_dev.{schema}.bronze")
    actual_count = df.count()
    
    assert actual_count == expected_count, \
        f"Expected {expected_count} records in bronze, but found {actual_count}"
    

def test_silver_table_record_count():
    """Test that silver table has expected number of records"""
    
    expected_count = 6717611  # Assuming some records were filtered out
    
    df = spark.sql(f"select * from medallion_dev.{schema}.silver")
    actual_count = df.count()
    
    assert actual_count == expected_count, \
        f"Expected {expected_count} records in silver, but found {actual_count}"