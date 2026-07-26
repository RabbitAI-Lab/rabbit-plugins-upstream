# Multimodal Transport Information Platform Plan

> **Version**: V1.0
> **Date**: ____ / __ / __
> **Prepared by**: _________
> **Reviewed by**: _________
> **Approved by**: _________

---

## Executive Summary

### Project Positioning
The [Project Name] Multimodal Transport Information Platform digitally breaks down the information barriers between rail, road, waterborne, and air transport, enabling a **single-document electronic waybill ("single-doc")**, "one-stop" information query, and "single-price" unified settlement, supporting high-quality multimodal transport development in [Region / Country].

### Objectives
By [Target Year], achieve:
- Platform onboarding: rail ____ / port ____ / shipping ____ / road ____ / air ____ partners
- Single-doc waybill share: reach ____%
- Multimodal transfer time: reduce by ____%
- End-to-end cargo visibility: reach ____%
- Online settlement share: reach ____%
- Multimodal volume growth: ____%

### Investment Overview
| Item | Value |
|------|------|
| Total estimated investment | $____ million |
| Construction period | ____ months |
| Operating revenue (Year 3) | $____ million / year |
| Payback period | ____ years |

---

## 1. Project Background

### 1.1 Industry Background
| Item | Content |
|------|------|
| Multimodal status | Multimodal share of total freight is about ____% in [region], below leading economies (30–50%); large headroom |
| Single-doc progress | Governments advancing multimodal "single-doc": unified waybill / e-waybill / blockchain bill of lading |
| Policy support | National multimodal development programmes; "Five-Year Plan" for integrated transport |
| Technology maturity | IoT / blockchain / big data / AI underpin the platform technically |

### 1.2 Core Pain Points
| Pain | Symptom | Impact |
|------|------|------|
| Fragmented information | Rail / port / shipping / road systems independent, no interconnection | No end-to-end tracking |
| Multiple documents | Each leg has its own waybill / bill of lading / warehouse receipt, inconsistent formats | Low efficiency / error-prone |
| Repeated settlement | Per-leg settlement, cumbersome reconciliation, high capital lock-up | High finance cost |
| Coordination difficulty | Transshipment / transfer / warehousing involve many parties, high coordination cost | Long / unreliable transfer |
| No platform | No unified platform integrating multi-party resources & information | No global optimization |

---

## 2. Requirements Analysis

### 2.1 User Analysis
| Role | Core need | Pain | Priority |
|----------|----------|------|:------------:|
| Shipper / consignor | One-doc / end-to-end tracking / lowest cost / fastest | Multi-party comms / opacity / liability | High |
| Freight forwarder / 3PL | Capacity matching / route opt. / unified settlement / CRM | Asymmetry / complexity / reconciliation | High |
| Rail operator | Sourcing / capacity dispatch / data interface | Closed rail system / hard data sharing | Medium-High |
| Port / terminal | Vessel ETA / yard / handling / transfer linkage | Poor inter-modal info flow | Medium |
| Shipping line | Slot matching / container mgmt. / transfer coord. | Missing inland leg info | Medium |
| Truck / fleet | Source / backhaul / e-waybill / fast settlement | Unstable source / high empty rate / slow pay | High |
| Customs / inspection | Clearance / inspection / supervision | Inconsistent docs / hard to obtain info | Medium |
| Finance / insurance | Trade verification / cargo tracking / risk control | Authenticity / status opacity | Medium |

### 2.2 Core Business Process
```
Shipper dispatches ──→ Multimodal platform ──→ Route planning (rail / road / sea / air combo)
    │                              │
    ├─ Select plan / quote / sign ─┤
    │                              │
    ├─ Electronic waybill (single-doc)         │
    │                              │
    ├─ Rail leg (rail operator API)──────────┤
    ├─ Sea leg (port TOS interface)──────────┤
    ├─ Road leg (TMS interface)─────────────┤
    ├─ Air leg (cargo terminal interface)────┤
    │                              │
    ├─ Transshipment node (IoT + RFID)       │
    │                              │
    ├─ End-to-end tracking ─────────────┘
    │
    ├─ Delivery (electronic POD)
    │
    └─ Unified settlement → multi-party split
```

---

## 3. Overall Architecture

