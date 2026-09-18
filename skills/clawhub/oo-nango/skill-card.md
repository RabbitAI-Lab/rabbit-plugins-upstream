## Description:

Nango (nango.dev). Use this skill for ANY Nango request - reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Nango connections, integrations, providers, tags, and metadata through an OOMOL-connected oo CLI workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup includes pipe-to-shell installer commands for the oo CLI.

Mitigation: Use the official oo CLI installation documentation or a pinned, verifiable package before installation.

Risk: Some Nango actions can update metadata, modify tags, or delete a connection.

Mitigation: Confirm the exact target, payload, and expected effect with the user before write or destructive actions.

Risk: Retrieving a connection can expose credentials when permissions allow it.

Mitigation: Only connect accounts or retrieve connection credentials when the user intends the agent to access that Nango environment.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-nango)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [Nango Homepage](https://nango.dev)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Installation Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash and PowerShell command blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may return JSON data from the oo CLI when actions are executed.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
