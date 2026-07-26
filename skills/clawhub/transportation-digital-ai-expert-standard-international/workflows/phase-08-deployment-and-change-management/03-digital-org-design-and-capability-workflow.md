# 03 — Digital Organization Design & Capability Building Workflow

## 1. Workflow Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│              Digital Org Design & Capability Building Map             │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐        │
│  │1.Org      │──>│2.Target   │──>│3.Role     │──>│4.Capability│       │
│  │  Diagnosis│   │  Structure│   │  Design & │   │  Model     │       │
│  │          │   │  Design   │   │  JD Author│   │  Build     │       │
│  └──────────┘   └──────────┘   └──────────┘   └──────────┘        │
│       │              │              │              │                │
│       v              v              v              v                │
│  ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐        │
│  │5.Talent   │──>│6.Training│──>│7.Recruit  │──>│8.Roadmap  │        │
│  │  Review   │   │  System  │   │  & Talent│   │  & Track  │        │
│  │  & Identify│  │  Design  │   │  Attraction│  │          │        │
│  └──────────┘   └──────────┘   └──────────┘   └──────────┘        │
└─────────────────────────────────────────────────────────────────────┘
```

## 2. Detailed Steps

---

### Step 1: Organization Current-State Diagnosis

**Objective**: Fully understand the client's current org structure, talent structure, and digital capability.

**Inputs**: T-DMM assessment (organization & talent dimension), stakeholder interviews
**Outputs**: Organization current-state diagnosis report

**Guidance:**

**1.1 Diagnosis dimensions**

| Dimension | Content |
|------|---------|
| Org structure | Current IT / digital department setup, reporting lines, functional split |
| Talent structure | Age / education / major / skill distribution |
| Role setup | Existing digital-related roles and JDs |
| Capability level | Digital-skill self-assessment + objective assessment |
| Compensation | Digital talent pay level and competitiveness |

**1.2 Common transport-industry org findings**

- IT department seen as "computer repair" rather than "innovation driver"
- Lack of new roles like data engineer, AI engineer
- Digital talent pay far below market; hard to recruit and retain
- The "gap" between business units and IT

---

### Step 2: Target Organization Structure Design

**Objective**: Design an org structure suited to digital transformation.

**Guidance:**

**2.1 Reference transport-digital org model**

```
Recommended structure (for a Department / Bureau of Transportation):

                ┌─────────────────┐
                │   Chief Digital Officer (CDO)│
                └────────┬────────┘
                         │
         ┌───────────────┼───────────────┐
         │               │               │
         v               v               v
  ┌────────────┐  ┌────────────┐  ┌────────────┐
  │ Tech & Info│  │ Data Center │  │ Business    │
  │ Division   │  │ (Platform + │  │ Departments │
  │(Strategy+   │  │  Data)      │  │(Digital     │
  │ standards) │  │            │  │ Liaisons)    │
  └─────┬──────┘  └─────┬──────┘  └─────┬─────┘
        │               │               │
        └───────────────┼───────────────┘
                        │
              ┌─────────┴─────────┐
              │ Digital Transform.│
              │ Working Group     │
              │ (cross-functional)│
              └───────────────────┘
```

**2.2 Key design principles**

| Principle | Note |
|------|------|
| Elevate strategic positioning | IT moves from "ops support" to "innovation driver" |
| Business–IT fusion | Set "digital liaisons" in business units |
| Centralized data management | Establish a unified data-management function |
| Internalize AI capability | Gradually build own AI / data team |

---

### Step 3: Role Design & JD Authoring

**Objective**: Design key roles and job descriptions for the digital organization.

**Guidance:**

**3.1 Key transport-digital role list**

| Category | Key roles | Core duty |
|---------|---------|---------|
| Data | Data architect, data engineer, data analyst | Data-platform build, governance, analysis |
| AI | AI algorithm engineer, AI product manager | Transport AI R&D, AI product design |
| Platform | Cloud engineer, DevOps engineer | Infrastructure, automated O&M |
| Security | Cybersecurity engineer, data-security specialist | Protection, security-baseline compliance |
| Business | Digital product manager, business analyst (BA) | Requirements, product planning |
| Management | Chief Digital Officer (CDO), digital PMO | Strategy, project management |

**3.2 JD template**

```
Job Description (JD) template:

Job title: Data Engineer
Department: Data Center
Reports to: Data Architect
Pay grade: P4–P6

Responsibilities:
1. Build and maintain the transport big-data platform
2. Design ETL/ELT flows for multi-source transport data ingestion & processing
3. Establish data-quality monitoring to ensure accuracy and timeliness
4. Support data analysts and AI engineers with data preparation
5. Participate in data governance; maintain the data-asset catalog

Requirements:
1. Bachelor's or above; CS / statistics / transport-related major
2. 3+ yrs big-data development; transport experience preferred
3. Proficient in Hadoop ecosystem (HDFS / Hive / Spark / Flink)
4. Skilled in Python / Java / Scala (at least one)
5. Familiar with data-warehouse modeling (Kimball / Inmon)

