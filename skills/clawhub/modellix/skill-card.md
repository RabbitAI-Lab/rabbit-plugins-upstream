## Description:

Integrates Modellix's unified API for AI image, video, and audio workflows through CLI-first or REST fallback guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[modellix](https://clawhub.ai/user/modellix)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to generate or edit images, create or transform videos, synthesize speech, transcribe audio, clone voices, and download Modellix task results. It is intended for workflows that need model selection, credential handling, paid-task safeguards, and CLI or REST execution guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends prompts or media inputs to Modellix APIs and may download generated resources.

Mitigation: Use it only for intended Modellix media workflows and avoid sending sensitive prompts or media unless the deployment policy permits that egress.

Risk: The skill uses MODELLIX_API_KEY or a saved CLI profile for authenticated API access.

Mitigation: Keep credentials session-scoped by default, do not print API keys, and persist credentials only when the user explicitly requests it.

Risk: Media-generation submissions may be paid asynchronous tasks, and retrying an ambiguous submit can duplicate charges.

Mitigation: Run preflight or doctor first, submit paid tasks once, and check task history, the console, or any returned task ID before retrying after an unknown outcome.

Risk: The workflow may install or update modellix-cli before execution.

Mitigation: Allow installation only in environments that permit npm-based CLI updates, or disable automatic updates with MODELLIX_CLI_AUTO_UPDATE=0 when the installed CLI must remain pinned.

## Reference(s):

- [Modellix Skill on ClawHub](https://clawhub.ai/modellix/skills/modellix)
- [Modellix AI Onboarding](https://docs.modellix.ai/get-started.md)
- [Modellix REST API](https://docs.modellix.ai/ways-to-use/api.md)
- [Modellix Models Index](https://docs.modellix.ai/llms.txt)
- [Modellix Docs MCP](https://docs.modellix.ai/mcp)
- [modellix-cli package](https://www.npmjs.com/package/modellix-cli)
- [CLI Playbook](artifact/references/cli-playbook.md)
- [REST Playbook](artifact/references/rest-playbook.md)
- [Capability Matrix](artifact/references/capability-matrix.md)
- [Task Result Schema](artifact/assets/output/task-result.schema.json)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API calls, JSON, Files]

**Output Format:** [Markdown guidance with inline shell commands, JSON request bodies, and local output file paths]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May submit paid asynchronous media-generation tasks, poll or wait for task status, and download image, video, audio, or transcript resources.]

## Skill Version(s):

1.0.23 (source: ClawHub release evidence; artifact metadata version 3.9.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
