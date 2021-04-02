import requests
import json
from pprint import pprint

class YaUploader:
    def __init__(self, token: str):
        self.token = token
        print(token)

    def get_headers(self):
        return {
            'Conten-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    # def get_files_list(self):
    #     files_url = "https://cloud-api.yandex.net/v1/disk/resources/files"
    #     headers = self.get_headers()
    #     response = requests.get(files_url, headers=headers)
    #     pprint(response)
    #     return response.json()


    def _upload_link(self, file_path: str):

        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        pprint(response)
        return response.json()


    def upload(self, file_path, filename):
        href = self._upload_link(file_path=file_path).get("href", "")
        # print(href)
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Sucsess")

if __name__ == '__main__':
    uploader = YaUploader('AQAAAAAWuB_0AAcDCLeAfb92pUlpndy20rowbIE')
    # pprint(uploader.get_files_list())
    result = uploader.upload('my.txt','c:\my_folder\my.txt')

