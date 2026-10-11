## Description:

Analyzes sleep-monitoring videos for sleep stages, body movement, awakenings, and possible apnea, and returns a structured sleep report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Individuals and developers use this skill to analyze sleep-monitoring footage and review sleep-stage estimates, movement, awakenings, and possible breathing interruptions. They can also retrieve prior reports linked to their account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Private bedroom or health footage is sent to a cloud service for analysis.

Mitigation: Obtain consent and review the provider's retention and access controls before submitting sensitive footage.

Risk: The skill can silently create or reuse an account identity and keep service tokens locally.

Mitigation: Review account-linked history access and local token storage before installation, and limit device access to trusted users.

Risk: Sleep-stage and apnea findings could be mistaken for a clinical diagnosis.

Mitigation: Treat results as informational and seek a clinician or validated sleep-monitoring device for diagnosis.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/smyx-sunjinhui/skills/smyx-sleep-quality-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [Bundled API reference](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Sleep analysis reports with structured results and Markdown tables for report history]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include links and recommendations; results are not a medical diagnosis. The documented video limit is 10 MB.]

## Skill Version(s):

1.0.16 (source: server-resolved release; artifact frontmatter says 1.0.17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
