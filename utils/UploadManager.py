import os
import requests


class UploadManager(object):

    def __init__(self):
        self.aws_proxy = os.getenv("AWS_PROXY")

    def upload_file(self, filename):
        files = {"upload_file": open(filename, "rb").read()}
        r = requests.post(f"{self.aws_proxy}/s3/upload/{filename.split('/')[-1]}",files=files)
        print(r.status_code)

