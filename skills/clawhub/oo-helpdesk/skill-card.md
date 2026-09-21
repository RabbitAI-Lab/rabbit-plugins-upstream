## Description:

HelpDesk enables agents to read, create, update, move, and delete HelpDesk tickets through the OOMOL oo connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Support operators and developers use this skill to automate HelpDesk ticket workflows through an OOMOL-connected account, including ticket search, creation, updates, assignment support, silo moves, and deletion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes downloaded installer scripts that could be run directly by an agent.

Mitigation: Review the installer path before installing, prefer installing the oo CLI from a trusted verified source yourself, and do not let an agent run remote pipe-to-shell commands.

Risk: Write and destructive HelpDesk actions can change, move, or delete ticket data.

Mitigation: Confirm the exact ticket, payload, and expected effect with the user before running write or destructive actions.

## Reference(s):

- [HelpDesk homepage](https://www.helpdesk.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector action responses are JSON objects that include data and meta.executionId.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