```
┌──────────────────────────────────────────────────────────────┐
│  User Layer                                                   │
│  ┌──────────┬──────────┬──────────┬──────────┬─────────────┐ │
│  │Shipper   │Logistics │Carrier   │Admin     │Reg./Customs │ │
│  │Portal    │Portal    │Portal    │Web       │Portal       │ │
│  │Web/App   │         │          │          │             │ │
│  └──────────┴──────────┴──────────┴──────────┴─────────────┘ │
├──────────────────────────────────────────────────────────────┤
│  Business Application Layer                                    │
│  ┌──────┬──────┬──────┬──────┬──────┬──────┬──────┬──────┐  │
│  │Single│Route │Capac.│Cargo │Cust. │Settle│Credit│Data  │  │
│  │Doc   │Opt.  │Match.│Track.│/Insp.│Split │Risk  │Analyt.│  │
│  └──────┴──────┴──────┴──────┴──────┴──────┴──────┴──────┘  │
├──────────────────────────────────────────────────────────────┤
│  Business Middle Platform Layer                                │
│  ┌──────────┬──────────┬──────────┬──────────┬─────────────┐ │
│  │Order     │Capacity  │Settle    │Document  │Notice       │ │
│  │Center    │Center    │Center    │Center    │Center       │ │
│  └──────────┴──────────┴──────────┴──────────┴─────────────┘ │
├──────────────────────────────────────────────────────────────┤
│  Data & AI Platform Layer                                      │
│  ┌──────────┬──────────┬──────────┬──────────┬─────────────┐ │
│  │Data Lake │Governance│AI Engine │Blockchain│IoT Platform │ │
│  │          │          │Route Opt│e-Waybill │Cargo Track  │ │
│  │          │          │Forecast │Notarize  │Device Mgmt  │ │
│  └──────────┴──────────┴──────────┴──────────┴─────────────┘ │
├──────────────────────────────────────────────────────────────┤
│  Integration Layer                                             │
│  ┌──────────┬──────────┬──────────┬──────────┬─────────────┐ │
│  │Rail      │Port/     │Road      │Air       │Public / Reg.│ │
│  │Operator  │Waterborne│TMS/GNSS  │Cargo     │Single Window│ │
│  │API/EDI   │TOS/VTS/  │          │Terminal  │Customs/     │ │
│  │          │EDI       │          │          │Transport    │ │
│  └──────────┴──────────┴──────────┴──────────┴─────────────┘ │
└──────────────────────────────────────────────────────────────┘
```

---

## 4. Core Function Detailed Design

### 4.1 Single-Document Electronic Waybill (single-doc)

#### 4.1.1 Waybill Elements
| Element | Content | Standard |
|------|------|------|
| Waybill no. | Unique code (platform + date + sequence) | Platform standard |
| Consignor / consignee | Company name / registration no. / contact | |
| Goods name / qty / weight / volume | By HS code / dangerous goods UN no. | HS / UN |
| Packaging type / pieces | | |
| Origin / destination | Address + GPS coordinates | |
| Route | Rail→Sea→Road / Rail→Road / etc., with per-leg carrier & node | |
| Freight & settlement | Through freight / per-leg split / method / terms | |
| Insurance | Amount / insurer / policy no. | |
| Document requirements | Customs / inspection / license attachments | |
| Time nodes | Planned / actual pickup / arrival / transfer / delivery | |
| Liability split | Per-leg liability / compensation standard | |

#### 4.1.2 Electronic Waybill Flow
```
Create waybill ──→ Each leg carrier confirms ──→ e-signature
    │
    └──→ Waybill on-chain (hash notarization)
    └──→ Per-leg status update (IoT / API)
    └──→ Delivery (e-POD: signature + photo + GPS + timestamp)
    └──→ Archive + notarization (retain ≥ ____ years)
```

#### 4.1.3 Blockchain Electronic Waybill
| Function | Explanation | Technology |
|------|------|------|
| Waybill notarization | Hash of create / change / sign key nodes on-chain | Smart contract |
| Multi-party consensus | Shipper / carrier / consignee / regulator nodes | Consortium chain |
| Immutable | Confirmed content cannot be unilaterally altered | Blockchain property |
| e-Bill of lading | Replaces paper bill (sea + multimodal) | e-BL + title transfer |

