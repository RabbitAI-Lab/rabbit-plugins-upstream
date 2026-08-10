## Description:

Integrate Modellix's unified API and CLI for AI image, video, and audio workflows, including generation, editing, speech synthesis, transcription, voice cloning, virtual try-on, and model API calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[modellix](https://clawhub.ai/user/modellix)

### License/Terms of Use:

MIT

## Use Case:

Developers and creative-automation users use this skill to call Modellix media models through a CLI-first workflow, falling back to REST when needed. It helps agents select models, validate credentials, submit asynchronous jobs, wait for completion, and download generated or transcribed outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: MODELLIX_API_KEY can expose account access if printed, committed, or persisted unintentionally.

Mitigation: Keep the key session-scoped by default, do not echo it in logs or screenshots, and persist credentials only after explicit user approval.

Risk: Prompts, media URLs, and generated-task data are sent to Modellix and may create paid tasks.

Mitigation: Review inputs before submission, prefer the CLI workflow, and do not blindly retry paid POST submissions when the outcome is unknown.

Risk: Generated resources can expire before the user has saved them locally.

Mitigation: Download task outputs promptly with the CLI or REST result URLs and store them in an appropriate local output directory.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/modellix/skills/modellix)
- [Modellix AI Onboarding](https://docs.modellix.ai/get-started.md)
- [Modellix REST API](https://docs.modellix.ai/ways-to-use/api.md)
- [Modellix Full Models Index](https://docs.modellix.ai/llms.txt)
- [Modellix Docs MCP](https://docs.modellix.ai/mcp)
- [modellix-cli npm package](https://www.npmjs.com/package/modellix-cli)
- [Capability Matrix](references/capability-matrix.md)
- [CLI Playbook](references/cli-playbook.md)
- [REST Playbook](references/rest-playbook.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with inline bash commands and JSON request examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce downloaded media or transcript files from Modellix task results; uses MODELLIX_API_KEY for CLI or REST access.]

## Skill Version(s):

1.0.21 (source: ClawHub release metadata; artifact skill version 3.8.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
