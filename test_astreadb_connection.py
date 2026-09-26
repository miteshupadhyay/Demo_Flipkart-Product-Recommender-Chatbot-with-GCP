from astrapy import DataAPIClient

# Initialize the client
client = DataAPIClient()
db = client.get_database(
  "https://04de9705-a5ca-47c3-b404-aa6ced0de562-us-east-2.apps.astra.datastax.com",
  token="AstraCS:vAnnIufuZWtkpFDmDFIGEJJx:27a7988ea87a632b199d39fa523749d7d5b59135ffc5007d425d2f4361da1c61"
)

print(f"Connected to Astra DB: {db.list_collection_names()}")