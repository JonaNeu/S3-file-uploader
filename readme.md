# Simple S3 file uploader

This is a simple upload formula to upload files to your Amazon S3 Bucket without the need of a server.

## Getting Started

You can read about the amazon S3 file uploading [here](https://aws.amazon.com/articles/1434).

First you have to create your policy json snippet and change the urls to your amazon bucket. You can see a simple example in the signer.py file. Use signer.py to create the base64 encoding and the signature of your policy.

Replace the policy and signature placeholder in the index.html file in each of the file uploader forms, also add in your amazon access key.

And you are finished.




## Built With

* [JQuery](https://jquery.com/) - JQuery
