import os
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
            os.path.join(self.folder_results, "altdns_results.txt"),
            os.path.join(self.folder_results, "words.txt"),
            self.threads
        )
        os.system(command)

    def regulator(self):
        with open(os.path.join(self.folder_results,"clean_wildcards.txt"), 'r') as f:
            for wildcard in f:
                os.system('python3 regulator.py -t {} -f {} -o regulator_{}'.format(wildcard.strip(), os.path.join(self.folder_results, "subfinder_results.txt"), os.path.join(self.folder_dns, wildcard)))

    def resolveRegulator(self):
        with open(os.path.join(self.folder_results,"clean_wildcards.txt"), 'r') as f:
            for wildcard in f:
                os.system('puredns regulator_{} --write {} | httpx -fr -sc -td -title -bp -silent -o {}' .format(
            os.path.join(self.folder_dns, wildcard),
            os.path.join(self.folder_dns, "regulator_resolve" + wildcard),
            os.path.join(self.folder_dns, "regulator_resolve_httpx_" + wildcard)
        ))
    
    def getWordlist(self):
        r = requests.get("https://raw.githubusercontent.com/infosec-au/altdns/master/words.txt", verify=False)
        if r.status_code == 200:
            with open(os.path.join(self.folder_results, "wordlists","altdns_words.txt"), 'w') as f:
                f.write(r.text)

    def resolvePureDns(self):
        command = 'puredns {} --write puredns_valids.txt | httpx -fr -sc -td -title -bp -silent -o puredns_httpx.txt' .format(
            os.path.join(self.folder_dns, "altdns_results.txt")
        )

    def getResolvers(self):
        r = requests.get("https://raw.githubusercontent.com/trickest/resolvers/main/resolvers.txt", verify=False)
        if r.status_code == 200:
            with open(os.path.join(self.folder_results, "wordlists","resolvers.txt"), 'w') as f:
                f.write(r.text)
