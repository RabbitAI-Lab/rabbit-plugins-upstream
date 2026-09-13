## Description:

Query and command a Kia vehicle directly with curl against the Kia Owners API for one-off vehicle status, location, EV charge, door, climate, and charging operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and vehicle owners use this skill when they need an agent to provide ready-to-run curl and jq commands for direct Kia Owners API reads or one-off remote vehicle commands from a shell.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill gives ready-to-run commands that can reveal vehicle location and change real vehicle state.

Mitigation: Verify the target vehicle and require deliberate user confirmation before lock, unlock, climate, charging, or location-sensitive commands.

Risk: The skill uses Kia account credentials, sid, rmtoken, and generated temporary/session files that can re-authenticate or expose account access.

Mitigation: Treat KIA_PASSWORD, sid, rmtoken, /tmp outputs, and the session JSON as secrets; avoid shared machines and keep session files restricted to the user.

Risk: Remote command acceptance is not proof that the vehicle state changed.

Mitigation: Re-read vehicle status and compare the specific relevant field after a delay before reporting a command as completed.

## Reference(s):

- [Ready-to-run requests](references/requests.md)
- [Kia Owners API endpoint](https://api.owners.kia.com/apigw/v1)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with Bash, curl, and jq command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may create local session/header files and require user-provided Kia account credentials plus one-time MFA.]

## Skill Version(s):

0.8.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
