## Description:

Creates a traceable, screening-level freedom-to-operate report from a supplied risk-point Word document and user-approved PatSnap search expressions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yuanzhian-patsnap](https://clawhub.ai/user/yuanzhian-patsnap)

### License/Terms of Use:

MIT-0

## Use Case:

Patent analysts, IP teams, product counsel, and R&D owners use this skill to convert a risk-point document and reviewed PatSnap search expressions into a structured FTO screening package. The skill supports feature extraction, patent retrieval, claim-data collection, claim-limitation comparison, triage labels, evidence JSON, and HTML/DOCX reporting, but it does not provide a legal clearance opinion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected risk documents, claim text, and product evidence may be transmitted to PatSnap REST APIs or configured PatSnap MCP connectors.

Mitigation: Run dry-run first, transmit only with user authorization, and use the configured secure PatSnap access mode.

Risk: API credentials could be exposed through configuration, logs, reports, or exceptions if handled carelessly.

Mitigation: Use environment-based keys or a private local config, keep Bearer credentials out of URLs and outputs, and redact credentials from diagnostics.

Risk: FTO screening outputs can be mistaken for legal clearance or a complete patent search.

Mitigation: Treat the output as screening material, preserve limitations and partial states, and require qualified local counsel for decision-material conclusions.

Risk: Generated reports and evidence packages may contain confidential product or patent-analysis material.

Mitigation: Write generated reports outside the skill package and manage them under the user's confidentiality and retention controls.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yuanzhian-patsnap/skills/create-fto-screening-report-ip)
- [Setup Guide](artifact/README.md)
- [PatSnap Data-Access Policy](artifact/references/api_call_policy.md)
- [PatSnap REST API Reference](artifact/references/api_reference.md)
- [Claim Chart JSON Schema](artifact/references/claim_chart_schema.md)
- [Generic FTO Screening Report Requirements](artifact/references/report_requirements.md)
- [PatSnap Developer Center](https://open.patsnap.com/devportal)
- [PatSnap REST API overview](https://open.patsnap.com/devportal/guides/rest-api-overview)
- [PatSnap MCP Servers](https://open.patsnap.com/marketplace/mcp-servers)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, JSON, HTML, DOCX]

**Output Format:** [Markdown guidance with shell commands plus generated JSON evidence, HTML reports, and DOCX reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated reports and evidence files are written to a selected output directory and remain screening materials for human review.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
