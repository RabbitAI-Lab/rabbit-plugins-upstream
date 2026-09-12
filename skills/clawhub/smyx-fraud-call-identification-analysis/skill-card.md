## Description:

Analyzes incoming call content for multi-dimensional risk, identifies scam scripts, determines whether a call is fraudulent, assesses risk level, and generates an Anti-Fraud Guardian analysis report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users, analysts, and security teams use this skill to submit call recordings, public media URLs, or call transcripts for fraud-risk analysis, scam-script detection, risk-level assessment, anti-fraud guidance, and history/report retrieval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Call content, report metadata, and internal identity values may be sent to the provider's cloud service.

Mitigation: Install only when this cloud processing is acceptable, and make upload and history retrieval behavior explicit to users before use.

Risk: The skill silently manages cloud identity and persists tokens.

Mitigation: Review identity and token handling before installation, avoid plaintext token persistence, and rotate or revoke credentials if exposed.

Risk: The security scan reports insecure or mismatched analysis configuration, including default development/private HTTP endpoints.

Mitigation: Require production HTTPS-only configuration and remove default development or private HTTP endpoints before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-fraud-call-identification-analysis)
- [API interface documentation](references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, code, shell commands, configuration, guidance]

**Output Format:** [Markdown reports and JSON-formatted analysis or history data, with optional saved text output files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can process a local audio file, a public media URL, or direct transcript text; history queries return report lists and links.]

## Skill Version(s):

9.9.16 (source: server release metadata; artifact frontmatter declares 1.0.16)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
