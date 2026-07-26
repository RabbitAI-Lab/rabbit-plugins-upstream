## Description: <br>
Detects pre-news ambient risk signals across human, legal, and operational systems and converts them into machine-readable, tradable risk primitives. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sieershafilone](https://clawhub.ai/user/sieershafilone) <br>

### License/Terms of Use: <br>
Proprietary <br>


## Use Case: <br>
External developers, analysts, and risk teams use this skill to collect legally accessible public signals, normalize them into a risk ontology, and package probabilistic risk primitives for finance, insurance, logistics, or policy workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Trading-oriented risk signals may be incorrect, misleading, or overinterpreted. <br>
Mitigation: Keep human review between outputs and any trading, insurance, logistics, or policy decision. <br>
Risk: Mock or demonstration data may be mixed with live harvested signals. <br>
Mitigation: Remove mock sources or clearly label them before production use. <br>
Risk: Some harvesters weaken HTTPS certificate verification. <br>
Mitigation: Require verified TLS for all network calls before production use. <br>
Risk: Persisted signal and vector outputs can create retention and access-control exposure. <br>
Mitigation: Document permissions, retention periods, and deletion procedures, and avoid storing personal data. <br>
Risk: Webhook delivery can send risk primitives to loosely controlled external endpoints. <br>
Mitigation: Restrict webhooks to trusted HTTPS endpoints and review payloads before enabling delivery. <br>


## Reference(s): <br>
- [BlackSnow Agent Specifications](references/agent_specs.md) <br>
- [BlackSnow Ontology](references/ontology.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/sieershafilone/skills/blacksnow) <br>
- [Federal Register API](https://www.federalregister.gov/api/v1/documents.json) <br>
- [SAM.gov Opportunities API](https://api.sam.gov/opportunities/v2/search) <br>
- [SEC EDGAR Current Filings Feed](https://www.sec.gov/cgi-bin/browse-edgar?action=getcurrent&type=8-K&company=&dateb=&owner=include&count=40&output=atom) <br>
- [USAspending Awards API](https://api.usaspending.gov/api/v2/search/spending_by_award/) <br>
- [FEMA Disaster Declarations API](https://www.fema.gov/api/open/v2/DisasterDeclarationsSummaries) <br>
- [NHTSA Recalls API](https://api.nhtsa.gov/recalls/recallsByDate) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Files, API Calls] <br>
**Output Format:** [JSON risk primitives with optional JSONL persistence and webhook delivery] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Probabilistic outputs only; downstream decisions require independent review and compliance controls.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
