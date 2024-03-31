import os, argparse, requests, signal
from subfinder import Subfinder
from initial_recon import Initial
from parser import Parser
from xss import Xss
from dns import DNS

parser = argparse.ArgumentParser(description='Hakaize Bug Bounty Automation')
parser.add_argument('-x', '--xss', default = "")
parser.add_argument('-p', '--program', help='Programa de bugbounty para hacerle recon (sale arriba en la url)')

args = parser.parse_args()

xss = args.xss
program = args.program
folder_name = program + "_results"
folder_vulns = os.path.join(folder_name, "parsed_vulns")

def def_handler(sig, frame):
    print("\n[+] Saliendo...")
    exit(1)
signal.signal(signal.SIGINT, def_handler)

def createFolders():
    os.makedirs(folder_name)
    os.makedirs(folder_vulns)

if __name__ == "__main__":
    createFolders()
    subfinder = Subfinder(program)
    initial = Initial(folder_name)
    parser = Parser(folder_name)
    xss_tester = Xss(folder_name, xss)
   
    #dominios = subfinder.leerDominios()
    #subfinder.generarSubdominios() 
    #while not subfinder.subdominios_generados:
    #    pass        
    initial.getGau()
    initial.getUro()
    initial.getHttpx()
    dns = DNS("../../daimler_truck", 4)
    dns.getWordlist()
    dns.altDns()

    #if xss != "":
    #    xss_tester.detectXSS()
    #xss_tester.reflectedXSS()
    
    parser.detectSSRF()
    parser.detectLFI()
    parser.detectRedirect()
    parser.detectRCE()
    parser.detectSQLI()
    parser.detectDebugLogic()