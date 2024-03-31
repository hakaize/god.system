#!/bin/bash

go install github.com/lc/gau/v2/cmd/gau@latest #gau
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest #subfinder
go install -v github.com/tomnomnom/gf@latest #gf
go install github.com/d3mondev/puredns/v2@latest
git clone https://github.com/1ndianl33t/Gf-Patterns
mkdir .gf
mv ~/Gf-Patterns/*.json ~/.gf #gf-patterns

pip install uro
pip install playwright
pip install regex
pip install argparse
pip install requests
pip3 install py-altdns==1.0.2