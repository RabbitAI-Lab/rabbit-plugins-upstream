## Description:

Cincopa helps agents search and read Cincopa assets, asset tags, galleries, and gallery items through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect Cincopa media account data, including asset tags, assets, galleries, and gallery items, without handling raw Cincopa API tokens directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup documents remote installer commands that can execute code from an external URL.

Mitigation: Run installer commands only after independently verifying the installer source and trusting the publisher, or use a preinstalled trusted oo CLI.

Risk: The skill relies on OOMOL as an intermediary for Cincopa access.

Mitigation: Install only when OOMOL is an acceptable intermediary for the connected Cincopa account and its server-side credential handling.

## Reference(s):

- [Cincopa homepage](https://www.cincopa.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub Cincopa skill page](https://clawhub.ai/oomol/skills/oo-cincopa)

## Skill Output:

**Output Type(s):** [shell commands, JSON, guidance]

**Output Format:** [Markdown with shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Cincopa list and search operations; first-time setup may require verified oo CLI installation and account connection.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
