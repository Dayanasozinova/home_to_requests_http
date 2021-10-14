import requests 
import json



class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Accept' : 'application/json',
            'Authorization' : "OAuth " + token
        }
    
    def _get_upload_link(self, path_to_file):
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload/'
        headers = self.get_headers()
        params = {'path': path_to_file, 'overwrite': 'true'}
        response  = requests.get(url=upload_url, headers=headers, params=params)
        return response.json()

    def upload_file_to_disk(self, file_path: str, path_to_file: str):
        response = self._get_upload_link(path_to_file)
        url = response.get("href", "")
        if url:
            response = requests.put(url=url, data=open(file_path, 'rb'))
            response.raise_for_status()
            if response.status_code == 201:
                print('Success')
            else: 
                print('Empty url')



if __name__ == '__main__':
    path_to_file = '/netology/file.txt'
    file_path = 'C:\\Users\\gayaz\\OneDrive\\Рабочий стол\\Sozinova Dayana\\дз пр http\\file.txt'
    token = 'secret'
    uploader = YaUploader(token)
    result = uploader.upload_file_to_disk(file_path, path_to_file)
    print(result)
    