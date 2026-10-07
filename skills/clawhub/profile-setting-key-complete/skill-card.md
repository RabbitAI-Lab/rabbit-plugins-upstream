## Description:

Identifies a profile setting key from a request and creates a profile-governance review item, with optional external delivery when configured.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wxt-ai](https://clawhub.ai/user/wxt-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and profile-governance teams use this skill to turn a profile-setting request into a local review item and, if configured, submit it to a delivery target.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Configured delivery settings may send review data to an external service without another prompt.

Mitigation: Review and control delivery endpoints, SMTP settings, credentials, and any delivery configuration before running; leave delivery unconfigured for local-only use.

## Reference(s):

- [Profile Setting Directory on ClawHub](https://clawhub.ai/wxt-ai/skills/profile-setting-key-complete)

## Skill Output:

**Output Type(s):** [JSON, Files]

**Output Format:** [JSON response and local review artifact]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes identification, review item, local artifact receipt, and delivery status.]

## Skill Version(s):

1.2.0 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
