## Description:

GroqCloud enables an agent to operate GroqCloud through an OOMOL-connected account for model discovery, non-streaming chat completions, audio transcription, and English translation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to run GroqCloud requests through the oo CLI with an OOMOL-connected account. It supports model listing and metadata lookup, chat completions, and audio transcription or translation workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup path recommends executing remote install scripts directly in a shell.

Mitigation: Review the oo CLI install path first; prefer a package manager, documented manual install, or a downloaded script that can be inspected and verified before execution.

Risk: Chat prompts, audio inputs, public audio URLs, and generated outputs may be sent to GroqCloud and OOMOL-connected services.

Mitigation: Confirm what data will be sent and that the user is authorized to submit it before running transcription, translation, or chat-completion actions.

Risk: Write-tagged actions can create GroqCloud jobs or other service-side effects.

Mitigation: Inspect the live connector schema and confirm the exact payload and expected effect with the user before running write-tagged actions.

## Reference(s):

- [ClawHub GroqCloud skill page](https://clawhub.ai/oomol/skills/oo-groqcloud)
- [GroqCloud homepage](https://groq.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [shell commands, JSON, guidance]

**Output Format:** [Markdown guidance with inline shell commands and structured JSON command responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill directs agents to inspect live connector schemas before action execution and to confirm payloads for write or destructive actions.]

## Skill Version(s):

1.0.5 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
