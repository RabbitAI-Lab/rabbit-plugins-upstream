# Case 04: Urban Rail Fully Automatic Operation (FAO) Upgrade

## Case Overview

| Dimension | Detail |
|-----------|--------|
| Line | Metro Line 3 (north–south trunk line) |
| Parameters | 35.2 km; 28 stations (22 underground, 6 elevated) |
| Legacy system | CBTC GoA2 (driver monitors in cab) |
| Target system | FAO GoA4 (unattended driverless) |
| Total investment | €165 million (vs ~€1.1B to build a new equivalent line) |
| Retrofit period | 2020–2023 (three years, no service suspension) |
| Operator | Metropolitan rail operator (public authority) |

---

## 1. Why Upgrade

### 1.1 An Aging Trunk Line

Metro Line 3 is the city's first north–south trunk, opened in 2005 and by 2020 carrying 850,000 passengers/day — about 30% of the network. Fifteen years brought accumulating problems:

1. **Aging signalling.** The original Siemens CBTC was end-of-life; spares grew scarce, some cards sourced from the second-hand market. In 2019, signal faults caused 23 delays >5 minutes, triggering public complaints.
2. **High crew cost.** 155 drivers (incl. relief) on three shifts, ~€4M/yr and rising 6%/year; recruitment was increasingly difficult.
3. **Capacity bottleneck.** Minimum headway 150 s; peak load factor 130%. The signalling limited further compression.
4. **Rising passenger expectations.** A newer GoA4 line (opened 2020) offered a clean, punctual, modern image in stark contrast; social media complaints mounted.

### 1.2 Upgrade or Rebuild?

An 8-month feasibility study was decisive:

| Dimension | Retrofit (GoA2→GoA4) | New parallel line |
|-----------|----------------------|-------------------|
| Investment | €165M | ~€1.1B (35 km new) |
| Schedule | 3 yrs (no service impact) | 5–6 yrs |
| Operations impact | Night works; daytime normal | None (new alignment) |
| Technical risk | Medium (mature global cases) | Low |
| Approval | Municipal | National infrastructure authority |

**Conclusion:** Retrofit was the only rational choice — €165M vs €1.1B.

---

## 2. Technical Solution

### 2.1 Path from GoA2 to GoA4

A "GoA2 → GoA3 → GoA4" transition:

| Stage | Period | Target | Key content |
|-------|--------|--------|-------------|
| GoA2→GoA3 | 2020–2021 | Driver moves from cab to saloon, on-board but not driving | DTO (driver-trained operation) |
| GoA3→GoA4 | 2021–2022 | Driver fully off-train; remote supervision | Auto wake/sleep, auto depot movements |
| GoA4 full | 2022–2023 | Fully unattended | Obstacle detection, platform-gap fault self-recovery |

### 2.2 Core Retrofit Scope

**(1) Signalling upgrade (€76M)**
- New FAO signalling (CBTC upgrade from a regional supplier)
- Added: interlocking renewal, new zone controllers, DSU upgrade
- Cutover: "dual-system parallel" — both old and new on-board equipment installed; days on old, nights testing new. A single 56-hour weekend cutover completed the line.
- Window: a 5-day holiday low-traffic period + adjacent weekends; actual cutover 56 hours.

**(2) Rolling-stock modification (€39M)**
- 42 trains (252 cars) returned to works for FAO adaptation
- Removed cabs → standing area; added obstacle detection, passenger–control direct emergency intercom, upgraded HVAC/lighting/PA
- Pace: one train per two weeks with backup trains maintaining capacity; all 42 in 21 months

**(3) Platform-screen doors & gap protection (€21M)**
- All 28 stations' PSDs upgraded; dual-mode gap detection (laser + infrared)
- PSD–signal interlock; foreign-object detection blocks departure
- Full platform CCTV to the control center

**(4) Depot automation (€8M)**
- Automatic wake/sleep, wash, and inspection; pantograph, wheelset, underbody inspection robots; depot protection zone (SPI)

**(5) Control-center upgrade (€11M)**
- New train, passenger, and maintenance dispatcher desks
- 8 on-board CCTV feeds per train to center
- Passenger emergency intercom (2 per car, direct to passenger dispatch)

**(6) Intelligent maintenance (€10M)**
- On-line condition monitoring (bogies, pantographs, traction)
- AI fault prediction (trained on historical faults)
- Maintenance knowledge graph (fault–cause–remedy)

### 2.3 Safety Case — the "Permit" for Driverless

