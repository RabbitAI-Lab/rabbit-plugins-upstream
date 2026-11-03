## Description:

Analyzes fry tank images or video with a known-size reference object to report fish length measurements, growth rates, and growth trends.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Aquaculturists and ornamental fish breeders use the skill to review fry images or video, track body-length measurements and growth over time, and view measurement reports. It can also retrieve prior reports for a tank.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Footage may be uploaded even when analysis is not requested.

Mitigation: Confirm upload behavior before use and submit only footage authorized for remote processing; verify applicable cloud-retention controls.

Risk: Account handling may mishandle API secrets and account identifiers.

Mitigation: Keep API secrets private and use the skill only where account registration and credential storage controls are clear.

## Reference(s):

- [API reference](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, JSON, Markdown, Files]

**Output Format:** [Structured analysis report or history report, with an optional saved result file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include fry length and growth measurements, group statistics, trends, suggested actions, and report links.]

## Skill Version(s):

1.0.13 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
