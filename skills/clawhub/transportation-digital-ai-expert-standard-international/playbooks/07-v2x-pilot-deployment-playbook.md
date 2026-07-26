# V2X Pilot Deployment Playbook

## Playbook Overview

| Item | Description |
|------|-------------|
| **Applicable scenarios** | Deploying a V2X (vehicle-to-everything) pilot — installing RSU / OBU / MEC / sensing equipment, system integration, and test validation on urban roads or highways |
| **Technical architecture** | "Vehicle–Road–Cloud–Network" four-layer architecture, aligned with the C-V2X / vehicle-infrastructure-cloud standard system (3GPP / ETSI / SAE) |
| **Pilot scale** | Typical pilot: 10–50 intersections (urban) / 10–30 km corridor (highway) |
| **Total duration** | 5–8 months (excl. weather-stoppage days) |
| **Core delivery team** | 1 PM + civil/construction crew (outsourced) + 1 network engineer + 2–3 system-integration engineers + 2 test engineers |
| **Safety requirement** | Construction safety is paramount — lane-closure work must follow national signage & safety standards; any safety incident is an automatic fail |

---

## Phase 1: Site Selection & Planning (Weeks 1–4)

### 1.1 Site-Selection Criteria

**Urban-intersection selection scorecard:**

| Dimension | Weight | Ideal condition | Score (1–5) | Note |
|-----------|--------|-----------------|-------------|------|
| Road class | 20% | Arterial / collector (not minor residential) | | Arterial 5, collector 4, minor 2 |
| Traffic volume | 20% | AADT >20,000, clear peaks | | High volume = more conflict = more V2X value |
| Crash history | 25% | Injury crashes in last 3 yr, or blackspot | | Blackspots = strongest V2X value — "solve pain" |
| Scenario complexity | 15% | Complex junction (odd geometry / uncontrolled / mixed traffic) | | V2X safety value stands out in complex scenes |
| Topology | 10% | Reasonable spacing (200–800 m), good sight distance / no obstruction | | RSU covers ~300–500 m radius |
| Power & comms | 10% | Nearby stable power & fiber | | No power = new cabling, much higher cost/time |
| **Weighted total** | | | | >3.5 priority, 2.5–3.5 optional, <2.5 not advised |

**Highway site-selection scorecard:**

| Dimension | Weight | Ideal condition | Note |
|-----------|--------|-----------------|------|
| Crash blackspot | 30% | Multi-crash segments (curve / grade / tunnel mouth / interchange) | V2V/V2I warning most valuable |
| Frequent adverse weather | 20% | Fog / ice / crosswind prone | V2X substitutes vision in low visibility |
| Traffic volume | 15% | AADT >30,000, high truck share | Truck crashes severe; warning valuable |
| Merge / diverge | 15% | Interchanges, ramp terminals | Merge conflict is a top highway-crash cause |
| Work / upgrade zone | 10% | Planned work zone (temp deploy) | Precise dynamic warning at work zones |
| Power & comms | 10% | Nearby power & fiber | |

### 1.2 Coverage Design

**RSU deployment principles:**

| Scenario | Recommended spacing | Coverage | Mount height | Note |
|---------|---------------------|----------|--------------|------|
| Urban open road | 300–500 m | ~300 m radius | 6–10 m (light/signal pole) | Watch building blockage — urban canyon |
| Urban intersection | 1 per intersection | Whole junction + 150 m approach | 6–10 m | On central signal pole or dedicated pole |
| Highway straight | 500–800 m | ~400 m radius | 8–15 m (gantry / dedicated) | High speed needs longer warning distance |
| Highway curve / grade | 300–500 m | Densify limited-sight areas | 8–15 m | Inside curve or crest |
| Tunnel | Tunnel mouth + 1 per 500 m inside | Inside/outside coordination | Tunnel wall | No GPS inside; dense RSU for positioning aid |

**RSU count:**
```
Urban pilot:  N_RSU ≈ intersections × 1.2 (corridor top-up factor)
Highway pilot: N_RSU ≈ corridor length(km) / 0.5 (avg one per 500 m)
```

### 1.3 Infrastructure Survey

**Pole / infrastructure survey checklist:**

