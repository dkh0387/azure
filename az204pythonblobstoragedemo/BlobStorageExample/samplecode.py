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

    def practice_operations(self):
        # Instantiate a BlobServiceClient using a connection string
        """
        Hint: This requires two lines of code:
        First, you will need to import the BlobServiceClient from azure.storage.blob,
        then, you will instantiate the client object.
        """

        my_blob_service_client = BlobServiceClient.from_connection_string(self.my_connection_string)

        # Instantiate a ContainerClient object and create the container.
        my_container_client = my_blob_service_client.create_container("democontainer")

        # Instantiate a new BlobClient object
        my_blob_client = my_container_client.get_blob_client("blobforlab")

        # Upload the BlobSample.txt file using the blob client
        with open(self.source_file, "rb") as data:
            my_blob_client.upload_blob(data, blob_type="BlockBlob")


example = PythonBlobLab()
example.practice_operations()
