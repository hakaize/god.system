import os
import requests

wordlist_array = []

class DNS():
    def __init__(self, folder_results, threads):
        self.folder_results = folder_results
        self.threads = threads

    def altDns(self):
        command = 'altdns -i {} -o {} -w {} -t {}'.format(
            os.path.join(self.folder_results, "subfinder_results.txt"),
            os.path.join(self.folder_results, "altdns_results.txt"),
            os.path.join(self.folder_results, "words.txt"),
            self.threads
        )
        os.system(command)

    def getWordlist(self):
        r = requests.get("https://raw.githubusercontent.com/infosec-au/altdns/master/words.txt")
        if r.status_code == 200:
            with open(os.path.join(self.folder_results, "wordlists","resolvers.txt"), 'w') as f:
                f.write(r.text)

    def resolvePureDns(self):
        command = 'puredns {} --write puredns_valids.txt | httpx -fr -sc -td -title -bp -silent -o puredns_httpx.txt' .format(
            os.path.join(self.folder_results, "altdns_results.txt")
        )

    def getResolvers(self):
        r = requests.get("https://raw.githubusercontent.com/danielmiessler/SecLists/master/Miscellaneous/dns-resolvers.txt")
        if r.status_code == 200:
            with open(os.path.join(self.folder_results, "wordlists","resolvers.txt"), 'w') as f:
                f.write(r.text)
