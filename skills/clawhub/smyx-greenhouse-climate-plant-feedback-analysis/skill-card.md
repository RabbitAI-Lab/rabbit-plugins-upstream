## Description:

Analyzes greenhouse plant images or videos and available environmental readings to provide plant-condition reports and suggested climate-control actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Greenhouse operators and developers use the skill to assess plant condition from images or videos, review environmental-control recommendations, and retrieve historical analysis reports. Control actions should be reviewed against local controller safety policies before execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Greenhouse images, videos, or URLs are sent to a configured cloud service.

Mitigation: Confirm the service account, data handling, and retention expectations before submitting greenhouse media.

Risk: The skill automatically creates or reuses a workspace identity and stores authentication tokens for report and history access without a clear consent boundary.

Mitigation: Obtain user approval before use or history lookups, and review local token storage and access permissions.

Risk: Suggested climate-control commands could be unsuitable for a particular greenhouse.

Mitigation: Have an operator review recommendations and apply local controller safety limits before acting.

## Reference(s):

- [Greenhouse analysis API documentation](references/api_doc.md)
- [ClawHub skill listing](https://clawhub.ai/smyx-sunjinhui/skills/smyx-greenhouse-climate-plant-feedback-analysis)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Structured analysis report or Markdown report list; optionally saved as a text file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes suggested control actions, report links, and optional history lookups; does not directly operate greenhouse equipment.]

## Skill Version(s):

1.0.11 (source: ClawHub release metadata; bundled SKILL.md states 1.0.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
