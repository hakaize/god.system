import requests,signal, sys, json, argparse, time
from bs4 import BeautifulSoup

# HARDCODED VARIABLES
loginUrl = "https://securitytrails.com/api/auth/login"
subdomainsUrl = "https://securitytrails.com/list/apex_domain/"
proxy = {'https':'http://127.0.0.1:8080'}

parser = argparse.ArgumentParser(description='SecurityTrails api bypass xd')
parser.add_argument('-m', '--mail')
parser.add_argument('-p', '--password')
parser.add_argument('-c', '--cf_clearance')
parser.add_argument('-f', '--filename')
parser.add_argument('-o', '--output_file')

args = parser.parse_args()

mail = args.mail
password = args.password
cf_clearance = args.cf_clearance
file = args.filename
output_file = args.output_file

#header = {"Cookie": "session=%s"}
#user_agent = {}

def def_handler(sig, frame):
    print("\n[+] Saliendo...")
    exit(1)
signal.signal(signal.SIGINT, def_handler)

def login(mail, password, cf_clearance):
    header = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36", "Cookie": "cf_clearance={}" .format(cf_clearance)}
    loginData = {"email": "{}".format(mail), "password": "{}".format(password)}
    r = requests.post(url = loginUrl, data = loginData, headers = header)
    cookie_header = r.headers.get('set-cookie', '')
    cookie_value = cookie_header.split('SecurityTrails=')[1].split(';')[0].strip()
    return cookie_value

#def makeRequest(url, cookie):
#    cookie = {"":}


def getSubdomains(file, st_cookie_value,  cf_clearance, output_file):
    logged_header = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Cookie": "cf_clearance={}; SecurityTrails={}".format(cf_clearance, st_cookie_value)
    }
    with open(output_file, "w") as output:
        with open(file, "r") as file:
            for line in file:
                for i in range(1,10000):
                    r = requests.get(subdomainsUrl + line.strip() + "?page=%i" % i, headers = logged_header, proxies = proxy, verify=False)
                    soup = BeautifulSoup(r.text, 'html.parser')
                    links = soup.find_all('a',class_='link')
                    time.sleep(2)
                    if "No results found" in r.text:
                        break
                    for link in links:
                        output.write(link.text + "\n")
        

#def getCookie():
    #r = requests.get(url = "https://securitytrails.com/app/auth/login?return=/app/account",)
    #print(r.headers)

    #return 
if __name__ == "__main__":
    st_cookie_value = login(mail, password, cf_clearance)
    getSubdomains(file, st_cookie_value, cf_clearance, output_file)