export const categoriesData = [
  { numeral: "I", name: "Mass Data Collection & Interception", slug: "mass-data-collection", sortOrder: 1 },
  { numeral: "II", name: "Targeted Hacking & Network Penetration", slug: "targeted-hacking", sortOrder: 2 },
  { numeral: "III", name: "Living-Off-the-Land & Stealth Techniques", slug: "lotl-stealth", sortOrder: 3 },
  { numeral: "IV", name: "Hack-and-Leak Operations", slug: "hack-and-leak", sortOrder: 4 },
  { numeral: "V", name: "Denial-of-Service & Disruption", slug: "dos-disruption", sortOrder: 5 },
  { numeral: "VI", name: "Internet Censorship & Content Control", slug: "censorship-control", sortOrder: 6 },
  { numeral: "VII", name: "Internet Shutdowns & Access Manipulation", slug: "shutdowns-manipulation", sortOrder: 7 },
  { numeral: "VIII", name: "Domestic Surveillance & Legal Frameworks", slug: "domestic-surveillance", sortOrder: 8 },
  { numeral: "IX", name: "Defensive Cyber Methods & Frameworks", slug: "defensive-cyber", sortOrder: 9 },
  { numeral: "X", name: "Intelligence Sharing & Coordination Methods", slug: "intelligence-sharing", sortOrder: 10 },
];

