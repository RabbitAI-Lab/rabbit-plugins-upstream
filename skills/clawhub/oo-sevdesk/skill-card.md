## Description:

This skill lets an agent use the OOMOL oo CLI to read, create, update, and delete sevdesk contacts through a connected sevdesk account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Users who manage sevdesk contacts can have an agent inspect live connector schemas and run contact listing, retrieval, creation, update, or deletion actions through an OOMOL-connected sevdesk account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance can invoke internet installer commands on the user's machine.

Mitigation: Do not let an agent automatically run curl|bash or irm|iex installer commands; install and verify the oo CLI manually where possible.

Risk: sevdesk operations are routed through OOMOL's oo CLI.

Mitigation: Install only if the user trusts OOMOL's oo CLI and is comfortable routing sevdesk operations through OOMOL.

Risk: Write and destructive actions can create, update, or delete sevdesk contact data.

Mitigation: Require explicit confirmation of the exact payload, target, and effect before creating, updating, or deleting contacts.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-sevdesk)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [sevdesk homepage](https://sevdesk.com)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON and include execution metadata; write and destructive contact actions require explicit user confirmation.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
