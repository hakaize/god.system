#!/bin/bash

go install github.com/lc/gau/v2/cmd/gau@latest #gau
go install -v github.com/projectdiscovery/subfinder/v2/cmd/subfinder@latest #subfinder
go install -v github.com/tomnomnom/gf@latest #gf
go install github.com/d3mondev/puredns/v2@latest # puredns
go install -v github.com/projectdiscovery/httpx/cmd/httpx@latest # httpx
# GF PATTERNS
git clone https://github.com/1ndianl33t/Gf-Patterns
mkdir .gf
mv ~/Gf-Patterns/*.json ~/.gf #gf-patterns

git clone https://github.com/cramppet/regulator.git #https://github.com/cramppet/regulator