**A. Pole condition:**
- [ ] Pole type: light / signal / enforcement-camera / sign / gantry / dedicated
- [ ] Height meets RSU requirement (6–15 m recommended)
- [ ] Load capacity sufficient (RSU + antenna + brackets, usually <20 kg, but confirm)
- [ ] Free arm / mounting position available
- [ ] If new pole, any underground utilities / street trees / building setback obstacles?
- [ ] Pole ownership clear? (light poles → municipal/utility; signal poles → traffic authority; need owner's permit)

**B. Power condition:**
- [ ] Nearby stable 220V AC source?
- [ ] Distance to source? If >50 m, lay cable or use solar + battery
- [ ] Separate meter needed? (large projects usually meter separately)
- [ ] Backup power? (key intersections: UPS or solar + battery)

**C. Comms condition:**
- [ ] Nearby fiber point (carrier FTTx / gov network)?
- [ ] Distance to fiber point? (>200 m greatly raises cost)
- [ ] If no fiber, can 5G / LTE-V2X backhaul? (confirm 5G coverage & bandwidth)
- [ ] Wireless backhaul: confirm carrier 5G signal strength, bandwidth, latency (measured)

**D. Sight condition:**
- [ ] RSU antenna position blocked by buildings / trees / billboards?
- [ ] All four approaches have open sight?
- [ ] For camera / radar / LiDAR, can the mount height see all approaches?

---

## Phase 2: Civil Works & Equipment Installation (Weeks 5–16)

### 2.1 Pole Installation

**New-pole construction steps:**

| Step | Content | Cure/wait | Note |
|------|---------|-----------|------|
| 1. Layout | Mark pole position per design on site | 1 day | Confirm no underground utility (call one-call / utility-locating service) |
| 2. Excavate | Dig foundation per drawing | 1–2 days | Usually 1.2×1.2×1.5 m (depth), adjust by height |
| 3. Pour base | Embed anchor bolts + pour concrete | Cure 7–14 days | C25/C30 concrete; embed PE conduit for cables |
| 4. Transport | Move pole from factory to site | 1 day | Hot-dip galvanize + paint before transport |
| 5. Erect | Crane lift + fix to anchor bolts | Half day | Traffic control + safety officer + licensed rigger |
| 6. Grounding | Lightning-protection ground | Half day | Ground resistance ≤10 Ω |
| 7. Accept | Verticality + bolt torque + coating | Half day | |

**Using existing poles — cautions:**
- Must obtain written consent from the pole owner
- Pre-construction structural safety assessment — corrosion / tilt / cracks; reject unfit poles
- Clamp mounting (no drilling) — never damage the original structure

### 2.2 Power Works

**Power-option selection:**

| Option | When | Strength | Limit |
|--------|-------|----------|-------|
| Tap municipal power | Within <50 m of a distribution/light box | Stable, low cost | Needs utility approval / meter |
| Solar + battery | Remote / no municipal power | Independent, renewable | Extended cloudy weather endurance; periodic battery replacement |
| Solar + grid hybrid | Unstable grid | High reliability | Higher cost |
| PoE (low-power only) | Short distance, low power | Simple cabling | <100 m, <30 W (std) / <90 W (PoE++) |

**Power checklist:**
- [ ] Power-connection permit obtained
- [ ] Cable rated for outdoor / buried (armored YJV22 or conduit-protected)
- [ ] Burial depth per code (generally >0.7 m)
- [ ] Leakage protection installed
- [ ] Surge-protection device installed
- [ ] Separate meter installed (if metered)
- [ ] Cable path marked (prevent later excavation damage)

### 2.3 Network / Backhaul Works

**Backhaul selection matrix:**

| Scenario | First choice | Fallback | Advice |
|---------|--------------|----------|--------|
| Fiber point nearby (<200 m) | Direct fiber | 5G private / CPE | Fiber = lowest latency, highest reliability |
| No fiber nearby (200–500 m) | 5G CPE | Self-built microwave / fiber | 5G CPE fastest, but test signal & latency |
| Highway corridor | Corridor fiber (along barrier / conduit) | 5G + segmented fiber | Highways usually have conduit; prefer fiber |
| Remote | 5G / 4G | Satellite + edge cache | Latency/bandwidth limited; degrade scenarios |

**Fiber-lay requirements:**
- Outdoor fiber: single-mode, armored, G.652D
- Connectors: LC/UPC or SC/UPC
- Splice loss: <0.3 dB/point
- Total attenuation: < link budget (usually <3 dB @1310 nm, short distance)
- Spare cores: ≥2 per site (1 active + 1 standby + expandable)
- Protection: buried in conduit (PVC/PE), aerial on messenger wire

### 2.4 RSU Installation

**RSU install steps & checklist:**

| Step | Content | Check |
|------|---------|-------|
| 1. Pre-check | Unbox & accept | Model, qty, accessories complete, no damage |
| 2. Bracket | Mount RSU bracket on arm/top | Tightened (torque wrench), waterproof seal |
| 3. Host | Fix RSU host on bracket | Correct orientation (usually vertical), heat sink unobstructed |
| 4. Antenna | Install V2X antenna (PC5/Uu dual or multi) | Correct polarization, no blockage, feed bend radius >5× diameter |
| 5. Cabling | Power (AC/DC/PoE), fiber/ethernet, antenna feed | Tight connectors, waterproof (IP67 + tape outdoors) |
| 6. Ground | Ground to pole system | Resistance ≤10 Ω |
| 7. Power-on | Check status LEDs | Green power, normal boot, network up |
| 8. Config | Set RSU IP, PC5 params, MEC/cloud address | Ping MEC/cloud, base-station timing normal |
| 9. Label & log | Tag + photo | Tag: site ID, RSU S/N, date, maintenance phone |
| 10. Report | Fill install record | Signed record + photo archived per site |

**Key install notes:**
- Keep ≥30 cm between RSU antenna and 4G/5G/WiFi antennas (avoid co/adjacent-channel interference)
- Keep feed line short (each +1 m ≈ 0.3–0.5 dB loss @5.9 GHz)
- All outdoor joints use "three-layer" waterproof: insulation tape → self-amalgamating tape → insulation tape
- After install, drive a V2X test unit at 300/500/800 m to measure signal strength

### 2.5 Sensor Installation & Calibration

**Common roadside sensor mounting:**

| Sensor | Mount | Height | Sight requirement | Calibration |
|--------|-------|--------|-------------------|-------------|
| Camera (bullet/PTZ) | Arm/top bracket | 6–12 m | Cover >150 m approach + stop line | Chessboard + road-feature GPS |
| Millimeter-wave radar | Arm bracket | 6–10 m | Cover 2–4 lanes, >200 m far | Corner-reflector + static-target verify |
| LiDAR | Arm/top | 6–10 m | 360° or directional | Point-cloud registration + GPS/IMU |
| MEC | Pole box / strap box | >1.5 m above ground | Ventilated, rain/sun shielded | - |

**Joint calibration flow:**
1. Camera intrinsic (chessboard)
2. Camera extrinsic — GPS RTK road control points → pixel↔world mapping
3. Radar — corner reflectors at known positions → calibrate azimuth/elevation/range
4. Multi-sensor joint — LiDAR↔camera, radar↔camera frame alignment
5. Verify — known-position target (calibration vehicle) detection error <0.5 m

---

## Phase 3: System Integration (Weeks 13–24, overlaps Phase 2)

### 3.1 RSU–MEC–Cloud Integration

**Integration architecture:**

```
RSU (roadside unit)
  ├─ PC5 interface (V2X direct) ←→ OBU (on-board unit)
  ├─ Ethernet / fiber ←→ MEC (multi-access edge compute)
  └─ Optional: 5G Uu interface ←→ V2X cloud platform
MEC (edge compute)
  ├─ Ingests multi-sensor (camera / radar / LiDAR)
  ├─ Runs sensor-fusion algorithm
  ├─ Generates V2X messages (BSM/RSI/RSM/MAP/SPAT)
  ├─ Ethernet / fiber ←→ V2X cloud platform
  └─ Optional: Ethernet ←→ traffic signal controller
V2X cloud platform
  ├─ V2X message management
  ├─ Cross-intersection / cross-region coordination
  ├─ Data storage & analytics
  └─ Application-service API
```

**Integration test steps:**

| Step | Content | Expected | Tool |
|------|---------|----------|------|
| 1. Connectivity | RSU↔MEC ping | Latency <5 ms | Ping |
| 2. Time sync | RSU & MEC GPS/GNSS/NTP | Sync error <1 µs (PC5 needs high precision) | NTP query / GPS status |
| 3. RSU registration | RSU registers to MEC/cloud | Platform shows RSU online | Cloud mgmt page |
| 4. Data report | RSU reports BSM/V2X to MEC/cloud | Normal receive, latency <50 ms (RSU→MEC) | Wireshark + cloud log |
| 5. MAP down | Cloud→MEC→RSU→OBU MAP | OBU parses & shows map | OBU test app |
| 6. SPAT down | Signal system→RSU→OBU SPAT | OBU shows green remaining secs | OBU app + compare to real signal |
| 7. RSI gen | MEC fusion → RSI | Correct detection + compliant format | MEC log + OBU app |

### 3.2 V2X Message Testing

**Core V2X message-set testing (Day 1 scenarios):**

| Message | Abbr | Sender | Content | Verify |
|---------|------|--------|---------|--------|
| Basic Safety Message | BSM | OBU | Position/speed/heading/accel | Periodic (10 Hz), RSU receives, content correct |
| Roadside Safety Message | RSM | RSU | Roadside-perceived road users (veh/ped/VRU) | MEC fusion → RSM, correct freq & content |
| Road Side Information | RSI | RSU | Road events (crash/work/congestion/weather/speed) | Create→RSI→OBU receive→correct alert |
| Map Data | MAP | RSU | Lane-level junction map | OBU renders map, links correct |
| Signal Phase & Timing | SPAT | RSU | Real-time phase & remaining time | OBU matches real signal (latency <100 ms) |

**V2X message conformance tools:**
- Independent test labs / certification bodies (e.g., DEKRA, TÜV, or the CAR 2 CAR / ETSI conformance suites)
- Open-source V2X test toolsets (e.g., OpenC2X / V2X test frameworks)
- Vendor-supplied RSU/OBU test apps
- Wireshark + V2X message dissector plugin

### 3.3 Application-Scenario Validation

**Day 1 mandatory scenarios (17 — per SAE J2735 / ETSI / industry Day-1 set):**

| # | Scenario | Type | Test method | Pass criteria |
|---|----------|------|-------------|---------------|
| 1 | Forward Collision Warning (FCW) | V2V | 2 vehicles, one slows/stops, other approaches | Warn when TTC<2 s |
| 2 | Intersection Collision Warning (ICW) | V2V | 2 vehicles approach uncontrolled junction perpendicularly | Warn 3–5 s before collision |
| 3 | Left Turn Assist (LTA) | V2V | Left-turn vs oncoming through | Warn on conflict |
| 4 | Blind-Spot / Lane-Change Warning (BSW/LCW) | V2V | Vehicle in adjacent blind spot | Warn when blind-spot occupied |
| 5 | Emergency Electronic Brake Light (EEBL) | V2V | Lead hard-brakes (decel >4 m/s²) | Warn within 100 ms |
| 6 | Wrong-Way Warning | V2V | Simulate wrong-way vehicle | Warn immediately on detection |
| 7 | Vulnerable Road User (VRU) Warning | V2P | Simulate ped/cyclist crossing | RSU detects → PC5 warn to vehicle |
| 8 | Green Light Optimal Speed Advisory (GLOSA) | V2I | Compute advised speed from SPAT | Pass on green at advised speed |
| 9 | In-Vehicle Signal Display | V2I | OBU receives & shows SPAT | Matches real signal, latency <100 ms |
| 10 | Curve/Spot Speed Warning (CSW) | V2I | RSU broadcasts speed limit | Warn on speeding |
| 11 | Hazardous Location Warning (HLW) | V2I | RSI broadcasts work/crash | OBU receives & warns |
| 12 | Congestion Ahead | V2I | RSI broadcasts congestion | OBU receives & suggests reroute |
| 13 | Emergency Vehicle Warning (EVP) | V2V | Simulate ambulance/fire approach | Warn to yield + signal priority |
| 14 | Cooperative Adaptive Cruise (CACC) | V2V | Multi-vehicle platoon | Gap down to 0.6–0.8 s (vs 1.5 s human) |
| 15 | Cooperative Lane Change (CLC) | V2V | Request–confirm–execute | No conflict during change |
| 16 | Sensor Sharing / Extended Senser | V2I | RSU perceives beyond-line-of-sight → OBU | OBU "sees" occluded target |
| 17 | Vehicle Control Loss Warning | V2V | Simulate loss of control (yaw/hard turn) | Surrounding vehicles warned |

---

## Phase 4: Testing & Optimization (Weeks 21–26)

### 4.1 Field Test Scenarios (30+)

**30+ scenario list (all 17 Day 1 + Day 2 extended):**

**Day 2 extended (13+):**

| # | Scenario | Type | Note |
|---|----------|------|------|
| 18 | Ramp Merge Assist | V2I | RSU senses ramp traffic, warns mainline |
| 19 | Work-Zone Warning | V2I | Work-zone RSU broadcasts precise zone |
| 20 | Adverse-Weather Warning | V2I | Fog/ice/standing-water broadcast |
| 21 | Dynamic Lane Management | V2I | Reversible/tidal lane via V2X |
| 22 | Signal Priority (bus/emergency) | V2I | Bus/ambulance requests → controller responds |
| 23 | Cooperative Perception Sharing | All V2X | MEC fuses multi-vehicle + multi-road sensing → share |
| 24 | Remote-Driving Assist | V2I | V2X + 5G remote control |
| 25 | HD-Map Dynamic Update | V2I | RSU broadcasts temp road change (closure/rerouting) |
| 26 | Closed-Area AV | V2I | Cooperative AV in campus/port/airport |
| 27 | Vehicle Platooning | V2V | 3+ trucks/buses platoon |
| 28 | Geo-Fence | V2I | Restricted/low-emission zone via V2X |
| 29 | Parking Guidance | V2I | Lot RSU broadcasts free spaces |
| 30 | Charging-Reservation Nav | V2I | Charging station RSU broadcasts availability |

### 4.2 Performance Benchmark Testing

**Key performance indicators (KPI):**

| KPI | Definition | Method | Industry benchmark | Target |
|-----|------------|--------|--------------------|--------|
| End-to-end latency | Event → OBU warning | High-precision GPS timestamp diff | <100 ms (Day1), <20 ms (Day2 adv) | <100 ms |
| PC5 latency | RSU→OBU over air | Send vs receive timestamp | <20 ms | <20 ms |
| Packet Delivery Rate (PDR) | Successful PC5 receive ratio | Send 1000 msgs, count received | >95% | >95% |
| Comm distance | Max distance at PDR>95% | Drive away, log PDR vs distance | LOS >800 m (urban), >1500 m (highway) | >500 m (urban) |
| Positioning accuracy | Vehicle self-position error | RTK reference vs OBU GPS | <1.5 m | <1.5 m (RTK <0.3 m) |
| RSU perception accuracy | RSU-detected vs true position | RTK reference vehicle vs RSU | Error <1 m | <1 m |
| RSU recall | Detected vehicles / all vehicles | Video playback manual vs RSU | >95% | >95% |
| Availability | 7×24 uptime | 1-week monitoring | >99.9% | >99.5% (pilot) |

**Latency measurement:**
1. All devices (RSU/MEC/OBU/test camera/reference sensor) synchronized via GPS/GNSS (incl. BeiDou/Galileo)
2. On triggering event (e.g., simulated pedestrian crossing), record T0 with high-precision GPS
3. On OBU warning receipt, record T1
4. E2E latency = T1 − T0 (subtract T0 detection time; pure comm latency = OBU receive − RSU send)

### 4.3 Performance Tuning

**Common issues & tuning:**

| Issue | Cause | Tuning |
|-------|-------|--------|
| Short comm range | Low antenna gain / blockage / multipath | Higher-gain antenna (5→8 dBi), adjust position & azimuth |
| Low PDR | Co-channel interference / too far / antenna | Channel scan → change channel, densify RSU (shorter spacing) |
| High latency | MEC load / congestion / queue backlog | MEC upgrade (GPU), optimize fusion, ensure QoS |
| False/missed detection | Bad calibration / weather / blockage | Re-calibrate, add redundant sensor (radar complements camera in rain) |
| Position drift | Urban-canyon GPS multipath / weak GNSS | Add IMU fusion, RTK differential, UWB local positioning |
| Instability | Poor cooling / unstable power / IP conflict | Check enclosure vent, UPS/regulator, network plan |

---

## Phase 5: Pilot Operations (Weeks 25–36)

### 5.1 Pilot KPI Monitoring

**Pilot monitoring dashboard:**

| Category | Metric | Source | Frequency |
|---------|--------|--------|-----------|
| **System health** | RSU online rate, MEC CPU/mem/GPU, disk | Monitoring (Prometheus/Zabbix) | 1 min |
| **Comm quality** | PC5 msg volume, PDR, avg latency | RSU+MEC stats | 5-min agg |
| **Perception quality** | Vehicle/ped detected, false/neg | MEC perception log | 1-hr agg |
| **App trigger** | Warning counts, accuracy (true positives) | MEC app log | 1 day |
| **UX** | OBU warning feedback (useful/useless/annoying), app crash | App telemetry | Real-time |

### 5.2 User-Feedback Collection

**Multi-channel feedback:**

| Channel | Audience | Method | Content | Frequency |
|---------|----------|--------|---------|-----------|
| Test-driver log | Test drivers | Electronic log post-test | Timeliness/accuracy, missed/false, usability | Per test |
| In-app feedback | Test drivers | One-click in app | Rate this warning (helpful/useless/wrong) | Real-time |
| Expert review | V2X / traffic-eng experts | Weekly ride-along + tech talk | Deep eval, benchmark vs international state-of-art | Weekly |
| Public demo day | Public / execs / media | Experience + survey | Perception, acceptance, concerns | 1–2 per phase |
| O&M log | System O&M | Daily record | Stability, maintainability, fault proneness | Daily |

### 5.3 System Optimization Iteration

**PDCA loop during pilot:**

```
Plan (weekly)
├─ Analyze last week's monitoring & feedback
├─ Identify Top 3 issues to optimize
├─ Set this week's optimization goal & plan
Do
├─ Execute (algorithm tuning / config / hardware)
├─ Log changes
Check
├─ Compare KPI before/after
├─ Test drivers verify improvement
Act
├─ If better: freeze config, update manual
├─ If worse: roll back, analyze cause
↓ next loop
```

**Optimization record template:**

| ID | Date | Item | Before | After | Method | Effect | Note |
|----|------|------|--------|-------|--------|--------|------|
| OPT-035 | 2026.07.05 | Junction fusion upgrade | Pedestrian recall 78% | Pedestrian recall 93% | Upgrade YOLO + raise radar-point-cloud fusion weight | Significant | Watch rainy-day behavior |

### 5.4 Scale-Up Plan

**Pilot → scale assessment checklist:**

- [ ] Did pilot KPIs clear the minimum bar for scale-up?
- [ ] Do the Top 10 pilot problems each have a mature solution?
- [ ] Is per-site deployment cost down to an acceptable level?
- [ ] Are construction / install / integration processes standardized? (SOP, std man-hours, std config template)
- [ ] Can the O&M system support larger scale? (toolchain, training, spare inventory)
- [ ] Is there a clear commercial / BOT / O&M partnership model?
- [ ] Is the 5.9 GHz ITS band (e.g., 5905–5925 MHz) use permitted by the local spectrum authority (for expansion)?
- [ ] Does scale-up trigger stricter security compliance (e.g., CII protection)?

**Scale-up path recommendation:**

| Stage | Scale | Time | Goal |
|-------|-------|------|------|
| PoC | 1–3 intersections | 3 mo | Tech validation |
| Small pilot | 10–50 intersections / 10–30 km | 6–8 mo | Scenario + O&M validation |
| Regional scale | 100–500 intersections / 50–200 km | 12–18 mo | Regional coverage + cost-down |
| City-wide | >1000 intersections / >500 km | 24–36 mo | City coverage + commercial ops |
| City-cluster | Multi-city interconnection | 36–60 mo | Cross-city coordination + integrated service |

---

## Appendix A: Site Survey Record Template

```
Site Survey Record
Project: XX City V2X Pilot
Date: 2026.07.05
Surveyors: Zhang San, Li Si

Site ID: V2X-SC-001
Address: Main St & Central Ave intersection (SE corner)
GPS: 30.274150N, 120.155070E

Road info:
- Junction type: 4-way signalized
- Lanes: 5 inbound (1 left + 3 through + 1 right)
- AADT: ~45,000 veh/day
- Crashes last 3 yr: 3 (1 rear-end, 2 sideswipe)

Pole condition:
☑ Use existing signal pole (No. TL-SC-1288)
□ New pole needed
Height: 8 m  Arm/mount: 1 free arm

Power:
☑ Nearby distribution box (No. PD-001, ~15 m, owned by utility)
Tap method: apply to utility for power

Comms:
☑ Nearby fiber point (carrier cabinet No. FO-SC-022, ~50 m)
□ 5G backhaul (5G signal: _____ dBm)

Sight:
☑ East approach clear (good)
☑ South approach clear (good)
☑ West approach blocked by building (fair — suggest add RSU at NW corner)
☑ North approach clear (good)

Underground utilities:
☑ Called one-call / locating service; confirmed no gas / HV cable at foundation
□ Pending (need further locate)

Photos: SC-001-E.jpg(E), SC-001-S.jpg(S), SC-001-W.jpg(W), SC-001-N.jpg(N), SC-001-pole.jpg

Assessment: ☑ Deployable □ Deploy after fix □ Not suitable

Note: Resolve west-side blockage; suggest add 1 RSU at NW corner
```

## Appendix B: Equipment-Install Checklist

```
Equipment Install Checklist
Site ID: V2X-SC-001
Equipment: RSU ×1, MEC ×1, Camera ×2, mmWave radar ×1

Pre-install
□ Goods received complete, no damage
□ Tools ready (torque wrench, level, RJ45 crimper, fiber splicer)
□ Safety gear (helmet, hi-vis, harness, cones, signs, temp signals)
□ Lane-closure permit obtained (if needed)
□ Installers hold working-at-height certificate

During
□ Bracket tightened (torque: ____ N·m)
□ RSU/camera/radar level (dev <1°)
□ Antenna azimuth per design (____°)
□ Antenna polarization checked
□ All connectors tight
□ All outdoor joints waterproofed (three-layer)
□ Power polarity correct (red+/black-)
□ Fiber duplex direction correct (TX to RX)

Post
□ Power LED normal
□ Network up (ping MEC IP)
□ Time sync (NTP/GNSS)
□ V2X msg tx/rx test passed
□ Camera image clear, angle correct
□ Radar output normal
□ Enclosure locked, keys handed over
□ Site cleaned (no tools/materials left, safety gear removed)
□ Install photos archived (overall + detail + nameplate/S/N)
□ Install report signed

Acceptor: _______ (client)  Installer: _______ (vendor)  Date: _______
```

## Appendix C: Safety Protocol (During Construction)

**Ten construction-safety rules:**

1. **Lane-closure work must be reported to the highway/traffic authority ≥24 h ahead**, with written permit before starting
2. **Advance warning per national standard (e.g., MUTCD / equivalent signage)**: warning sign (>100 m ahead) → work sign → speed limit → cones/water-filled barriers → work zone
3. **All personnel wear hi-vis vests & helmets**; work-at-height (>2 m) needs full harness with double lanyard
4. **Crane work needs a dedicated signalperson** — 1 operates, 1 directs — no substitution
5. **Live electrical work by licensed electrician only** — isolate → verify → tag → work → restore
6. **Stop height & live work in bad weather** (wind >6 Bft / heavy rain / lightning / fog visibility <200 m)
7. **Daily pre-work safety briefing** — what, where's the danger, what to do
8. **Clear site daily** — no open pits, no sharp objects, no trip hazards from temp cable
9. **Keep ≥1 lane open during work** — full closure needs a detour plan announced ahead
10. **Anyone may stop work for safety** — safety > schedule

**Emergency plan (during construction):**
- Injury: call emergency services (911/112) → on-site first aid → preserve scene → report to PM
- Cut cable / utility: stop → notify owner → isolate hazard → start repair
- Severe congestion: open temp lane → notify authority → adjust plan
- Equipment fall: evacuate below → cordon → find cause

---

> **Legal notice**: This playbook is protected under applicable copyright law. Without the author's written authorization, no commercial use is permitted (including resale, bundling, commercial training, or SaaS-ification).
> **Disclaimer**: The methodology herein is for learning reference only and does not constitute professional advice of any kind. V2X involves traffic safety; any deployment must be performed by certified professionals under applicable national regulations and standards. Construction safety is a matter of life; safety rules are not negotiable.
> **Author**: yinjianheng (Yin Jianheng) | yinjianheng@foxmail.com | WeChat: YJH-yinjianheng
