## Description:

Register an event callback address.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and integration operators use this skill to prepare an event callback subscription, record its receipt locally, and optionally submit the subscription to a configured delivery endpoint.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Creates a local subscription artifact in the selected output directory.

Mitigation: Run in a dedicated writable workspace and review the generated artifact.

Risk: Configured delivery can send the callback record and local artifact path to an external endpoint using available credentials.

Mitigation: Use only a trusted endpoint; clear delivery and credential settings unless external submission is intended.

## Reference(s):

- [Subscription Receipt Desk on ClawHub](https://clawhub.ai/wxt-ai/skills/event-callback-url-workbench)

## Skill Output:

**Output Type(s):** [JSON, Files]

**Output Format:** [JSON response and local JSON receipt]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes the recorded callback and local artifact receipt, plus a delivery receipt when delivery is configured.]

## Skill Version(s):

1.1.1 (source: skill frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
