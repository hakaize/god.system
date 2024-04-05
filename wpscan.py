import os

class Wordpress():
    def __init__(self, folder_name, folder_dns):
        self.folder_name = folder_name
        self.folder_dns = folder_dns

    def all_wpscan(self):
        command = 'cat {} | grep "WordPress" | httpx -fr -bp -silent -o {} | cut -d ' ' -f 1 | xargs -I % wpscan  --url %'.format(os.path.join(self.folder_name, "all_subdomains_httpx.txt"), os.path.join(self.folder_name, "wpscan.txt"))
        os.system(command)