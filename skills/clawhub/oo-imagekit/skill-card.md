## Description:

Provides agent guidance for managing ImageKit assets through the OOMOL oo CLI connector, including listing assets, retrieving metadata, purging cache, and deleting files with confirmation for destructive actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect and manage ImageKit media-library assets through an OOMOL-connected account. It supports read workflows such as listing assets and metadata lookup, plus cache purge and file deletion workflows that require explicit confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote installer commands that could execute changing code on a user's machine.

Mitigation: Review the installer source before use, and prefer an official pinned installer or package-manager flow with checksum or signature verification.

Risk: Some supported ImageKit actions purge cache or permanently delete files and all versions.

Mitigation: Confirm the exact target, payload, and expected effect with the user before running destructive actions.

Risk: Inline JSON command payloads can be fragile when they contain user-supplied text.

Mitigation: Use file-based JSON payloads for values that may contain user-supplied text.

## Reference(s):

- [ClawHub ImageKit skill](https://clawhub.ai/oomol/skills/oo-imagekit)
- [ImageKit homepage](https://imagekit.io)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON command payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector actions return JSON-shaped responses when executed through the oo CLI.]

## Skill Version(s):

1.0.2 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
