## Description:

OOMOL Fusion API helps agents operate the fusion-api connector through the oo CLI for reading, creating, updating, deleting, generating, transforming, and retrieving multimodal content.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect OOMOL Fusion API action schemas, build JSON payloads, and run connector actions through the oo CLI. It supports multimodal workflows including image, audio, video, OCR, ASR, TTS, document conversion, file upload, web reading, and task result retrieval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports unsafe CLI install instructions.

Mitigation: Install only when the oo command is missing and only from a trusted OOMOL CLI source; avoid repeating one-time setup steps unnecessarily.

Risk: Some generation or cost-incurring actions may be understated as safe reads.

Mitigation: Require explicit user confirmation before write, destructive, upload, generation, transformation, or billing-related actions, including untagged actions that are not passive reads.

Risk: Connector actions can change or delete data when tagged as write or destructive.

Mitigation: Fetch the live schema first, confirm the exact payload and effect with the user, and require explicit approval for destructive targets.

## Reference(s):

- [OOMOL Fusion API homepage](https://www.oomol.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-fusion-api)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution; may return asynchronous task IDs, state, and result data from provider workflows.]

## Skill Version(s):

1.0.8 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
