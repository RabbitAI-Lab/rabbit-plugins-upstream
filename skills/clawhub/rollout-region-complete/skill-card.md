## Description:

Selects a deployment region from a rollout request, writes a local deployment brief, and optionally delivers the record to a configured destination.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Release engineers use this skill to choose a regional deployment location, create a local deployment brief, and optionally submit the record to a configured destination.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A configured delivery target can submit deployment records to an arbitrary external endpoint, including through environment settings that may be overlooked.

Mitigation: Review or unset DELIVERY_ENDPOINT, CLAWHUB_DELIVERY_ENDPOINT, SMTP_*, and CLAWHUB_SMTP_* settings and any delivery config before running; leave delivery unconfigured for local-only use.

## Reference(s):

- [Regional Rollout Planner on ClawHub](https://clawhub.ai/wxt-ai/skills/rollout-region-complete)

## Skill Output:

**Output Type(s):** [Text, Files]

**Output Format:** [JSON response and local deployment brief]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes the selected region, recorded region, local artifact receipt, and delivery status; supports APAC, EU, and US residency requests.]

## Skill Version(s):

1.2.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
