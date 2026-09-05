## Description:

Query and command a Kia vehicle directly with curl against the Kia Owners API (api.owners.kia.com), without running the MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and vehicle owners use this skill for one-off shell-based reads and commands against a Kia account, including vehicle status, location, EV charge state, door locks, climate, and charging controls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can access Kia account sessions, vehicle identifiers, vehicle location, and command outputs.

Mitigation: Treat generated session files, /tmp outputs, rmtoken, sid, location results, and vehicle identifiers as sensitive; remove them when done and avoid shared machines.

Risk: The skill enables real vehicle commands, including lock, unlock, climate, charging, and location actions.

Mitigation: Require explicit confirmation before lock, unlock, climate, charging, or location actions, and verify command effects with a follow-up vehicle status read.

Risk: Durable re-authentication tokens can continue to access the account without repeating MFA.

Mitigation: Store the rmtoken only in the dedicated curl session file with restrictive permissions and delete it when access is no longer needed.

## Reference(s):

- [Ready-to-run requests](references/requests.md)
- [Kia Owners API endpoint](https://api.owners.kia.com/apigw/v1)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Code]

**Output Format:** [Markdown with inline bash, curl, and jq examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce session files and temporary JSON/header outputs that should be treated as sensitive.]

## Skill Version(s):

0.8.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
