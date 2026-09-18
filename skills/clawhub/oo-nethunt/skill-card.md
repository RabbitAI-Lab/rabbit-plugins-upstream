## Description:

NetHunt (nethunt.com). Use this skill for ANY NetHunt request: reading, creating, updating, and deleting data through the OOMOL NetHunt connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and external users with connected NetHunt accounts use this skill to inspect CRM schemas, read and search CRM data, and create or update records, comments, and call logs through confirmed connector actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include direct execution of downloaded installer scripts.

Mitigation: Prefer a verifiable installation method, or inspect and verify the installer before execution.

Risk: The skill can read CRM data and perform write or destructive NetHunt actions.

Mitigation: Install only when OOMOL is trusted as an intermediary, confirm exact payloads for write actions, and require explicit approval before deletion.

## Reference(s):

- [NetHunt homepage](https://nethunt.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-nethunt)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance, API calls]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are returned as JSON objects containing data and execution metadata.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
