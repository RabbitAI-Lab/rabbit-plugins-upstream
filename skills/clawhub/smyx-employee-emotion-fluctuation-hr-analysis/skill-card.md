## Description:

This skill analyzes fixed-camera workplace video to produce HR-facing employee emotion fluctuation alerts, baseline comparisons, and care suggestions when consented, anonymized monitoring detects sustained changes in facial expression or behavior.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

HR and authorized workplace well-being teams use this skill to review anonymized employee emotion-trend reports and identify sustained changes that may warrant voluntary support conversations. It is intended for consented enterprise camera settings with privacy, access-control, and retention controls in place.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: High-impact workplace emotion surveillance can affect employee privacy and workplace decisions.

Mitigation: Use only with explicit employee notice and consent, legal and HR approval, and documented limits that prohibit performance, promotion, or termination use.

Risk: Remote processing and report history access may expose sensitive workplace monitoring data.

Mitigation: Require strict access controls, audit logging, clear retention and deletion rules, and review before installation.

Risk: Persistent identity or token handling may not match local-only or no-persistent-identity requirements.

Mitigation: Do not install where local-only processing, no persistent identity, or approved-camera-source enforcement is required.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-employee-emotion-fluctuation-hr-analysis)
- [API Reference](artifact/references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown or JSON report text, with optional saved output file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can call remote analysis and report-history APIs for submitted workplace video inputs or report-list requests.]

## Skill Version(s):

1.0.5 (source: server release evidence; SKILL.md frontmatter says 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
