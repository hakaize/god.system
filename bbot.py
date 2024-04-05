import os

class BBOT():

    def __init__(self, folder_name):
        self.folder_name = folder_name
        
        
    def startBbot(self):
        command = 'bbot -t {} -f subdomain-enum cloud-enum web-basic portscan web-paramminer iis-shortnames subdomain-hijack subdomain-hijack -m nmap gowitness -n my_scan -o .'.format(self.folder_name)
        os.system(command)