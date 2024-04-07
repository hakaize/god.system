import os
import subprocess
from urllib.parse import urlparse

class Wordpress():
    def __init__(self, folder_name,folder_wpscan):
        self.folder_wpscan = folder_wpscan
        self.folder_name = folder_name

    def allWpscan(self):
        input_file = os.path.join(self.folder_wpscan, "all_subdomains_httpx_wp.txt")

        # Leer el archivo de entrada línea por línea
        with open(input_file, "r") as f:
            for line in f:
                url = line.strip()
                print(url)
                if "WordPress" in line:
                    # Ejecutar wpscan para el subdominio actual
                    subdomain_name = subprocess.run(['echo', url], stdout=subprocess.PIPE, text=True).stdout.strip()
                    subdomain_name = subprocess.run(['cut', '-d', ' ', '-f', '1'], input=subdomain_name, capture_output=True, text=True).stdout.strip()
                    print(subdomain_name)
                    # Eliminar caracteres no válidos del nombre del subdominio
                    wpscan_command = ["wpscan", "--url", subdomain_name, "--random-user-agent"]
                    result = subprocess.run(wpscan_command, capture_output=True, text=True)
                    subdomain_name = urlparse(subdomain_name)
                    output_file = os.path.join(self.folder_wpscan, f"{subdomain_name.hostname}_wpscan_results.txt")
                    
                    # Escribir los resultados de wpscan en un archivo separado para cada subdominio
                    with open(output_file, "w") as wpscan_output:
                        wpscan_output.write(result.stdout)

    def getHttpx(self):
        os.system('cat {} | httpx -fr -td -o all_subdomains_httpx_wp.txt'.format(os.path.join(self.folder_wpscan, "all_subdomains.txt")))
