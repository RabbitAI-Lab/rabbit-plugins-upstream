## Description:

Mistral AI lets agents operate Mistral AI through an OOMOL-connected account using the oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect Mistral AI action schemas and run reads, writes, and administrative operations through an OOMOL-connected Mistral AI account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill exposes broad write and destructive actions through the connected Mistral AI account.

Mitigation: Confirm the exact Mistral resource, action, and payload with the user before running write or delete operations.

Risk: Fallback setup includes remote installer commands for the oo CLI.

Mitigation: Do not let an agent run the remote installer automatically; install through trusted OOMOL documentation or verify the installer before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-mistral-ai)
- [Mistral AI homepage](https://mistral.ai)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses OOMOL-connected credentials; write and destructive actions require explicit user confirmation before execution.]

## Skill Version(s):

1.0.4 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
