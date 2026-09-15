## Description:

NeetoDesk enables agents to read, create, comment on, list, and update NeetoDesk support tickets through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Support teams, operators, and agents use this skill to manage NeetoDesk ticket workflows, including listing tickets, retrieving ticket details, creating tickets and comments, updating tickets, and listing workspace team members.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup guidance can lead an agent to run remote installer scripts directly in a shell.

Mitigation: Install the oo CLI manually from trusted official instructions after reviewing or verifying the installer; do not let an agent automatically run curl-to-bash or irm-to-iex setup commands.

Risk: Write actions can create tickets, add comments, or update existing NeetoDesk records.

Mitigation: Review the exact payload and expected effect with the user before allowing ticket creation, comments, or updates.

## Reference(s):

- [ClawHub NeetoDesk skill page](https://clawhub.ai/oomol/skills/oo-neetodesk)
- [NeetoDesk homepage](https://www.neeto.com/neetodesk)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are expected to include a data object and execution metadata.]

## Skill Version(s):

1.0.2 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
