# Global Smart Mobility Best-Practice Deep Dive

> This document systematically deconstructs the strategic positioning, technology platforms, key metrics, and lessons learned of 24 global benchmark enterprises and public agencies in the smart-mobility domain, providing an authoritative reference for transport digital-transformation programs. Data current as of end of 2025.

---

## Table of Contents

1. [Global Technology & Infrastructure Vendors](#i-global-technology--infrastructure-vendors)
   - 1.1 Nokia
   - 1.2 Mobileye (Intel)
   - 1.3 Microsoft (Azure)
   - 1.4 Bosch
   - 1.5 TransCore
   - 1.6 Siemens Mobility
   - 1.7 Kapsch TrafficCom
   - 1.8 Hitachi
   - 1.9 Thales
   - 1.10 Cubic Corporation
2. [Public Agencies, Operators & Ecosystem](#ii-public-agencies-operators--ecosystem)
   - 2.1 Singapore LTA
   - 2.2 ITS Japan
   - 2.3 Transport for London (TfL)
   - 2.4 Waymo
   - 2.5 Tesla
   - 2.6 Deutsche Bahn (DB)
   - 2.7 PSA Singapore
   - 2.8 Port of Rotterdam
   - 2.9 FedEx Memphis SuperHub
   - 2.10 New York City DOT
   - 2.11 Dubai RTA
   - 2.12 ERTICO – ITS Europe
   - 2.13 Waze / Google
   - 2.14 Joby Aviation & Skydio

---

## I. Global Technology & Infrastructure Vendors

### 1.1 Nokia — Full-Stack Transport ICT

| Dimension | Detail |
|----------|--------|
| **Company Profile** | A global leader in networking and communications infrastructure; its Nokia for Rail and Nokia for Ports portfolios deliver private 5G, IP routing, and cloud-native platforms for transport operators. Mobility/network revenue ~€20B (FY2024). |
| **Transport Strategy** | "Connectivity + Mission-Critical" — private wireless (4.9G/5G), IP/MPLS backbones, and edge clouds that underpin digital rail, ports, and road operators. |
| **Core Technologies** | Private and campus 5G, Nokia DAC (Digital Automation Cloud), IP routing, optical transport, NetGuard security, MX Industrial Edge, cloud-native core. |
| **Transport Portfolio** | Rail communications (FRMCS-ready), automated-port private networks, road-operator C-ITS connectivity, mission-critical broadband (MCPTT), digital-twin enablement. |
| **Flagship Projects** | Deutsche Bahn "Digital Rail for Germany" backbone; Hamburg port private 5G; SNCF trackside connectivity; multiple metro CBTC data networks. |
| **Key Data** | Present in 70+ countries; serves the majority of the world's top-20 freight and passenger rail operators. |
| **Distinct Strengths** | End-to-end connectivity stack (chip-to-cloud-to-device), carrier-grade reliability, global services footprint, standards leadership (3GPP, FRMCS). |
| **Weaknesses** | Less depth in vertical application software than pure-play IT majors; heavy-asset operator sales cycles are long. |
| **Core Lesson** | Full-stack connectivity capability is irreplaceable in large transport programs — the foundation of smart mobility is the network itself. |

### 1.2 Mobileye (Intel) — Autonomous Driving + City Safety

| Dimension | Detail |
|----------|--------|
| **Company Profile** | An Intel company and one of the world's largest providers of advanced driver-assistance systems (ADAS); its REM (Road Experience Management) crowd-sourced mapping powers both autonomy and city safety. |
| **Autonomous Driving** | Mobileye Drive (L4 robotaxi / shuttle stack); SuperVision and Chauffeur consumer ADAS; more than 150 million eyeQ chips shipped. |
| **Architecture** | "True Redundancy" — independent camera and radar/lidar sensing, plus REM for always-fresh HD maps derived from fleet data. |
| **Core Technologies** | EyeQ system-on-chips, REM crowd-sourced mapping, Responsibility-Sensitive Safety (RSS), imaging radar, RSS-based driving policy. |
| **Flagship Projects** | City safety programs (MTSS) across Europe, Japan, and the US; L4 pilots with transit agencies; mapping data covering millions of km of roads. |
| **Key Data** | ADAS in vehicles from 50+ OEMs; REM data harvested from consumer fleets at near-zero marginal cost. |
| **Distinct Strengths** | Camera-first perception leadership, the world's largest crowd-sourced mapping data flywheel, a clear safety formalism (RSS). |
| **Weaknesses** | Robotaxi service scale trails Waymo; consumer-ADAS regulatory scrutiny is rising. |
| **Core Lesson** | "Autonomy + traffic management" is a dual-engine model — feed L4 perception back into signal optimization, and use city data to sharpen autonomy. |

### 1.3 Microsoft (Azure) — Cloud & City-Data Platform Pioneer

| Dimension | Detail |
|----------|--------|
| **Company Profile** | A top-tier global public-cloud provider; Azure and its industry clouds are the digital backbone for public-sector and transport transformation. |
| **Smart-Mobility Platform** | Azure for Mobility and Azure Digital Twins enable city-scale data fusion, real-time analytics, and simulation. |
| **Core Technologies** | Azure Digital Twins, Azure IoT Hub, Synapse analytics, Fabric data platform, Azure OpenAI, cloud-native PaaS. |
| **Transport Products** | Azure Maps, traffic analytics, digital-twin platforms, AI signal-control toolkits, smart-highway and MaaS accelerators. |
| **Flagship Projects** | Digital-twin programs for multiple metro and highway agencies; cloud backbones for transit and port operators worldwide. |
| **Key Data** | Underpins data platforms for dozens of city and national transport agencies; Azure Maps serves billions of daily location requests. |
| **Distinct Strengths** | Enterprise-grade cloud + digital-twin stack, strong data-governance and security posture, broad partner ecosystem. |
| **Weaknesses** | No transport-specific field hardware; large programs depend on system integrators. |
| **Core Lesson** | The "city brain" concept shaped industry expectations — but the real barrier is not data ingestion, it is business-process re-engineering. |

### 1.4 Bosch — Global Leader in Traffic Perception

| Dimension | Detail |
|----------|--------|
| **Company Profile** | A global leader in mobility technology and industrial sensing; a top supplier of traffic detection, video analytics, and road-side perception. |
| **Transport Products** | Traffic cameras (enforcement / ANPR / speed / flow), radar-video fusion units, signal controllers, event-detection servers, sensors. |
| **Core Technologies** | AI vision, radar-video fusion, edge computing, multi-spectral imaging, connected-sensor platforms. |
| **Market Position** | Among the leading suppliers of traffic-enforcement and detection equipment in Europe and beyond; strong in automotive perception. |
| **Flagship Projects** | Perception and enforcement systems for cities and highways across Europe, the Middle East, and Asia-Pacific. |
| **Distinct Strengths** | World-class sensing hardware, full stack from silicon to algorithm to device to platform, extensive channel coverage. |
| **Weaknesses** | Software-platform breadth trails pure IT majors; solutions remain hardware-anchored. |
| **Core Lesson** | "Perception is king" — without high-quality sensing data, every AI model and control center is built on sand. |

### 1.5 TransCore — Global Tolling & Road-Pricing Leader

| Dimension | Detail |
|----------|--------|
| **Company Profile** | A US-based leader in tolling, RFID, and nationwide road-pricing systems; a long track record of open-road and all-electronic tolling. |
| **Core Business** | All-electronic tolling, multi-lane free-flow (MLFF), congestion pricing, transponders (RFID), toll-system integration. |
| **Core Technologies** | RFID (transponder) and ANPR, DSRC/C-V2X roadside, tolling back-office, violation enforcement, account-based tolling. |
| **Flagship Projects** | National and state tolling programs across the US; express-lane and congestion-pricing deployments; interoperable transponder systems. |
| **Key Data** | Tens of thousands of lane-miles of electronic tolling under management; transponder base in the tens of millions. |
| **Distinct Strengths** | Deepest free-flow tolling experience in North America, multi-technology fusion (RFID + ANPR + GNSS), proven reliability at scale. |
| **Weaknesses** | Narrower geographic reach than European peers; limited rail/transit portfolio. |
| **Core Lesson** | The crux of free-flow pricing is not device accuracy (often >99.9%) but the legal framework and enforcement regime behind it. |

### 1.6 Siemens Mobility — Global Rail Signaling Leader

| Dimension | Detail |
|----------|--------|
| **Company Profile** | Holds the #1 global share of rail signaling (~25%); FY2024 revenue ~€10.5B. |
| **Core Products** | CBTC metro signaling, ETCS (European Train Control System), intelligent traffic-management systems, V2X roadside units. |
| **Flagship Projects** | London Thameslink ATO (first mainline ATO), New York subway CBTC upgrades, Singapore metro signaling. |
| **Key Data** | Operations in 70+ countries; #1 in rail signaling; 100+ CBTC lines delivered. |
| **Distinct Strengths** | Full-stack rail capability from signaling to electrification to rolling stock to digital services; deep SIL4 safety-certification experience. |
| **Core Lesson** | "Safety certification" is the highest barrier in rail digitalization — it is not a technology problem but a verification problem. |

### 1.7 Kapsch TrafficCom — Global ETC Benchmark

| Dimension | Detail |
|----------|--------|
| **Company Profile** | An Austrian firm leading globally in ETC / free-flow tolling; FY2024 revenue ~€0.55B. |
| **Core Products** | Multi-lane free flow (MLFF), ETC systems, traffic-management systems (TMS), V2X roadside units. |
| **Flagship Projects** | Bulgaria national MLFF (16,000 km), Germany truck-tolling system, Australia M5 motorway. |
| **Key Data** | Operations in 50+ countries; >30,000 km of MLFF deployed. |
| **Distinct Strengths** | Deepest global ETC/MLFF experience, reliability proven across many countries, fusion of GNSS/DSRC/ANPR. |
| **Core Lesson** | Free-flow tolling hinges on a compliant charging legal framework and enforcement system — not just device precision. |

### 1.8 Hitachi — Shinkansen ITS

| Dimension | Detail |
|----------|--------|
| **Company Profile** | Japan's largest integrated electronics and industrial group; expanded its transport business materially by acquiring Thales' Ground Transportation Systems (GTS) in 2023. |
| **Transport Products** | Shinkansen ITS (operations management / signaling / disaster prevention), rolling stock, HMAX digital platform (on Lumada IoT). |
| **Flagship Projects** | Japan Shinkansen (world's highest punctuality, average delay under 1 minute); UK Great Western Railway signaling upgrade. |
| **Core Lesson** | Japan's "zero-delay" culture — digitalization enhances rather than replaces an extreme operations philosophy. |

### 1.9 Thales — Aviation-Grade Rail & Transport Security

| Dimension | Detail |
|----------|--------|
| **Company Profile** | A French aerospace, defense, and cybersecurity group; 2024 revenue ~€18.5B. After selling GTS to Hitachi (2023) it focuses on air-traffic management, airport security, and transport cybersecurity. |
| **Core Products** | Air-traffic management (ATM/ATC), airport security and operations, rail signaling (via JV), transport cybersecurity. |
| **Key Data** | >30% global share of air-traffic-management systems; manages >40% of the world's airspace. |
| **Core Lesson** | Aviation-grade safety standards (SIL4 / DO-178C) are spilling into rail and autonomous driving — safety-engineering capability becomes the core moat. |

### 1.10 Cubic Corporation — Global Transit Fare & Management

| Dimension | Detail |
|----------|--------|
| **Company Profile** | A US leader in transit payment and management; taken private by Veritas Capital in 2021; transport segment revenue ~$1.8B. |
| **Core Products** | Public-transit fare systems (card + account + mobile pay), traffic-management systems, NextCity MaaS platform. |
| **Flagship Projects** | London Oyster card (among the world's largest transit-card systems), New York OMNY (contactless), Chicago Ventra. |
| **Key Data** | Operations in 60+ major cities; processes >40 million transactions per day. |
| **Core Lesson** | Transit fare is the highest-frequency digital touchpoint for citizens — upgrading from "payment tool" to "MaaS entry point" is the strategic direction. |

---

## II. Public Agencies, Operators & Ecosystem

### 2.1 Singapore LTA — Global Urban ITS Benchmark (ERP 2.0)

| Dimension | Detail |
|----------|--------|
| **Profile** | Land Transport Authority of Singapore — a global benchmark in urban transport governance. ERP 2.0 (next-generation electronic road pricing) went live in 2025. |
| **Core Systems** | ERP 2.0 (GNSS-based distance-time-location charging), i-Transport (unified mobility-management platform), Green Man+ (pedestrian-friendly signals). |
| **Key Data** | Peak-period average speed >27 km/h (among the best of world cities); public-transit modal share >67% at peak. |
| **Distinct Strengths** | City-state advantage — an extremely fast closed loop from policy design → deployment → impact evaluation. |
| **Core Lesson** | ERP 2.0 is not really about charging — it is a digital instrument of Travel Demand Management (TDM) that prices road-network load. |

### 2.2 ITS Japan — World's Largest ETC 2.0 Deployment

| Dimension | Detail |
|----------|--------|
| **Profile** | Japan's ITS promotion organization, driving the world's largest ETC 2.0 (high-capacity DSRC) deployment. |
| **Core Systems** | ETC 2.0 (>80 million onboard units), VICS (road-traffic info comms), ITS Spot (>4,000 roadside units). |
| **Key Data** | ETC usage >93%; highway congestion reduced >30%. |
| **Core Lesson** | Japan's ITS model — "industry-led + unified standard + mandated fitment" — is highly efficient but slows technology iteration. |

### 2.3 Transport for London (TfL) — Congestion Charge + Open Data

| Dimension | Detail |
|----------|--------|
| **Profile** | One of the world's exemplary city-transport governance bodies. |
| **Core Systems** | Congestion Charge + Ultra Low Emission Zone (ULEZ), Oyster/Contactless ticketing, open-data APIs (used by >600 apps). |
| **Key Data** | Congestion Charge cut central traffic -15%; ULEZ cut NOx -46% in the central zone. |
| **Core Lesson** | "Open data" is a low-cost, high-impact digital strategy — TfL spends only a few million pounds a year maintaining APIs, yet unlocked 600+ apps and changed how tens of millions travel. |

### 2.4 Waymo — #1 in Global L4 Driverless

| Dimension | Detail |
|----------|--------|
| **Profile** | Alphabet's autonomous-driving company; the largest L4 robotaxi operation in the world. |
| **Operating Scale** | Operating in San Francisco + Phoenix + Los Angeles + Austin; >150,000 paid trips per week (2025). |
| **Core Technologies** | Fully in-house stack (sensors + compute + software + HD maps + remote assistance); Waymo Driver now in its 6th generation. |
| **Key Data** | >50 million cumulative L4 miles; crash rates materially below human drivers. |
| **Core Lesson** | Waymo chose the "vehicle-intelligence" path (heavy sensors + strong AI) versus the "vehicle-infrastructure-cloud" path — two technology routes coexist in the industry. |

### 2.5 Tesla — Full-Stack FSD

| Dimension | Detail |
|----------|--------|
| **Profile** | The world's largest smart-EV maker; delivered >1.8 million vehicles in 2024. |
| **Autonomy** | FSD (Full Self-Driving) V12 — end-to-end AI from camera input to control output via a single neural network. |
| **Core Technologies** | Vision-only (no lidar), Dojo training supercomputer, shadow-mode data collection, global fleet data flywheel. |
| **Key Data** | >6 million vehicles worldwide with FSD hardware; >3 billion cumulative FSD miles. |
| **Core Lesson** | The "data flywheel" is the strongest moat — more cars → more data → better AI → more cars. |

### 2.6 Deutsche Bahn (DB) — Digital Rail for Germany

| Dimension | Detail |
|----------|--------|
| **Profile** | Europe's largest rail operator; runs one of the world's densest high-speed and mixed-traffic networks. |
| **Digital Priorities** | Digital Rail for Germany (digitization of the network), ETCS rollout, ATO, predictive maintenance (PHM), intelligent stations, FRMCS. |
| **Core Technologies** | ETCS L2 baseline 3, GSM-R/FRMCS, rail BIM, AI obstacle detection, rail data platform. |
| **Flagship Projects** | "Digital Rail for Germany" corridor program; Stuttgart 21 digital station; ICE modernization. |
| **Key Data** | Operates ~33,000 km of track; punctuality programs targeting double-digit improvement via digital signaling. |
| **Distinct Strengths** | Unmatched operational data from Europe's largest rail entity; end-to-end control from infrastructure to operations to service. |
| **Core Lesson** | Rail digitalization is a classic "standard-driven + safety-first" domain — every upgrade needs SIL4 certification and extensive validation. |

### 2.7 PSA Singapore — Global Automated-Terminal Benchmark

| Dimension | Detail |
|----------|--------|
| **Profile** | One of the world's largest global port operators, running multiple automated container terminals. |
| **Automation Highlights** | Tuas Port — a greenfield, fully automated terminal with automated stacking cranes and automated guided vehicles at scale. |
| **Core Technologies** | Intelligent TOS, GNSS positioning, automated yard cranes, AGVs, digital twin, remote-controlled quay cranes. |
| **Key Data** | Single-terminal throughput among the highest globally; labor cost and safety-incident reductions in the double digits. |
| **Distinct Strengths** | Greenfield full-automation model enabling step-change productivity; group-wide digital platforms across terminals. |
| **Core Lesson** | Port automation need not be "all or nothing" — a phased, twin-track model offers a viable path for legacy ports. |

### 2.8 Port of Rotterdam — Europe's Largest Automated Port

| Dimension | Detail |
|----------|--------|
| **Profile** | Europe's largest port; container throughput >14 million TEU/year. |
| **Digital Highlights** | Pronto (vessel ETA prediction platform based on AI + multi-party data sharing), digital-twin port, smart energy management. |
| **Key Data** | Pronto cut vessel anchorage waiting time -20%; port CO2 emissions -25% (2025 vs 2019). |
| **Core Lesson** | "Data sharing" is the core difficulty of port digitalization — how do competitors share data? Pronto built an independent data-trust governance framework. |

### 2.9 FedEx Memphis SuperHub — Purpose-Built Digital Cargo Hub

| Dimension | Detail |
|----------|--------|
| **Profile** | One of the world's first purpose-built express-air-cargo hubs; the backbone of the FedEx super-network. |
| **Digital Highlights** | BIM-driven design-construct-operate handover, fully automated sortation (capacity >500,000 pieces/hour), digital-twin hub. |
| **Key Data** | Peak daily parcel throughput in the hundreds of millions; >100 km of sortation lines; thousands of AGVs. |
| **Distinct Strengths** | Digital from scratch (not retrofit) — no legacy debt; BIM model carries from design through operations. |
| **Core Lesson** | "Digital by design" costs far less than "digital by retrofit" — digital requirements should be embedded at the infrastructure-design stage. |

### 2.10 New York City DOT — City-Scale Traffic Operations Center

| Dimension | Detail |
|----------|--------|
| **Profile** | One of the world's leading city-level traffic operations agencies; manages one of the most complex urban networks. |
| **Core Systems** | Real-time traffic management, Midtown congestion pricing, Vision Zero safety analytics, NYC DOT real-time traffic dashboard. |
| **Key Data** | Manages signals across >13,000 intersections; congestion pricing launched in 2025; injury reductions via data-driven safety. |
| **Distinct Strengths** | Early "real-time online simulation" of city traffic — moving from after-the-fact statistics to live what-if analysis; data-driven management. |
| **Core Lesson** | The data-asset path for city mobility: data → information → knowledge → decision → action → feedback. |

### 2.11 Dubai RTA — Air Taxis + Hyperloop

| Dimension | Detail |
|----------|--------|
| **Profile** | Roads and Transport Authority of Dubai — among the world's most forward-leaning city-transport authorities. |
| **Core Projects** | Air taxi (eVTOL) targeted for operation in 2026, Hyperloop research, driverless metro (Red / Green lines). |
| **Core Lesson** | "Vision-driven" transport digitalization — top-down, ambitious goal-setting that attracts global technology suppliers with world-class projects. |

### 2.12 ERTICO – ITS Europe — European ITS Ecosystem Integrator

| Dimension | Detail |
|----------|--------|
| **Profile** | European ITS industry organization driving cross-border ITS standard harmonization and project coordination. |
| **Core Projects** | C-Roads Platform (cross-border C-ITS interoperability), DATEX II (traffic data-exchange standard), ITS World Congress. |
| **Core Lesson** | Europe's core ITS challenge is "fragmentation" (27 countries, multiple languages / laws / tech stacks) — ERTICO's value is standard coordination. |

### 2.13 Waze / Google — World's Largest Crowd-Sourced Traffic Data

| Dimension | Detail |
|----------|--------|
| **Profile** | Waze operates independently under Google; the world's largest crowd-sourced navigation and traffic-data platform. |
| **Data Scale** | >150 million monthly active users; >1 million traffic events reported per day. |
| **Core Lesson** | "Crowd-sourced traffic data" is the lowest-cost means of whole-network sensing — every vehicle's every trip is a sensor. |

### 2.14 Joby Aviation & Skydio — Advanced Air Mobility (AAM) Pioneers

| Dimension | Detail |
|----------|--------|--------|
| **Positioning** | Joby Aviation — a pioneer of certified eVTOL (passenger autonomous aircraft). Skydio — the leading US manufacturer of autonomous drones for government and enterprise. |
| **Market Position** | Joby — among the first eVTOL firms to secure FAA certification milestones for commercial passenger operations. Skydio — US market leader in autonomous drone systems. |
| **Core Products** | Joby S4 (five-seat eVTOL) + long-range variants; Skydio X-series drones + Skydio Dock autonomous docking. |
| **Transport Applications** | Joby: Urban Air Mobility (UAM), air tourism, emergency transport. Skydio: traffic inspection, crash-scene mapping, logistics, low-altitude surveying. |
| **Key Data** | Joby progressing through FAA type-certification phases; Skydio drones deployed by dozens of US public-safety and transport agencies. |
| **Core Lesson** | The bottleneck in Advanced Air Mobility is not the aircraft but airspace management and safety-supervision digitalization — a UTM platform is the "traffic-management center" of the low-altitude economy. |

---

## III. Integrated Benchmark Matrix

| Dimension | Nokia | Mobileye | Microsoft | Bosch | Siemens | Waymo | LTA |
|----------|:-----:|:--------:|:---------:|:-----:|:-------:|:-----:|:---:|
| **Hardware Capability** | ★★★★☆ | ★★★☆ | ★☆☆ | ★★★★★ | ★★★★★ | ★★★★ | ★★☆ |
| **AI / Software Capability** | ★★★☆ | ★★★★★ | ★★★★★ | ★★★★ | ★★★☆ | ★★★★★ | ★★★ |
| **Large-Project Delivery** | ★★★★ | ★★★ | ★★★ | ★★★ | ★★★★ | ★★☆ | ★★★★★ |
| **International Market** | ★★★★★ | ★★★★ | ★★★★★ | ★★★★★ | ★★★★★ | ★★★★ | ★☆☆ |
| **Supply-Chain Sovereignty** | ★★★★ | ★★★★ | ★★★★★ | ★★★★★ | ★★★★ | ★★★★ | N/A |
| **Transport Depth** | ★★★★ | ★★★ | ★★★ | ★★★★★ | ★★★★★ | ★★★ | ★★★★★ |

---

## IV. Eight Strategic Insights

1. **"Full-stack" vs "single-point"**: Nokia chose full-stack connectivity (network → edge → cloud → app), Mobileye chose "AI + autonomy," Bosch chose "perception as anchor" — each has merit; choose based on your own positioning.

2. **"Vehicle intelligence" vs "vehicle-infrastructure-cloud"**: Waymo / Tesla represent vehicle intelligence; the C-ITS / V2X world represents infrastructure-coupled autonomy — not either/or, but complementary and coexisting.

3. **Data assets are the ultimate moat**: NYC DOT (450 TB/day), Tesla (3B FSD miles), Azure Maps (billions of daily requests) — the scale of data determines the qualitative leap in AI.

4. **"Safety" is not a feature but a system property**: Siemens / Thales' SIL4, NIST CSF 2.0, ISO 27001 — safety is not an add-on module but a system-engineering discipline that begins at design.

5. **"Standards" are the high ground**: 3GPP C-V2X, DATEX II, NTCIP, GTFS — whoever controls the standard controls the industry.

6. **Three models of the public-sector role**: Singapore model (industry-led + mandated + fast), US model (market-driven + federal devolution), European model (cross-border coordination + standards-first).

7. **"Advanced Air Mobility" is a new track**: the Joby / Skydio path shows that the binding constraint on AAM is not the aircraft but the digitalization of airspace management.

8. **"Data openness" unlocks social value**: TfL's open-data APIs spawned 600+ mobility apps — invest millions, unlock hundreds of millions in social value.

---

> **Version Record**: V1.0.0 | 2026-07-05 | Compiled from public annual reports / industry reports / technical white papers. Sources include listed-company annual reports, public-agency statistics, and analyst reports from Gartner, IDC, and McKinsey.
