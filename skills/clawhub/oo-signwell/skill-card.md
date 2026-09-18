## Description:

SignWell (signwell.com). Use this skill for ANY SignWell request: reading, creating, and updating SignWell data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to inspect SignWell account, document, and template data, create documents from templates, send draft documents for signing, and send reminder emails after confirming write actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote shell installer commands for the oo CLI, which can execute unverified code during installation.

Mitigation: Review the installer source before use and prefer a pinned, signed, checksum-verified, or package-manager installation path.

Risk: Write actions can create SignWell documents, send documents for signature, or send reminder emails.

Mitigation: Confirm the exact payload and expected effect with the user before running any action tagged as write.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-signwell)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [SignWell homepage](https://www.signwell.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Skill icon](https://static.oomol.com/logo/third-party/signwell.svg)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses oo CLI connector schemas and JSON payloads; write actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
