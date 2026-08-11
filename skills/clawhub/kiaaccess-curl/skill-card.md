## Description:

Query and command a Kia vehicle directly with curl against the Kia Owners API for one-off shell access to status, location, EV charging, door locks, and climate controls, using KIA_USERNAME/KIA_PASSWORD and one-time SMS or email MFA bootstrap.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and vehicle owners use this skill for one-off Kia account and vehicle operations from the shell, including status, location, EV charging, door locks, and climate commands. It is best suited for direct curl-based debugging or occasional use when the MCP server is not running.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Commands can change the state of a real Kia vehicle, including lock, unlock, climate, and charging behavior.

Mitigation: Run state-changing commands only with explicit owner consent, confirm the intended vehicle and action before execution, and verify completion by re-reading vehicle state.

Risk: Vehicle location and status responses may expose sensitive personal information.

Mitigation: Treat command output and saved response files as sensitive data, avoid sharing logs, and remove temporary response files when they are no longer needed.

Risk: Kia account credentials and refresh tokens can grant account access if exposed.

Mitigation: Protect KIA_USERNAME, KIA_PASSWORD, and rmtoken values, store the session file with restrictive permissions, and use a private per-user runtime directory instead of shared temporary paths.

Risk: HTTP 200 responses and accepted command status do not prove a vehicle command completed.

Mitigation: Inspect body status codes and confirm state-changing commands by re-reading and comparing the relevant vehicle status fields.

## Reference(s):

- [Ready-to-run requests](artifact/references/requests.md)
- [Kia Owners API endpoint](https://api.owners.kia.com/apigw/v1)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/kiaaccess-curl)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash, curl, and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes credential setup, request headers, request bodies, response checks, and command verification guidance.]

## Skill Version(s):

0.6.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
