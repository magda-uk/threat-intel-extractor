# Threat Intelligence Triage Automation

## 🔹 Project Overview: Engineering SOC Automation
In modern Security Operations Centers (SOC), analysts face significant alert fatigue. By applying software engineering principles and REST API integration to defensive operations, this project automates the enrichment of Indicators of Compromise (IoCs). The Python-based tool extracts network artifacts and queries threat intelligence feeds, bridging the gap between raw telemetry and actionable incident response data.

## 🔹 Real-World Integration: Phishing Incident Response
This tool does not operate on theoretical data. It is integrated directly with my 🔗 [Phishing Incident Response Lab](https://github.com/magda-uk/phishing-incident-response-lab/blob/main/README.md) as part of an end-to-end SecOps workflow. 

The IPs analyzed below were extracted from raw `.eml` headers of real-world phishing attacks targeting my personal inboxes, including:
* **Brand Impersonation:** Mercadona Food Box & Doble Pack Gafas campaigns.
* **Financial Fraud:** Advance Fee Fraud (419) and Santander invoice lures.
* **Service Spoofing:** NHS Medicare Kits and UK TV Licence verification phishing.


## 🔹  Threat Intelligence Findings: The Cloud Evasion Paradox
The automated triage against the AbuseIPDB API yielded a critical operational insight: **all extracted origin IPs returned a 0% risk score**. 

Rather than a failure of detection, this highlights a sophisticated evasion strategy by modern threat actors:
1. **Evasion via Cloud Providers (DE, FR, AE):** Attackers hosted malicious infrastructure on legitimate virtual private servers across Hetzner, OVH, and Oracle to leverage their default positive network reputation.
2. **Abuse of Trusted Services (US, FI):** The campaigns actively abused enterprise email marketing platforms (SparkPost/Bird.com) and legitimate webmail gateways (Google LLC) to successfully bypass SPF/DKIM authentication checks.
3. **CDN Masking:** Malicious landing pages were hidden behind Cloudflare reverse proxies to obfuscate the true origin server IP.

**Conclusion:** Static IP reputation is insufficient for modern triage. Because attackers continuously rotate through trusted enterprise infrastructure, automated IP checks must be correlated with behavioral analysis, payload inspection, and URL/Domain intelligence.

## 🔹 SOC Visualization & Triage Reporting
To facilitate rapid decision-making, the Python script exports the enriched data into a structured CSV format. This dataset is ingested into Power BI to generate a geographic heatmap of the attack infrastructure, a standard practice for tracking persistent threat origins.

![Geographic Threat Map](/images/mapa-amenazas.png)
*(Geographic distribution of phishing infrastructure showing nodes across US, Germany, France, Finland, and UAE).*

## 🔹 Future Enhancements
To counter the "0% Risk Score" paradox observed in shared cloud infrastructure, future iterations of this tool will include:
* **VirusTotal API Integration:** Expanding the script to analyze associated domains, URLs, and file hashes to detect malicious payloads hidden behind legitimate CDN proxies.
* **Automated ASN Extraction:** Grouping threat actors by Autonomous System Number to identify systemic abuse in specific hosting providers.

## 🔹Connect with me

[![Magda Dominguez LinkedIn](https://img.shields.io/badge/Magda_Dominguez-Connect_on_LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white&labelColor=000000)](https://www.linkedin.com/in/magda-d-infosec)

I'm actively seeking a Cyber Security / SOC role where I can bring my structured troubleshooting, log analysis, and secure architecture skills to a dedicated security team.