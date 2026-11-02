## Description:

Analyzes images and videos of pet enclosures to estimate visible waste coverage and provide cleanliness reports and cleaning alerts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet boarding and animal care staff use the skill to review enclosure images or videos, estimate visible waste coverage, and identify when cleaning may be needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The export-only option may still upload footage.

Mitigation: Treat export-only as potentially uploading; use only media you are authorized to share and confirm the service's retention and account practices before sending sensitive footage.

Risk: Requests may send credentials to an unintended destination.

Mitigation: Verify the authenticated destination before use, and do not send credentials or sensitive footage until the destination checks are corrected.

## Reference(s):

- [API interface reference](references/api_doc.md)
- [Sample demonstration](https://lifeemergence.com/sample.html)
- [ClawHub release page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-cage-cleanliness-detection-analysis)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Guidance]

**Output Format:** [Structured cleanliness report with text or Markdown summaries, estimates, alerts, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include cleanliness scores, estimated waste coverage, threshold alerts, annotated images, and historical report links.]

## Skill Version(s):

1.0.14 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
