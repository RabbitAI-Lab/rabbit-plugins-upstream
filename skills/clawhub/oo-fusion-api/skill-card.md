## Description:

OOMOL Fusion API (oomol.com). Use this skill for ANY OOMOL Fusion API request: reading, creating, updating, and deleting data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate the OOMOL Fusion API through the oo CLI for AI media generation and editing, speech, OCR, document conversion, web-content workflows, file uploads, and related task status/result checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan reports unsafe CLI installation guidance using pipe-to-shell commands.

Mitigation: Prefer a verified installer or package manager path and review the installer source before executing installation commands.

Risk: The security scan reports that some generation or processing actions may be treated as safe even though they can upload, transform, or create user-facing content.

Mitigation: Confirm the payload, target files, and expected effect with the user before generation, upload, conversion, voice, image, video, or document-processing actions.

Risk: The skill operates through an OOMOL-connected account via the oo CLI.

Mitigation: Use the skill only when the user trusts OOMOL and understands that connector actions run against their connected account.

## Reference(s):

- [OOMOL Fusion API skill page](https://clawhub.ai/oomol/skills/oo-fusion-api)
- [OOMOL homepage](https://www.oomol.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include oo CLI schema-inspection commands, connector-run commands, JSON request payloads, and guidance for confirming state-changing or destructive actions.]

## Skill Version(s):

1.0.7 (source: server release metadata and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
