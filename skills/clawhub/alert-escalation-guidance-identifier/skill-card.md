## Description:

Maps incident severity and service context to an accountable response owner and queue.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Service operators and incident responders use this skill to draft severity-to-queue assignment guidance from a service profile before routing alerts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The default severity-to-queue template may not identify the actual service owner or reflect after-hours and unclassified-alert policy.

Mitigation: Review and customize the service profile and routing rules against the organization's escalation policy before using the guidance for real incidents.

## Reference(s):

- [Service Assignment Guide on ClawHub](https://clawhub.ai/wxt-ai/skills/alert-escalation-guidance-identifier)

## Skill Output:

**Output Type(s):** [Guidance, Text]

**Output Format:** [JSON with an assignment_guidance string]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local advisory severity-to-queue template; no alert or page is sent.]

## Skill Version(s):

1.1.1 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
