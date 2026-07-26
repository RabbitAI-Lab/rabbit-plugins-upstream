# 03 — System Integration & Testing Management Workflow

## 1. Workflow Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│              System Integration & Testing Management Map              │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐        │
│  │1.Integration│>│2.Test Case│──>│3.Test     │──>│4.Defect   │        │
│  │  Test Strat.│  │  Design   │   │  Execution│   │  Mgmt &   │        │
│  │           │   │          │   │  & Track  │   │  Fix      │        │
│  └──────────┘   └──────────┘   └──────────┘   └──────────┘        │
│       │              │              │              │                │
│       v              v              v              v                │
│  ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐        │
│  │5.Performance│>│6.Security │──>│7.UAT      │──>│8.Test     │        │
│  │  Test &   │   │  Test &   │   │  Acceptance│   │  Report &  │        │
│  │  Tuning   │   │  Penetr.  │   │  Test     │   │  Summary   │        │
│  └──────────┘   └──────────┘   └──────────┘   └──────────┘        │
│                                                                     │
│  Four test phases: Unit → Integration → System → Acceptance (UAT)  │
└─────────────────────────────────────────────────────────────────────┘
```

## 2. Detailed Steps

---

### Step 1: Integration Test Strategy

**Objective**: Define a comprehensive test strategy; clarify scope, methods, and resources.

**Guidance:**

**1.1 Test strategy document structure**

```
Test strategy document:

1. Test objectives & scope
2. Test environment plan
   - Dev / test / pre-prod / production environments
3. Test types & phases
   - Unit → Integration → System → UAT
4. Tool chain
   - Automation: Selenium / Cypress / JMeter
   - Performance: JMeter / Locust
   - Security: OWASP ZAP / Burp Suite
   - Test management: TestLink / Zephyr / Xray
5. Test data strategy
   - Test-data prep, masking, refresh strategy
6. Defect-management process
7. Test exit criteria
8. Resources & schedule
```

**1.2 Transport-system integration test focus**

| Integration scenario | Test focus | Test data |
|---------|---------|---------|
| Video-platform integration | ONVIF Profile S / RTSP streaming interoperability, media playback | Multi-stream live / historical video |
| GIS integration | Map loading, layer overlay, coordinate conversion | Real road-network GIS data |
| IoT device integration | MQTT messages, device commands, heartbeats | Mixed simulated + real devices |
| Third-party data source | API calls, timeout/retry, data format | Mock + real API |
| SSO / unified auth | Login / logout / token refresh / permissions | Multiple role accounts |

---

### Step 2: Test Case Design

**Objective**: Design systematic, reusable test cases based on the requirements document.

**Guidance:**

**2.1 Test-case design methods**

| Method | Applicable scenario | Example |
|------|---------|------|
| Equivalence partitioning | Input has range limits | Flow value normal (0–9999), boundary (0,9999), abnormal (-1,10000) |
| Boundary value analysis | Data boundaries | Concurrent users = 10 / 100 / 1000 |
| Scenario method | Business process | Event detection → confirm → dispatch → handle → archive |
| Error guessing | Experience-based | Network drop → data re-send after recovery |

**2.2 Test case template**

| Attribute | Example |
|------|------|
| Case ID | TC-MON-001 |
| Title | Verify AI traffic-event detection — stopped-vehicle event |
| Module | Road-network operations monitoring |
| Precondition | Video stream connected, AI model deployed |
| Steps | 1. Play test video with stopped-vehicle event 2. Observe AI result 3. Record detection time & location |
| Expected | Detect stopped-vehicle event, location error <50 m, latency <3 s |
| Test data | test_video_parking_01.mp4 |
| Priority | P0 (core function) |
| Case type | Functional test |

---

### Step 3: Test Execution & Tracking

**Objective**: Execute tests systematically; track test progress.

**Guidance:**

**3.1 Test execution rounds**

```
Recommended at least 3 rounds:

Round 1: Smoke Test
  · Purpose: Verify core functions work; decide whether to proceed
  · Timing: Immediately after each build deployment
  · Pass std: Core functions 100% pass

Round 2: Full Regression
  · Purpose: Comprehensive regression verification
  · Timing: 2–3 days
  · Pass std: Case pass rate >95%, 0 P0/P1 defects

Round 3: Pre-UAT
  · Purpose: Ensure UAT is basically usable
  · Timing: 1 day
  · Pass std: Case pass rate >98%
```

**3.2 Test progress tracking**

| Metric | Target | Frequency |
|------|:---:|:---:|
| Case execution rate | 100% | Daily |
| Case pass rate | >95% | Daily |
| P0 defect count | 0 | Daily |
| P1 defect count | <5 | Daily |
| Defect fix rate | >90% | Weekly |

---

### Step 4: Defect Management & Fix

**Objective**: Govern the full defect lifecycle, from discovery to closure.

**Guidance:**

**4.1 Defect lifecycle**

```
Defect state flow:

  New → Open → In Progress →
    Resolved → Verified → Closed
                  │
                  └→ Reopened → In Progress ...
