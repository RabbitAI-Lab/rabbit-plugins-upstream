## Description:

Analyzes local video files or public video URLs with Alibaba Cloud DashScope/Qwen multimodal models to produce scene descriptions, object and action observations, summaries, content review notes, and prompt-directed answers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, content teams, media operators, educators, and automated workflows use this skill to ask an agent for video understanding tasks such as scene description, object and action recognition, video summarization, content review, and question-answer analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local or sensitive videos may be sent to Alibaba Cloud DashScope/Qwen during analysis.

Mitigation: Use only videos that are approved for that provider and avoid private, regulated, or confidential footage until data-handling terms are confirmed.

Risk: The artifact shows cat/grep API-key commands that can expose secrets in terminal output or logs.

Mitigation: Do not run those commands; configure DashScope credentials through a clearly scoped secret mechanism and avoid echoing keys.

Risk: The artifact contains inconsistent credential paths and incomplete command examples.

Mitigation: Review and correct credential configuration and execution commands before using the skill in production workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/analyze-video-by-qwen)
- [Publisher profile](https://clawhub.ai/user/thcjp)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and optional JSON-shaped result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are prompt-directed video analysis results; higher FPS may increase cost and latency.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
