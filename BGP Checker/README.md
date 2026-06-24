# Cisco BGP Health Checker

Automates BGP peer validation on Cisco devices.

## Features
- SSH connectivity using Netmiko
- Runs 'show ip bgp summary'
- Checks BGP session health
- Generates PASS/FAIL output

## Usage
pip install -r requirements.txt
python bgp_checker.py
