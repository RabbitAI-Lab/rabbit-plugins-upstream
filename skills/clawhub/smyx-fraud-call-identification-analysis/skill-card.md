## Description:

Analyzes incoming call content for multi-dimensional risk, identifies scam scripts, determines whether a call is fraudulent, assesses risk levels, and generates an Anti-Fraud Guardian analysis report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users, analysts, and safety teams use this skill to submit call recordings, audio URLs, or call text for fraud-risk analysis and structured anti-fraud reporting. It can also query cloud-hosted historical analysis reports associated with the resolved user identity.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Call recordings, media files, text, and report queries may be sent to a third-party cloud service.

Mitigation: Use only with trusted deployments and non-sensitive inputs until remote processing, retention, and data handling are documented.

Risk: The security scan reports under-disclosed local identity persistence and token storage.

Mitigation: Review identity creation and stored credentials before installation, and make identity use explicit and controllable for the operator.

Risk: The security scan reports active plaintext HTTP endpoints in the package.

Mitigation: Disable development HTTP endpoints and require HTTPS endpoints before handling sensitive recordings or reports.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-fraud-call-identification-analysis)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API Interface Documentation](artifact/references/api_doc.md)
- [Analysis API Interface Documentation](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON-style structured analysis output with optional report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write analysis results to a user-specified output file and may return cloud report export links.]

## Skill Version(s):

9.9.16 (source: server release metadata; artifact frontmatter version: 1.0.16)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