FAO requires a rigorous safety case:
1. **HAZOP:** 47 hazard scenarios identified; 12 high-risk, each mitigated so residual risk is ALARP.
2. **SIL assessment:** safety functions assigned SIL levels; critical functions reach SIL4 (per IEC 61508 / EN 50129).
3. **Independent Safety Assessment (ISA):** a Notified Body (TÜV) tracked design, manufacture, install, and test, issuing the safety certificate.
4. **Trial operation:** 100,000 km / 2,000 hours of unattended (night, empty) trial — zero safety incidents.
5. **Multi-scenario testing:** 28 fault scenarios validated, including train fire (auto-station, auto-open, auto-evacuation broadcast), signalling degradation (auto fallback to restricted manual driving mode), obstacle detection (auto emergency brake), passenger emergency intercom.

---

## 3. Delivering Without Suspension — "Changing Engines in Flight"

### 3.1 Operations–Works Coordination

Retrofitting a live line was the greatest challenge. Strategy: "night window + backup trains + contingency":
1. **Daily window:** 00:00–04:30 (4.5 h), ~3 h effective
2. **Weekend extended window:** Sat 00:00 – Sun 06:00 (6 h)
3. **Holiday large window:** 3–5 consecutive days

### 3.2 Three Near-Misses
1. **Mar 2021:** a mis-wired cable caused packet loss on the old system. New system was not yet cut in; impact 15 min. Physical isolation standards were tightened.
2. **Sep 2021:** a storm lost a weekend window; schedule slipped 3 days. Added 15% weather buffer.
3. **Jan 2022 (night before cutover):** integration testing found 3 incorrect interlocking-table configs — would have caused an operating accident. Team worked 48 h; cutover postponed to post-holiday. Automated config-validation was strengthened.

---

## 4. Public Communication Strategy

### 4.1 Passengers' Fear
- "Would you dare ride a train with no driver?"
- "What if it fails? Can a computer beat a human?"

### 4.2 Communication Strategy
1. **Transparent showcase:** a "future train" experience zone with VR.
2. **Data speaks:** published a *Driverless Safety White Paper* — global GoA4 lines have logged >500M safe km, accident rate far below manual.
3. **Influencer experience:** 20 local KOLs as "first riders" publishing trial reports.
4. **Emergency transparency:** disclosed all safety-test scenarios and results — "unmanned, but always guarded" (24/7 professional control-center team).
5. **Gradual trust building:** GoA3 (driver in saloon) ran 6 months before GoA4.

### 4.3 Result (post GoA4, Jan 2023)
- Satisfaction: 72 → 89
- Positive recognition of "driverless safety": 38% → 82%
- Line ridership +8% YoY (above the 5% network average)

---

## 5. Outcomes

| Metric | Before (GoA2) | After (GoA4) | Change |
|--------|---------------|--------------|--------|
| Minimum headway | 150 s | 110 s | −26.7% |
| Peak-hour capacity | 24 tph | 32 tph | +33.3% |
| Drivers | 155 | 0 (15 remote supervisors) | −90.3% |
| Crew cost | €4.0M/yr | €0.95M/yr | −76.8% |
| Punctuality | 99.80% | 99.95% | +0.15pp |
| Delays >5 min | 23/yr | 3/yr | −87.0% |
| Train energy | 5.8 kWh/veh-km | 4.9 kWh/veh-km | −15.5% |
| Equipment failure | 12.5 /Mio veh-km | 5.2 /Mio veh-km | −58.4% |
| Satisfaction | 72 | 89 | +17 pts |

---

## 6. Lessons

1. **Retrofit is far better value than rebuild:** €165M vs €1.1B — under one-sixth for equivalent effect. Retrofitting aging lines should be the priority for urban-rail modernization.
2. **Safety case is not a formality:** HAZOP, SIL, ISA matter. Three of the 47 hazards were missed by the designer initially; without the safety case they could have been latent major hazards.
3. **"Dual-system parallel" is the master key:** running both systems 6+ months safeguarded operations and gave the new system full testing. Cost ~15% extra equipment — worth it.
4. **Public communication equals engineering:** ~€2.8M spent (experience zone + KOLs) bought smooth social acceptance — value far beyond cost.
5. **Intelligent maintenance is FAO's "standard fit":** with no driver as last-resort fallback, maintenance must self-diagnose/self-heal/respond fast. The system flagged 12 potential faults in year one, avoiding ≥3 service-affecting failures.
6. **Reshape the talent structure:** from "driver-operated" to "remote-supervision + intelligent-maintenance" demands different skills. Driver reskilling (electrical/automation/data) started a year early.

---

*Case authored: May 2024 | Sources: operator annual report, retrofit acceptance report, independent safety-assessment report*
