## Description:

Analyzes pet-feeding videos or video URLs for selective eating behaviors and provides feeding-behavior reports and suggestions without diagnosing disease.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and staff at smart-feeder services, boarding centers, or pet hospitals use the skill to identify selective eating patterns in feeding-area videos, review past reports, and consider feeding adjustments. It does not provide veterinary diagnoses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet-feeding videos or video URLs are sent to a Life Emergence cloud service.

Mitigation: Use only when the user accepts cloud processing of the footage and links.

Risk: The skill automatically creates or reuses a local cloud identity and persists tokens; shared workspace state can expose report history.

Mitigation: Keep identity and token storage isolated per user, especially in shared workspaces.

Risk: A hidden identity value could grant access to another user's reports if passed without authentication.

Mitigation: Do not pass or reveal hidden identity values unless the host platform authenticates them.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/smyx-sunjinhui/skills/smyx-picky-eater-detection-analysis)
- [Skill API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Structured results or Markdown reports and history tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes selective-eating observations, feeding suggestions, and links to cloud reports; not a medical diagnosis.]

## Skill Version(s):

1.0.10 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
