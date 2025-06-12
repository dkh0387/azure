import os
from azure.cosmos import CosmosClient, PartitionKey

class PythonCosmosLab(object):
    my_connection_string = "AccountEndpoint=https://az204cosmosdb20250611.documents.azure.com:443/;AccountKey=l84vrvnTHGSFZNlLQ5rtg0SjBpETzlmkS6GFQIB3U8mLsoQn6FDg8XsmHZxpREuOYS96UF9rA53LACDbzOzXZg==;"

    def practice_operations(self):
        my_cosmos_client = CosmosClient.from_connection_string(conn_str=self.my_connection_string)

        my_database = my_cosmos_client.create_database_if_not_exists("az204database")

        partition_key_path = PartitionKey(path="/male")

        my_container = my_database.create_container_if_not_exists("cars", partition_key_path)

        generic_item = {'id': '3',
                        'male': 'mercedes'
                        }

        my_container.create_item(body=generic_item)


example = PythonCosmosLab()
example.practice_operations()
