## Description:

ImageKit lets agents operate an ImageKit account through the OOMOL oo CLI, including listing assets, retrieving file metadata, purging cache targets, and deleting files with confirmation safeguards.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage ImageKit media-library assets from an agent when their OOMOL account is connected to ImageKit.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that execute downloaded scripts.

Mitigation: Review the oo CLI installation path before use and prefer a pinned, signed, or checksum-verified release over pipe-to-shell installation.

Risk: The skill can permanently delete ImageKit files and submit cache purge requests.

Mitigation: Require explicit user approval of the exact target and payload before running delete or purge actions.

## Reference(s):

- [ImageKit homepage](https://imagekit.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub ImageKit skill page](https://clawhub.ai/oomol/skills/oo-imagekit)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live ImageKit connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.2 (source: release evidence and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
