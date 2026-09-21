## Description:

WeCom Voice Agent helps teams handle WeCom voice messages, outbound calls, call summaries, compliant recording workflows, and voice-driven office tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fyniujin](https://clawhub.ai/user/fyniujin)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and operations teams use this skill to process WeCom voice interactions, route intents, manage calls, generate summaries, and produce operational reports. Developers can deploy and configure the webhook, intent, voice, and reporting modules for enterprise WeCom workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release can expose a public webhook and may persist or forward sensitive conversation and emotion-derived data.

Mitigation: Review it as an enterprise service, require authenticated and signed WeCom callback validation before exposure, and define retention and deletion rules for tickets, recordings, transcripts, emotion labels, and memory summaries.

Risk: Supervisor, custom, memory, and voice-clone features can expand data access or data sharing when enabled.

Mitigation: Disable or allowlist supervisor, custom, clone, memory, and voice-clone features unless explicitly approved for the deployment.

## Reference(s):

- [WeCom Voice Agent release page](https://clawhub.ai/fyniujin/skills/wecom-voice-agent)
- [Step-by-step setup guide](references/step_by_step_setup.md)
- [WeCom bot API reference](references/wecom_bot_api.md)
- [WeCom official bot documentation](https://developer.work.weixin.qq.com/document/path/101039)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON/YAML configuration examples and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local service guidance, voice interaction handling logic, call summaries, reports, and configuration files for WeCom voice workflows.]

## Skill Version(s):

2.8.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
