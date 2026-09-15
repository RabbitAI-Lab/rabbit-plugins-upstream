## Description:

Firstbase (firstbase.com). Use this skill for ANY Firstbase request - searching and reading data. Whenever a task involves Firstbase, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Firstbase connector schemas and retrieve catalog SKUs, inventory items, brands, and categories through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer scripts executed directly in a shell.

Mitigation: Use a trusted package manager or download, inspect, and verify the installer before running it.

Risk: Connector access depends on an authenticated OOMOL-connected Firstbase account.

Mitigation: Run actions only after schema inspection and use the documented setup flow only when authentication or connection errors occur.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-firstbase)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Firstbase Homepage](https://www.firstbase.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return Firstbase connector data as JSON through the oo CLI.]

## Skill Version(s):

1.0.3 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