```

**4.2 Defect severity definitions**

| Level | Definition | Response time | Fix time |
|:---:|------|:---:|:---:|
| P0 — Critical | System crash / core function unusable / data loss | 2 hrs | 24 hrs |
| P1 — Major | Major function abnormal / has clear workaround | 4 hrs | 3 days |
| P2 — Minor | Secondary function abnormal / UX issue | 1 day | 7 days |
| P3 — Trivial | UI / copy optimization / suggestion | Within Sprint | Next Sprint |

**4.3 Common transport-system defects**

| Defect type | Common symptom |
|---------|---------|
| Video stutter / artifacts | Bitrate adaptation issue, browser incompatibility |
| GIS coordinate offset | Coordinate-system conversion error (e.g., WGS84 vs. local projected CRS) |
| Data inconsistency | Same data shows different values in different places |
| Time-format chaos | Millisecond-to-date format not unified |
| Interface timeout | Large-volume interface not paginated |
| Concurrency issue | Multiple users operating same data simultaneously |

---

### Step 5: Performance Testing & Tuning

**Objective**: Verify that system performance meets requirements.

**Guidance:**

**5.1 Performance test scenarios**

| Scenario | Content | Metric |
|------|---------|---------|
| Baseline | Single-user basic operation | Single-step response time |
| Load | Simulate normal user concurrency | Average response time |
| Stress | Gradually increase concurrency to find knee | Max concurrency, TPS |
| Stability | Long run (24 h+) | Memory leak, GC |
| Peak | Simulate holiday / event peak | Peak TPS |

**5.2 Transport-system performance focus**

| Focus | Typical metric |
|-------|---------|
| Map load (1000+ segments) | <3 s |
| Video list load (1000 streams) | <2 s |
| Data dashboard refresh | <1 s |
| API query response | <200 ms (P99) |
| Report export (millions of rows) | <30 s |
| Concurrent users | >500 |

---

### Step 6: Security Testing & Penetration

**Objective**: Verify system security; identify vulnerabilities.

**Guidance:**

**6.1 Security test types**

| Type | Content | Tool |
|---------|------|------|
| Vulnerability scan | Tool-based known-vulnerability scan | Nessus / Tenable / Qualys |
| Web pentest | OWASP Top 10 | Burp Suite / ZAP |
| Code review | Static code security analysis | SonarQube / Fortify |
| Config check | Security-baseline config check | Baseline-check scripts |
| Auth testing | Login / permission / session security | Manual + tool |

**6.2 Security-baseline technical checklist (aligned with ISO/IEC 27001 / CIS Benchmarks)**

- [ ] Identity authentication (password strength, lockout on failure, MFA)
- [ ] Access control (least privilege, role separation, sensitive labeling)
- [ ] Security audit (complete logs, non-deletable, periodic review)
- [ ] Communication confidentiality (TLS 1.3 in transit)
- [ ] Data confidentiality (AES-256 at rest)
- [ ] Data integrity (digital signature / checksum)

---

### Step 7: UAT (User Acceptance Testing)

**Objective**: Organize client UAT; obtain acceptance sign-off.

**Guidance:**

**7.1 UAT preparation**

- Prepare UAT environment (identical to production)
- Prepare UAT accounts (cover all roles)
- Prepare UAT data (masked version of real business data)
- Write UAT guide (operating guide for non-technical users)
- UAT training (30–60 min hands-on)

**7.2 UAT execution**

| Stage | Content | Duration |
|------|------|:---:|
| UAT training | System operation training | 0.5 day |
| UAT execution | Users operate per test cases | 1–2 weeks |
| Issue collection | Collect user feedback and defects | Ongoing |
| Issue fix | Fix issues found in UAT | 1–2 weeks |
| UAT retest | Verify fix effectiveness | 3–5 days |
| UAT sign-off | User signs acceptance confirmation | 1 day |

---

### Step 8: Test Report & Summary

**Objective**: Author the complete test report as acceptance evidence.

**Guidance:**

**8.1 Test report structure**

```
Test summary report:

1. Test overview
2. Test environment
3. Test execution
   - Test-case execution statistics
   - Defect statistics & analysis
   - Performance test results
   - Security test results
4. Quality assessment
   - Whether exit criteria are met
   - Residual defects and risk assessment
5. UAT acceptance conclusion
6. Recommendations & improvements
```

---

## 5. Key Checkpoints

| # | Checkpoint | Pass standard |
|---|--------|---------|
| CP1 | Integration test | Core interfaces 100% pass |
| CP2 | Full regression | Pass rate >95%, 0 P0 defects |
| CP3 | Performance test | Metrics meet contract requirements |
| CP4 | Security test | No high-risk vulnerabilities; baseline checks pass |
| CP5 | UAT complete | Client signs UAT acceptance confirmation |
| CP6 | Test report | Test report confirmed by both parties |

---

## 6. Estimated Duration

| Stage | Small | Medium | Large |
|------|:---:|:---:|:---:|
| Integration test | 1 wk | 2–3 wks | 3–5 wks |
| System test | 1–2 wks | 2–3 wks | 3–5 wks |
| UAT | 1 wk | 2–3 wks | 3–4 wks |
| **Total** | **3–5 wks** | **6–9 wks** | **9–14 wks** |

---

> **Version**: V1.0 | **Date**: 2025-07
