import os
import dropbox

LeoCam_dir = os.path.abspath(os.path.dirname(__file__))

class DropBoxAgent(object):

    def __init__(self):
        return

    def connect(self):

        config_file = LeoCam_dir + '/DropBox.config'
        app_key = None
        app_secret = None
        access_token = None

        with open(config_file, 'r') as cf:
            exec(cf.read())

        client = dropbox.client.DropboxClient(access_token)

        client_info = client.account_info()

        for info in client_info:
            print info, client_info[info]

        
        

