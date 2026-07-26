## Description: <br>
Runs a public-data, multi-step company due-diligence scan across business background, IP assets, technical risk, funding compliance, and overall risk posture. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[golngod](https://clawhub.ai/user/golngod) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Investment teams, government or park recruitment staff, reviewers, financial advisors, founders, and other external evaluators use this skill to screen a target company's public signals before deeper due diligence. It is intended for risk marking and triage, not valuation, legal advice, or investment advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Target company names may be sent to public third-party services such as Wikidata and USPTO. <br>
Mitigation: Use the skill only for targets where disclosure to those public services is acceptable, and avoid confidential acquisition, investment, or investigation targets. <br>
Risk: The report is a screening aid and may be incomplete because it depends on public API coverage and freshness. <br>
Mitigation: Treat findings as preliminary risk markers and verify important conclusions through professional legal, financial, technical, or on-site due diligence. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/golngod/skills/opc-chain-due-diligence) <br>
- [Wikidata API](https://www.wikidata.org/w/api.php) <br>
- [Wikidata entity data](https://www.wikidata.org/wiki/Special:EntityData/{qid}.json) <br>
- [USPTO PatentsView API](https://api.patentsview.org/patents/query) <br>
- [WIPO documents](https://www.wipo.int/edocs/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, analysis, guidance] <br>
**Output Format:** [Markdown-style due-diligence report with structured JSON summary] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses public API results to assign green, yellow, or red risk markers across enterprise background, IP assets, technical strength, funding compliance, and overall risk.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
