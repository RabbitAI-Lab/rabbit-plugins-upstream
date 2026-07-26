# 04-AI Strategy Planning

## Triggers
- Client explicitly says "we want to do AI" / "implement AI"
- OR the client's digital foundation has reached L3+ (systems integrated, data usable), and AI is the natural next step

## AI Strategy Planning Process

### Step 1: AI Readiness Check

**If any of the following 5 conditions is NOT met, do not proceed with AI yet**:
- [ ] Core systems (POS + CRM + at least 1 operational system) are unified and running stably for >6 months
- [ ] Data quality baseline is met (order data accuracy >95%, menu item / location master data standards established)
- [ ] At least 1 quantifiable AI use case exists (not "we want AI", but "AI will specifically solve problem X, with expected cost reduction / efficiency gain of XX")
- [ ] Owner / decision-maker is personally driving this (AI is not an IT project; it is a business transformation)
- [ ] Capacity to execute exists (can leverage SaaS vendor AI capabilities; in-house team not necessarily required)

**If 3 or more are not met**, recommend completing foundational digitalization before considering AI.

### Step 2: AI Scenario Inventory

Use RICE + scoring card to evaluate each of the following 15 scenarios:
1. AI Voice Ordering
2. AI Demand Forecasting
3. AI Smart Scheduling
4. AI Visual Recognition (Kitchen QA)
5. AI Personalized Recommendations
6. AI Dynamic Pricing
7. AI Smart Customer Service
8. AI Kitchen Quality Inspection
9. AI Food Safety Compliance Monitoring
10. AI Marketing Automation
11. AI Supply Chain Optimization
12. AI Energy Optimization
13. AI Sentiment / Review Analysis
14. AI Site Selection Model
15. AI Recipe / Menu Optimization

### Step 3: Scenario Prioritization

See `tools/ai-scenario-priority-scoring-card.md` and `templates/ai-scenario-priority-scoring-card-template.md`

### Step 4: ROI Estimation for Each P0 Scenario

For each P0 (start immediately) scenario, create a 1-page ROI estimate:
- Investment: software / hardware / data labeling / integration / organizational costs
- Benefits: quantified estimates of cost reduction / efficiency gain / revenue increase
- Risks: data quality, technical feasibility, organizational acceptance

### Step 5: AI Technology Strategy

| Client Size | Recommended AI Technology Strategy |
|-------------|-----------------------------------|
| <10 locations | Use SaaS vendor-integrated AI features (do not build in-house) |
| 10-100 locations | Public cloud APIs (OpenAI / Anthropic / Google AI) + lightweight RAG |
| 100-1,000 locations | Hybrid architecture (public cloud API + on-premise deployment) + domain fine-tuning |
| >1,000 locations | Multi-model gateway + in-house Agent framework + private LLM |

### Step 6: AI Organization Development

| Stage | AI Organization Model |
|-------|-----------------------|
| Initiation | 1-2 "AI Champions" (part-time, but passionate about AI) |
| Growth | 3-5 person AI team (data engineer + ML engineer + business analyst) |
| Maturity | AI Center of Excellence + AI Ambassadors embedded in each business line |

## Deliverables
- AI readiness check results
- AI scenario priority matrix (RICE + scoring card)
- Detailed ROI estimation for P0 scenarios
- AI technology strategy recommendation
- AI implementation roadmap (3-4 quarters)

## Quality Checks
- [ ] For clients not ready for AI, clearly state "complete foundational digitalization first"
- [ ] AI scenario selection is based on ROI, not "AI is cool"
- [ ] Technology strategy matches the client's scale
- [ ] AI ethics and compliance are addressed (data privacy per GDPR, algorithmic bias, food safety)
