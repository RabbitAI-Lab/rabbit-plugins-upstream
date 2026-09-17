## Description:

Bitrise lets agents read Bitrise data and trigger builds through an OOMOL-connected oo CLI connector instead of calling the Bitrise API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to inspect Bitrise apps and builds, retrieve build details, and trigger Bitrise builds or pipelines through an authenticated OOMOL connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path can execute a remote oo CLI installer on the user's machine.

Mitigation: Review the installer URL and prefer a verified, signed, or package-managed installation path before running installer commands.

Risk: Triggering a Bitrise build or pipeline changes external CI state.

Mitigation: Inspect the live action schema, construct an exact payload, and get explicit user confirmation before running write actions.

## Reference(s):

- [ClawHub Bitrise Skill Page](https://clawhub.ai/oomol/skills/oo-bitrise)
- [Bitrise Homepage](https://bitrise.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [State-changing Bitrise actions require explicit user confirmation before execution.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
