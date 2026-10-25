## Description:

Analyzes pet-area video for defecation events and returns a cleaning-trigger indicator after the pet leaves, for use with a separately connected robot vacuum.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and smart-home developers use the skill to analyze video of a designated pet toilet area, review event reports, and pass a cleaning-trigger indicator to their own robot-vacuum integration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet-area videos or URLs are sent to an external cloud service.

Mitigation: Use only footage you are authorized to share and review the service's data-handling terms before installation.

Risk: A shared local service identity may expose another workspace user's report records or links.

Mitigation: Isolate agent workspaces and service identities per user; avoid shared installations without that separation.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-poop-clean-trigger-analysis)
- [API documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Structured analysis result or JSON; Markdown table of historical report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes an event-based cleaning trigger and report links; actual vacuum control requires a separate integration.]

## Skill Version(s):

1.0.12 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
