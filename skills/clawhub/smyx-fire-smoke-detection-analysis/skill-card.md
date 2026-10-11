## Description:

Analyzes images and video for fire and smoke and returns detection results and reports for early-warning use cases.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Security and safety teams use this skill to assess images and video for possible fire or smoke in surveillance, forest monitoring, and industrial settings. Results support early warning and require human confirmation before emergency action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Images, videos, or supplied URLs are sent to the LifeEmergence cloud service.

Mitigation: Check the service's data-retention policy and obtain authorization before sending sensitive footage.

Risk: The skill silently creates or reuses a cloud identity and stores service tokens locally.

Mitigation: Review account controls and restrict access to the workspace data directory before installation.

Risk: Bundled API documentation references pet health endpoints rather than fire and smoke analysis.

Mitigation: Verify the publisher and confirm the actual API endpoints and behavior before using the skill.

## Reference(s):

- [Bundled API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured detection results, report links, or a Markdown table of historical reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save results to a file; historical reports are retrieved from the cloud service.]

## Skill Version(s):

1.0.16 (source: server-resolved ClawHub release metadata; bundled SKILL.md states 1.0.19)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
