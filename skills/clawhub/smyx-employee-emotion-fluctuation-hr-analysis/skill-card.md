## Description:

Monitors consented workplace camera video for anonymized facial-expression and posture changes against employee baselines and produces HR care alerts and trend reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

HR senior management and authorized workplace well-being teams use this skill to generate anonymized employee emotion-fluctuation alerts and weekly or monthly trend reports from consented office camera footage. It is intended for voluntary support and care workflows, not diagnosis or employment decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: This is a high-impact employee emotion surveillance skill that may send workplace videos or video URLs and derived reports to remote services.

Mitigation: Use only with documented employee consent, legal and privacy approval, trusted endpoints, strict HR access controls, audit logging, and retention limits.

Risk: Derived emotion alerts could be misused for performance, promotion, termination, or mental-health diagnosis decisions.

Mitigation: Limit use to voluntary care workflows, prohibit employment-decision use and medical diagnosis, provide opt-out, and route concerns through appropriate EAP or professional support channels.

Risk: Persistent local identity tokens and stored reports can link sensitive workplace observations to an identity over time.

Mitigation: Provide a documented way to remove local tokens and stored reports, minimize retained data, and restrict report access to approved HR administrators.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-employee-emotion-fluctuation-hr-analysis)
- [API Interface Documentation](references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, files, shell commands, guidance]

**Output Format:** [Markdown or JSON report, with optional saved output file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts local workplace video paths or video URLs and can list historical reports from a remote API.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter states 1.0.12)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
