## Description:

Guides authorized Workday users in reading HR data through their signed-in browser session with fpx, without running an MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Authorized employees and administrators use this skill to retrieve their permitted Workday org, profile, pay, benefits, and task data from a shell without an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Workday responses may expose confidential HR information.

Mitigation: Access only authorized tenant data, project only needed fields, and avoid logging raw responses.

Risk: Raw response envelopes can include a session secret.

Mitigation: Use the field-selecting filters rather than printing the full response.

Risk: The CLI and paired browser extension require access to the signed-in Workday session.

Mitigation: Review the CLI installation, extension, pairing, and site-access permissions before use.

## Reference(s):

- [Workday FPX on ClawHub](https://clawhub.ai/chrischall/skills/workday-fpx)
- [Workday endpoint and filtering guide](artifact/references/endpoints.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Text and Markdown with shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only guidance; responses can contain confidential HR data.]

## Skill Version(s):

1.1.7 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
