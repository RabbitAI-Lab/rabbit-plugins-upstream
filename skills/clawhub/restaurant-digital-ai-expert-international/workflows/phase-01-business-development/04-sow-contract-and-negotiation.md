# 04-SOW Contract & Negotiation

## Triggers
- After the proposal is approved, entering the contract/SOW signing phase
- OR client says "draft the SOW" / "how do we negotiate the contract"

## Pre-requisites
- Confirmed proposal
- Client's procurement process and compliance requirements

## SOW Standard Structure (Restaurant Industry Edition, 8 Sections)

```
Section 1: Project Overview
  1.1 Project Background (reference core findings from the Proposal)
  1.2 Project Objectives (quantified KPIs)
  1.3 Project Scope (with clear system boundaries, In/Out Scope checklist)

Section 2: Scope of Work
  2.1 Detailed Scope of Work (listed by system/module)
  2.2 Deliverables List (name + format + submission date)
  2.3 Explicit Exclusions (what is NOT in scope -- this is equally important as inclusions)

Section 3: Technical Solution Summary
  3.1 Technical Approach
  3.2 Key Assumptions (e.g., "client provides stable WiFi network")
  3.3 Technical Constraints (e.g., "client's existing POS version XX must be upgraded first")

Section 4: Implementation Plan
  4.1 Phase Breakdown & Milestones (including payment milestones)
  4.2 Resource Allocation (our team / client team)
  4.3 Project Organization Structure (RACI matrix)
  4.4 Implementation Locations (HQ / which pilot locations first)

Section 5: Acceptance Criteria
  5.1 Acceptance Methods (functional testing / performance testing / data reconciliation / UAT)
  5.2 Acceptance Criteria Checklist (measurable: response time <2 seconds / accuracy >99.9%...)
  5.3 Acceptance Process & Timeline
  5.4 Non-Compliance Handling Mechanism

Section 6: Responsibilities of Both Parties
  6.1 Our Responsibilities
  6.2 Client Responsibilities (providing premises / network / personnel coordination / data)
  6.3 Third-Party Responsibilities (e.g., if involving existing POS vendor / delivery platform integration)

Section 7: Assumptions & Constraints
  7.1 Key Assumptions (changes trigger re-evaluation of timeline and cost)
  7.2 Constraints
  7.3 Risk Disclosure & Liability Boundaries

Section 8: Commercial Terms
  8.1 Fee Breakdown
  8.2 Payment Schedule (milestone-based: 30% at signing -> 40% at system go-live -> 30% at acceptance)
  8.3 Warranty Period & Maintenance Period
  8.4 Change Management Mechanism
```

## Restaurant SOW Negotiation Key Points

### The 6 Most Contentious Points (Prepare Your Response in Advance)

| Point of Contention | Counter-Strategy |
|---------------------|------------------|
| "Who is responsible for data migration?" | Clarify: client provides the data, we clean and migrate. Additional work due to poor data quality = change order |
| "How many people need training?" | Specify number of trainees, duration, delivery method, and whether refresher training is included |
| "What does 'system go-live' actually mean?" | Define: "Core functionality operational and usable at all agreed-upon locations" |
| "What if the client delays sign-off?" | Agree: if client does not raise written objections within X business days after go-live = deemed accepted by default |
| "Client changes requirements mid-project" | Agree on change management process: written request -> evaluation -> quotation -> approval -> execution |
| "Who handles third-party system integration?" | Clarify: which integrations are our responsibility, which require client coordination with third parties, and what happens if integration fails |

### Restaurant-Specific Considerations

- **Peak-hour stability**: Explicitly state in the SOW: "System availability >= 99.9% during peak hours (lunch 11:30-13:00, dinner 17:30-19:30)"
- **Offline capability**: Explicitly state: "Core POS functions must operate offline during network interruptions"
- **Data sovereignty**: Explicitly state: "All business data belongs to the client. Full data export supported upon partnership termination"
- **Food safety compliance**: For solutions involving kitchen/supply chain, clearly define food safety compliance responsibility boundaries per FDA Food Code / EU regulations

## Contract Legal Considerations (International)

- Ensure data processing terms comply with GDPR (or applicable local data protection regulations)
- Intellectual property: reference Berne Convention and applicable international copyright law for custom development IP
- Dispute resolution: specify governing law and venue (preferably client's jurisdiction)
- Vendor acquisition or insolvency: define data migration and continuity obligations
- Service credits / penalties for SLA breaches must have actual financial consequence
- Limit of liability: ensure it is commercially reasonable and not a blanket exclusion

## Quality Checks
- [ ] Scope and exclusions are both clearly defined
- [ ] Acceptance criteria are measurable (not subjective descriptions like "works well" or "user-friendly")
- [ ] Payment milestones are tied to delivery milestones
- [ ] Change management process is clearly defined
- [ ] Data ownership and exit clauses are explicitly stated
- [ ] GDPR / local data protection compliance addressed
