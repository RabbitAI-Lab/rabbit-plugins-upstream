## Description:

Integrate Modellix's unified API for AI image, video, and audio workflows through CLI-first or REST fallback execution.

This skill is ready for commercial/non-commercial use.

## Publisher:

[modellix](https://clawhub.ai/user/modellix)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative automation teams use this skill to submit asynchronous Modellix image, video, and audio jobs, inspect model schemas, wait for task completion, and download generated outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may install or update a global npm CLI before execution.

Mitigation: Review the installed CLI version, preinstall a trusted version, or set MODELLIX_CLI_AUTO_UPDATE=0 when tighter change control is required.

Risk: Prompts, media URLs, and task data are sent to Modellix during model invocation.

Mitigation: Use the skill only for data that is appropriate to send to Modellix and avoid submitting sensitive media or prompts without approval.

Risk: API credentials may become persistent if the user explicitly chooses CLI profile or environment persistence.

Mitigation: Prefer session-only MODELLIX_API_KEY usage and persist credentials only after explicit user approval.

## Reference(s):

- [Modellix AI Onboarding](https://docs.modellix.ai/get-started.md)
- [Modellix REST API](https://docs.modellix.ai/ways-to-use/api.md)
- [Modellix Full Models Index](https://docs.modellix.ai/llms.txt)
- [Modellix Docs MCP](https://docs.modellix.ai/mcp)
- [modellix-cli npm Package](https://www.npmjs.com/package/modellix-cli)
- [Capability Matrix](references/capability-matrix.md)
- [CLI Playbook](references/cli-playbook.md)
- [REST Playbook](references/rest-playbook.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, Files]

**Output Format:** [Markdown guidance with shell commands, JSON request bodies, and downloaded media or task-result files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include Modellix task metadata, resource URLs, local download paths, and generated image, video, audio, or transcript files.]

## Skill Version(s):

1.0.1 (source: server release metadata; source skill metadata version 4.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
