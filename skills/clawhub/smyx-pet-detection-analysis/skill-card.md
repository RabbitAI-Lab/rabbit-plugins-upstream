## Description:

Detects cats, dogs, and birds in images and video for home pet monitoring, and retrieves cloud-stored detection reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Home pet owners and developers use the skill to detect cats, dogs, and birds in uploaded images or video, review detection reports, and retrieve past reports from the cloud service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet images, videos, or media URLs are sent to the lifeemergence cloud service.

Mitigation: Do not submit sensitive home footage unless you have verified the service's retention and deletion controls.

Risk: The skill automatically creates or reuses an account and persists access tokens in the workspace data directory.

Mitigation: Review account creation and deletion practices, restrict access to the workspace data directory, and confirm how tokens are cleaned up.

Risk: Historical reports are retrieved from the cloud service.

Mitigation: Confirm that cloud report access and retention meet your privacy requirements before using report history.

## Reference(s):

- [API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Text or Markdown detection report and history table; optional JSON detail or saved result file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include cloud report links and pet counts.]

## Skill Version(s):

1.0.16 (source: server-resolved ClawHub release; bundled SKILL.md says 1.0.20)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