### 4.2 Multimodal Route Optimization

#### 4.2.1 Optimization Algorithms
| Objective | Input | Algorithm | Output |
|----------|------|------|------|
| Lowest cost | Per-leg rate / fees / storage / handling | Shortest path + dynamic programming | Lowest-cost route + per-leg quote |
| Fastest | Per-leg time / transfer / customs time | Shortest path + queueing | Fastest route + ETA |
| Lowest carbon | Per-mode emission factor / distance | Multi-objective optimization | Green route + footprint |
| Multi-objective | Cost + time + carbon + reliability | Pareto + preference | Multi-scenario comparison |

#### 4.2.2 Route Combination Example
| Plan | Origin→Destination | Combination | Total time | Total cost | CO2 | Rec. |
|------|-------------|----------|:-----:|:-----:|:---:|:---:|
| A | Singapore→Munich | Sea (Singapore→Rotterdam) + rail (Rotterdam→Duisburg) + road (Duisburg→Munich) | 28 d | $__ k | __ t | √ |
| B | Singapore→Munich | Sea (Singapore→Rotterdam) + road (Rotterdam→Munich) | 32 d | $__ k | __ t | |
| C | Singapore→Munich | Air (Singapore→Frankfurt) + road (Frankfurt→Munich) | 3 d | $__ k | __ t | |

### 4.3 Capacity Matching and Trading

#### 4.3.1 Capacity Resource Pool
| Mode | Capacity type | Source | Frequency |
|----------|----------|----------|:--------:|
| Rail | Wagons / block trains / containers (type / qty) / timetable | Rail operator / terminal | Near-real-time |
| Sea | Vessels / slots / routes / schedules / rates | Port / line / forwarder | Near-real-time |
| Road | Vehicles (type / load / position / status) | TMS / GNSS / fleet platform | Real-time |
| Air | Flights / slots / routes / schedules / rates | Airline / cargo terminal | Near-real-time |

#### 4.3.2 Intelligent Matching
| Scenario | Method | Explanation |
|----------|------|------|
| Freight matching | Cargo attributes → capacity filter (type / route / time / price / rating) → TOP-N | AI recommendation + manual confirm |
| Backhaul matching | Vehicle / container at destination → auto-match backhaul → push to driver / fleet | Lower empty rate |
| Multi-leg combo | Rail→Sea→Road auto-combined → quote | One-stop solution |
| Emergency capacity | Ad-hoc / urgent need → broadcast → bid / grab | Elastic capacity |

#### 4.3.3 Trading Models
| Model | Explanation | Use case |
|------|------|----------|
| Single price | Platform fixed quote by route / volume / market | Standard transport |
| Bidding | Shipper posts → carriers quote → shipper selects | Bulk / non-standard |
| Grab order | Platform posts source → eligible drivers / fleets grab | LTL / FTL road |
| Contract price | Signed customers at contracted price | Key / long-term clients |

### 4.4 Cargo Tracking

#### 4.4.1 End-to-End Tracking
| Leg | Method | Data | Frequency |
|--------|----------|----------|:--------:|
| Rail | Rail freight tracking system / operator API / GNSS | Wagon no. / position / speed / ETA | Near-real-time |
| Sea | AIS + vessel GNSS | Vessel / position / speed / ETA | Near-real-time |
| Road | Onboard GNSS + mobile app | Plate / position / speed / ETA | Real-time |
| Air | Airline flight-tracking API | Flight no. / dep. / arr. / delay | Near-real-time |
| Transfer node | RFID + barcode + video AI + IoT | Node in/out time / status | Event-driven |
| Warehouse | WMS + RFID + sensors | In / in-stock / out / temp-humidity | Near-real-time |

#### 4.4.2 Exception Alerts
| Exception | Detection | Alert | Process |
|----------|----------|----------|----------|
| Route deviation | Geo-fence + GNSS deviation | Platform + SMS + app push | Confirm cause → contingency |
| Late arrival | Actual vs. planned | Same | Notify consignee → adjust |
| Long stop | GNSS stationary timeout | Same | Contact driver / carrier |
| Temp anomaly (cold chain) | IoT sensor threshold | Same + reefer alarm | Check reefer + transfer + loss assess |
| Unseal / open | Smart seal / sensor change | Same | Verify + preserve evidence + liability |
| Customs hold | Customs status interface | Notify shipper / forwarder | Assist clearance + update |

