## Description:

Use this skill for Truvera (truvera.io) requests that read, create, update, or delete data through the OOMOL `oo` CLI instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Truvera account resources through OOMOL, including DIDs, credential schemas, account profile lookup, and background job polling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that could be unsafe if executed automatically or from an unverified source.

Mitigation: Review the OOMOL CLI installation path before installing; prefer verified, versioned documentation or a trusted package manager, and do not let an agent run remote installer commands automatically.

Risk: Write and destructive Truvera actions can create or delete DIDs and credential schemas.

Mitigation: Confirm the exact payload, target, and intended effect with the user before executing write or destructive actions.

## Reference(s):

- [Truvera homepage](https://truvera.io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [Truvera ClawHub skill page](https://clawhub.ai/oomol/skills/oo-truvera)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live action-schema inspection before constructing payloads; write and destructive actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
