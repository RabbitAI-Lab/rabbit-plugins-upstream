## Description:

Helps agents use shell commands to sign in to iAqualink, list pool systems, and read iAqua screens or an eXO chlorinator's reported state.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and pool-system owners use this skill for one-off status checks, shell scripting, and API debugging without running an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper accesses iAqualink account credentials and stores session tokens locally.

Mitigation: Use only with an account you authorize; protect the session file as a credential and delete it when signing out.

Risk: The read-oriented helper also exposes commands that can change pool equipment state, including toggle actions.

Mitigation: Prefer the confirmed-control MCP tools; before any direct write, check current device state and confirm the intended change.

## Reference(s):

- [iAqualink curl helper](references/iaqualink.sh)
- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/iaqualink-curl)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell commands and JSON query examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read responses are JSON; the eXO shadow read is not yet verified live.]

## Skill Version(s):

0.2.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
