## Description:

Query Kia vehicle status, location, EV charging information, and selected remote commands from the shell using curl against the Kia Owners API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and vehicle owners use this skill for one-off Kia account queries and shell-based remote actions, including checking vehicle status, location, EV charge state, locks, climate, and charging settings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires Kia account credentials and stores a reusable refresh token that can re-authenticate the account.

Mitigation: Store the session file with restrictive permissions, protect it as a credential, and remove it when access is no longer needed.

Risk: The skill can expose vehicle location and status information.

Mitigation: Use it only in trusted environments and avoid sharing command output or saved response files that include location or vehicle data.

Risk: The skill can issue real remote vehicle commands such as unlock, climate, and charging actions.

Mitigation: Require explicit confirmation before state-changing commands and verify the result with a fresh status read.

## Reference(s):

- [Ready-to-run requests](references/requests.md)
- [Kia Owners API base URL](https://api.owners.kia.com/apigw/v1)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/kiaaccess-curl)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with bash, curl, jq, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes credential setup, session handling, request examples, response checks, and command verification guidance.]

## Skill Version(s):

0.9.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
