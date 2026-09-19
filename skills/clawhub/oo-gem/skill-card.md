## Description:

Uses the OOMOL oo CLI Gem connector to search and read Gem CRM data through an authenticated OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to let an agent inspect Gem connector schemas and run read-oriented Gem CRM actions for candidates, projects, sequences, users, custom fields, and project memberships.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote installer commands for the oo CLI.

Mitigation: Do not allow the agent to run installer commands automatically; install the oo CLI only from a trusted source, preferably with a pinned version and verified checksum or signature.

Risk: Authentication and Gem connection setup can open account access or billing workflows.

Mitigation: Have the user confirm login, connection, billing, and credential-recovery steps manually before any command or browser action is taken.

Risk: Connector request payloads can drift from the live Gem connector contract.

Mitigation: Inspect the live action schema with `oo connector schema` before constructing each payload.

## Reference(s):

- [ClawHub Gem skill page](https://clawhub.ai/oomol/skills/oo-gem)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Gem homepage](https://www.gem.com)

## Skill Output:

**Output Type(s):** [shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands use the oo CLI and return connector JSON responses when run with --json.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
