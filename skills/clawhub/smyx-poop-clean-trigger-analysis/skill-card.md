## Description:

Analyzes pet toilet-area videos and reports defecation events with a cleaning trigger after the pet leaves the area.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and smart-home integrators use this skill to analyze dog toilet or other designated pet-area videos, review defecation event reports, and obtain a cleaning trigger for their own robot-vacuum integration. The skill does not directly control a vacuum or provide medical diagnosis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet-area household videos and report queries may be sent to lifeemergence.com services.

Mitigation: Review the service and obtain household consent before sharing videos or querying cloud reports.

Risk: The skill may create or reuse an account and persist login tokens locally without a separate account prompt.

Mitigation: Review account access before installation and protect or remove stored tokens when they are no longer needed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/smyx-sunjinhui/skills/smyx-poop-clean-trigger-analysis)
- [API documentation](references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, Cleaning trigger signal, Guidance]

**Output Format:** [JSON or Markdown report with event results and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Historical cloud reports can be listed; vacuum control requires a separate integration.]

## Skill Version(s):

1.0.11 (source: server-resolved ClawHub release; bundled SKILL.md states 1.0.17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
