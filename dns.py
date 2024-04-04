import os, re
import requests

wordlist_array = []

class DNS():
    def __init__(self, folder_results, folder_dns, threads):
        self.folder_results = folder_results
        self.folder_dns = folder_dns
        self.threads = threads

    def altDns(self):
        command = 'altdns -i {} -o {} -w {} -t {}'.format(
            os.path.join(self.folder_results, "subfinder_results.txt"),
            os.path.join(self.folder_dns, "altdns_results.txt"),
            os.path.join(self.folder_results, "wordlists", "altdns_words.txt"),
            self.threads
        )
        os.system(command)

    def regulator(self):
        with open(os.path.join(self.folder_results,"clean_wildcards.txt"), 'r') as f:
            for wildcard in f:
                os.system('python3 regulator.py -t {} -f {} -o {}'.format(wildcard.strip(), os.path.join(self.folder_results, "subfinder_results.txt"), os.path.join(self.folder_dns, "regulator_" + wildcard)))

    def resolveRegulator(self):
        with open(os.path.join(self.folder_results,"clean_wildcards.txt"), 'r') as f:
            for wildcard in f:
                os.system('puredns resolve {} -r {} --write {}' .format(
                os.path.join(self.folder_dns, "regulator_" + wildcard.strip()),
                os.path.join(self.folder_results, "wordlists", "resolvers.txt".strip()),
                os.path.join(self.folder_dns, "resolve_regulator" + wildcard.strip())
            ))
    
    def getWordlist(self):
        r = requests.get("https://raw.githubusercontent.com/infosec-au/altdns/master/words.txt", verify=False)
        if r.status_code == 200:
            with open(os.path.join(self.folder_results, "wordlists","altdns_words.txt"), 'w') as f:
                f.write(r.text)

    def resolvePureDns(self):
        command = 'puredns resolve {} --write puredns_valids.txt' .format(
            os.path.join(self.folder_dns, "altdns_results.txt")
        )

    def clearOutput(self):
        # Verificar si el archivo all_dns_subdomains.txt ya existe
        output_file = os.path.join(self.folder_dns, "all_dns_subdomains.txt")
        if not os.path.exists(output_file):
            # Si no existe, crear el archivo
            open(output_file, mode='a').close()
        # Limpiamos la mierda de arriba que creo para poder hacerle el anew
        os.system('rm {}'.format(os.path.join(self.folder_dns, "regulator_*")))
        pattern = re.compile(r"httpx", re.IGNORECASE)
        for file in os.listdir(self.folder_dns):
            match = pattern.search(file)
            if not match:
                os.system('cat {} | anew {}'.format(os.path.join(self.folder_dns, file),os.path.join(self.folder_dns,"all_dns_subdomains.txt")))
        os.system('rm {}'.format(os.path.join(self.folder_dns, "resolve_*")))

    def getResolvers(self):
        r = requests.get("https://raw.githubusercontent.com/trickest/resolvers/main/resolvers.txt", verify=False)
        if r.status_code == 200:
            with open(os.path.join(self.folder_results, "wordlists","resolvers.txt"), 'w') as f:
                f.write(r.text)
