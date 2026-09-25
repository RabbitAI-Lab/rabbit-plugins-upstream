## Description:

llm-provider Whisper helps agents guide local Whisper CLI speech-to-text workflows and related automation, with Chinese-language usage guidance and optional command, file, and configuration steps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, content creators, and automation users can use this skill to prepare and run local speech-to-text workflows with Whisper CLI, then review text, markdown, JSON-like status output, or generated file-handling guidance. Reviewers should clarify whether the intended run uses only local Whisper or any external API before processing audio or credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill documentation is inconsistent about local Whisper-only use versus API keys or external services.

Mitigation: Confirm the intended runtime mode and any external service use before providing audio files, credentials, or network access.

Risk: The skill may require command execution and file read/write access.

Mitigation: Review commands before execution, run in a constrained workspace, and limit access to only the audio files and output paths needed for the task.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/openai-whisper-1-0-0)
- [Publisher profile](https://clawhub.ai/user/thcjp)
- [Artifact homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with optional JSON-like status examples and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include file read/write and command execution guidance depending on the agent environment.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter lists 1.0.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
