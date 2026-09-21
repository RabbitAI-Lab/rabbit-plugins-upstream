## Description:

Operates OneSignal through the OOMOL connector so agents can list and retrieve messages, create push notifications, and cancel scheduled messages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage OneSignal messaging from an agent through OOMOL, including listing messages, retrieving message details, creating push notifications, and canceling scheduled messages after confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: OneSignal actions are routed through OOMOL rather than directly through OneSignal.

Mitigation: Use the skill only when this routing model is acceptable for the account and data involved.

Risk: Push-notification creation and scheduled-message cancellation can change or remove live messaging state.

Mitigation: Confirm the exact payload, target audience, message ID, and expected effect with the user before running write or destructive actions.

Risk: The setup path references remote shell installer scripts for the oo CLI.

Mitigation: Install the CLI through a trusted, verified method and review installer scripts before execution.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-onesignal-rest-api)
- [OneSignal Homepage](https://onesignal.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Configuration instructions]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses oo CLI JSON responses from the OneSignal connector.]

## Skill Version(s):

1.0.4 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
