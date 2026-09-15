## Description:

Qwen (qwen.ai). Use this skill for ANY Qwen request, including reading, creating, updating, and deleting data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate Qwen through an OOMOL-connected account, including document analysis, OCR, translation, image generation or editing, speech generation, transcription, and custom voice management.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path includes remote installer scripts that can change after review.

Mitigation: Review the installer path before use and prefer a pinned, signed, or checksum-verified oo CLI release.

Risk: Write actions can create Qwen resources or submit asynchronous jobs.

Mitigation: Confirm the exact payload and expected effect with the user before running any action tagged as write.

Risk: Destructive actions can delete custom Qwen voices.

Mitigation: Confirm the target and obtain explicit approval before running any destructive action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-qwen)
- [Qwen homepage](https://qwen.ai/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands return JSON responses from the oo connector, including data and execution metadata.]

## Skill Version(s):

1.0.3 (source: release evidence and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
