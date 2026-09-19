## Description:

Provides OOMOL-connected access to Kontent.ai for searching and reading content items, content types, and languages through the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect live Kontent.ai connector schemas and run read-only get or list actions against a connected Kontent.ai environment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path can execute a remote installer script for the oo CLI when the CLI is missing.

Mitigation: Review the installer source and prefer a package manager or downloaded installer with published verification before allowing installation.

Risk: Connector commands access content in the user's connected Kontent.ai environment.

Mitigation: Run only user-requested read actions, inspect the live action schema before building payloads, and avoid proactive authentication or connection changes.

## Reference(s):

- [Kontent.ai ClawHub skill page](https://clawhub.ai/oomol/skills/oo-kontent-ai)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [Kontent.ai homepage](https://kontent.ai)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Primarily read-only connector actions for Kontent.ai content items, content types, and languages.]

## Skill Version(s):

1.0.3 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
