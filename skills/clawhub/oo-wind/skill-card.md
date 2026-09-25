## Description:

Wind lets an agent operate Wind financial data and Alice analysis workflows through an OOMOL-connected account using schema-driven oo connector actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, analysts, and agent users use this skill to query Wind stock, fund, bond, index, economic indicator, news, announcement, and risk data through an existing OOMOL Wind connection. It also supports Wind Alice analysis, report downloads, and task resumption.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup references remote installer commands that execute external shell scripts.

Mitigation: Review and perform the oo CLI installation yourself, prefer the vendor installation guide, and verify the installer source before use.

Risk: Wind Alice analysis is a write action that may continue running and consume Wind credits.

Mitigation: Confirm the exact payload and expected effect before execution, retain execution identifiers, and resume existing tasks instead of submitting duplicates.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-wind)
- [Wind homepage](https://market.windalice.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload conventions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector actions can return JSON data, execution identifiers, and transferable report file URLs.]

## Skill Version(s):

1.0.0 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
