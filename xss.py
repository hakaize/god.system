import requests, os

class Xss():

    def __init__(self, folder_name, xss):
        self.folder_name = folder_name
        self.xss = xss
    
    def detectXSS(self):
        with open(os.path.join(self.folder_name, "gau_results_uro.txt"), "r") as file:
            with open(os.path.join(self.folder_name, "xss_replace.txt"), "w") as output:
                for url in file:
                    domain = str(url.strip())
                    replaced_url = re.sub(r"=[^?\|&]*", '=' + str(self.xss), str(domain) + '\n')
                    if xss in replaced_url:
                        output.write(replaced_url + '\n')

    def reflectedXSS(self):
        with open(os.path.join(self.folder_name, "xss_reflected.txt"), "w") as output:
            with open(os.path.join(self.folder_name, "xss_replace.txt"), "r") as file:
                for url in file:
                    url = url.strip()
                    try:
                        r = requests.get(url = url)
                        if self.xss in r.text:
                            output.write(url)
                    except requests.exceptions.RequestException as e:
                        print("Error en: {} \n\n" .format(url))