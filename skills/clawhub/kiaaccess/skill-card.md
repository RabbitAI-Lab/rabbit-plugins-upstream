## Description:

This skill lets agents use a user's Kia Access account to read Kia vehicle status, location, and EV charge data and send confirm-gated door, climate, and charging commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and their agents use this skill to manage their own Kia vehicle through a Kia Access account, including checking vehicle state, location, EV charge, and issuing confirm-gated comfort, charging, and door commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Kia credentials, local sessions, and exported refresh tokens are sensitive and can bypass MFA.

Mitigation: Treat tokens like passwords, never echo secrets in conversation, and use token export only to move a locally bootstrapped session into a hosted deployment.

Risk: Vehicle commands can affect a real vehicle, and unlocking leaves the vehicle unsecured.

Mitigation: Prefer KIA_WRITE_MODE=none for read-only use, enable comfort or all only when command capability is intended, and require explicit user confirmation before every command.

Risk: Kia accepting a command does not prove the vehicle completed the requested action.

Mitigation: Report accepted and confirmed states separately, wait and re-read vehicle status when confirmation matters, and avoid presenting dry runs as completed actions.

Risk: Rejected login retries can cause Kia to enforce reCAPTCHA and block server-side login for the account.

Mitigation: Stop after a rejected login and ask the user to verify credentials in the Kia Access app before trying again.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/kiaaccess)
- [npm package: kiaaccess-mcp](https://www.npmjs.com/package/kiaaccess-mcp)
- [Skill-documented source: chrischall/kiaaccess-mcp](https://github.com/chrischall/kiaaccess-mcp)

## Skill Output:

**Output Type(s):** [text, configuration, shell commands, guidance]

**Output Format:** [Markdown with inline JSON configuration and tool-result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return vehicle status, location, command previews, and command result summaries; write actions require explicit confirmation.]

## Skill Version(s):

0.5.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
