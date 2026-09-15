## Description:

Provides agent guidance for operating USPTO through OOMOL's oo CLI to read, create, and update USPTO data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to run USPTO connector actions through an OOMOL-connected account, including trademark case status, update-date, and document metadata lookups.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup includes remote shell installer commands for the oo CLI.

Mitigation: Review the installer path first and prefer a pinned, verified release or trusted package manager instead of piping remote scripts directly to a shell.

Risk: Some USPTO connector actions may alter account or filing data.

Mitigation: Inspect the live action schema and confirm the exact payload and expected effect with the user before running any write or destructive action.

## Reference(s):

- [ClawHub USPTO Skill](https://clawhub.ai/oomol/skills/oo-uspto)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [USPTO homepage](https://www.uspto.gov/)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON, XML]

**Output Format:** [Markdown guidance with oo CLI shell commands and connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may include JSON envelopes and USPTO XML data depending on the selected action.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
