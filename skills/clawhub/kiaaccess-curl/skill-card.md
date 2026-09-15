## Description:

kiaaccess-curl helps an agent query and command a Kia vehicle directly with curl against the Kia Owners API for one-off status, location, EV charge, lock, unlock, and climate operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, and Kia vehicle owners use this skill for one-off shell-based reads and owner-authorized remote commands when the Kia MCP server is not running or when direct curl debugging is needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires Kia account credentials and handles a refresh token that can re-authenticate the account.

Mitigation: Use a private session file with restrictive permissions, keep session data out of shared locations, and remove stored tokens when they are no longer needed.

Risk: The skill can issue state-changing vehicle commands, including lock, unlock, climate, and charging actions.

Mitigation: Run state-changing commands only after explicit vehicle-owner confirmation, and verify completion by re-reading vehicle state rather than relying on HTTP status alone.

Risk: Shared temporary files can expose response headers or related session material on multi-user machines.

Mitigation: Replace shared /tmp paths with a private temporary directory that has restrictive permissions, then clean it up after each run.

Risk: Repeated rejected login attempts can trigger Recaptcha enforcement and break shell-based login.

Mitigation: Do not retry rejected credentials in a loop; fix the credential issue before attempting login again.

## Reference(s):

- [Ready-to-run requests](references/requests.md)
- [Kia Owners API endpoint](https://api.owners.kia.com/apigw/v1)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/kiaaccess-curl)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline bash, curl, jq, and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces commands and usage guidance for Kia Owners API workflows; users must provide Kia credentials and confirm state-changing commands.]

## Skill Version(s):

0.8.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
