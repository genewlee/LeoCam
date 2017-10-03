import os
import dropbox

class DropBoxAgent(object):

    def __init__(self):
        self.LeoCam_dir = os.path.abspath(os.path.dirname(__file__))
        self.client = None

        self.connect()

    def connect(self):
        '''
        Connect to the Dropbox account
        '''
        config_file = self.LeoCam_dir + '/LeoDropBox.config'
        app_key = None
        app_secret = None
        access_token = None

        try:
            with open(config_file, 'r') as cf:
                exec(cf.read())

            self.client = dropbox.client.DropboxClient(access_token)

        except Exception, e:
            print e

    def get_account_info(self):
        '''
        Return account information of Dropbox account
        '''
        return self.client.account_info()

    def upload (self, filepath):
        '''
        Upload passed in file to Dropbox
        '''

        try:
            f = open(filepath, 'rb')
            filename = os.path.basename(filepath)
            res = self.client.put_file('/' + filename, f)

            print 'uploaded: ', res
            
        except Exception, e:
            print e


