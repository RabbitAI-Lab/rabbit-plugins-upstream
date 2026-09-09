## Description:

Integrate Modellix's unified API and CLI for asynchronous image, video, and audio workflows, including model schema lookup, task execution, waiting, and result download.

This skill is ready for commercial/non-commercial use.

## Publisher:

[modellix](https://clawhub.ai/user/modellix)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creative operators, and automation agents use this skill to run Modellix media-generation, transcription, speech, and model-schema workflows through the CLI or REST API. It helps select default models, validate request bodies, submit paid asynchronous tasks, wait for completion, and persist generated results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, media URLs, and task data are sent to Modellix for media-generation and transcription workflows.

Mitigation: Use the skill only for data appropriate to send to Modellix, and avoid submitting confidential or regulated content unless the deployment has approved that use.

Risk: Paid workflows require MODELLIX_API_KEY or a saved Modellix CLI profile.

Mitigation: Use session-only credentials by default, avoid printing or logging secrets, and persist credentials only after explicit user approval.

Risk: The helper can automatically update the global modellix-cli package before paid work.

Mitigation: Set MODELLIX_CLI_AUTO_UPDATE=0 when the environment must keep its installed CLI version, and resolve the CLI before starting a paid workflow.

## Reference(s):

- [Modellix AI Onboarding](https://docs.modellix.ai/get-started.md)
- [Modellix REST API](https://docs.modellix.ai/ways-to-use/api.md)
- [Modellix Full Models Index](https://docs.modellix.ai/llms.txt)
- [Modellix Docs MCP](https://docs.modellix.ai/mcp)
- [modellix-cli Package](https://www.npmjs.com/package/modellix-cli)
- [Capability Matrix](references/capability-matrix.md)
- [CLI Playbook](references/cli-playbook.md)
- [REST Playbook](references/rest-playbook.md)
- [Task Result Schema](assets/output/task-result.schema.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with inline shell commands and JSON request bodies; completed Modellix tasks may produce downloaded image, video, audio, or transcript files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses MODELLIX_API_KEY or a saved Modellix CLI profile for authenticated paid workflows.]

## Skill Version(s):

1.0.24 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
