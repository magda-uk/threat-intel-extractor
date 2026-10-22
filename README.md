#  Threat Intelligence IoC Extractor

<p align="left">
  <img src="https://img.shields.io/badge/Python-3.11+-3776AB?style=flat-square&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Security-Blue_Team-0052CC?style=flat-square">
  <img src="https://img.shields.io/badge/API-AbuseIPDB-FF6600?style=flat-square">
</p>

## 🔹 Project Overview
This Python-based command-line utility automates the initial triage of suspicious IP addresses (Indicators of Compromise - IoCs). 

Designed for Security Operations Center (SOC) workflows, the script parses local alert logs, queries the **AbuseIPDB REST API** for threat intelligence, and exports the enriched telemetry into a structured CSV report for further defensive analysis.

## 🔹 Core Capabilities
* **Automated Threat Triage:** Batch processes IP addresses from raw text files (`alerts.txt`), simulating SIEM alert extraction workflows.
* **API Integration & JSON Parsing:** Connects to the AbuseIPDB API to retrieve real-time risk scores, geographic origins, and ISP data, efficiently parsing and filtering the JSON payload.
* **Secure Credential Management:** Implements `python-dotenv` to isolate and protect sensitive API keys from version control.
* **Structured Data Export:** Automatically flattens and writes the correlated threat intelligence into a `triage_report.csv` file for seamless integration into ticketing systems or SIEM watchlists.

## 🔹 Installation & Usage

**1. Clone the repository and install dependencies:**
```js
git clone [https://github.com/magda-uk/threat-intel-extractor.git](https://github.com/magda-uk/threat-intel-extractor.git)
cd threat-intel-extractor
pip install requests python-dotenv
```
**2. Configure API Credentials:**
Create a `.env` file in the root directory and add your free AbuseIPDB API key:
```js
ABUSEIPDB_API_KEY=your_api_key_here
```
**3. Run the Analyzer:**
Add suspicious IPs to `alerts.txt` (one per line) and execute the script:
```js
python threat_intel.py
```
## 🔹Connect with me

[![Magda Dominguez LinkedIn](https://img.shields.io/badge/Magda_Dominguez-Connect_on_LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white&labelColor=000000)](https://www.linkedin.com/in/magda-d-infosec)

I'm actively seeking a Cyber Security / SOC role where I can bring my structured troubleshooting, log analysis, and secure architecture skills to a dedicated security team.