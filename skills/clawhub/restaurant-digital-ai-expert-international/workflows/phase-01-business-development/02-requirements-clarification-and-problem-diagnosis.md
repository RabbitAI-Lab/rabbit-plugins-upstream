# 02-Requirements Clarification & Problem Diagnosis

## Triggers
- After the initial communication, the client expresses willingness to continue exploring
- OR the client has provided relevant materials (system inventory / data reports / existing process flows, etc.)

## Pre-requisites
- Basic client information (from Process 01)
- Any materials provided by the client (system inventory / reports / process flows / pain point descriptions, etc.)

## Diagnostic Framework: MECE Five-Dimension Diagnosis

### Dimension 1: Technology Diagnosis

| Diagnostic Item | Analysis Questions | Information Source |
|----------------|-------------------|-------------------|
| POS & Payment | What system? Which version? Coverage across locations? Usage rate? | Client interview / system screenshots |
| KDS / Kitchen | How does the kitchen receive orders? Is there a KDS? If not, how are orders transmitted? | Client interview / site visit |
| Delivery Integration | Which platforms are integrated? Auto-accept or manual? Is there an aggregator? | System screenshots |
| System Integration | Are loyalty and POS connected? Inventory and POS? How many data silos exist? | Interview + verification |
| Network Infrastructure | Is in-store WiFi stable? Is bandwidth sufficient? What happens during an outage? | Interview |
| Hardware Level | POS terminal models? Printers? KDS screens? Tablets? | Hardware inventory |

### Dimension 2: Operations Diagnosis

| Diagnostic Item | Analysis Questions |
|----------------|-------------------|
| Ordering Efficiency | How long from customer seating to order completion during peak? QR code ordering adoption rate? |
| Kitchen Speed | Average time from order to dish completion? During peak? Rate of order follow-ups? |
| Queue Experience | How is queuing managed? Average wait time? Walk-away rate? |
| Delivery Efficiency | Delivery order handling process? Error rate? Missed order rate? |
| Labor Efficiency | Revenue per employee? How does this compare to the industry average for this format? |

### Dimension 3: Data Diagnosis

| Diagnostic Item | Analysis Questions |
|----------------|-------------------|
| Revenue Data | Can you see daily revenue in real time? On your phone? |
| Cost Data | Can you see real-time food cost percentage? How is waste calculated? |
| Customer Data | How many loyalty members? Activity level? Repeat purchase rate? |
| Data Quality | Is the data accurate? Do different systems reconcile? |
| Analytical Capability | Who is looking at the data? Are decisions being made based on it? |

### Dimension 4: Organization Diagnosis

| Diagnostic Item | Analysis Questions |
|----------------|-------------------|
| IT Team | Is there an IT team? How many people? At HQ or in stores? |
| Digital Awareness | What is the owner's attitude toward digital? "Leading the charge" or "let's give it a try"? |
| Staff Capability | Average age? Comfortable with smartphones? Willing to learn? |
| Change Resistance | Have they implemented systems before? How did it go? Any "bad experience" history? |

### Dimension 5: Financial Diagnosis

| Diagnostic Item | Analysis Questions |
|----------------|-------------------|
| Budget Capacity | Annual IT budget? One-time or phased? |
| Cost Structure | Food/labor/rent ratios? Profit margin? |
| Investment Logic | What drives digital investment decisions? ROI? Efficiency? Brand value? |
| Willingness to Pay | "How much would you pay for a 10% cost reduction?" vs. "How much for a 10% revenue increase?" |

## Deliverable: Problem Diagnostic Summary

```
## Problem Diagnostic Summary

### Key Findings (Top 3)
1. [Finding 1 -- quantified in financial terms]
2. [Finding 2]
3. [Finding 3]

### Five-Dimension Scoring
| Dimension | Score (1-5) | Key Assessment |
|-----------|:---:|----------------|
| Technology | [X] | [...] |
| Operations | [X] | [...] |
| Data       | [X] | [...] |
| Organization | [X] | [...] |
| Financial  | [X] | [...] |

### Root Cause Analysis of Key Pain Points
[Use 5-Why or Issue Tree to analyze at least 1 core pain point]

### Quick Win Opportunities
[List 3-5 opportunities with low investment, fast results, and high certainty]

### Recommended Direction
[Based on the client's specific format and pain points, provide 1-3 major directional recommendations]
```

## Quality Checks
- [ ] All five dimensions have been covered (no omissions)
- [ ] Key findings are quantified with data or financial terms
- [ ] At least 1 core pain point has undergone root cause analysis
- [ ] At least 3 quick-win opportunities have been identified
- [ ] No false judgments made based on uncertain information
