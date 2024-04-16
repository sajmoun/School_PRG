import re

def check_dhcp_config(line: str) -> bool:
    pattern = re.compile(r'^\s*\w+\.\w+\.\w+\s+ha=[\da-fA-F]{12}:ip=\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3};\s*$')
    return bool(pattern.match(line))

def transfer_dhcp_config(text: str) -> str:
    pattern = re.compile(r'\b(\d{1,3}\.\d{1,3}\.\d{1,3}\.)\d{1,3}(;)\s*$')
    substitution = r'\g<1>444\2'
    
    text = pattern.sub(substitution, text)
    return text

