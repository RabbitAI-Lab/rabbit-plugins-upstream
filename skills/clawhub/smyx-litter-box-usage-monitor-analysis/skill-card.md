## Description:

Analyzes litter-box video to summarize each cat's visit frequency and duration, compare activity with historical patterns, and flag behavior changes for veterinary follow-up without making a diagnosis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners, catteries, boarding facilities, and veterinary staff use litter-box video to review visit patterns, spot unusual changes, and access prior reports. Alerts are behavioral indicators, not medical diagnoses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet or home video may be sent to a cloud service.

Mitigation: Use only with informed user consent and an acceptable cloud data-retention and deletion policy.

Risk: Persistent identities and tokens may expose or mix private report history in shared workspaces.

Mitigation: Use isolated workspaces per user and review identity separation and token handling before enabling historical reports.

Risk: Behavioral alerts may be mistaken for medical diagnoses.

Mitigation: Present findings as monitoring signals and refer concerning changes to a veterinarian.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-litter-box-usage-monitor-analysis)
- [Litter-box analysis API reference](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Behavioral analysis report or historical-report list, with optional JSON and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include per-cat visit frequency, duration, trend alerts, and follow-up guidance.]

## Skill Version(s):

1.0.10 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
