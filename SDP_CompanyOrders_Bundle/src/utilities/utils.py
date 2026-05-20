from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DoubleType, DateType

def bronze_schema_expectations():
    return {
            'order_id': StringType(),
            'customer_id': StringType(),
            'product_id': StringType(),
            'order_date': DateType(),
            'quantity': IntegerType(),
            'total_amount': DoubleType()
    }

def make_to_struct(schema):
    return StructType([StructField(column, data_type, True) for column, data_type in schema.items()])