export const methodsData = [
  // Category I: Mass Data Collection & Interception
  { categorySlug: "mass-data-collection", methodNumber: 1, title: "Bulk Internet Metadata Collection", description: "Large-scale automated harvesting of metadata (sender, receiver, timestamps, duration) from emails, calls, and messages across telecom networks.", keywords: ["metadata", "bulk collection", "telecom", "surveillance", "NSA", "SIGINT"] },
  { categorySlug: "mass-data-collection", methodNumber: 2, title: "Fiber-Optic Cable Tapping", description: "Physical or logical interception of data flowing through undersea and terrestrial fiber-optic backbone cables to capture raw internet traffic in transit.", keywords: ["fiber optic", "cable tapping", "undersea cables", "interception", "backbone"] },
  { categorySlug: "mass-data-collection", methodNumber: 3, title: "Upstream Traffic Collection", description: "Intercepting data directly from internet backbone infrastructure (major switches, routers, and cables) rather than from individual endpoints.", keywords: ["upstream", "backbone", "switches", "routers", "traffic collection"] },
  { categorySlug: "mass-data-collection", methodNumber: 4, title: "SMS/MMS Bulk Collection & Analysis", description: "Mass harvesting of text messages globally, searchable by phone number, keyword, content, geolocation, and contact graphs.", keywords: ["SMS", "MMS", "text messages", "bulk collection", "geolocation"] },
  { categorySlug: "mass-data-collection", methodNumber: 5, title: "Full-Take Content Storage", description: "Capturing and storing the complete content of communications (not just metadata) in large data buffers for retrospective analysis.", keywords: ["full-take", "content storage", "data buffer", "retrospective analysis"] },
  { categorySlug: "mass-data-collection", methodNumber: 6, title: "Legal Wiretap Backdoors in Telecom Architecture", description: "Mandated backdoors built into telecom switching equipment to allow lawful interception, which can be exploited by unauthorized parties.", keywords: ["wiretap", "backdoor", "CALEA", "lawful interception", "telecom"] },
  { categorySlug: "mass-data-collection", methodNumber: 7, title: "IoT Device Exploitation for Reconnaissance", description: "Compromising internet-connected cameras, sensors, and smart devices to gather intelligence, conduct surveillance, or map physical environments.", keywords: ["IoT", "smart devices", "cameras", "sensors", "reconnaissance"] },
  { categorySlug: "mass-data-collection", methodNumber: 8, title: "Compromised Security Camera Networks", description: "Leveraging internet-connected cameras lacking encryption and security controls on critical infrastructure networks to conduct espionage.", keywords: ["security cameras", "CCTV", "espionage", "critical infrastructure"] },

  // Category II: Targeted Hacking & Network Penetration
  { categorySlug: "targeted-hacking", methodNumber: 9, title: "Credential Phishing Campaigns", description: "Crafting convincing fake login pages or emails to steal usernames and passwords from high-value targets (officials, executives, researchers).", keywords: ["phishing", "credentials", "spear phishing", "social engineering"] },
  { categorySlug: "targeted-hacking", methodNumber: 10, title: "Telecom Network Infiltration", description: "Long-term persistent access inside telecommunications providers' internal networks to intercept calls, messages, and subscriber data.", keywords: ["telecom", "APT", "persistent access", "infiltration"] },
  { categorySlug: "targeted-hacking", methodNumber: 11, title: "University & Research Network Exploitation", description: "Targeting academic institutions to access research data, intellectual property, and as pivot points to other networks.", keywords: ["university", "academic", "research", "intellectual property", "pivot"] },
  { categorySlug: "targeted-hacking", methodNumber: 12, title: "Supply Chain Compromise (Hardware)", description: "Embedding surveillance or exfiltration capabilities into hardware components (chips, cameras, networking equipment) during manufacturing.", keywords: ["supply chain", "hardware", "implant", "manufacturing", "chip"] },
  { categorySlug: "targeted-hacking", methodNumber: 13, title: "Supply Chain Compromise (Software)", description: "Injecting malicious code into legitimate software updates or dependencies to gain access to downstream users and organizations.", keywords: ["supply chain", "software", "SolarWinds", "dependency", "update"] },
  { categorySlug: "targeted-hacking", methodNumber: 14, title: "Network Backbone Attacks", description: "Targeting core internet routing and switching infrastructure to gain access to massive volumes of traffic or thousands of individual endpoints simultaneously.", keywords: ["backbone", "routing", "BGP", "switching", "infrastructure"] },
  { categorySlug: "targeted-hacking", methodNumber: 15, title: "Social Engineering", description: "Manipulating individuals through psychological techniques (pretexting, impersonation, trust exploitation) to gain unauthorized access to systems or data.", keywords: ["social engineering", "pretexting", "impersonation", "manipulation"] },
  { categorySlug: "targeted-hacking", methodNumber: 16, title: "AI-Driven Intelligence Gathering Tools", description: "Deploying artificial intelligence applications with hidden data exfiltration capabilities embedded in their code to silently transmit user data to external servers.", keywords: ["AI", "artificial intelligence", "data exfiltration", "hidden capabilities"] },

  // Category III: Living-Off-the-Land & Stealth Techniques
  { categorySlug: "lotl-stealth", methodNumber: 17, title: "Living-Off-the-Land (LotL) Techniques", description: "Using legitimate, pre-installed system tools (PowerShell, WMI, built-in admin utilities) to traverse networks and execute operations without deploying detectable malware.", keywords: ["LotL", "PowerShell", "WMI", "fileless", "living off the land"] },
  { categorySlug: "lotl-stealth", methodNumber: 18, title: "Fileless Malware Execution", description: "Running malicious code entirely in memory, leveraging native OS processes, leaving no traditional file-based forensic artifacts.", keywords: ["fileless", "in-memory", "malware", "forensics", "evasion"] },
  { categorySlug: "lotl-stealth", methodNumber: 19, title: "False Front / Proxy Operations", description: "Conducting offensive operations under the cover of fake hacktivist groups or unrelated entities to obscure the true operator's identity.", keywords: ["false flag", "proxy", "hacktivist", "attribution", "cover"] },
  { categorySlug: "lotl-stealth", methodNumber: 20, title: "Hacktivist Proxy Coordination", description: "Outsourcing or coordinating disruptive operations (DDoS, defacement) through ideologically motivated volunteer groups who publicly claim responsibility.", keywords: ["hacktivist", "DDoS", "coordination", "proxy", "volunteer"] },

  // Category IV: Hack-and-Leak Operations
  { categorySlug: "hack-and-leak", methodNumber: 21, title: "Data Exfiltration & Public Release", description: "Stealing sensitive data from compromised systems and publishing it on public platforms to cause reputational, political, or strategic damage.", keywords: ["exfiltration", "data leak", "public release", "WikiLeaks"] },
  { categorySlug: "hack-and-leak", methodNumber: 22, title: "Disinformation Injection into Leaked Data", description: "Embedding fabricated or altered documents within authentic stolen datasets to amplify confusion and undermine trust in the leaked material.", keywords: ["disinformation", "fabricated", "documents", "manipulation"] },
  { categorySlug: "hack-and-leak", methodNumber: 23, title: "Timed Strategic Leaks", description: "Releasing stolen information at politically or strategically calculated moments (before elections, during negotiations) to maximize impact.", keywords: ["timed", "strategic", "election", "political", "leak"] },
  { categorySlug: "hack-and-leak", methodNumber: 24, title: "Selling Exfiltrated Data", description: "Monetizing or weaponizing stolen data by selling it on dark web marketplaces or to interested third parties.", keywords: ["dark web", "marketplace", "selling data", "monetize", "stolen data"] },

  // Category V: Denial-of-Service & Disruption
  { categorySlug: "dos-disruption", methodNumber: 25, title: "Distributed Denial-of-Service (DDoS) Attacks", description: "Flooding target websites and services with massive volumes of traffic to render them unavailable.", keywords: ["DDoS", "flooding", "botnet", "availability", "traffic"] },
  { categorySlug: "dos-disruption", methodNumber: 26, title: "Coordinated Target List Distribution", description: "Publishing curated lists of target IPs/URLs on public forums along with flooding instructions for volunteer participation in DDoS campaigns.", keywords: ["target list", "DDoS", "coordination", "volunteer", "forums"] },
  { categorySlug: "dos-disruption", methodNumber: 27, title: "Destructive Wiper Malware (e.g., WhisperGate-type)", description: "Deploying malware designed to irreversibly destroy data on targeted systems while disguising itself as ransomware.", keywords: ["wiper", "WhisperGate", "destructive", "ransomware", "data destruction"] },
  { categorySlug: "dos-disruption", methodNumber: 28, title: "Website Defacement", description: "Unauthorized modification of public-facing websites to display propaganda, disinformation, or intimidation messages.", keywords: ["defacement", "website", "propaganda", "modification"] },

  // Category VI: Internet Censorship & Content Control
  { categorySlug: "censorship-control", methodNumber: 29, title: "Deep Packet Inspection (DPI)", description: "Inspecting the full payload of network packets in real-time to identify, classify, block, or modify traffic based on content, protocol, or application signatures.", keywords: ["DPI", "packet inspection", "payload", "classification", "filtering"] },
  { categorySlug: "censorship-control", methodNumber: 30, title: "DNS Poisoning / DNS Hijacking", description: "Returning false DNS responses to redirect users to incorrect websites, block access, or serve government-controlled pages.", keywords: ["DNS", "poisoning", "hijacking", "redirect", "blocking"] },
  { categorySlug: "censorship-control", methodNumber: 31, title: "HTTP Host & URL Keyword Filtering", description: "Inspecting HTTP request headers and URLs for banned hostnames or keywords, and injecting block pages or TCP resets when matches are found.", keywords: ["HTTP", "URL filtering", "keyword", "block page", "censorship"] },
  { categorySlug: "censorship-control", methodNumber: 32, title: "TLS Connection Reset Injection", description: "Forcibly aborting encrypted HTTPS/TLS connections by injecting TCP RST packets when targeted SNI (Server Name Indication) values are detected.", keywords: ["TLS", "HTTPS", "TCP RST", "SNI", "connection reset"] },
  { categorySlug: "censorship-control", methodNumber: 33, title: "Protocol Whitelisting", description: "Configuring national-level firewalls to forward only approved protocols (e.g., DNS, HTTP, HTTPS) while silently dropping all other traffic types.", keywords: ["protocol", "whitelist", "firewall", "national", "dropping traffic"] },
  { categorySlug: "censorship-control", methodNumber: 34, title: "Centralized Block Page Redirection", description: "Intercepting forbidden web requests at the network core and redirecting them to a government-controlled block page hosted at a private IP address.", keywords: ["block page", "redirect", "censorship", "centralized", "government"] },
  { categorySlug: "censorship-control", methodNumber: 35, title: "HTTPS / SSH / VPN Throttling & Blocking", description: "Selectively degrading or completely blocking encrypted protocols during periods of civil unrest to prevent circumvention of censorship.", keywords: ["HTTPS", "SSH", "VPN", "throttling", "blocking", "encryption"] },
  { categorySlug: "censorship-control", methodNumber: 36, title: "VPN Signature Detection & Blocking", description: "Using DPI to identify and drop known VPN protocol signatures, even on standard ports like 443, to prevent tunneling past censorship systems.", keywords: ["VPN", "DPI", "signature", "detection", "blocking"] },
  { categorySlug: "censorship-control", methodNumber: 37, title: "DPI-Based Tor / Anonymizer Blocking", description: "Fingerprinting and blocking Tor protocol handshakes and other anonymizing services through deep packet inspection at network chokepoints.", keywords: ["Tor", "anonymizer", "DPI", "fingerprinting", "blocking"] },
  { categorySlug: "censorship-control", methodNumber: 38, title: "Layered Multi-Method Filtering", description: "Combining DNS, HTTP, HTTPS, and protocol-level blocking into a multi-layered censorship architecture for redundancy and thoroughness.", keywords: ["layered", "multi-method", "censorship", "architecture", "redundancy"] },

  // Category VII: Internet Shutdowns & Access Manipulation
  { categorySlug: "shutdowns-manipulation", methodNumber: 39, title: "Stealth Internet Blackout (Selective BGP Manipulation)", description: "Maintaining BGP route visibility while silently filtering traffic at lower layers, creating an invisible blackout where only whitelisted users retain access.", keywords: ["BGP", "blackout", "stealth", "filtering", "whitelisting"] },
  { categorySlug: "shutdowns-manipulation", methodNumber: 40, title: "Full Internet Shutdown", description: "Ordering ISPs to completely sever international internet connectivity for a defined geographic region or entire country.", keywords: ["shutdown", "ISP", "connectivity", "blackout", "severance"] },
  { categorySlug: "shutdowns-manipulation", methodNumber: 41, title: "National Intranet / Domestic-Only Internet", description: "Building a parallel domestic network to keep essential services operational while severing access to the global internet.", keywords: ["intranet", "domestic", "parallel network", "isolation"] },
  { categorySlug: "shutdowns-manipulation", methodNumber: 42, title: "ISP Price Manipulation", description: "Directing ISPs to dramatically increase pricing for international internet access to economically discourage usage.", keywords: ["ISP", "pricing", "economic", "manipulation", "access"] },

  // Category VIII: Domestic Surveillance & Legal Frameworks
  { categorySlug: "domestic-surveillance", methodNumber: 43, title: "Mandatory Data Retention by ISPs/Telecoms", description: "Legally requiring mobile operators and internet service providers to collect, store, and share extensive personal and technical subscriber data with authorities.", keywords: ["data retention", "ISP", "telecom", "mandatory", "subscriber data"] },
  { categorySlug: "domestic-surveillance", methodNumber: 44, title: "Lawful Interception Infrastructure (SORM-type)", description: "Installing government-controlled interception equipment directly at ISP and telecom facilities, enabling real-time monitoring of all traffic without provider involvement.", keywords: ["SORM", "lawful interception", "monitoring", "real-time", "government"] },
  { categorySlug: "domestic-surveillance", methodNumber: 45, title: "Mass Camera Surveillance Networks", description: "Deploying hundreds of millions of networked cameras with facial recognition and behavioral analytics across public spaces.", keywords: ["cameras", "facial recognition", "surveillance", "behavioral analytics"] },
  { categorySlug: "domestic-surveillance", methodNumber: 46, title: "Mandatory VPN Licensing / Prohibition of Unlicensed VPNs", description: "Requiring all VPN services to register with authorities and criminalizing the use of unapproved VPN tools.", keywords: ["VPN", "licensing", "prohibition", "regulation", "criminalization"] },
  { categorySlug: "domestic-surveillance", methodNumber: 47, title: "Targeted Digital Surveillance of Dissidents", description: "Employing spyware, device compromise, and network monitoring to track specific individuals (activists, journalists, organizers).", keywords: ["spyware", "surveillance", "dissidents", "activists", "Pegasus"] },
  { categorySlug: "domestic-surveillance", methodNumber: 48, title: "Malicious Circumvention Tool Distribution", description: "Creating trojanized versions of popular anti-censorship tools (VPNs, proxies) embedded with tracking software that records and reports user activity.", keywords: ["trojanized", "VPN", "proxy", "tracking", "circumvention"] },
  { categorySlug: "domestic-surveillance", methodNumber: 49, title: "Legislation Centralizing Internet Backbone Control", description: "Enacting laws that consolidate control of internet exchange points, international gateways, and backbone infrastructure under a single governmental authority.", keywords: ["legislation", "backbone", "internet exchange", "centralization", "government"] },

  // Category IX: Defensive Cyber Methods & Frameworks
  { categorySlug: "defensive-cyber", methodNumber: 50, title: "Pre-Ransomware Early Warning Notification", description: "Monitoring for early-stage ransomware indicators across networks and proactively notifying affected organizations before encryption occurs.", keywords: ["ransomware", "early warning", "monitoring", "notification", "prevention"] },
  { categorySlug: "defensive-cyber", methodNumber: 51, title: "Known Exploited Vulnerabilities (KEV) Catalog", description: "Maintaining a continuously updated, authoritative catalog of actively exploited vulnerabilities to prioritize patching across all organizations.", keywords: ["KEV", "vulnerabilities", "patching", "CISA", "catalog"] },
  { categorySlug: "defensive-cyber", methodNumber: 52, title: "Network Segmentation", description: "Dividing networks into isolated zones to prevent lateral movement and contain the spread of malicious activity following a breach.", keywords: ["segmentation", "isolation", "lateral movement", "containment"] },
  { categorySlug: "defensive-cyber", methodNumber: 53, title: "Secure Cloud Business Application Hardening", description: "Implementing standardized security baselines for cloud platforms (email, collaboration, storage) to reduce misconfiguration and unauthorized access.", keywords: ["cloud", "hardening", "baseline", "misconfiguration", "security"] },
  { categorySlug: "defensive-cyber", methodNumber: 54, title: "Free/No-Cost Cyber Hygiene Scanning Services", description: "Offering vulnerability scanning, web application assessment, and phishing testing services to organizations at no charge to reduce attack surface.", keywords: ["scanning", "cyber hygiene", "vulnerability", "phishing test", "free"] },
  { categorySlug: "defensive-cyber", methodNumber: 55, title: "Adversarial Framework-Based Security Testing (MITRE ATT&CK)", description: "Continuously testing security controls in production environments against a comprehensive taxonomy of known adversary tactics, techniques, and procedures.", keywords: ["MITRE ATT&CK", "adversarial", "testing", "TTPs", "taxonomy"] },
  { categorySlug: "defensive-cyber", methodNumber: 56, title: "Integrated Cyber Defence Centre", description: "Establishing a centralized facility to enhance real-time network protection, shared situational awareness, and coordination of cyber operations across allied nations.", keywords: ["cyber defence", "centralized", "coordination", "situational awareness"] },
  { categorySlug: "defensive-cyber", methodNumber: 57, title: "Five-Pillar Cybersecurity Architecture", description: "Network & software protection, Data integrity assurance, Hardware security validation, Access & identity controls, Security-by-design & awareness training.", keywords: ["five pillars", "architecture", "defense in depth", "identity", "security by design"] },
  { categorySlug: "defensive-cyber", methodNumber: 58, title: "Quantum-Resistant Cryptography Preparation", description: "Assessing and planning for the risk that quantum computing will break current encryption standards, and beginning migration to post-quantum algorithms.", keywords: ["quantum", "cryptography", "post-quantum", "encryption", "migration"] },
  { categorySlug: "defensive-cyber", methodNumber: 59, title: "Insider Threat Detection Programs", description: "Deploying behavioral analytics, access monitoring, and anomaly detection to identify and mitigate risks from authorized personnel with malicious intent or compromised credentials.", keywords: ["insider threat", "behavioral analytics", "anomaly detection", "access monitoring"] },

  // Category X: Intelligence Sharing & Coordination Methods
  { categorySlug: "intelligence-sharing", methodNumber: 60, title: "Multi-National Intelligence Sharing Alliances", description: "Establishing formal agreements between partner nations to share signals intelligence, cyber threat indicators, and vulnerability data in real time.", keywords: ["intelligence sharing", "alliances", "SIGINT", "Five Eyes", "indicators"] },
  { categorySlug: "intelligence-sharing", methodNumber: 61, title: "Joint Cyber Threat Advisories", description: "Publishing coordinated multi-agency technical advisories detailing observed threat actor TTPs (Tactics, Techniques, and Procedures) to enable collective defense.", keywords: ["advisories", "TTPs", "multi-agency", "threat actors", "collective defense"] },
  { categorySlug: "intelligence-sharing", methodNumber: 62, title: "Coordinated Vulnerability Disclosure", description: "Working with technology vendors and international partners to identify, patch, and publicly disclose software vulnerabilities in a synchronized manner.", keywords: ["CVD", "vulnerability disclosure", "patching", "vendors", "coordinated"] },
];

