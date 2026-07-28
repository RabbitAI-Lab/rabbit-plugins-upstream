## Description: <br>
Modellix helps agents use the Modellix CLI or REST API to generate, edit, wait for, and download AI image and video outputs through a unified media-generation workflow. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[modellix](https://clawhub.ai/user/modellix) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to route media-generation requests through Modellix, choose default or named models, run CLI-first generation workflows, and persist returned images or videos. It is intended for image generation, video generation, image editing, virtual try-on, and related Modellix model API tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: API keys may be exposed if copied into logs, command history, screenshots, transcripts, or committed files. <br>
Mitigation: Use MODELLIX_API_KEY or CLI profiles without printing key values, prefer session-only credentials, and persist credentials only after explicit user approval. <br>
Risk: Prompts and referenced media are sent to Modellix when generation tasks are submitted. <br>
Mitigation: Use the skill only for content appropriate to send to Modellix and review media inputs before submission. <br>
Risk: Batch or repeated submissions can create paid Modellix tasks, and blind retries after uncertain outcomes may duplicate charges. <br>
Mitigation: Approve paid batch submissions deliberately, set batch limits, and check task history or existing task IDs before retrying unknown paid submissions. <br>
Risk: Generated result URLs expire after about seven days. <br>
Mitigation: Download generated media promptly with the CLI download workflow or an equivalent trusted REST download step. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/modellix/skills/modellix) <br>
- [Modellix AI Onboarding](https://docs.modellix.ai/get-started.md) <br>
- [Modellix REST API](https://docs.modellix.ai/ways-to-use/api.md) <br>
- [Modellix Full Models Index](https://docs.modellix.ai/llms.txt) <br>
- [Modellix Docs MCP](https://docs.modellix.ai/mcp) <br>
- [modellix-cli package](https://www.npmjs.com/package/modellix-cli) <br>
- [Capability Matrix](references/capability-matrix.md) <br>
- [CLI Playbook](references/cli-playbook.md) <br>
- [REST Playbook](references/rest-playbook.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, JSON, files] <br>
**Output Format:** [Markdown guidance with shell commands, JSON responses, configuration steps, and downloaded media file paths] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses MODELLIX_API_KEY for authenticated Modellix CLI or REST calls; generated media should be downloaded before result URLs expire.] <br>

## Skill Version(s): <br>
1.0.19 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
