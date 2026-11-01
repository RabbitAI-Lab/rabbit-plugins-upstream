## Description:

Detects delivery packages in surveillance images or videos for inventory checks and unattended alerts at parcel stations, residential entrances, and office lobbies.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Facility operators can analyze surveillance images or videos to detect, count, and locate parcels, and review previous reports for inventory tracking and unattended alerts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review says the no-analysis option can still permit uploads.

Mitigation: Use a separate workspace and non-sensitive test video, and have the publisher correct export-only behavior before using real footage.

Risk: The security review says automatic sign-in handles credentials without clear safeguards.

Mitigation: Ask the publisher to separate secrets from account identifiers and protect stored tokens.

Risk: Cloud retention, access, and deletion terms need confirmation before footage is uploaded.

Mitigation: Confirm the service terms for retention, access, and deletion before using surveillance footage.

## Reference(s):

- [Package Detection API Reference](references/api_doc.md)
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-package-detection-analysis)
- [Skill Demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown, JSON]

**Output Format:** [Structured analysis reports and Markdown report lists]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include detection results, recommendations, and report links.]

## Skill Version(s):

1.0.17 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
