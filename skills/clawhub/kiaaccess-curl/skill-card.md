## Description:

Query and command a Kia vehicle from shell workflows with curl against the Kia Owners API for one-off status, location, EV charge, door, climate, and charging tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate curl and jq workflows for direct, one-off Kia Owners API reads and remote vehicle commands from a trusted shell.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can issue commands that affect a real vehicle, including door, climate, and charging actions.

Mitigation: Run mutating examples only when the user explicitly intends the real vehicle action, and confirm completion by re-reading vehicle state.

Risk: The workflow persists a durable Kia refresh token that can re-authenticate the account.

Mitigation: Use the skill only on a trusted single-user machine, protect the session file permissions, and delete the token when it is no longer needed.

Risk: The provided request helper writes sensitive session headers to a predictable temporary path.

Mitigation: Replace the fixed temporary header capture with a safer temporary file or in-memory approach before using the workflow on shared systems.

Risk: Repeated rejected login attempts can make shell-based login unusable by triggering additional anti-abuse controls.

Mitigation: Do not retry failed credentials in a loop; correct credentials first and attempt login deliberately.

## Reference(s):

- [Ready-to-run requests](references/requests.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/kiaaccess-curl)

## Skill Output:

**Output Type(s):** [shell commands, code, configuration, guidance]

**Output Format:** [Markdown with bash, curl, and jq snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user-supplied Kia credentials and MFA bootstrap; examples can read from or command a real vehicle.]

## Skill Version(s):

0.5.1 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
