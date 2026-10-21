## Description:

Analyzes reptile enclosure videos to report basking and hiding patterns, zone transitions, and possible thermoregulation concerns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Reptile keepers and enclosure-monitoring developers use this skill to review camera footage, track time spent in temperature zones, and retrieve behavior reports and alerts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Enclosure videos or video URLs are sent to the lifeemergence.com cloud service.

Mitigation: Use only media approved for cloud processing and confirm with the user before uploading or submitting a URL.

Risk: The skill creates or reuses an internal identity and stores service tokens in a local workspace database with limited user control.

Mitigation: Review identity and token storage before installation; restrict workspace access and remove stored data when no longer needed.

Risk: History lookups may expose previously stored enclosure reports.

Mitigation: Request explicit user confirmation before retrieving historical reports.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/18072937735/skills/smyx-reptile-thermoregulation-behavior-analysis)
- [Reptile thermoregulation API documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured analysis results and Markdown report listings with links; optional JSON output file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes zone-dwell statistics, behavior labels, recommendations, and report links when available.]

## Skill Version(s):

1.0.13 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
