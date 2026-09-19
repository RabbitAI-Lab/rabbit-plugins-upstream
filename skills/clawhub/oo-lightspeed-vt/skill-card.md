## Description:

This skill supports LightSpeed VT requests for searching and reading data through the OOMOL-connected lightspeed_vt connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect LightSpeed VT action schemas and retrieve courses, locations, and users through an OOMOL-connected LightSpeed VT account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include direct remote script execution for installing the oo CLI.

Mitigation: Review the official oo CLI installation guide and prefer a verified or package-manager-based install path before running installer commands.

Risk: Future connector actions could be write-capable even though the current listed actions are read-oriented.

Mitigation: Inspect the live action schema before constructing payloads and require explicit user confirmation before any write-capable or destructive action is run.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-lightspeed-vt)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI installation guide](https://cli.oomol.com/install-guide.md)
- [LightSpeed VT homepage](https://lightspeedvt.com/)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before forming action payloads; read actions return JSON data with execution metadata.]

## Skill Version(s):

1.0.2 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