export const resourcesData: Array<{
  methodNumber: number;
  title: string;
  url: string;
  source: string;
  resourceType: string;
  description: string;
}> = [
  // Method 1: Bulk Internet Metadata Collection
  { methodNumber: 1, title: "CISA: Signals Intelligence Overview", url: "https://www.cisa.gov/topics/cyber-threats-and-advisories", source: "CISA", resourceType: "government", description: "Official CISA resources on cyber threats including bulk collection methods." },
  { methodNumber: 1, title: "EFF: NSA Spying", url: "https://www.eff.org/nsa-spying", source: "EFF", resourceType: "advocacy", description: "Electronic Frontier Foundation's comprehensive overview of NSA surveillance programs." },
  { methodNumber: 1, title: "MITRE ATT&CK: Collection Techniques", url: "https://attack.mitre.org/tactics/TA0009/", source: "MITRE", resourceType: "framework", description: "MITRE ATT&CK framework collection tactics and techniques." },

  // Method 2: Fiber-Optic Cable Tapping
  { methodNumber: 2, title: "Submarine Cable Map", url: "https://www.submarinecablemap.com/", source: "TeleGeography", resourceType: "tool", description: "Interactive map of global submarine fiber-optic cables." },
  { methodNumber: 2, title: "Fiber Optic Tapping Techniques", url: "https://www.schneier.com/tag/fiber-optic-tapping/", source: "Schneier on Security", resourceType: "blog", description: "Bruce Schneier's analysis of fiber-optic interception methods." },

  // Method 3: Upstream Traffic Collection
  { methodNumber: 3, title: "MITRE ATT&CK: Network Sniffing", url: "https://attack.mitre.org/techniques/T1040/", source: "MITRE", resourceType: "framework", description: "Network sniffing technique description in ATT&CK framework." },

  // Method 4: SMS/MMS Bulk Collection
  { methodNumber: 4, title: "SMS Security Best Practices", url: "https://www.nist.gov/topics/cybersecurity", source: "NIST", resourceType: "government", description: "NIST cybersecurity resources covering communications security." },

  // Method 5: Full-Take Content Storage
  { methodNumber: 5, title: "Data at Rest Encryption", url: "https://csrc.nist.gov/topics/security-and-privacy/cryptographic-standards-and-guidelines", source: "NIST CSRC", resourceType: "standard", description: "NIST cryptographic standards for data storage security." },

  // Method 6: Legal Wiretap Backdoors
  { methodNumber: 6, title: "CALEA Technical Standards", url: "https://www.fcc.gov/public-safety-and-homeland-security/policy-and-licensing-division/general/communications-assistance", source: "FCC", resourceType: "government", description: "FCC CALEA compliance and wiretap architecture standards." },

  // Method 7: IoT Device Exploitation
  { methodNumber: 7, title: "OWASP IoT Top 10", url: "https://owasp.org/www-project-internet-of-things/", source: "OWASP", resourceType: "framework", description: "OWASP Internet of Things security project." },
  { methodNumber: 7, title: "NIST IoT Cybersecurity", url: "https://www.nist.gov/programs-projects/nist-cybersecurity-iot-program", source: "NIST", resourceType: "government", description: "NIST IoT cybersecurity program and guidelines." },

  // Method 8: Compromised Security Cameras
  { methodNumber: 8, title: "CISA ICS Security", url: "https://www.cisa.gov/topics/industrial-control-systems", source: "CISA", resourceType: "government", description: "CISA Industrial Control Systems security guidance." },

  // Method 9: Credential Phishing
  { methodNumber: 9, title: "MITRE ATT&CK: Phishing", url: "https://attack.mitre.org/techniques/T1566/", source: "MITRE", resourceType: "framework", description: "Phishing technique classification in MITRE ATT&CK." },
  { methodNumber: 9, title: "Anti-Phishing Working Group", url: "https://apwg.org/", source: "APWG", resourceType: "organization", description: "Anti-Phishing Working Group reports and statistics." },
  { methodNumber: 9, title: "KnowBe4 Phishing Resources", url: "https://www.knowbe4.com/phishing", source: "KnowBe4", resourceType: "vendor", description: "Phishing awareness training and statistics." },

  // Method 10: Telecom Network Infiltration
  { methodNumber: 10, title: "MITRE ATT&CK: Network Service Discovery", url: "https://attack.mitre.org/techniques/T1046/", source: "MITRE", resourceType: "framework", description: "Telecom network discovery and exploitation techniques." },

  // Method 11: University Network Exploitation
  { methodNumber: 11, title: "EDUCAUSE Security Resources", url: "https://www.educause.edu/focus-areas-and-initiatives/policy-and-security/cybersecurity-program", source: "EDUCAUSE", resourceType: "organization", description: "Higher education cybersecurity program resources." },

  // Method 12: Supply Chain Compromise (Hardware)
  { methodNumber: 12, title: "NIST Supply Chain Risk Management", url: "https://csrc.nist.gov/Projects/cyber-supply-chain-risk-management", source: "NIST", resourceType: "government", description: "NIST Cyber Supply Chain Risk Management guidelines." },
  { methodNumber: 12, title: "MITRE ATT&CK: Supply Chain Compromise", url: "https://attack.mitre.org/techniques/T1195/", source: "MITRE", resourceType: "framework", description: "Supply chain compromise techniques in ATT&CK." },

  // Method 13: Supply Chain Compromise (Software)
  { methodNumber: 13, title: "CISA Supply Chain Security", url: "https://www.cisa.gov/supply-chain-compromise", source: "CISA", resourceType: "government", description: "CISA guidance on software supply chain security." },
  { methodNumber: 13, title: "OpenSSF Scorecard", url: "https://securityscorecards.dev/", source: "OpenSSF", resourceType: "tool", description: "Automated security health metrics for open source projects." },

  // Method 14: Network Backbone Attacks
  { methodNumber: 14, title: "BGP Security Resources", url: "https://www.manrs.org/resources/", source: "MANRS", resourceType: "organization", description: "Mutually Agreed Norms for Routing Security resources." },

  // Method 15: Social Engineering
  { methodNumber: 15, title: "SANS Social Engineering Resources", url: "https://www.sans.org/blog/social-engineering-in-cybersecurity/", source: "SANS", resourceType: "education", description: "SANS Institute social engineering awareness resources." },
  { methodNumber: 15, title: "MITRE ATT&CK: Social Engineering", url: "https://attack.mitre.org/techniques/T1598/", source: "MITRE", resourceType: "framework", description: "Social engineering techniques in the ATT&CK framework." },

  // Method 16: AI-Driven Intelligence Gathering
  { methodNumber: 16, title: "NIST AI Risk Management Framework", url: "https://www.nist.gov/artificial-intelligence/executive-order-safe-secure-and-trustworthy-artificial-intelligence", source: "NIST", resourceType: "government", description: "NIST AI security and trustworthiness framework." },

  // Method 17: Living-Off-the-Land
  { methodNumber: 17, title: "LOLBAS Project", url: "https://lolbas-project.github.io/", source: "LOLBAS", resourceType: "tool", description: "Living Off The Land Binaries, Scripts and Libraries catalog." },
  { methodNumber: 17, title: "MITRE ATT&CK: System Binary Proxy Execution", url: "https://attack.mitre.org/techniques/T1218/", source: "MITRE", resourceType: "framework", description: "LotL proxy execution techniques in ATT&CK." },

  // Method 18: Fileless Malware
  { methodNumber: 18, title: "MITRE ATT&CK: Process Injection", url: "https://attack.mitre.org/techniques/T1055/", source: "MITRE", resourceType: "framework", description: "Process injection and fileless execution techniques." },

  // Method 19: False Front Operations
  { methodNumber: 19, title: "MITRE ATT&CK: Masquerading", url: "https://attack.mitre.org/techniques/T1036/", source: "MITRE", resourceType: "framework", description: "Masquerading and false front techniques in ATT&CK." },

  // Method 20: Hacktivist Proxy Coordination
  { methodNumber: 20, title: "CrowdStrike Threat Intel", url: "https://www.crowdstrike.com/en-us/blog/", source: "CrowdStrike", resourceType: "vendor", description: "CrowdStrike blog on hacktivist threat intelligence." },

  // Method 21: Data Exfiltration & Public Release
  { methodNumber: 21, title: "MITRE ATT&CK: Exfiltration", url: "https://attack.mitre.org/tactics/TA0010/", source: "MITRE", resourceType: "framework", description: "Data exfiltration tactics and techniques." },

  // Method 22: Disinformation Injection
  { methodNumber: 22, title: "Stanford Internet Observatory", url: "https://cyber.fsi.stanford.edu/io", source: "Stanford", resourceType: "academic", description: "Stanford research on information operations and disinformation." },

  // Method 23: Timed Strategic Leaks
  { methodNumber: 23, title: "Election Infrastructure Security", url: "https://www.cisa.gov/topics/election-security", source: "CISA", resourceType: "government", description: "CISA election infrastructure security resources." },

  // Method 24: Selling Exfiltrated Data
  { methodNumber: 24, title: "Dark Web Monitoring", url: "https://www.recordedfuture.com/platform/dark-web-monitoring", source: "Recorded Future", resourceType: "vendor", description: "Dark web intelligence and monitoring capabilities." },

  // Method 25: DDoS Attacks
  { methodNumber: 25, title: "Cloudflare DDoS Trends", url: "https://radar.cloudflare.com/security-and-attacks", source: "Cloudflare", resourceType: "vendor", description: "Real-time DDoS attack trends and statistics." },
  { methodNumber: 25, title: "MITRE ATT&CK: Network DoS", url: "https://attack.mitre.org/techniques/T1498/", source: "MITRE", resourceType: "framework", description: "Network denial of service techniques." },

  // Method 26: Coordinated Target List Distribution
  { methodNumber: 26, title: "CISA DDoS Guidance", url: "https://www.cisa.gov/news-events/news/understanding-denial-service-attacks", source: "CISA", resourceType: "government", description: "CISA guidance on understanding and mitigating DDoS attacks." },

  // Method 27: Destructive Wiper Malware
  { methodNumber: 27, title: "MITRE ATT&CK: Data Destruction", url: "https://attack.mitre.org/techniques/T1485/", source: "MITRE", resourceType: "framework", description: "Data destruction and wiper malware techniques." },

  // Method 28: Website Defacement
  { methodNumber: 28, title: "MITRE ATT&CK: Defacement", url: "https://attack.mitre.org/techniques/T1491/", source: "MITRE", resourceType: "framework", description: "Website and internal defacement techniques." },

  // Method 29: Deep Packet Inspection
  { methodNumber: 29, title: "Open Net Initiative", url: "https://opennet.net/", source: "ONI", resourceType: "academic", description: "Research on internet filtering and surveillance technologies." },
  { methodNumber: 29, title: "OONI Explorer", url: "https://explorer.ooni.org/", source: "OONI", resourceType: "tool", description: "Open Observatory of Network Interference - censorship measurement." },

  // Method 30: DNS Poisoning
  { methodNumber: 30, title: "MITRE ATT&CK: DNS Manipulation", url: "https://attack.mitre.org/techniques/T1584/002/", source: "MITRE", resourceType: "framework", description: "DNS manipulation and hijacking techniques." },
  { methodNumber: 30, title: "DNSSEC Deployment Guide", url: "https://www.icann.org/resources/pages/dnssec-what-is-it-why-important-2019-03-05-en", source: "ICANN", resourceType: "standard", description: "ICANN DNSSEC deployment and security resources." },

  // Method 31: HTTP Keyword Filtering
  { methodNumber: 31, title: "Citizen Lab Research", url: "https://citizenlab.ca/category/research/", source: "Citizen Lab", resourceType: "academic", description: "Citizen Lab research on internet censorship and surveillance." },

  // Method 32: TLS Connection Reset
  { methodNumber: 32, title: "Censored Planet", url: "https://censoredplanet.org/", source: "Censored Planet", resourceType: "academic", description: "Global censorship measurement observatory." },

  // Method 33: Protocol Whitelisting
  { methodNumber: 33, title: "Freedom House Internet Freedom", url: "https://freedomhouse.org/report/freedom-net", source: "Freedom House", resourceType: "advocacy", description: "Annual global assessment of internet freedom." },

  // Method 34: Centralized Block Page
  { methodNumber: 34, title: "OONI Block Page Detection", url: "https://ooni.org/post/", source: "OONI", resourceType: "tool", description: "OONI research on block page detection methods." },

  // Method 35: HTTPS/SSH/VPN Throttling
  { methodNumber: 35, title: "Access Now KeepItOn", url: "https://www.accessnow.org/campaign/keepiton/", source: "Access Now", resourceType: "advocacy", description: "Access Now's campaign tracking internet shutdowns globally." },

  // Method 36: VPN Signature Detection
  { methodNumber: 36, title: "VPN Protocol Analysis", url: "https://www.top10vpn.com/research/", source: "Top10VPN", resourceType: "research", description: "VPN protocol detection and censorship research." },

  // Method 37: Tor Blocking
  { methodNumber: 37, title: "Tor Project: Censorship", url: "https://www.torproject.org/", source: "Tor Project", resourceType: "tool", description: "Tor Project resources on censorship circumvention." },

  // Method 38: Layered Multi-Method Filtering
  { methodNumber: 38, title: "Internet Censorship Lab", url: "https://iclab.org/", source: "ICLab", resourceType: "academic", description: "Internet Censorship Lab measurement and analysis." },

  // Method 39: BGP Manipulation
  { methodNumber: 39, title: "RIPE BGP Monitoring", url: "https://www.ripe.net/analyse/internet-measurements/routing-information-service-ris", source: "RIPE NCC", resourceType: "tool", description: "RIPE NCC BGP routing monitoring and analysis." },
  { methodNumber: 39, title: "BGPStream", url: "https://bgpstream.caida.org/", source: "CAIDA", resourceType: "tool", description: "Real-time BGP data streaming and analysis." },

  // Method 40: Full Internet Shutdown
  { methodNumber: 40, title: "Internet Society Shutdowns", url: "https://pulse.internetsociety.org/shutdowns", source: "Internet Society", resourceType: "advocacy", description: "Internet Society tracking of global internet shutdowns." },
  { methodNumber: 40, title: "NetBlocks Internet Observatory", url: "https://netblocks.org/", source: "NetBlocks", resourceType: "tool", description: "Real-time monitoring of internet governance and shutdowns." },

  // Method 41: National Intranet
  { methodNumber: 41, title: "Freedom on the Net Report", url: "https://freedomhouse.org/report/freedom-net", source: "Freedom House", resourceType: "advocacy", description: "Comprehensive assessment of internet freedom worldwide." },

  // Method 42: ISP Price Manipulation
  { methodNumber: 42, title: "ITU ICT Statistics", url: "https://www.itu.int/en/ITU-D/Statistics/Pages/stat/default.aspx", source: "ITU", resourceType: "organization", description: "International Telecommunication Union internet access statistics." },

  // Method 43: Mandatory Data Retention
  { methodNumber: 43, title: "EFF Data Retention Policies", url: "https://www.eff.org/issues/mandatory-data-retention", source: "EFF", resourceType: "advocacy", description: "EFF analysis of mandatory data retention policies worldwide." },

  // Method 44: SORM-type Interception
  { methodNumber: 44, title: "Privacy International Surveillance", url: "https://privacyinternational.org/", source: "Privacy International", resourceType: "advocacy", description: "Research on government surveillance infrastructure worldwide." },

  // Method 45: Mass Camera Surveillance
  { methodNumber: 45, title: "Comparitech Camera Statistics", url: "https://www.comparitech.com/vpn/the-worlds-most-surveilled-cities/", source: "Comparitech", resourceType: "research", description: "Global surveillance camera statistics and analysis." },

  // Method 46: VPN Licensing
  { methodNumber: 46, title: "VPN Legality Map", url: "https://www.top10vpn.com/research/are-vpns-legal/", source: "Top10VPN", resourceType: "research", description: "Global map of VPN legality and restrictions." },

  // Method 47: Targeted Surveillance
  { methodNumber: 47, title: "Amnesty International Digital Surveillance", url: "https://www.amnesty.org/en/tech/", source: "Amnesty International", resourceType: "advocacy", description: "Amnesty's technology and human rights research." },
  { methodNumber: 47, title: "Citizen Lab Pegasus Research", url: "https://citizenlab.ca/", source: "Citizen Lab", resourceType: "academic", description: "Citizen Lab spyware and surveillance research." },

  // Method 48: Malicious Circumvention Tools
  { methodNumber: 48, title: "MITRE ATT&CK: Trojanized Software", url: "https://attack.mitre.org/techniques/T1195/002/", source: "MITRE", resourceType: "framework", description: "Compromise through trojanized software supply chain." },

  // Method 49: Legislation Centralizing Backbone
  { methodNumber: 49, title: "Internet Governance Forum", url: "https://www.intgovforum.org/", source: "IGF", resourceType: "organization", description: "UN Internet Governance Forum on backbone control policies." },

  // Method 50: Pre-Ransomware Warning
  { methodNumber: 50, title: "CISA Pre-Ransomware Notifications", url: "https://www.cisa.gov/stopransomware", source: "CISA", resourceType: "government", description: "CISA's Stop Ransomware initiative and early warning system." },

  // Method 51: KEV Catalog
  { methodNumber: 51, title: "CISA Known Exploited Vulnerabilities", url: "https://www.cisa.gov/known-exploited-vulnerabilities-catalog", source: "CISA", resourceType: "government", description: "Official CISA Known Exploited Vulnerabilities catalog." },
  { methodNumber: 51, title: "NIST National Vulnerability Database", url: "https://nvd.nist.gov/", source: "NIST", resourceType: "government", description: "National Vulnerability Database for CVE tracking." },

  // Method 52: Network Segmentation
  { methodNumber: 52, title: "NIST Network Segmentation Guide", url: "https://csrc.nist.gov/pubs/sp/800/41/r1/final", source: "NIST", resourceType: "standard", description: "NIST guidelines on firewall policies and network segmentation." },

  // Method 53: Cloud Hardening
  { methodNumber: 53, title: "CIS Benchmarks", url: "https://www.cisecurity.org/cis-benchmarks", source: "CIS", resourceType: "standard", description: "Center for Internet Security cloud and application benchmarks." },
  { methodNumber: 53, title: "CISA Secure Cloud Business Applications", url: "https://www.cisa.gov/scuba", source: "CISA", resourceType: "government", description: "CISA SCuBA cloud security project." },

  // Method 54: Free Cyber Hygiene Services
  { methodNumber: 54, title: "CISA Cyber Hygiene Services", url: "https://www.cisa.gov/cyber-hygiene-services", source: "CISA", resourceType: "government", description: "Free CISA vulnerability scanning and assessment services." },

  // Method 55: MITRE ATT&CK Testing
  { methodNumber: 55, title: "MITRE ATT&CK Framework", url: "https://attack.mitre.org/", source: "MITRE", resourceType: "framework", description: "The complete MITRE ATT&CK adversarial framework." },
  { methodNumber: 55, title: "MITRE ATT&CK Evaluations", url: "https://attackevals.mitre-engenuity.org/", source: "MITRE Engenuity", resourceType: "framework", description: "MITRE ATT&CK security product evaluations." },

  // Method 56: Integrated Cyber Defence Centre
  { methodNumber: 56, title: "NATO CCDCOE", url: "https://ccdcoe.org/", source: "NATO", resourceType: "organization", description: "NATO Cooperative Cyber Defence Centre of Excellence." },

  // Method 57: Five-Pillar Architecture
  { methodNumber: 57, title: "NIST Cybersecurity Framework", url: "https://www.nist.gov/cyberframework", source: "NIST", resourceType: "standard", description: "NIST Cybersecurity Framework (CSF) for organizational security." },

  // Method 58: Quantum-Resistant Cryptography
  { methodNumber: 58, title: "NIST Post-Quantum Cryptography", url: "https://csrc.nist.gov/Projects/post-quantum-cryptography", source: "NIST", resourceType: "standard", description: "NIST Post-Quantum Cryptography standardization project." },

  // Method 59: Insider Threat Detection
  { methodNumber: 59, title: "CISA Insider Threat Mitigation", url: "https://www.cisa.gov/topics/physical-security/insider-threat-mitigation", source: "CISA", resourceType: "government", description: "CISA insider threat mitigation resources." },
  { methodNumber: 59, title: "Carnegie Mellon CERT Insider Threat", url: "https://www.sei.cmu.edu/our-work/insider-threat/", source: "CMU CERT", resourceType: "academic", description: "CERT insider threat research and best practices." },

  // Method 60: Intelligence Sharing Alliances
  { methodNumber: 60, title: "CISA Information Sharing", url: "https://www.cisa.gov/topics/cyber-threats-and-advisories/information-sharing", source: "CISA", resourceType: "government", description: "CISA cyber threat information sharing programs." },

  // Method 61: Joint Cyber Threat Advisories
  { methodNumber: 61, title: "CISA Cybersecurity Advisories", url: "https://www.cisa.gov/news-events/cybersecurity-advisories", source: "CISA", resourceType: "government", description: "CISA joint cybersecurity advisories and alerts." },

  // Method 62: Coordinated Vulnerability Disclosure
  { methodNumber: 62, title: "CERT/CC Vulnerability Disclosure", url: "https://www.kb.cert.org/vuls/", source: "CERT/CC", resourceType: "government", description: "CERT Coordination Center vulnerability notes database." },
  { methodNumber: 62, title: "FIRST CVSS Resources", url: "https://www.first.org/cvss/", source: "FIRST", resourceType: "standard", description: "Forum of Incident Response and Security Teams CVSS resources." },
];
