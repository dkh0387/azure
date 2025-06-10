# coding: utf-8

"""
FILE: samplecode.py
DESCRIPTION:
    This file provides a guided experience in performing a few basic tasks against Azure Blob storage.
USAGE: python samplecode.py
    IMPORTANT:
    Make sure you have retrieved the primary connection string from the pre-deployed storage account
    using the Azure Portal. Find the my_connection_string variable, below, and assign the connection string
    that you copied to that variable by pasting it between the double-quotes.

    Take note of the source_file variable just below the my_connection_string variable. You will need that
    for the last block of code in this exercise.

    Save your work before running the code.
"""
from azure.storage.blob import BlobServiceClient


class PythonBlobLab(object):
    my_connection_string = "DefaultEndpointsProtocol=https;AccountName=az204storageacc20250602;AccountKey=hW7iboZG+G+0aNWhYTZqxIt5Jp9FbaFqUMiF1VqA0/yWYNbsGIjmOY8MMu9yH4wlyjFm0pq7iwDb+ASt1XSsbQ==;EndpointSuffix=core.windows.net"
    source_file = "BlobSample.txt"
    source_container = "democontainer"

    def practice_operations(self):
        # Instantiate a BlobServiceClient using a connection string
        """
        Hint: This requires two lines of code:
        First, you will need to import the BlobServiceClient from azure.storage.blob,
        then, you will instantiate the client object.
        """

        my_blob_service_client = BlobServiceClient.from_connection_string(self.my_connection_string)

        # Instantiate a ContainerClient object and create the container.
        my_container_client = my_blob_service_client.create_container(self.source_container)

        # Instantiate a new BlobClient object
        my_blob_client = my_container_client.get_blob_client("blobforlab")

        # Upload the BlobSample.txt file using the blob client
        with open(self.source_file, "rb") as data:
            my_blob_client.upload_blob(data, blob_type="BlockBlob")

    def copy_operations(self):
        blob_service_client = BlobServiceClient.from_connection_string(self.my_connection_string)

        target_blob_client = blob_service_client.get_blob_client(container="targetcontainer", blob=self.source_file)

        source_blob_url = "https://az204storageacc20250602.blob.core.windows.net/{0}/blobforlab?sp=r&st=2025-06-10T16:57:39Z&se=2025-06-11T00:57:39Z&spr=https&sv=2024-11-04&sr=b&sig=3p63tpLpgKnRs0ez7ngqnRRv3y8Vx4udMFeV%2BRwJkfk%3D".format(
            self.source_container)

        copy_properties = target_blob_client.start_copy_from_url(source_blob_url)

        print("Copy ID:", copy_properties['copy_id'])
        print("Copy status:", copy_properties['copy_status'])

    def properties_operations(self):
        blob_service_client = BlobServiceClient.from_connection_string(self.my_connection_string)
        target_blob_client = blob_service_client.get_blob_client(container="targetcontainer", blob=self.source_file)

        target_blob_properties = target_blob_client.get_blob_properties()
        print(target_blob_properties)

    def set_metadata_operations(self):
        blob_service_client = BlobServiceClient.from_connection_string(self.my_connection_string)
        target_blob_client = blob_service_client.get_blob_client(container="targetcontainer", blob=self.source_file)
        target_blob_client.set_blob_metadata({'CreatedBy': 'Denis Khaskin'})


example = PythonBlobLab()
# example.practice_operations()
# example.copy_operations()
#example.properties_operations()
example.set_metadata_operations()