Plus:
· Knowledge of transport-industry standards (e.g., ISO 14827 / SAE / CEN)
· Experience with time-series DBs (InfluxDB / TDengine)
```

---

### Step 4: Capability Model Build

**Objective**: Build a digital-talent capability model as the standard for hiring, training, and appraisal.

**Guidance:**

**4.1 Digital capability model**

```
Transport-digital talent capability model:

┌─────────────────────────────────────────────┐
│ General digital literacy (all staff)         │
│ ·Data mindset ·Digital tools ·Security ·Learn│
├─────────────────────────────────────────────┤
│ Professional skills (by role)                │
│ Data:  modeling|ETL|viz|SQL                  │
│ AI:    ML|DL|CV/NLP|model deploy             │
│ Dev:   Java/Python|microservices|K8s|CI/CD   │
│ Sec:   pentest|audit|baseline|data security  │
├─────────────────────────────────────────────┤
│ Business understanding (by domain)           │
│ ·Transport-engineering basics ·process ·req  │
│ ·Standards awareness ·trend insight          │
├─────────────────────────────────────────────┤
│ Soft skills                                  │
│ ·Comms ·PM ·Change leadership ·Innovation    │
└─────────────────────────────────────────────┘
```

**4.2 Capability level definitions**

| Level | Name | Definition |
|:---:|------|------|
| L1 | Entry | Completes basic work under guidance |
| L2 | Proficient | Independently completes routine work |
| L3 | Skilled | Solves complex problems, mentors others |
| L4 | Expert | Deep industry expertise, novel methods |
| L5 | Leader | Industry benchmark, sets direction |

---

### Step 5: Talent Review & Identification

**Objective**: Review existing talent; identify potential and gaps.

**Guidance:**

**5.1 9-box talent grid**

```
         High performance
         ↑
   Develop  │  Core talent │  Superstar
         │            │
  ───────┼────────────┼──────────→  High potential
         │            │
  Problem   │  Solid contributor│ High-potential
         │            │
         ↓  Low performance
```

**5.2 Digital-talent gap analysis**

| Role | Needed | Current | Gap | Trainable | To hire |
|------|:---:|:---:|:---:|:---:|:---:|
| Data engineer | 3 | 0 | -3 | 0 | 3 |
| Data analyst | 2 | 1 | -1 | 1 | 0 |
| AI engineer | 2 | 0 | -2 | 1 | 1 |

---

### Step 6: Training System Design

**Objective**: Design a tiered, categorized digital training system.

**Guidance:**

**6.1 Training-system architecture**

| Tier | Content | Audience | Format |
|------|---------|------|------|
| Exec | Digital strategy, industry trends, data-driven decisions | Senior / mid mgmt | Seminar + benchmark visits |
| Technical | Tech skills, tool use, platform ops | IT staff | Certification + project practice |
| Business | Digital-tool use, data-analysis basics, security | Key staff | Centralized training + on-the-job |
| All-staff | Digital-literacy basics, new-system ops | All employees | Online course + assessment |

**6.2 Transport-digital training catalog**

- Transport Big-Data Analytics & Applications
- AI in Transport Management: Practice
- Transport Digital-Twin Technology & Applications
- Transport Data Security & Personal-Information Protection
- Smart-Highway Operations & Management
- Python Data Analysis Intro (transport scenarios)

---

### Step 7: Recruitment & Talent Attraction

**Objective**: Define the digital-talent recruitment plan and attraction strategy.

**Guidance:**

**7.1 Attraction strategies**

| Strategy | Note |
|------|------|
| External hiring | Attract digital talent from internet / tech firms |
| Campus recruiting | Partner with strong transport / CS universities for targeted cultivation |
| Flexible engagement | Expert advisors / project collaboration / secondments |
| Outsourcing transition | Build core roles in-house; outsource non-core if needed |
| Premium compensation band | Establish premium band for scarce market roles |

---

### Step 8: Roadmap & Tracking

**Objective**: Define a phased org-building plan and track continuously.

**Guidance:**

**8.1 Three-phase roadmap**

| Phase | Period | Focus |
|------|:---:|------|
| Build framework | 0–6 mo | Org adjustment, key-role JDs published, first recruitment |
| Strengthen capability | 6–18 mo | Training lands, second recruitment, talent pipeline built |
| Institutionalize | 18–36 mo | Digital culture forms, talent system runs stably |

**8.2 Tracking metrics**

- Digital-talent fill rate
- Staff digital-skill pass rate
- Digital-talent attrition rate
- Training coverage & satisfaction

---

## 3. Output Catalog

1. **Organization current-state diagnosis report** (.docx)
2. **Target org-structure design** (.pptx + .docx)
3. **Key-role JD compendium** (.docx)
4. **Digital capability model** (.pptx)
5. **Talent-review report** (.xlsx)
6. **Training-system design** (.docx)
7. **Recruitment & talent-attraction plan** (.docx)
8. **Org-building roadmap** (.pptx)

---

> **Version**: V1.0 | **Date**: 2025-07
