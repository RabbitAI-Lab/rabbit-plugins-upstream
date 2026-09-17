## Description:

Mindbody (mindbodyonline.com). Use this skill for ANY Mindbody request - searching and reading data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to search and read Mindbody business data through an OOMOL-connected Mindbody account. The skill is suited for listing businesses from the Mindbody Consumer API Business Directory after inspecting the live connector schema.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes commands that execute remote installer scripts.

Mitigation: Review the installer source or use a trusted package distribution path before installing the oo CLI.

Risk: The scanner notes that the available action scope may be broader than the read-only description suggests.

Mitigation: Require explicit user confirmation before any action beyond listing or reading data, and inspect each live action schema before submitting a payload.

Risk: The skill depends on OOMOL server-side credentials and the Mindbody connector.

Mitigation: Use it only in environments where OOMOL and the configured Mindbody connection are trusted.

## Reference(s):

- [Mindbody homepage](https://www.mindbodyonline.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-mindbody)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are returned as JSON with data and meta.executionId fields.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
