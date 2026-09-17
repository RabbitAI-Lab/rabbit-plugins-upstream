## Description:

Gleap (gleap.io) skill for reading, creating, updating, and deleting Gleap data through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and support operators use this skill to inspect Gleap action schemas and manage contacts, tickets, and the current Gleap user through an OOMOL-connected Gleap account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that execute downloaded scripts.

Mitigation: Inspect official installation documentation, prefer signed or checksum-verified releases, and do not allow an agent to run curl|bash or irm|iex installer commands automatically.

Risk: Write and destructive Gleap actions can change or delete contacts and tickets.

Mitigation: Fetch the live action schema first, confirm the exact payload and target with the user, and require explicit approval before destructive actions.

## Reference(s):

- [ClawHub Gleap skill page](https://clawhub.ai/oomol/skills/oo-gleap)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Gleap homepage](https://www.gleap.io)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