### 4.5 Customs and Inspection Integration (Single Window)

#### 4.5.1 Single Window Interface
| System | Content | Method | Status |
|----------|----------|----------|:---:|
| National Single Window | Declaration / inspection / license / origin / manifest | API / EDI | [done / pending] |
| Rail port system | Rail port clearance / transshipment | EDI | |
| Port EDI | Port declaration / inspection / release | EDI / API | |
| Customs modernization programme | Supervision / risk analysis | API | |

#### 4.5.2 Clearance Assistance
| Function | Explanation |
|------|------|
| AI classification | Goods description → AI suggests HS code + duty + control |
| Auto document gen. | From waybill / invoice / packing list → draft declaration |
| Progress tracking | Real-time declaration → review → inspect → duty → release |
| Historical clearance | Past records / inspection rate / time statistics |
| Compliance check | Auto-check prohibited / license / quarantine requirements |

### 4.6 Settlement and Split

#### 4.6.1 Unified Settlement
| Function | Explanation |
|------|------|
| Multi-currency | USD / EUR / and other major currencies |
| Multi-method | Bank transfer / direct bank connect / e-payment / LC |
| Staged settlement | Prepaid → COD → POD → monthly, etc. |
| Auto billing | By contract / quote + actual transport data |
| Reconciliation | Auto reconciliation + variance handling + statement download |
| Invoicing | E-invoice auto-issue / push / credit note |

#### 4.6.2 Multi-Party Split
```
Consignor pays through freight ($total)
    ├── Platform service fee ($____, ____%)
    ├── Rail leg freight ($____, ____%) → Rail operator
    ├── Sea leg freight ($____, ____%) → Shipping line
    ├── Road leg freight ($____, ____%) → Fleet / owner-driver
    ├── Port / terminal fee ($____) → Port / terminal
    ├── Customs / inspection fee ($____) → Broker
    ├── Insurance ($____) → Insurer
    └── ...
```

#### 4.6.3 Blockchain Split
| Function | Explanation |
|------|------|
| Smart-contract split | On waybill completion → auto-trigger split (preset ratio) |
| Transparent & auditable | All splits on-chain, verifiable by each party |
| Fast settlement | T+1 / T+0 (traditional T+30~90 days) |
| Supply-chain finance | Receivables financing / factoring on trusted waybill |

### 4.7 Credit and Risk Management

#### 4.7.1 Credit System
| Object | Dimensions | Source | Frequency |
|----------|----------|----------|:--------:|
| Shipper | Order vol. / on-time pay / cancel rate / dispute rate | Platform transactions | Monthly |
| Carrier | On-time / damage / complaint / cooperation / license compliance | Transport + GNSS + rating | Monthly |
| Forwarder | Volume / error rate / satisfaction / compliance | Platform | Monthly |

#### 4.7.2 Risk Management
| Risk | Control |
|----------|----------|
| Credit | Score + deposit / escrow + limit + blacklist |
| Cargo | End-to-end tracking + geo-fence + alert + insurance |
| Document | e-Waybill + blockchain notarization + OCR verify + e-signature |
| Compliance | Auto license check + KYC + AML |
| Funds | E-payment / bank custody + split system + reconciliation + audit |

### 4.8 Data Analytics and BI

#### 4.8.1 Analysis Themes
| Theme | Content | Deliverable | Frequency |
|----------|----------|--------|:----:|
| Operations | Orders / volume / freight / capacity use / on-time / damage | Daily / weekly / monthly report | D / W / M |
| Route | Per-route volume / cost / time / margin / seasonality | Route optimization advice | M / Q |
| User | Activity / retention / repurchase / churn / ARPU / LTV | User ops report | M |
| Market | Rate trend / supply-demand / season / hotspot | Market report | M / Q |
| Risk | Abnormal orders / disputes / complaint rate / credit decay | Risk alert | Real-time / W |

#### 4.8.2 Data Wall
| Module | Content |
|----------|----------|
| Real-time ops | Today orders / volume / freight GMV / active users / online capacity |
| Logistics heatmap | Source / capacity distribution + live freight flow |
| TOP 10 routes | Most popular routes + volume + rate trend |
| Modal split | Single / two-mode / three-mode share pie + trend |
| Exception monitor | In-transit exceptions (delay / deviation / temp) + map |

