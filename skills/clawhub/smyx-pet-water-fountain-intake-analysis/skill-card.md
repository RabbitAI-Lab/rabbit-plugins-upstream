## Description:

Analyzes pet water-fountain videos to report drinking frequency, session duration, estimated intake, and changes from historical baselines.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet caregivers and operators of smart fountains can use the skill to review video-based drinking activity, compare estimated intake with historical patterns, and receive alerts about changes. Results are for health monitoring and do not provide a diagnosis or treatment plan.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan rates the skill suspicious, citing credential and privacy risks, unexpected account-management behavior, and a command that may analyze despite an export-only option. Scanner coverage was partial.

Mitigation: Before installation, verify the API destination and credential handling, understand what account data is stored, and confirm video uploads and export-only behavior match expectations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-pet-water-fountain-intake-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [API reference](artifact/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON]

**Output Format:** [Structured drinking-activity report with estimates, change alerts, and report links; Markdown or JSON output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Daily intake is estimated from observed drinking behavior and is not a direct measurement.]

## Skill Version(s):

1.0.16 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
