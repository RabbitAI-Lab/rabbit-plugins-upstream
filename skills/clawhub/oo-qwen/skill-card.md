## Description:

Qwen (qwen.ai). Use this skill for ANY Qwen request: reading, creating, updating, and deleting data through the OOMOL-connected Qwen connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to work with Qwen through the OOMOL oo CLI for document analysis, OCR, translation, image generation and editing, text-to-speech, speech recognition, and custom voice workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands that can execute code on the user's machine.

Mitigation: Review the installer path and prefer a verifiable package or inspected download before installing the oo CLI.

Risk: The skill can submit confidential, personal, voice, image, audio, or document content to OOMOL and Qwen-connected services.

Mitigation: Submit sensitive content only when the user is comfortable with OOMOL and Qwen processing it.

Risk: Write actions can create Qwen resources and destructive actions can delete custom voices.

Mitigation: Confirm the exact payload and expected effect with the user before write actions, and require explicit approval before destructive actions.

## Reference(s):

- [ClawHub Qwen Skill](https://clawhub.ai/oomol/skills/oo-qwen)
- [Qwen Homepage](https://qwen.ai/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON payloads; connector responses are JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill instructs the agent to inspect live action schemas before requests and to confirm write or destructive actions with the user.]

## Skill Version(s):

1.0.3 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
