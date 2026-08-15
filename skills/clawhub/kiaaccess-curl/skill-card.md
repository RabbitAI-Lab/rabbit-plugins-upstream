## Description:

Query and command a Kia vehicle directly with curl against the Kia Owners API, including status, location, EV charge state, door locks, climate, and charging operations after Kia credential and MFA setup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill for one-off shell access to Kia vehicle status, location, EV charge state, and supported remote commands when the Kia MCP server is not running or is not the right interface.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can issue physical vehicle commands such as unlock, climate, and charging actions.

Mitigation: Use it only for an account and vehicle you are authorized to control, review each command before execution, and confirm completion by re-reading vehicle state.

Risk: The saved rmtoken can re-authenticate the Kia account without another MFA prompt.

Mitigation: Store it in a safer secret store or on a locked-down single-user machine, restrict file permissions, and rotate or revoke it if exposure is suspected.

Risk: The provided curl helper captures response headers in a predictable temporary file path.

Mitigation: Replace the fixed /tmp header capture with a private temporary file before operational use.

Risk: Repeated rejected logins can trigger Kia account protections that break shell-based login.

Mitigation: Do not retry invalid credentials in a loop; correct the username or password before attempting login again.

## Reference(s):

- [Ready-to-run requests](artifact/references/requests.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/kiaaccess-curl)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash, curl, and jq command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes credential setup, request examples, response checks, and safety notes for vehicle commands.]

## Skill Version(s):

0.6.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
