## Description:

Provides bounded local desktop controls for explicit requests to adjust volume or brightness, open an allowlisted application, or close an exact process.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iyeque](https://clawhub.ai/user/iyeque)

### License/Terms of Use:

MIT-0

## Use Case:

People using a desktop agent can request volume or brightness changes and ask it to open or close supported applications. Device control runs only on an explicit request.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Closing an application can discard unsaved work.

Mitigation: Confirm the application and check for unsaved work before requesting closure.

## Reference(s):

- [device-control on ClawHub](https://clawhub.ai/iyeque/skills/iyeque-device-control)

## Skill Output:

**Output Type(s):** [Text, Shell commands]

**Output Format:** [Plain text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Controls local settings or allowlisted applications only on explicit request.]

## Skill Version(s):

1.3.0 (source: skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
