import system, os

class BBOT():
        
    def startBbot():
        command = 'bbot -t daimler_truck/wildcards_daimler_truck.txt -f subdomain-enum cloud-enum web-basic portscan web-paramminer iis-shortnames subdomain-hijack subdomain-hijack -m nmap gowitness nuclei -n my_scan -o .'
        os.system(command)