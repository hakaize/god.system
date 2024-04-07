import os, argparse, signal
from subfinder import Subfinder
from initial_recon import Initial
from vulns_parser import Parser
from xss import Xss
from dns import DNS
from wpscan import Wordpress

parser = argparse.ArgumentParser(description='Hakaize Bug Bounty Automation')
parser.add_argument('-p', '--program', help='Programa de bugbounty para hacerle recon (sale arriba en la url)')
parser.add_argument('-as', '--aggresivescan', default="xss,wpscan")

args = parser.parse_args()

aggresive_scan = args.aggresivescan
program = args.program

folder_name = program + "_results"
folder_vulns = os.path.join(folder_name, "parsed_vulns")
folder_wpscan = os.path.join(folder_name, "wpscan")
folder_wordlists = os.path.join(folder_name, "wordlists")
folder_dns = os.path.join(folder_name, "dns")

def def_handler(sig, frame):
    print("\n[+] Saliendo...")
    exit(1)
signal.signal(signal.SIGINT, def_handler)

def createFolders():
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        os.makedirs(folder_vulns)
        os.makedirs(folder_dns)
        os.makedirs(folder_wpscan)
        os.makedirs(folder_wordlists)
        os.system('touch {}'.format(os.path.join(folder_name, "all_subdomains.txt")))
    
def passiveEnumeration():
    initial = Initial(folder_name)
    subfinder = Subfinder(program)
    dns = DNS(folder_name , folder_dns, 50)
    parser = Parser(folder_name)
    
    subfinder.leerDominios()
    subfinder.generarSubdominios() 
    while not subfinder.subdominios_generados:
        pass  

    dns.getResolvers()
    dns.getWordlist()
    dns.altDns()  
    dns.regulator()
    dns.resolveRegulator()
    dns.resolvePureDns()
    dns.appendAllSubdomains()
    dns.clearOutput()
    
      
    initial.getGau()
    initial.getUro()
    initial.getHttpx()

    parser.detectSSRF()
    parser.detectLFI()
    parser.detectRedirect()
    parser.detectRCE()
    parser.detectSQLI()
    parser.detectDebugLogic()

if __name__ == "__main__":
    createFolders()
    passiveEnumeration()

    if "xss" in aggresive_scan:
        xss_tester = Xss(folder_name, xss)
        xss_tester.detectXSS()
        xss_tester.reflectedXSS()
    
    if "wpscan" in aggresive_scan:
        wpscan_tester = Wordpress(folder_name, folder_wpscan)
        wpscan_tester.getHttpx()
        wpscan_tester.allWpscan()
