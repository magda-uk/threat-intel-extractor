import requests
import csv
import os
from dotenv import load_dotenv

# Cargar las variables de entorno
load_dotenv()

# Extraer la clave API de forma segura
API_KEY = os.getenv("ABUSEIPDB_API_KEY")

if not API_KEY:
    raise ValueError("[!] Error: ABUSEIPDB_API_KEY not found in .env file")

def load_iocs(filepath):
    """Reads a text file and extracts a list of IP addresses (IoCs)."""
    try:
        with open(filepath, 'r') as file:
            iocs = [line.strip() for line in file if line.strip()]
        print(f"[*] Successfully loaded {len(iocs)} IoCs from {filepath}")
        return iocs
    except FileNotFoundError:
        print(f"[!] Error: File {filepath} not found.")
        return []

def check_ip_reputation(ip):
    """Queries the AbuseIPDB API for the reputation of an IP address."""
    url = "https://api.abuseipdb.com/api/v2/check"
    
    # Mandatory API parameters
    querystring = {
        'ipAddress': ip,
        'maxAgeInDays': '90'
    }
    
    headers = {
        'Accept': 'application/json',
        'Key': API_KEY
    }
    
    try:
        response = requests.get(url, headers=headers, params=querystring)
        response.raise_for_status()
        data = response.json()
        
        # JSON parsing: extracting the critical data points
        score = data['data']['abuseConfidenceScore']
        country = data['data']['countryCode']
        isp = data['data']['isp']
        
        print(f"[+] IP: {ip} | Risk Score: {score}% | Origin: {country} | ISP: {isp}")
        return data['data']
        
    except requests.exceptions.RequestException as e:
        print(f"[!] API connection error for IP {ip}: {e}")
        return None

def export_triage_csv(results):
    """Exports the parsed threat intelligence data to a CSV file."""
    filename = "triage_report.csv"
    headers = ['IP_Address', 'Risk_Score', 'Country', 'ISP']
    
    try:
        with open(filename, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(headers)
            
            for data in results:
                if data:  # Ensure data is not None
                    writer.writerow([
                        data.get('ipAddress'), 
                        data.get('abuseConfidenceScore'), 
                        data.get('countryCode'), 
                        data.get('isp')
                    ])
        print(f"\n[+] Triage report successfully exported to {filename}")
    except Exception as e:
        print(f"[!] CSV Export Error: {e}")

if __name__ == "__main__":
    suspicious_ips = load_iocs("alerts.txt")
    triage_results = []

    print("\n[*] Starting threat intelligence analysis...")
    for ip in suspicious_ips:
        result = check_ip_reputation(ip)
        triage_results.append(result)
        
    if triage_results:
        export_triage_csv(triage_results)