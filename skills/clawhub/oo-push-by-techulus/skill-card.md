## Description:

Push by Techulus helps an agent send Push by Techulus notifications through the OOMOL oo connector after inspecting the live action schema.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to send Push by Techulus notifications to device groups or all devices associated with an account or team API key.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that could execute arbitrary local code.

Mitigation: Install the oo CLI from a verified, pinned, signed, or package-manager source before running connector commands.

Risk: Notification actions can send messages to device groups or all targeted devices.

Mitigation: Confirm the exact recipients, action name, and message payload with the user before running write actions.

## Reference(s):

- [Push by Techulus homepage](https://push.techulus.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-push-by-techulus)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses oo connector commands and JSON responses that include data and meta.executionId.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
