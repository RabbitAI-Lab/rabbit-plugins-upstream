# Transport Cybersecurity & Critical-Infrastructure Protection — In-Depth Framework

> This document presents a systematic in-depth framework for transport-sector cybersecurity and critical-infrastructure (CII) protection. It covers NIST CSF 2.0 mapping, CII identification criteria, control baselines aligned to NIST SP 800-53 / ISO 27001 / NIS2, ISO 21434 vehicle-cybersecurity TARA, defense-in-depth architecture, incident response, product selection, applied cryptography, supply-chain security & SBOM, penetration testing, a compliance checklist, and cost estimation. Data current as of mid-2025.

---

## Table of Contents

1. [NIST CSF 2.0 Mapping for Transport Systems](#i-nist-csf-20-mapping-for-transport-systems)
2. [CII Identification & Protection Regime](#ii-cii-identification--protection-regime)
3. [Control Baselines: NIST SP 800-53 / ISO 27001 / NIS2](#iii-control-baselines-nist-sp-800-53--iso-27001--nis2)
4. [ISO 21434 Vehicle Cybersecurity TARA](#iv-iso-21434-vehicle-cybersecurity-tara)
5. [Defense-in-Depth Security Architecture](#v-defense-in-depth-security-architecture)
6. [Incident Response & Emergency Management](#vi-incident-response--emergency-management)
7. [Security Product Selection Guide](#vii-security-product-selection-guide)
8. [Applied Cryptography (FIPS-Validated)](#viii-applied-cryptography-fips-validated)
9. [Supply-Chain Security & SBOM](#ix-supply-chain-security--sbom)
10. [Penetration Testing Methodology](#x-penetration-testing-methodology)
11. [Compliance Checklist](#xi-compliance-checklist)
12. [Security Build Cost Estimation](#xii-security-build-cost-estimation)

---

## I. NIST CSF 2.0 Mapping for Transport Systems

### 1.1 Mapping the Six CSF 2.0 Functions to Transport Systems

NIST Cybersecurity Framework 2.0 (released February 2024) expands the traditional five functions to six (adding GOVERN). Each function is mapped to transport systems below.

#### **GOVERN**
| CSF subcategory | Transport mapping | Key control | Owner |
|-----------------|-------------------|-------------|-------|
| GV.OC-01 Org cybersecurity strategy | Transport cybersecurity management system | Draft + publish cybersecurity policy | CIIO security office |
| GV.RM-01 Risk-mgmt objectives | Transport risk register | Refresh risk register + risk matrix every 6 months | CISO |
| GV.SC-03 Supply-chain risk mgmt | Vendor security assessment | Vendor security rating + SBOM requirement | Procurement + security |
| GV.RR-01 Roles & responsibilities | Cybersecurity org structure | Define CISO/CIIO duties + staffing | Exec sponsor |
| GV.OC-02 Comms framework | Security incident reporting | Report major incidents to authority within 24h | CIIO |

#### **IDENTIFY**
| CSF subcategory | Transport mapping | Key control | Tool / method |
|-----------------|-------------------|-------------|---------------|
| ID.AM-01 Asset inventory | Transport IT/OT asset register | Include OT assets: controllers / RSUs / cameras / PLCs / SCADA | CMDB + asset platform |
| ID.AM-02 Software inventory | Applications + firmware + 3rd-party components | Versions + patch status + EOL dates | SBOM + SW asset mgmt |
| ID.RA-01 Risk assessment | Annual cybersecurity risk assessment | Threat modeling (TARA/STRIDE) + vuln scan | Pro tools + external firm |
| ID.RA-02 Impact analysis | Business impact analysis (BIA) | Identify RTO/RPO + recovery priority | BIA template |
| ID.IM-01 Data-flow mapping | Transport data-flow diagram | Trace collect → transmit → process → store → share | Data-flow tooling |

#### **PROTECT**
| CSF subcategory | Transport mapping | Specific measure | Tech implementation |
|-----------------|-------------------|------------------|---------------------|
| PR.AA-01 Identity & access | MFA + least privilege | Bastion host + weak-password detection + periodic review | AD/LDAP + IAM + PAM |
| PR.AA-02 Network segmentation | Prod / test / office / internet separation | OT physical/logical isolation + firewall policy | VLAN + ACL + industrial FW |
| PR.DS-01 Data encryption | FIPS-validated AES transmission + RSA/ECC signatures | Mandatory encryption for CII + key mgmt | HSM + KMS |
| PR.DS-02 Data classification | Core / important / general (3 tiers) | Varying storage / transmission / access control | DLP |
| PR.PS-01 Secure config baseline | OS/DB/network device baselines | CIS Benchmark + NIS2/800-53 + crypto config | Automated compliance scanner |
| PR.IR-01 Security training | All-staff awareness + specialist skills | ≥12 training hours/yr + phishing tests | LMS + attack simulation |

#### **DETECT**
| CSF subcategory | Transport mapping | Key capability | Tooling |
|-----------------|-------------------|----------------|---------|
| DE.CM-01 Security monitoring | 7×24 SOC | Log aggregation + correlation + alerting | SIEM + SOAR |
| DE.CM-02 Physical monitoring | Server-room / field-device physical security | Access + video + env monitoring + intrusion alert | Env monitoring + video AI |
| DE.CM-03 OT anomaly detection | ICS anomalies | Protocol anomaly + engineering-change detection | OT IDS (Nozomi/Claroty) |
| DE.AE-01 Event correlation | UEBA user-behavior analytics | Anomalous login / privilege abuse / data exfil | SIEM + UEBA |
| DE.AE-02 Threat intelligence | Transport-sector threat intel | Vuln warnings + block malicious IP/domains | TIP platform |

#### **RESPOND**
| CSF subcategory | Transport mapping | SOP | Timing |
|-----------------|-------------------|-----|:------:|
| RS.MA-01 Incident response plan | Transport cyber incident plan | Incident grading (1–4) + response flow + duties | Drill every 6 months |
| RS.AN-01 Investigation | Root cause + evidence preservation | Log preservation + disk image + memory dump | Within 1h |
| RS.MI-01 Containment | Isolate infected + block attacker IP | Network isolation + disable accounts + pause service | Within 15 min of confirmation |
| RS.CO-01 Internal comms | Escalation chain | CISO → CIIO lead → authority | Major incident within 24h |
| RS.CO-02 External comms | Regulator + public comms | Report to sector regulator / supervisor | Per statutory deadline |

#### **RECOVER**
| CSF subcategory | Transport mapping | Recovery requirement | RTO/RPO |
|-----------------|-------------------|----------------------|:------:|
| RC.RP-01 Recovery plan | DR recovery plan | Per-scenario SOP (corruption / ransomware / hardware / disaster) | Refresh every 6 months |
| RC.CO-01 Backup mgmt | 3-2-1 backup | 3 copies + 2 media + 1 off-site/offline | — |
| RC.CO-03 Recovery validation | Periodic recovery drill | ≥1 recovery drill every 6 months, record results | Post-drill review |
| RC.IM-01 Post-incident | Improvement | Root cause + fixes + policy update + KB update | Within 30 days |

### 1.2 Transport NIST CSF Maturity Self-Assessment

| Function | L1 (Initial) | L2 (Developing) | L3 (Established) | L4 (Optimizing) |
|----------|--------------|-----------------|------------------|-----------------|
| GOVERN | No formal policy | Policy exists, not enforced | Institutionalized + periodic review | Measured + continuous improvement |
| IDENTIFY | No asset inventory | Partial inventory | Full assets + data-flow | Automated asset mgmt |
| PROTECT | Basic firewall | Policy + partial measures | Defense-in-depth + full protection | Adaptive security |
| DETECT | Manual discovery | Partial log collection | SOC + SIEM operations | AI + SOAR automation |
| RESPOND | No plan | Plan unexercised | Plan + regular drills | Automated orchestration |
| RECOVER | No backup | Basic backup | DR + recovery drills | Continuous availability + self-healing |

---

## II. CII Identification & Protection Regime

### 2.1 Transport CII Identification Criteria

**Basis**: Critical-infrastructure protection frameworks such as the EU **NIS2 Directive (2022/2555)**, the **EU CER Directive (2022/2557)**, and the US **CISA critical-infrastructure** regime. Transport is designated an "essential" (NIS2) or "critical" (CER) sector.

**Identification conditions (meeting any one may qualify a system as CII)**:
1. Disruption, loss of function, or data breach that could cause major operational-safety risk and loss of public interest.
2. Important network facilities belonging to key sectors (telecom / energy / finance / transport / water / emergency / health / social security, etc.).

**Per-modal CII identification detail**:

| Transport mode | CII system | Designating authority | Basis | CIIO |
|----------------|-----------|-----------------------|-------|------|
| Rail | CTC/TDCS dispatch, CTCS train control, TRS ticketing (12306) | National rail operator → competent authority | Affects national rail ops | Regional rail bureaus |
| Rail | GSM-R / 5G-R rail dedicated comms | National rail operator | Dispatch-comms lifeline | Regional rail bureaus |
| Road | National ETC tolling network | Authority → network center | Affects national highway transit | Provincial highway cos. |
| Road | Long-tunnel (>3km) monitoring | Provincial transport dept. | Tunnel safety-critical | Road operator |
| Road | Cross-province highway integrated monitoring | Provincial transport dept. | Regional traffic control | Road operator |
| Urban | Urban rail signal (CBTC/TACS) | Municipal transport comm. → authority | Affects public transit | Metro operator |
| Urban | Large city (>2M pop) signal control | Municipal traffic bureau → traffic authority | Affects city order | Transport dept. |
| Urban | Transit dispatch & payment | Municipal transport comm. | Affects public travel | Transit authority |
| Water | Vessel Traffic Service (VTS) | Maritime safety authority | Affects vessel safety | Maritime authority |
| Water | AIS (Automatic Identification System) | Maritime safety authority | National water comms | Maritime authority |
| Water | Large port (>100M t/yr) TOS | Provincial transport dept. → authority | Affects port production | Port authority |
| Aviation | ATC / ATFM | Civil aviation authority | Affects flight safety | ATC provider |
| Aviation | Flight operations control | Civil aviation authority | Affects flight ops | Airline |
| Aviation | 10M+ passenger airport departure/security | Civil aviation authority | Affects airport ops | Airport operator |

### 2.2 CIIO (CII Operator) Legal Duties

**Five core obligations**:

1. **Dedicated security organization** ("top-tier" requirement)
   - Full-time cybersecurity lead (with statutory residency/background rules)
   - Security-org lead participates in cybersecurity decisions
   - Report security status to authority annually

2. **Protective measures**
   - ≥1 security assessment & risk evaluation per year
   - Background checks for critical-role staff
   - Establish monitoring, early-warning, and info-reporting regime

3. **Secure product/service procurement**
   - Procure network products/services that may affect critical systems only after security review
   - Prefer trusted, assured products (effectively requiring sovereign/controllable tech at key links)
   - Sign confidentiality & security agreements clarifying duties

4. **Emergency management**
   - Maintain incident plan; ≥1 drill every 6 months
   - Report major cyber incidents to the authority per regulations

5. **Security evaluation**
   - Self or commissioned assessment ≥1×/year
   - Remediate and report discovered issues promptly

**Penalty benchmarks (NIS2-aligned)**: NIS2 sets fines up to **€10M or 2% of global annual turnover** (essential entities) for serious breaches; US sector regimes impose comparable enforcement. Lower-tier breaches may draw warnings, orders to remediate, or fines up to €7M / 1% of turnover.

---

## III. Control Baselines: NIST SP 800-53 / ISO 27001 / NIS2

### 3.1 Mapping MLPS Tiers to International Baselines

NIST SP 800-53 (Rev. 5), ISO/IEC 27001:2022, and NIS2 define control baselines that map naturally onto the familiar five MLPS tiers. For international programs, use the mapping below.

| Tier | Name | Scenario | Int'l equivalent | Assessment cadence |
|:----:|------|----------|------------------|:------:|
| Tier 1 | Self-protected | Non-essential IS | ISO 27001 (basic) | None mandated |
| Tier 2 | Guided protection | General business systems | NIST 800-53 Low / NIS2 basic | Every 2 years |
| Tier 3 | Supervised protection | Important systems / CII | NIST 800-53 Moderate / NIS2 essential / ISO 27001 + controls | Annual |
| Tier 4 | Mandatory protection | Extreme need (rail control / ATC) | NIST 800-53 High / NIS2 enhanced / IEC 62443 SIL | Every 6 months |
| Tier 5 | Advanced protection | (National security) | Highest-grade | Special |

### 3.2 Ten Control Domains (mapped to NIST SP 800-53 / ISO 27001)

| Domain | Tier 2 | Tier 3 | Tier 4 |
|--------|--------|--------|--------|
| Physical (PE / A.11) | Basic access + fire/theft | + Precision HVAC + video + 7×24 guard | + EM shielding + blast protection |
| Network (SC / A.13) | Basic firewall | + IDS + traffic monitoring + malware defense | + trusted verification + dynamic policy |
| Host (AC / A.8) | ID + access control | + secure baseline + intrusion prevention + patch mgmt | + mandatory access control |
| Application (SA / A.14) | Auth + permissions | + comms integrity + non-repudiation + resource control | + software fault tolerance + trusted path |
| Data (SC / A.8) | Basic backup | + encryption + integrity + masking | + provenance + full lifecycle |
| Security governance | Management system | + systematic system | + quantified KPIs |
| Security organization | Roles | + dedicated staff + approval | + independent audit |
| Personnel security | Onboarding training | + background check + offboarding | + periodic assessment |
| System acquisition (SA / A.15) | Basic design | + secure design review + secure SDLC | + security engineering mgmt |
| System O&M (SI / A.12) | Basic O&M | + change mgmt + incident plan | + continuous monitoring + automation |

### 3.3 Recommended Tiering for Key Transport Systems

| System | Recommended tier | Rationale | Build focus |
|--------|:----------------:|-----------|-------------|
| Rail control (CBTC/TACS) | Tier 4 | Safety-critical, SIL4 | Safety redundancy + 2-out-of-3 + formal verification + physical isolation |
| ATC air traffic control | Tier 4 | Safety-critical | Multi-redundancy + emergency backup + dedicated comms |
| National ETC tolling | Tier 3 | CII + centralized data | FIPS crypto + DR + AI anomaly-tx detection |
| Urban signal control | Tier 3 | Affects city traffic | Audit logging + redundant control + MFA |
| TOC / Intelligent Mobility Platform | Tier 3 | Aggregates sensitive data | Data classification + masking + access control |
| Rail ISCS | Tier 3 | Linked to signaling | OT/IT isolation + industrial-protocol security |
| Transit dispatch | Tier 2/3 | By scale | Dispatch redundancy + payment security + passenger privacy |
| Video surveillance | Tier 2/3 | By scale & data | Video encryption + access + privacy masking |
| Parking platform | Tier 2 | Lower impact | Payment security + data encryption |
| Info-publishing | Tier 2 | Anti-tamper | Content review + signed publish + tamper-proofing |

---

## IV. ISO 21434 Vehicle Cybersecurity TARA

### 4.1 About ISO 21434

ISO/SAE 21434:2021 *Road Vehicles — Cybersecurity Engineering* is the international standard for connected-vehicle cybersecurity. It covers the lifecycle of electrical/electronic (E/E) systems from concept to decommissioning.

**Core process**:
```
Item definition → Threat Analysis & Risk Assessment (TARA) → Risk treatment → Verification & validation → Production & operations monitoring
```

### 4.2 TARA Methodology (Transport Edition)

**TARA = Threat Analysis and Risk Assessment**

**Step 1: Asset identification**
| Asset class | Example | Security property (CIA) |
|-------------|---------|--------------------------|
| Comms data | V2X messages (BSM/RSM/MAP/SPAT) | Integrity + Authenticity + Availability |
| Vehicle control | Remote commands (brake/steer/accelerate) | Integrity + Authenticity + Availability |
| Personal info | Driver identity / location / behavior | Confidentiality + Privacy |
| Roadside devices | RSU / controller / camera firmware & config | Integrity + Availability |
| Key material | PKI cert / private key / symmetric key | Confidentiality + Integrity |

**Step 2: Threat scenarios (STRIDE)**
| Threat | Transport example |
|--------|-------------------|
| Spoofing | Fake RSU sends false road-condition info |
| Tampering | Alter signal-control command |
| Repudiation | Deny sending a hazard-warning message |
| Information Disclosure | Leak vehicle trajectory & location |
| Denial of Service | DDoS against signal-control system |
| Elevation of Privilege | Lateral move from video network to signal network |

**Step 3: Impact assessment (safety relevance)**
| Safety level | ISO 26262 ASIL | Example scenario |
|:------------:|:--------------:|-----------------|
| Severe | ASIL D | Signal tampered → conflicting movement → collision → fatality |
| Major | ASIL C | V2X warning blocked → high-speed rear-end → serious injury |
| Moderate | ASIL B | Guide sign tampered → misrouted to congestion → delay |
| Negligible | QM | Wrong parking guidance → can't find space |

**Step 4: Attack-feasibility assessment**
| Vector | Skill | Time window | Equipment | Opportunity | Feasibility |
|--------|:----:|:----------:|:---------:|:-----------:|:-----------:|
| Air interface (PC5) | Expert | Persistent | Pro (SDR) | Close range | Medium |
| CAN bus injection | Proficient | <5 min | Physical + tools | During service | High |
| Remote OTA hijack | Expert | Persistent | Advanced | Remote | Low |
| Social-engineering phishing | Basic | Weeks | Basic | Persistent | Medium-High |

**Step 5: Risk-level determination**

Risk = Impact severity × Attack feasibility

| Risk level | Treatment | Timing |
|:----------:|-----------|:------:|
| Very high | Must eliminate or reduce (mandatory) | Concept phase |
| High | Must reduce ≥1 level | Before SOP |
| Medium | Decide by cost-benefit | Post-SOP ongoing |
| Low | Acceptable | No action |

> **UNECE R155** (Cybersecurity Management System) makes a CSMS a type-approval prerequisite for vehicles—directly operationalizing ISO 21434 / TARA for OEMs and their V2X infrastructure partners.

---

## V. Defense-in-Depth Security Architecture

### 5.1 Four-Horizontal, Three-Vertical Overlay

To make the layering actionable, we overlay a **four-horizontal (technical layers) × three-vertical (management disciplines)** grid on the classic defense-in-depth stack:

- **Four horizontals (technical layers)**: ① Physical/Environmental → ② Network/Host → ③ Application → ④ Data.
- **Three verticals (disciplines)**: A) Governance & Strategy (policy, risk, compliance) · B) Protection Technology (controls, crypto, segmentation) · C) Operations & Assurance (monitoring, response, audit).

Every control below can be placed at a (horizontal, vertical) coordinate—e.g., "MFA" = (Network/Host, Protection Technology); "annual risk register" = (all, Governance & Strategy).

### 5.2 Five-Layer Defense-in-Depth Model

```
┌──────────────────────────────────────────────────────────────┐
│ L5 Application security — WAF | RASP | API security | code audit | software supply chain │
├──────────────────────────────────────────────────────────────┤
│ L4 Data security — encryption | masking | DLP | watermark | audit | backup | classification │
├──────────────────────────────────────────────────────────────┤
│ L3 Host/Endpoint security — HIDS | EDR | AV | patch | baseline | trusted compute      │
├──────────────────────────────────────────────────────────────┤
│ L2 Network security — FW | IPS | IDS | WAF | VPN | NAC | segmentation | traffic analysis │
├──────────────────────────────────────────────────────────────┤
│ L1 Physical security — access | video | env monitor | fire | UPS | cabinet lock | cable anti-theft │
└──────────────────────────────────────────────────────────────┘
```

### 5.3 Zero-Trust in Transport Systems

**Three zero-trust principles**:
- Never trust, always verify
- Least privilege
- Assume breach

**Transport zero-trust rollout path**:

| Phase | Action | Cycle |
|-------|--------|:----:|
| 1: Identity & access | Unified IAM + MFA + SSO + PAM | 3–6 mo |
| 2: Device trust | Device-health check + NAC + cert mgmt | 3–6 mo |
| 3: Micro-segmentation | App-level segmentation + dynamic FW + ZT gateway | 6–12 mo |
| 4: Data-tier control | Label-based access + data-not-landing + DLP | 6–12 mo |
| 5: Continuous monitoring | UEBA + SOAR + automated threat response | Ongoing |

### 5.4 OT/IT Network Isolation Principles

In transport, OT (signal/toll/sensing/control) and IT (office/mail/admin) must be strictly isolated:

| Measure | Requirement | Exception |
|---------|-------------|-----------|
| Physical/logical isolation | OT & IT on different switches/VLANs | Necessary exchange via one-way gateway |
| Firewall policy | Default-deny, allowlist | Only open required IP + port |
| Security-domain split | ≥5 domains: external / internal / mgmt / OT-prod / OT-sec | — |
| O&M channel | Dedicated O&M net + jump host + audit | No direct internet-to-OT remote |
| Data exchange | One-way guard or dedicated exchange server | No direct file copy OT↔IT |

---

## VI. Incident Response & Emergency Management

### 6.1 Transport Security Incident Grading

| Level | Definition | Example | Response requirement |
|:----:|-----------|---------|----------------------|
| I (Catastrophic) | Cross-province/national impact, or casualties | National ETC outage / CBTC intrusion | Launch within 1h + report to ministry |
| II (Major) | Province-wide / city-wide impact | Citywide signal-control paralysis | Within 2h + report to province |
| III (Serious) | Localized / single line | One highway's monitoring down | Within 4h + report to city |
| IV (Minor) | Individual device/system | Single-intersection controller fault | Respond within 8h |

### 6.2 Transport-Specific Response Playbooks

**Scenario 1: Signal-control system hit by ransomware**
```
T+0min    Confirm attack (ransom note / RDP unreachable / files encrypted)
T+5min    Activate IR team + security management
T+15min   Isolate infected zone (disconnect core signal net from other segments)
T+30min   Assess impact scope (which intersections affected)
T+1h      Enter degraded mode (on-site police manual / fixed timing / flash-yellow)
T+2h      Notify superior authority (traffic mgmt / transport) + start backup
T+4h      Restore data from offline backup (note: backup must not be encrypted too)
T+24–72h  Gradually restore (low-risk zones first) + deploy security patches
T+1–2w    Post-mortem + hardening + report to authority
```

**Scenario 2: ETC tolling data breach**
```
T+0min    Detect abnormal export / external tip / dark-web find
T+15min   Block abnormal channel + suspend suspicious accounts
T+1h      Start forensics (preserve logs / traffic / DB access records)
T+2h      Assess breach scope (which data / how many users / how long)
T+4h      Notify authority (sector regulator / supervisor / toll-network center)
T+24h     Notify affected users (per GDPR/PIPL)
T+3d      Complete incident report + publish notice
T+1–4w    Complete hardening + policy revision + accountability
```

**Scenario 3: V2X message-injection attack**
```
T+0min    RSU security monitor flags abnormal V2X msg (unsigned / abnormal rate)
T+2min    Auto-isolate suspect RSU + switch to degraded mode
T+15min   Security engineer confirms attack type + scope
T+1h      Revoke attacked RSU cert + push CRL
T+4h      Notify OEMs / AV operators (affected V2X msg scope)
T+24h     Deploy patch (PKI hardening / msg-rate limiting)
```

### 6.3 Drill Requirements

| Drill type | Frequency | Participants | Focus |
|------------|:--------:|--------------|-------|
| Tabletop | Quarterly | Security mgmt + technical leads | Process + decision rehearsal |
| Functional | Every 6 mo | Security + O&M teams | Specific-system recovery + backup validation |
| Full-scale | Annually | Whole org + superior + vendors | All-scenario + cross-agency + media handling |

---

## VII. Security Product Selection Guide

### 7.1 Transport Security Product Matrix

| Domain | Product | Global leaders | Selection key points |
|--------|---------|----------------|----------------------|
| Perimeter | NGFW | Palo Alto / Fortinet | OT-protocol recognition |
| Perimeter | IDS/IPS | Cisco / Fortinet | OT deep parsing + low false-positive |
| Perimeter | WAF | F5 / Cloudflare | SQLi/XSS + API security |
| Perimeter | Industrial firewall | Nozomi / Claroty | OT protocols (Modbus/DNP3/OPC) |
| Endpoint | EDR | CrowdStrike / VMware Carbon Black | Low resource + offline detection |
| Endpoint | AV | Symantec / McAfee | OS support + low false-positive |
| Network | NAC | Cisco / Forescout | Dumb-terminal ID (IoT/cameras) |
| Network | VPN / ZT | Zscaler / Netskope | Concurrency capacity |
| Data | DB audit / FW | Imperva / Oracle | DB support + crypto performance |
| Data | DLP | Symantec / Forcepoint | Transport-data type ID + flexible policy |
| Data | Data masking | Informatica / Delphix | Dynamic + format-preserving |
| Central | SIEM | Splunk / IBM QRadar | Log performance + correlation rules |
| Central | SOAR | Palo Alto / Swimlane | Local-platform integration + playbooks |
| Central | Bastion / PAM | CyberArk / BeyondTrust | Audit + MFA + session recording |
| Crypto & IAM | HSM | Thales / Utimaco | FIPS 140-2/3 AES/RSA/ECC performance |
| Crypto & IAM | PKI/CA | DigiCert / Entrust | Cert + OCSP/CRL |
| Vuln mgmt | Scanner | Tenable / Rapid7 | OT scanning + false-positive control |
| OT security | OT asset & anomaly | Nozomi / Claroty / Dragos | Passive ID + OT deep parsing |

> *Regional (APAC) alternatives exist (e.g., Huawei, Sangfor, Qi-Anxin, Venustech, Topsec, WoTrus) and may be mandated by local sovereign-IT rules; evaluate against the same functional criteria and supply-chain assurance.*

### 7.2 Recommendation by Organization Size

| Size | Product bundle | Annual budget (USD) | Security team |
|------|----------------|:------------------:|:------------:|
| Large (province highway / metro / port) | NGFW+IPS+WAF+EDR+SIEM+PAM+DLP+OT+NAC+SOAR | $0.7–2.8M | 10–20 |
| Medium (city traffic / transport authority) | NGFW+IDS/IPS+EDR+SIEM+PAM+vuln scan | $0.2–0.7M | 3–8 |
| Small (county / SME) | NGFW+AV+PAM+MSS | $42k–140k | 1–2 + MSS |

---

## VIII. Applied Cryptography (FIPS-Validated)

### 8.1 FIPS-Validated Algorithms in Transport

| FIPS algorithm | Use in transport | Purpose |
|:--------------:|------------------|---------|
| RSA / ECDSA (FIPS 186) | ETC tx signing, V2X PKI cert, auth | Asymmetric + digital signature |
| SHA-2 / SHA-3 (FIPS 180/202) | Integrity check, MAC, cert hash | Cryptographic hash |
| AES (FIPS 197) | Data-transmission / DB / file / comms / video-stream encryption | Symmetric encryption |
| AES-GCM / HMAC | Message authentication, V2X msg integrity | Authenticated encryption |
| SNOW 3G / AES (3GPP) | 4G/5G air-interface encryption | Stream cipher |

> For deployments under Chinese jurisdiction, substitute the SM series (SM2/SM3/SM4/SM9/ZUC) per national crypto law; for EU/US/NATO-aligned programs, use FIPS 140-2/3-validated modules.

### 8.2 Crypto Requirements for CII Systems

**Statutory basis (NIS2 / sector crypto rules)**: CII systems must use compliant, reviewed cryptography; procured crypto products should carry FIPS 140-2/3 validation (or national equivalent); Tier-3+ systems should pass cryptographic-module assessment.

**Transport CII crypto deployment checklist**:

| System | Mandatory crypto | Recommended crypto | Deadline |
|--------|------------------|-------------------|:--------:|
| ETC tolling | Tx signature (ECDSA), key distribution, SAM | Transmission encryption (AES) | Implemented |
| V2X comms | PKI cert (ECDSA), msg signature | Comms encryption (AES-GCM) | End 2025 |
| Rail signal | Maintenance-terminal auth (ECDSA) | Train-wayside encryption | End 2026 |
| Urban signal | Command signature (ECDSA) | Controller comms encryption | End 2026 |
| TOC / Mobility Platform | Transmission encryption (AES) | Storage encryption | End 2027 |
| Video surveillance | — | Video-stream encryption (AES) | End 2027 (rec.) |

---

## IX. Supply-Chain Security & SBOM

### 9.1 Transport Software Supply-Chain Risks

**Typical risks**:
- Open-source component vulnerabilities (e.g., Log4Shell affected many transport systems)
- Malicious third-party SDK/library
- Vendor dev-environment compromise
- Firmware / BIOS-level malicious implant
- Dependency end-of-life (EOL)

### 9.2 SBOM Requirements

**SBOM = Software Bill of Materials**

Require vendors to provide an SBOM including:
- Component name (open-source lib / 3rd-party SDK / in-house module)
- Version
- License type
- Known vulnerabilities (CVE IDs)
- Dependency tree
- Source (official / mirror / self-built)
- Last update + EOL date

**SBOM formats**: Prefer SPDX or CycloneDX.

### 9.3 Vendor Security Assessment Framework

| Dimension | Items | Weight |
|-----------|-------|:------:|
| Security credentials | 800-53 assessment / ISO 27001 / CMMI / security-service cert | 20% |
| Secure development | SDL / code audit / penetration test | 25% |
| Supply-chain control | SBOM / 3rd-party component mgmt / OSS compliance | 20% |
| Security capability | Vuln response / security team / IR capability | 20% |
| Track record | Major incidents / disclosure / CVEs | 15% |

---

## X. Penetration Testing Methodology

### 10.1 Seven-Phase Penetration Testing Method

```
1. Reconnaissance (OSINT + passive scan)
2. Threat modeling (based on TARA/STRIDE)
3. Vulnerability discovery (network + web + wireless + OT-protocol + physical)
4. Exploitation (penetrate + privilege escalation + lateral movement)
5. Post-exploitation (data-theft simulation + persistence + trace cleanup)
6. Reporting (findings + impact + remediation + risk score)
7. Retest validation (re-test after fixes)
```

### 10.2 Transport-Specific Test Focus

| Target | Focus | Tools / method |
|--------|-------|----------------|
| Signal control | Weak pwd, unauthorized access, protocol injection, firmware, wireless hijack | Nmap / Wireshark / custom scripts |
| ETC | SAM security, tx tamper, replay, MITM | Custom tooling |
| V2X | PC5 sniffing, msg tamper/replay, cert forgery, DoS | SDR + OpenC2X |
| OT/SCADA | Industrial-protocol vuln, PLC firmware, HMI weak pwd, physical bypass | Metasploit / Modbus tools |
| Video | Weak pwd, open RTSP, ONVIF vuln, stream hijack | Hydra / Nmap / Nessus |
| Web | SQLi, XSS, broken access, upload, SSRF, RCE | Burp Suite / SQLmap / AWVS |
| Mobile app | Decompile, data store, API security, cert-pin bypass | MobSF / Frida / Objection |
| Cloud | Misconfig, open bucket, leaked key, container escape | ScoutSuite / Prowler / Trivy |

### 10.3 Test Frequency

| System type | Full pentest | Targeted test | Vuln scan |
|-------------|:------------:|:-------------:|:---------:|
| CII systems | ≥1×/yr | After major update | Quarterly |
| Tier-3 | 1×/yr | After major change | Quarterly |
| Tier-2 | 1×/2yr | After major change | Every 6 mo |
| Public-facing | 1×/yr | On new feature | Monthly |

---

## XI. Compliance Checklist

### 11.1 Transport Cybersecurity Compliance Overview

| # | Requirement | Basis | Check item | Status |
|---|-------------|-------|-----------|:------:|
| 1 | System tiering & filing | NIST 800-53 / ISO 27001 | All systems tiered + documented | [ ] |
| 2 | Control assessment | NIST 800-53 / ISO 27001 | Periodic assessment + cert | [ ] |
| 3 | CII identification | NIS2 / CER Directive | CII identified + dedicated org | [ ] |
| 4 | CII annual assessment | NIS2 | ≥1 security assessment/yr | [ ] |
| 5 | Crypto assessment | FIPS 140-2/3 / sector rules | CII/Tier-3 crypto-module review | [ ] |
| 6 | Data classification | GDPR / sector data law | Classified + protection regime | [ ] |
| 7 | Personal-info protection | GDPR / PIPL | Privacy policy + consent + DPIA | [ ] |
| 8 | Cross-border data | GDPR Chap. V / sector law | Transfer impact assessment if needed | [ ] |
| 9 | Security review of procurement | NIS2 / sector rules | CII procurement security-reviewed | [ ] |
| 10 | Plan + drills | NIS2 / 800-53 | Complete plan + ½-yrly drill | [ ] |
| 11 | Security-lead system | NIS2 / 800-53 | Qualified lead + background check | [ ] |
| 12 | Sovereign-IT compliance | Local rules | Key links controllable/assured | [ ] |
| 13 | Supply-chain security | NIS2 / EO 14028 | Vendor assess + SBOM + agreement | [ ] |
| 14 | Log retention | Sector law | Network logs ≥6 mo + audit trail | [ ] |
| 15 | Security training | 800-53 / NIS2 | All-staff ≥12 h/yr + phishing test | [ ] |
| 16 | Vulnerability mgmt | 800-53 / NIS2 | Regular scan + critical fix ≤30d | [ ] |
| 17 | Incident reporting | NIS2 / sector law | Major incident within 24h | [ ] |
| 18 | Personal-data export | GDPR / PIPL | Transfer assessment + SCC | [ ] |
| 19 | Video-surveillance compliance | GDPR | Publish scope + face-data protection | [ ] |
| 20 | Cloud security | 800-53 / NIS2 | Cloud assessed + data residency | [ ] |

### 11.2 Top-10 Common Tier-3 Assessment Findings

| Rank | Finding | Rate | Remediation |
|:----:|---------|:----:|-------------|
| 1 | No IDS/IPS deployed | 38% | Deploy IDS/IPS, update rules regularly |
| 2 | No periodic log audit | 35% | Enable log audit, retain ≥6 mo |
| 3 | No MFA | 32% | MFA on critical systems (PAM + TOTP) |
| 4 | Data not encrypted in transit | 28% | TLS / VPN / AES encryption |
| 5 | No/inactive security policy | 25% | Build system + periodic checks |
| 6 | No regular vuln scan | 24% | Deploy scanner + fix workflow |
| 7 | No/unverified DR | 22% | DR plan + ½-yrly recovery drill |
| 8 | Chaotic account rights | 20% | Full account lifecycle + periodic review |
| 9 | No training records | 18% | Training plan + exam + archive |
| 10 | Incomplete perimeter defense | 15% | FW + segmentation + ACL |

---

## XII. Security Build Cost Estimation

### 12.1 By Organization Type & Size

**Large (province highway / metro group)** — USD:
| Build item | One-time (USD) | Annual O&M (USD) |
|------------|:--------------:|:----------------:|
| Security products | $1.1–2.8M | $0.28–0.7M |
| SOC build | $0.4–1.1M | $0.21–0.56M |
| Compliance (800-53/NIS2) | $0.14–0.42M | $70k–140k |
| Pentest + red/blue | $110k–280k | $42k–110k/test |
| DR build | $0.7–2.1M | $110k–280k |
| Crypto-module retrofit | $0.21–0.56M | $70k–140k |
| Security staff (10–20) | — | $0.42–1.1M/yr |
| **Total** | **$2.7–7.3M** | **$1.2–3.0M/yr** |

**Medium (city traffic / transport authority)** — USD:
| Build item | One-time (USD) | Annual O&M (USD) |
|------------|:--------------:|:----------------:|
| Security products | $0.28–0.7M | $70k–210k |
| Compliance | $84k–210k | $28k–70k |
| Pentest | $28k–70k | $14k–42k/test |
| DR build | $140k–420k | $28k–70k |
| Security staff (3–8) | — | $126k–336k/yr |
| **Total** | **$0.53–1.4M** | **$0.27–0.73M/yr** |

**Small (county / SME)** — USD:
| Build item | One-time (USD) | Annual O&M (USD) |
|------------|:--------------:|:----------------:|
| Base security + compliance | $70k–210k | $21k–56k |
| MSS managed security | 0 | $42k–112k |
| Security staff (1–2 + MSS) | — | $42k–84k/yr |
| **Total** | **$70k–210k** | **$105k–252k/yr** |

### 12.2 Security Investment as Share of Total IT

| Organization type | Security share | International benchmark |
|-------------------|:--------------:|------------------------|
| CII operator (metro/highway/airport) | 8–15% | US federal agencies: 10–15% |
| Large transport enterprise | 5–10% | Global finance: 7–10% |
| Medium transport unit | 3–8% | — |
| Small transport unit | 2–5% | — |

> *Note: above shares are total security (build + O&M, incl. personnel) as a percentage of total IT spend.*

---

> **Legal Notice**: This document is a reference file of the *Transportation Digital & AI Transformation Expert (Standard Edition)* Skill. Cybersecurity and CII-protection requirements are subject to the latest laws/regulations and authority documents. This content is for study reference only and does not constitute compliance legal advice. Each transport organization should engage qualified professional bodies for security assessment and compliance review.

> **Last updated**: July 2025 | **Version**: v1.0
