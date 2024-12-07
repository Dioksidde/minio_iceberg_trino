from pyiceberg.catalog import load_catalog
from pyiceberg.schema import Schema, NestedField
from pyiceberg.types import IntegerType, StringType


catalog = load_catalog(
    name="my_hive",
    catalog_type="hive",
    uri="thrift://localhost:9083",
    warehouse="s3a://warehouse/",
    properties={
        "hive.metastore.uri": "thrift://localhost:9083",
        "fs.s3a.endpoint": "http://localhost:9000",
        "fs.s3a.access.key": "minioadmin",
        "fs.s3a.secret.key": "minioadmin",
        "fs.s3a.path.style.access": "true"
    }
)


schema = Schema(
    NestedField(id=1, name="id", field_type=IntegerType(), required=True),
    NestedField(id=2, name="data", field_type=StringType(), required=False),
)

table = catalog.create_table("default.my_table", schema=schema)
print("Table created:", table)

loaded_table = catalog.load_table("default.my_table")
print("Loaded table:", loaded_table)
