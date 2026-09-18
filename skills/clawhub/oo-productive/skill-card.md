## Description:

Productive enables agents to read, create, update, and delete Productive tasks and time entries through an OOMOL-connected oo CLI workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents working with a connected Productive account use this skill to inspect live action schemas and manage Productive tasks and time entries without handling raw credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path includes curl-to-bash and PowerShell remote installer commands that can execute remote code.

Mitigation: Install the oo CLI through a verified method and do not let an agent run the remote installer automatically.

Risk: Write and destructive actions can create, update, or delete Productive business records.

Mitigation: Confirm exact payloads and effects with the user before write actions, and require explicit approval before deleting records.

Risk: Payload fields may be incorrect if the agent uses stale assumptions about Productive action schemas.

Mitigation: Inspect the live connector schema before constructing each action payload.

## Reference(s):

- [Productive homepage](https://productive.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-productive)
- [Publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live connector schema inspection before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
