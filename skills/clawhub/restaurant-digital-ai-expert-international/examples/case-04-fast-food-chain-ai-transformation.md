# Case 4: AI Transformation at a Fast-Food Chain

## Background

| Item | Detail |
|------|--------|
| **Brand** | QuickBite (pseudonym) |
| **Type** | Chinese fast-food chain |
| **Scale** | 280 company-owned locations |
| **Daily Orders per Location** | 400--600 |
| **Avg. Ticket** | $3.50--$5 |
| **Annual Revenue** | ~$210M |

## Pre-Transformation State

### Existing Foundation
- Unified POS: Oracle MICROS across 180 locations; 100 locations pending migration
- Basic loyalty: points + stored value, but only 12% member activity rate
- Delivery live: DoorDash + Uber Eats, accounting for 35% of revenue
- Some data reports: but store managers "never looked at them"

### Core Pain Points
1. **Peak-hour congestion**: 80% of orders concentrated in the lunch window (11:30 AM--1:00 PM); queues frequently exceeded 15 minutes.
2. **Uncontrolled fulfillment speed**: Order-to-serve time fluctuated wildly (3--12 minutes) with no KPI tracking.
3. **Severe food waste**: Forecast-based prep resulted in ~8% daily food waste.
4. **Imprecise scheduling**: Understaffed at peaks, overstaffed during lulls.
5. **Drive-thru inefficiency**: Traditional manual ordering + intercom averaged 90 seconds per vehicle.

## AI Transformation Plan

### Overall Strategy: Pick the 3 highest-ROI scenarios; validate and scale in phases.

### Phase 1: Data Foundation Remediation (3 months)

**Critical**: Fix the data foundation before applying AI.

| Action | Output |
|--------|--------|
| Migrate 100 legacy POS to Oracle MICROS | Unified data across all locations |
| Data quality audit | Discovered and fixed 12% of menu-item code mismatches |
| Real-time dashboards | Three-tier dashboards (HQ + regional manager + store manager) |

### Phase 2: AI Scenario 1 -- Demand Forecasting + Smart Prep (4 months)

**Technical approach**:
- Inputs: historical orders, weather, day of week, holidays, nearby office events
- Model: LightGBM (chosen for low training/inference cost; no GPU required)
- Output: hourly forecast for the next 1--7 days, guiding kitchen prep quantities

**Implementation process**:

| Week | Action | Key Decision |
|------|--------|-------------|
| W1--W4 | Model training + testing | Trained on 6 months of historical data; shadow mode on 10 stores (system forecast vs. human actual) |
| W5--W8 | 10-store pilot | Forecast accuracy improved from 75% to 92% (shadow -> production) |
| W9--W12 | Expanded to 50 stores | Continued model iteration |
| M4 | Full 280-store deployment | Every store's daily prep quantity = AI recommendation + manager confirmation |

### Phase 3: AI Scenario 2 -- Intelligent Scheduling (3 months)

Integrated 7shifts workforce management SaaS, auto-generating schedules based on forecasted footfall.

### Phase 4: AI Scenario 3 -- AI Voice Ordering (Drive-Thru) (5 months)

**Technical approach**:
- Dual microphone array (noise cancellation) + cloud ASR (Deepgram / AssemblyAI) + LLM + TTS
- Seamless human handoff: AI cannot handle -> transferred to human in under 0.5 seconds

## Results (after 12 months)

| Metric | Before | After | Change |
|--------|:------:|:-----:|:------:|
| Food Waste Rate | 8% | 4.2% | **-47%** |
| Avg. Peak Fulfillment Time | 7.5 min | 4.8 min | **-36%** |
| Labor Cost Ratio | 24% | 20.5% | **-3.5pp** |
| Avg. Drive-Thru Time | 90 sec | 62 sec | **-31%** |
| AI Voice Order Accuracy | -- | 96% | On target |
| Human Handoff Rate | -- | 8% | Below 10% target |
| Queue Abandonment Rate | 18% | 8% | **-56%** |
| Manager Scheduling Time | 2 hr/week | 15 min/week | **-87%** |
| Upsell Rate (via AI recs) | 3% | 16% | **+13pp** |

### ROI

| Item | Amount |
|------|:------:|
| Total Investment (systems + hardware + AI) | $530K |
| Annualized Savings | ~$870K |
| Payback Period | ~7.5 months |
| 3-Year ROI | ~490% |

## Lessons Learned

### What Went Right
1. **Fixed the data before applying AI**: Spent 3 months unifying data and fixing quality; this is the bedrock of AI success.
2. **Shadow-mode validation**: AI ran silently in the background, compared against human decisions; only replaced when proven superior.
3. **Chose the right model**: LightGBM was sufficient for fast-food demand forecasting; no need for deep learning.
4. **Started drive-thru AI with a simple menu**: Supported only standard menu items initially; expanded once stable.
5. **Scheduling as "recommendation," not "command"**: AI suggests, manager confirms and adjusts; trust built incrementally.

### Mistakes We Made
1. **Overestimated voice AI accuracy in noisy environments**: Initial accuracy was only 82%; added a dual microphone array to reach 96%.
2. **Forgot accent/dialect training**: The pilot city had strong regional accents; spent 2 extra weeks on retraining.
3. **First scheduling model was too aggressive**: The algorithm produced the "optimal" solution but ignored employee preferences (who prefers morning shifts, who hates night shifts) -> staff pushback -> resolved by adding preference constraints.

## Universal Takeaway

> Don't try to go from zero to full AI in one leap. Pick 1--3 highest-ROI scenarios and run them in "shadow mode" until stable. The most critical pre-conditions are not the AI technology itself, but: 1) unified and clean data, 2) willing store managers, 3) clear "AI vs. before" comparison metrics.
