## Description:

AnySearch lets agents search and read data through an OOMOL-connected AnySearch account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to run AnySearch searches, batch searches, HTML extraction, and sub-domain discovery through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup can execute remote installer scripts directly in a shell.

Mitigation: Review the installer or use a verified package or release, and require explicit approval before CLI installation or account connection.

## Reference(s):

- [ClawHub AnySearch skill page](https://clawhub.ai/oomol/skills/oo-anysearch)
- [AnySearch homepage](https://anysearch.com/home)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with oo CLI commands and JSON command payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return structured source results, cleaned page Markdown, and execution metadata from AnySearch actions.]

## Skill Version(s):

1.0.2 (source: release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
