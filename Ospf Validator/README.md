# Cisco OSPF Validator

Automates OSPF neighbor validation on Cisco devices.

## Features
- SSH connectivity using Netmiko
- Runs 'show ip ospf neighbor'
- Checks for FULL state
- Generates PASS/FAIL output

## Usage
pip install -r requirements.txt
python ospf_validator.py
