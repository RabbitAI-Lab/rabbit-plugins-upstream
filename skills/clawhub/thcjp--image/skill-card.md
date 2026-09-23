## Description:

Creates, inspects, processes, and optimizes images and visual assets, including format selection, conversion, resizing, compression, denoising, enhancement, batch processing, style presets, model customization, commercial-rights workflows, and result comparison for professional image-processing tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and teams use this skill to ask an agent to create, inspect, process, optimize, convert, resize, compress, denoise, or enhance image files and visual assets. It is not positioned for complex decisions that require human judgment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may request read or write access to local image files and may propose command execution for image-processing tasks.

Mitigation: Review each requested file operation and command before execution, especially operations involving local files or credentials.

Risk: Image inputs or outputs may contain sensitive information.

Mitigation: Inspect images before processing or sharing them, avoid exposing sensitive content, and store processed outputs only in approved locations.

Risk: API keys or other credentials used for image-processing services could be exposed if pasted into prompts, logs, or files.

Mitigation: Provide credentials through environment variables or approved secret-management mechanisms and keep them out of version control and conversational output.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/image)
- [ClawHub publisher profile](https://clawhub.ai/user/thcjp)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [JSON status objects, Markdown guidance, and inline shell commands or configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include generated or modified image files, image metadata, execution logs, processing status, and follow-up guidance.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
