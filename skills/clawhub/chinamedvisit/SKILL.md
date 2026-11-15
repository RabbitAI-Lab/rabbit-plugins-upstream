---
name: chinamedvisit
description: "China Tier-3A hospital international medical center directory, out-of-pocket medical cost estimator (RMB/USD/GBP), visit itinerary planner, and English-Chinese hospital triage phrasebook via ChinaMedVisit."
homepage: https://chinamedvisit.com
version: 1.0.0
license: MIT
compatibility: "Works with Claude Code, Cursor, Windsurf, Cline, OpenClaw, and any MCP client supporting Streamable HTTP."
metadata:
  homepage: "https://chinamedvisit.com"
  mcp_endpoint: "https://chinamedvisit.com/api/mcp"
  version: "1.0.0"
---

# ChinaMedVisit — China Tier-3A Hospital Guide & Medical Cost Estimator

Connects AI coding assistants and travel planners to [**ChinaMedVisit**](https://chinamedvisit.com) via its stateless `streamable-http` Model Context Protocol endpoint (`https://chinamedvisit.com/api/mcp`).

## Available MCP Tools

- **`estimate_china_medical_cost`**: Compare out-of-pocket costs in Chinese RMB and USD between China Tier-3A International Medical Centers (IMC), Private Clinics, US averages, and UK private rates across PET-CT, 3T MRI, endoscopy, and surgical care.
- **`lookup_tier3a_international_hospital`**: Look up verified Tier-3A (三甲) public hospital International Medical Centers (IMC) in Beijing, Shanghai, Guangzhou, Shenzhen, and Chengdu with official addresses, phones, registration portals, and card acceptance.
- **`get_medical_tourism_itinerary_plan`**: Generate a day-by-day China Tier-3A hospital diagnostic schedule (fasting bloodwork, 3T MRI/PET-CT same-day imaging turnaround, and chief physician MDT review) with mandatory medical dossier requirements.
- **`get_bilingual_hospital_phrasebook`**: Retrieve essential English-Chinese-Pinyin hospital communication phrases for registration desks, symptom description, drug allergy alerts, radiology consent, and pharmacy pickups.
- **`check_china_medical_visa_and_payment_prep`**: Verify payment methods accepted by Chinese public Tier-3A IMC desks (Visa, Mastercard, Alipay/WeChat Pay foreign card binding, CNY cash) and passport registration rules for 240h TWOV vs medical visas.
- **`compare_tier3a_imc_vs_private_hospital`**: Compare China national academic public Tier-3A International Medical Centers (PUMCH, Huashan, Ruijin) against private international clinics across academic subspecialty depth, cost, wait time, and English support.

## Official Web Workbenches & Reference

- [**China Medical Cost Estimator (PET-CT, MRI, MDT)**](https://chinamedvisit.com/cost-calculator)
- [**Verified China Tier-3A IMC Hospital Directory**](https://chinamedvisit.com/hospitals)
- [**China Outpatient Visit Itinerary Planner**](https://chinamedvisit.com/planner)
- [**Patient Survival Kit & Bilingual Hospital Guide**](https://chinamedvisit.com/guide)
- [**Machine-Readable Corpus**](https://chinamedvisit.com/llms.txt)
