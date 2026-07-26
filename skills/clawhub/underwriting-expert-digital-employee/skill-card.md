## Description: <br>
Supports insurance professionals with health disclosure review, medical underwriting assessment, underwriting decision explanation, follow-up outreach, and sales recording quality review. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[gechengling](https://clawhub.ai/user/gechengling) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Insurance underwriting, operations, and quality teams use this skill to structure applicant risk review, interpret underwriting outcomes, prepare follow-up communications, and produce review-ready reports that require qualified human approval before business use. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may support live customer contact through phone or message workflows. <br>
Mitigation: Require explicit human approval before outreach, confirm the intended recipient and contact channel, and respect opt-out or no-contact signals. <br>
Risk: The skill references external systems and MCP tools for customer data, underwriting rules, OCR, ASR, calling, and messaging. <br>
Mitigation: Enable only intentionally authorized tools and pause workflows when required systems or rule sources are unavailable. <br>
Risk: Audit logs and reports may include sensitive customer, health, financial, or recording data. <br>
Mitigation: Redact personal data, define retention limits, and review logs before storage or sharing. <br>
Risk: Underwriting, medical, compliance, and customer-intent outputs can be incomplete or incorrect if source data or rules are missing. <br>
Mitigation: Treat outputs as advisory, require qualified human review, and mark missing evidence before business use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/gechengling/skills/underwriting-expert-digital-employee) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/gechengling) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Structured Markdown reports, templates, checklists, and follow-up guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs are advisory and require human review before real-world insurance, compliance, or customer-contact decisions.] <br>

## Skill Version(s): <br>
2.0.1 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
