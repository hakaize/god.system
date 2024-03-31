import requests, os

class Initial():

    def __init__(self, folder_name):
        self.folder_name = folder_name

    def getGau(self):

        os.system('cat {} | gau --threads 20 | tee -a {}' .format(os.path.join(self.folder_name, "subfinder_results.txt"), os.path.join(self.folder_name, "gau_results.txt")))

    def getUro(self):
        os.system('uro -i {} -o {}'.format(os.path.join(self.folder_name, "gau_results.txt"), os.path.join(self.folder_name , "gau_results_uro.txt")))

    def getHttpx(self):
        os.system('httpx -l gau_results_uro.txt -fr -sc -td -title -bp -silent -o {}'.format(os.path.join(self.folder_name, "httpx_gau_uro_results.txt")))