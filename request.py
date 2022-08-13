import requests
import os
import sys
import json

if __name__ == "__main__":
    url1 = "http://103.141.140.74:8014/api/comparative"
    url2 = "http://103.141.140.74:8014/api/downloadFile"
    # data_path = sys.argv[1]
    # data = []
    # with open(data_path,"rb") as f:
    #     files = {'data': (data_path, f, 'multipart/form-data', {'Expires': '0'}) }
    #     res = requests.post(url1, files=files)
    #     print("Successful." if json.loads(res.text)['status'] == 0 else "Failed.")
    # file_download = requests.get(url2)
    # file_save = open("returned_file.txt", "wb")
    # file_save.write(file_download.content)
    # file_save.close()
    inp = input("Enter your sentece: ")
    # f = {'text':inp,'features':'comparative'}
    jf = json.dumps(inp)
    res = requests.post(url1, json=inp)