import re, os


class Parser():
    def __init__(self, folder_name):
        self.folder_name = folder_name

    def detectSSRF(self):
        os.system('cat {} | gf ssrf | tee -a {}'.format(os.path.join(self.folder_name, "gau_results_uro.txt"), os.path.join(self.folder_name, "ssrf.txt")))

    def detectLFI(self):
        os.system('cat {} | gf lfi | tee -a {}'.format(os.path.join(self.folder_name, "gau_results_uro.txt"), os.path.join(self.folder_name, "lfi.txt")))

    def detectRedirect(self):
        os.system('cat {} | gf redirect | tee -a {}'.format(os.path.join(self.folder_name, "gau_results_uro.txt"), os.path.join(self.folder_name, "open_redirect.txt")))

    def detectRCE(self):
        os.system('cat {} | gf rce | tee -a {}'.format(os.path.join(self.folder_name, "gau_results_uro.txt"), os.path.join(self.folder_name, "rce.txt")))

    def detectSQLI(self):
        os.system('cat {} | gf sqli | tee -a {}'.format(os.path.join(self.folder_name, "gau_results_uro.txt"), os.path.join(self.folder_name, "sqli.txt")))

    def detectDebugLogic(self):
        os.system('cat {} | gf debug_logic | tee -a {}'.format(os.path.join(self.folder_name, "gau_results_uro.txt"), os.path.join(self.folder_name, "debug_logic.txt")))


