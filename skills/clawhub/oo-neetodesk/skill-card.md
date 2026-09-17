## Description:

NeetoDesk enables agents to read, create, and update NeetoDesk tickets, comments, and workspace team data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and support teams use this skill to operate NeetoDesk ticket workflows through an OOMOL-connected account, including ticket lookup, creation, updates, comments, and team member listing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that execute downloaded scripts directly in a shell.

Mitigation: Install the oo CLI only from an official, integrity-checked OOMOL channel and avoid running curl | bash or irm | iex commands unless independently verified.

Risk: Write actions can create comments, create tickets, or update existing tickets in NeetoDesk.

Mitigation: Confirm the exact action, target, payload, and expected effect with the user before running any write action.

## Reference(s):

- [ClawHub NeetoDesk Skill](https://clawhub.ai/oomol/skills/oo-neetodesk)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [NeetoDesk Homepage](https://www.neeto.com/neetodesk)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include oo CLI connector commands, schema-inspection steps, setup guidance, and confirmation prompts for write actions.]

## Skill Version(s):

1.0.2 (source: evidence release and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
