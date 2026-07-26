## Description: <br>
Helps agents analyze submitted tables, CSV, Excel, or structured data blocks to find relationships, data-quality issues, anomalies, and action-oriented insights. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[renshengruozhiruchujian-sudo](https://clawhub.ai/user/renshengruozhiruchujian-sudo) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Agents use this skill when a user provides spreadsheet-like data or asks to compare tables, find relationships, check data quality, or diagnose anomalies. It guides the response toward calculations, row-level evidence, sensitive-field labeling, and practical next actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Spreadsheet or CSV analysis may involve sensitive business, HR, finance, legal, compliance, or personal data. <br>
Mitigation: Use the skill only with data the user is allowed to share, preserve sensitivity labels in outputs, and review high-impact conclusions before acting on them. <br>
Risk: The artifact asks for detailed reasoning output, which can encourage hidden chain-of-thought disclosure. <br>
Mitigation: Ask for concise rationale, formulas, and row-level evidence instead of hidden chain-of-thought. <br>
Risk: Incorrect calculations or misread rows can lead to misleading operational recommendations. <br>
Mitigation: Verify key numbers against source rows and require human review before acting on HR, finance, legal, or compliance conclusions. <br>


## Reference(s): <br>
- [ClawHub listing](https://clawhub.ai/renshengruozhiruchujian-sudo/skills/data-analysis-skills) <br>
- [Methodology reference](artifact/REFERENCE.md) <br>
- [Role perspective reference](artifact/ROLES.md) <br>
- [Examples](artifact/EXAMPLES.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown or concise text with calculations, evidence references, sensitivity labels, and recommended actions.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May ask for missing context or corrected source data before analyzing; should avoid fabricating unavailable data.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
