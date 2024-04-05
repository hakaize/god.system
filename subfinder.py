import time, re, os
from playwright.sync_api import sync_playwright

class Subfinder:

    def __init__(self, program_name):
        self.subf_url = "https://hackerone.com/{}/policy_scopes".format(program_name)
        self.folder_name = program_name + "_results"
        self.subdominios_generados = False
        

    def leerDominios(self):
        if not os.path.exists(self.folder_name):
            os.makedirs(self.folder_name)

        with sync_playwright() as p:
            browser = p.firefox.launch(headless=False)
            context = browser.new_context(user_agent="Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:124.0) Gecko/20100101 Firefox/124.0")
            page = browser.new_page()
            
            page.goto(self.subf_url)

            page.wait_for_timeout(3000)
           
            html = page.content()
            lista = []
            wildcards_length = page.evaluate("document.getElementsByClassName('spec-asset-identifier break-words').length")
            with open(os.path.join(self.folder_name, "wildcards.txt"), "w") as output:
                for i in range(wildcards_length):
                    title = page.evaluate(f"document.getElementsByClassName('spec-asset-identifier break-words')[{i}].getElementsByTagName('strong')[0].getAttribute('title')")
                    if '.' in title or '*' in title:
                        output.write(title + "\n")

    def generarSubdominios(self):
        with open(os.path.join(self.folder_name, "clean_wildcards.txt"), "w") as output:
            with open(os.path.join(self.folder_name, "wildcards.txt"), "r") as file:
                regex = re.compile(r'^\*\.|^(\*)')
                for domain in file:
                    if '.' not in domain or '*' not in domain:
                        continue 
                    clean_domain = regex.sub('', domain)
                    output.write(clean_domain)
                
        os.system("subfinder -all -dL {} -o {}".format(os.path.join(self.folder_name, "clean_wildcards.txt"), os.path.join(self.folder_name, "subfinder_results.txt")))
        self.subdominios_generados = True