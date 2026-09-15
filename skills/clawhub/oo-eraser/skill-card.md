## Description:

Eraser helps agents read, create, update, delete, and render Eraser files and diagrams through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and teams with Eraser accounts use this skill to manage Eraser files and diagrams through OOMOL, including reads, writes, rendering, and natural-language diagram generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup may execute remote installer scripts without independent verification.

Mitigation: Review the oo CLI installation path and prefer verified, versioned OOMOL documentation or a package manager with signature or checksum verification.

Risk: Write, archive, update, and delete actions can alter or remove Eraser content.

Mitigation: Require explicit approval before any write, archive, update, or delete action and confirm the target, payload, and expected effect.

Risk: Connector requests can be wrong if the agent assumes stale action inputs.

Mitigation: Inspect the live connector schema before constructing payloads for Eraser actions.

## Reference(s):

- [Eraser homepage](https://www.eraser.io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-eraser)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with oo CLI shell commands and JSON connector payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can produce or modify Eraser files and diagrams through connector actions after required user confirmation.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
