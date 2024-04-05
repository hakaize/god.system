import os

class BBOT():

    def __init__(self, folder_name):
        self.folder_name = folder_name
        
        
    def startBbot():
        command = 'bbot -t daimler_truck/wildcards_daimler_truck.txt -f subdomain-enum cloud-enum web-basic portscan web-paramminer iis-shortnames subdomain-hijack subdomain-hijack -m nmap gowitness -n my_scan -o .'
        os.system(command)