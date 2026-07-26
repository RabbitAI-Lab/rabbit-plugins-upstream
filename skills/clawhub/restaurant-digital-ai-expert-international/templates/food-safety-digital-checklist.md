# Food Safety Digital Checklist (HACCP-Based)

## Instructions
A digital food safety inspection tool based on HACCP's seven principles, aligned with the FDA Food Code (United States), ISO 22000:2018 (International), and EU Regulation (EC) No 852/2004 where applicable. This checklist is designed for digitization -- each inspection point maps to a specific digital control mechanism. See also: [Digital Maturity Assessment](./digital-maturity-assessment-report-template.md) to baseline your food safety digital maturity level.

---

## 1. Receiving & Inbound Inspection

| # | Check Item | Standard Requirement | Digital Method | Status |
|---|-----------|---------------------|----------------|:------:|
| 1.1 | Supplier qualification | Business license + food safety certification valid and current | Supplier management system auto-expiry alerts | [ ] |
| 1.2 | Receiving records | Certificate of analysis / inspection report for every batch | Scan-to-record + image archive + auto-verification | [ ] |
| 1.3 | Shelf-life management | Record at receiving; system-driven expiry alerts | Inventory management + auto-alert 3 days / 1 day before expiry | [ ] |
| 1.4 | Cold chain temperature | Record cold-chain vehicle temperature at receiving | Bluetooth thermometer + auto-upload | [ ] |
| 1.5 | Supplier documentation | Digitally stored, retrievable on demand | OCR scan + auto-classification + archive | [ ] |

---

## 2. Storage Management

| # | Check Item | Standard Requirement | Digital Method | Status |
|---|-----------|---------------------|----------------|:------:|
| 2.1 | Temperature & humidity monitoring | Freezer <= 0 degF (-18 degC) / Refrigerator 32--40 degF (0--4 degC) / Dry storage < 77 degF (25 degC) per FDA Food Code | IoT sensors + real-time monitoring + anomaly auto-alerts | [ ] |
| 2.2 | FIFO (First-In, First-Out) | Use oldest production-date stock first | System auto-sorts by batch date for FIFO picking | [ ] |
| 2.3 | Inventory count | Daily (critical items) / Weekly (all items) / Monthly (full) | PDA / mobile count + auto variance analysis | [ ] |
| 2.4 | Expiry management | No expired ingredients in use | Auto-lock item at expiry + block from issuing | [ ] |
| 2.5 | Pest control | Regular inspections; insect light traps functional | IoT pest monitoring + scheduled inspection records | [ ] |

---

## 3. Food Preparation (Kitchen CCP Controls)

| # | CCP (Critical Control Point) | Standard Requirement | Digital Method | Status |
|---|------------------------------|---------------------|----------------|:------:|
| 3.1 | Employee health | Daily health check; valid food handler certification | Certification management system with expiry alerts + digital morning check records | [ ] |
| 3.2 | Hand hygiene | Wash and sanitize hands before entering prep area per FDA Food Code | IoT hand-wash monitoring (optional) + timed reminders | [ ] |
| 3.3 | Cooking temperature | Internal temperature >= 165 degF (74 degC) per FDA Food Code | Probe thermometer + auto-record + upload to cloud | [ ] |
| 3.4 | Cooling temperature | Hot food -> 70 degF (21 degC) within 2 hours -> 41 degF (5 degC) within 4 additional hours | Auto temperature logging + anomaly alerts | [ ] |
| 3.5 | Cross-contamination | Raw/cooked separation; protein/produce separation; color-coded tools | AI video recognition (optional) + inspection photos | [ ] |
| 3.6 | Frying oil management | Total polar compounds <= 27% (or per local regulation) | Oil quality tester + digital log | [ ] |
| 3.7 | Food additive control | Designated person / cabinet / ledger / tools / quantity ("5-D" principle) | Digital additive ledger + auto-usage validation | [ ] |

---

## 4. Food Sample Retention

| # | Check Item | Standard Requirement | Digital Method | Status |
|---|-----------|---------------------|----------------|:------:|
| 4.1 | Retention scope | Every meal period, every menu item | System auto-generates retention checklist | [ ] |
| 4.2 | Sample quantity | >= 125 g (4.4 oz) per item | RFID / barcode label + weight association | [ ] |
| 4.3 | Retention duration | 48 hours (or per local regulation) | System timer + disposal reminder | [ ] |
| 4.4 | Retention records | Item name / date / time / person responsible | Digital retention ledger | [ ] |

---

## 5. Cleaning & Sanitizing