---

## 5. Stakeholder Integration

### 5.1 Integration Plan
| Stakeholder | Content | Method | Difficulty | Priority |
|--------|----------|----------|:-------:|:------:|
| Rail (operator / API) | Waybill / wagon / train / schedule / tracking | EDI / API | High (closed system) | P0 |
| Port (TOS) | Vessel ETA / yard / handling / release | EDI / API | Medium | P0 |
| Shipping line | Schedule / slot / rate / B/L / position | API / EDI | Medium | P0 |
| Large fleet / platform | Vehicle / driver / position / rate / e-waybill | API / GNSS | Low | P1 |
| SME fleet / owner-driver | Register / certify / accept / upload track | App / mini-program | Low | P1 |
| Air cargo terminal | Flight / slot / ULD / waybill | API / EDI | Medium | P1 |
| Customs / Single Window | Declaration / inspection / manifest / release | EDI / API | Medium-High | P1 |
| Insurer | Policy / certificate / claim | API | Low | P2 |
| Financial inst. | Payment / finance / factoring / LC | API / H5 | Medium | P2 |

### 5.2 Standards Compliance
| Standard | Explanation | Application |
|------|------|------|
| UN/EDIFACT | UN electronic data interchange standard | Multimodal EDI messages (IFTMBF / IFTMCS / IFTSTA) |
| GS1 | Global identification system | Goods / container / logistics unit coding (GTIN / SSCC) |
| CEFACT | UN Centre for Trade Facilitation & E-Business | International trade documents |
| ISO 6346 | Container coding & identification | Container no. coding / check |
| e-CMR | Electronic road consignment note convention | Road e-waybill |
| DCSA | Digital Container Shipping Association | Container shipping digitalization |
| ISO 14825 (GDF) | Geographic data files | Location / route reference |

---

## 6. Business Model

### 6.1 Revenue Model
| Source | Method | Est. share |
|----------|----------|:------:|
| Transaction commission | Platform fee [0.5–3%] of freight | __% |
| SaaS subscription | Logistics / shipper per account / month | __% |
| Value-added | e-Waybill / notarization / reports / API | __% |
| Financial | Payment fee / finance / insurance commission | __% |
| Ads / bidding | Capacity bid ranking / homepage rec. | __% |
| Data service | Industry report / data API / consulting | __% |

### 6.2 Pricing Strategy
| Customer type | Model | Explanation |
|----------|----------|------|
| Large shipper / 3PL | Contract + customization | Annual frame / deep integration / dedicated |
| Mid logistics firm | SaaS subscription + commission | Standard + volume-based |
| Small shipper / driver | Free base + paid add-ons | First order free / base free |
| Regulator / port authority | Free (public service) | Open data interface |

---

## 7. Implementation Plan

| Phase | Time | Content | Milestone | Investment |
|------|------|------|--------|:----:|
| Phase 1 (Foundation) | ____ yr | Platform 1.0 (e-waybill + order mgmt + route planning + road tracking) + key rail / port integration | MVP live | $___ M |
| Phase 2 (Scale & quality) | ____ yr | Sea / air integration + multi-leg tracking + settlement split + blockchain + BI + app | Full multimodal coverage | $___ M |
| Phase 3 (Intelligent) | ____ yr | AI route opt. + smart matching + credit + supply-chain finance + data products + open platform | Smart ops + ecosystem | $___ M |

---

> **Usage note**: This template is for national / regional / sector multimodal transport information platforms. Success factors: willingness of monopolistic resource owners (rail / port) to cooperate, strength of single-doc standard promotion, and inter-modal data interoperability. Replace `[placeholder]` content with actual project data.

> **Legal notice**: This template is protected by copyright and related laws. It is provided for individual study and reference only; commercial use requires the author's written authorization.

> **Disclaimer**: This template is for study and reference only and does not constitute professional advice. Multimodal transport involves multiple carriers, cross-border data flows, and customs supervision with complex legal relations; conduct thorough legal and compliance review before implementation. The author accepts no liability for any loss arising from the use of or reliance on this template.

> **Author**: yinjianheng | yinjianheng@foxmail.com