| # | Check Item | Standard Requirement | Digital Method | Status |
|---|-----------|---------------------|----------------|:------:|
| 5.1 | Utensil sanitizing | Hot water >= 171 degF (77 degC) for 30 seconds OR chemical sanitizer at correct concentration per FDA Food Code | IoT temperature sensor + auto-record | [ ] |
| 5.2 | Sanitizer concentration | Chlorine-based 50--100 ppm (or per manufacturer / local regulation) | Concentration test + digital record | [ ] |
| 5.3 | Dishwasher temperature | Wash >= 150 degF (66 degC) / Rinse >= 180 degF (82 degC) | Auto temperature monitoring + anomaly alerts | [ ] |
| 5.4 | Clean equipment storage | Covered / clean / clearly labeled | Inspection photos + scheduled check records | [ ] |

---

## 6. Waste Management

| # | Check Item | Standard Requirement | Digital Method | Status |
|---|-----------|---------------------|----------------|:------:|
| 6.1 | Food waste | Daily removal; designated containers | Weight recording + collection log | [ ] |
| 6.2 | Waste oil / grease | Collected by licensed recycler | Digital recycling records + vendor license management | [ ] |
| 6.3 | Expired food | Separate storage + labeled + documented disposal | Issue record + destruction record fully traceable | [ ] |

---

## 7. Traceability & Recall

| # | Check Item | Standard Requirement | Digital Method | Status |
|---|-----------|---------------------|----------------|:------:|
| 7.1 | Batch traceability | Every ingredient batch traceable to supplier / production date / lot number | Full-chain scan traceability (supplier -> receiving -> usage -> served item) | [ ] |
| 7.2 | Forward trace | A batch of ingredients -> which menu items -> served to which customers | Inventory + POS + loyalty linkage | [ ] |
| 7.3 | Backward trace | A menu item -> which batches of which ingredients were used | Recipe costing card + BOM reverse lookup | [ ] |
| 7.4 | Mock recall drill | Annual simulated recall exercise per FDA / ISO 22000 guidelines | System-simulated trace -> measure trace time (target: < 4 hours) | [ ] |

---

## 8. Kitchen Transparency ("Open Kitchen")

| # | Check Item | Standard Requirement | Digital Method | Status |
|---|-----------|---------------------|----------------|:------:|
| 8.1 | Kitchen video monitoring | Full coverage of critical areas (no blind spots) | Video surveillance + cloud storage (>= 30 days) | [ ] |
| 8.2 | Customer visibility | Dining area display OR QR-code-accessible live kitchen feed | QR code -> view kitchen live stream | [ ] |
| 8.3 | AI behavior detection | Detect: no mask / smoking / pest activity / other violations | AI video analytics + real-time alerts | [ ] |
| 8.4 | Regulatory integration | Connect to local health authority's digital inspection platform where applicable | Video stream push to regulatory platform | [ ] |

---

## 9. Record Digitization

| Record Type | Traditional Method | Digital Method |
|-------------|-------------------|----------------|
| Daily morning health check | Paper + signature | Mobile form + digital signature + cloud storage |
| Receiving / procurement log | Paper ledger | Scan + voice input + auto-archive |
| Temperature monitoring log | Manual thermometer + handwritten | IoT sensors + auto-recording |
| Sanitizing log | Paper checklist with checkmarks | Mobile photo + timestamp + GPS |
| Training records | Paper sign-in sheet | Digital records + facial recognition check-in |
| Corrective action records | Paper notice + paper reply | Photo -> system dispatch -> time-bound fix -> photo verification |

---

## 10. Food Safety Digital Maturity Scoring

| Dimension | L1 (Initial) | L2 (Partial) | L3 (Standardized) | L4 (Intelligent) | L5 (Leading) |
|-----------|:------------:|:------------:|:-----------------:|:----------------:|:------------:|
| Receiving inspection | Paper ledger | Partial digital ledger | Full-chain digital | IoT + auto-verification | Blockchain traceability |
| Temperature monitoring | Manual measurement | Timed manual + paper | IoT automated | AI predictive alerts | Predictive maintenance |
| Employee hygiene | Verbal instruction | Signed morning check | Digital health records | AI behavior recognition | Fully automated, zero-human oversight |
| Traceability | Cannot trace | Partial (> 24 hrs) | Full (4--24 hrs) | Real-time (< 4 hrs) | Sub-second + blockchain |

---

## Guidance

1. Go through each check item and mark current status as "Compliant" or "Needs Improvement."
2. Prioritize "Needs Improvement" items by food safety risk: CCP items > regulatory items > management items.
3. Use digital tools first to address CCP (Critical Control Point) monitoring: temperature, expiry, cross-contamination.
4. Reference: Using this checklist + IoT temperature monitoring, a typical restaurant can upgrade from L2 to L3 food safety digital maturity in under 8 weeks.

---

> **Related Templates**: [Digital Maturity Assessment](./digital-maturity-assessment-report-template.md) -- baseline your food safety digital maturity level against the 5-stage model in Section 10. [ROI & Business Case](./roi-and-business-case-template.md) -- quantify the cost of a food safety incident and build the financial case for digital investment.
>
> **Regulatory References**: FDA Food Code (United States), ISO 22000:2018 (International), EU Regulation (EC) No 852/2004. Always consult local food safety regulations in your jurisdiction of operation.
